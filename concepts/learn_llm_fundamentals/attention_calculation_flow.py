import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gensim.downloader as api

def print_step(title, matrix=None, shape=True):
    """Helper function to print formatted steps."""
    print(f"--- {title} ---\n")
    if matrix is not None:
        print(matrix)
        if shape:
            print(f"\nShape: {matrix.shape}\n")
    print("-" * (len(title) + 8) + "\n")

def plot_heatmap(matrix, title, y_labels, filename):
    """Helper function to plot and save a heatmap."""
    plt.figure(figsize=(10, 4))
    sns.heatmap(matrix, cmap='viridis', yticklabels=y_labels, annot=False)
    plt.title(title)
    plt.xlabel("Vector Dimensions")
    plt.ylabel("Tokens")
    plt.savefig(filename)
    print(f"Saved plot: {filename}\n")
    plt.close()

# --- Step 1: Define Tokens and Load Model ---
tokens = ["tower", "building", "sky", "river", "man", "woman"]
print_step("Step 1: Input Tokens", np.array(tokens), shape=False)

print("Loading GloVe model... (this may take a moment)")
model = api.load("glove-wiki-gigaword-50")
embedding_dim = model.vector_size

# --- Step 2: Get Word Embeddings ---
embeddings = np.array([model[word] for word in tokens])
print_step("Step 2: Word Embeddings (Token -> Vector)", embeddings)
plot_heatmap(embeddings, "1. Word Embeddings", tokens, "1_word_embeddings.png")

# --- Step 3: Define and Show Projection Matrices (Wq, Wk, Wv) ---
# In a real Transformer, these are learned. We use random matrices for simulation.
qkv_dim = 8  # Using a smaller dimension to make the output easier to read
np.random.seed(42)
W_q = np.random.randn(embedding_dim, qkv_dim)
W_k = np.random.randn(embedding_dim, qkv_dim)
W_v = np.random.randn(embedding_dim, qkv_dim)

print_step("Step 3a: Query Weight Matrix (W_q)", W_q)
print_step("Step 3b: Key Weight Matrix (W_k)", W_k)
print_step("Step 3c: Value Weight Matrix (W_v)", W_v)

# --- Step 4: Project Embeddings to Q, K, V ---
# Calculation: Q = Embeddings @ W_q
queries = embeddings @ W_q
keys = embeddings @ W_k
values = embeddings @ W_v

print_step("Step 4a: Query Vectors (Q = Embeddings @ W_q)", queries)
plot_heatmap(queries, "2. Query Vectors", tokens, "2_query_vectors.png")

print_step("Step 4b: Key Vectors (K = Embeddings @ W_k)", keys)
plot_heatmap(keys, "3. Key Vectors", tokens, "3_key_vectors.png")

print_step("Step 4c: Value Vectors (V = Embeddings @ W_v)", values)
plot_heatmap(values, "4. Value Vectors", tokens, "4_value_vectors.png")

# --- Step 5: Calculate Attention Scores for ONE word ("tower") ---
# We focus on the first token: "tower"
q1 = queries[0]
print_step("Step 5: Select Query vector for 'tower' (q1)", q1)

# Calculation: scores = q1 @ K^T
# This measures the alignment of "tower"'s query with all other keys.
attention_scores = q1 @ keys.T
print_step("Step 5a: Attention Scores (q1 @ K^T)", attention_scores)

# --- Step 6: Scale the Scores ---
# Divide by the square root of the key dimension to stabilize gradients.
scale_factor = np.sqrt(qkv_dim)
scaled_scores = attention_scores / scale_factor
print(f"Scaling factor (sqrt(d_k)): {scale_factor:.4f}\n")
print_step("Step 6: Scaled Attention Scores", scaled_scores)

# --- Step 7: Apply Softmax ---
# Convert scores into probabilities (weights that sum to 1).
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

attention_weights = softmax(scaled_scores)
print_step("Step 7: Softmax -> Attention Weights", attention_weights)

# Visualize the final weights for "tower"
plt.figure(figsize=(8, 1.5))
sns.heatmap(attention_weights.reshape(1, -1), annot=True, cmap='Reds', xticklabels=tokens, yticklabels=["tower"])
plt.title("Attention Weights: How much 'tower' focuses on other tokens")
plt.savefig("5_attention_weights.png")
print("Saved plot: 5_attention_weights.png\n")
plt.close()

# --- Step 8: Calculate the Final Context Vector ---
# The output for "tower" is a weighted sum of all Value vectors.
# Calculation: z1 = Attention_Weights @ V
context_vector = attention_weights @ values
print_step("Step 8: Final Context Vector for 'tower' (z1 = Weights @ V)", context_vector)

print("--- END OF CALCULATION FLOW ---")
