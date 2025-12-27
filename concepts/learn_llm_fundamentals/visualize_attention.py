import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gensim.downloader as api

# --- 1. Setup: Words and Model ---
# Your list of words (tokens)
tokens = ["tower", "building", "sky", "river", "man", "woman"]

# Load a pre-trained model (e.g., GloVe with 50 dimensions)
# This might take a few minutes on the first run as it downloads the model
print("Loading GloVe model...")
model = api.load("glove-wiki-gigaword-50")
embedding_dim = model.vector_size
print("Model loaded.")

# --- 2. Get Embeddings for Tokens ---
# Each token is converted into its corresponding embedding vector
embeddings = np.array([model[word] for word in tokens])

# --- 3. Simulate Self-Attention Projections ---
# In a real Transformer, these weight matrices (W_q, W_k, W_v) are learned during training.
# Here, we'll create random weight matrices to simulate the projection process.
# The dimension of Q, K, V vectors is often smaller than the embedding dimension.
qkv_dim = 32

np.random.seed(42) # for reproducibility
W_q = np.random.rand(embedding_dim, qkv_dim)
W_k = np.random.rand(embedding_dim, qkv_dim)
W_v = np.random.rand(embedding_dim, qkv_dim)

# Project embeddings into Query, Key, and Value spaces
# This is the core operation: Matrix multiplication
queries = np.dot(embeddings, W_q)
keys = np.dot(embeddings, W_k)
values = np.dot(embeddings, W_v)

# --- 4. Visualization ---
def plot_matrix(matrix, title, y_labels):
    """Helper function to plot a matrix as a heatmap."""
    plt.figure(figsize=(10, 4))
    sns.heatmap(matrix, cmap='viridis', yticklabels=y_labels)
    plt.title(title)
    plt.xlabel("Vector Dimensions")
    plt.ylabel("Tokens")
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    print(f"Saved plot: {title.replace(' ', '_').lower()}.png")

# Plot each matrix
plot_matrix(embeddings, "1. Word Embeddings", tokens)
plot_matrix(queries, "2. Query Vectors", tokens)
plot_matrix(keys, "3. Key Vectors", tokens)
plot_matrix(values, "4. Value Vectors", tokens)

# --- 5. Bonus: Attention Scores ---
# To complete the picture, let's calculate the attention scores for the first token ("tower")
# Attention_Scores = (Query_of_token_1 * Key_of_all_tokens^T) / sqrt(d_k)
attention_scores = np.dot(queries[0], keys.T) / np.sqrt(qkv_dim)

# Apply softmax to get the attention weights (how much "tower" should focus on each other token)
attention_weights = np.exp(attention_scores) / np.sum(np.exp(attention_scores))

# Plot the attention weights
plt.figure(figsize=(8, 2))
sns.heatmap(attention_weights.reshape(1, -1), annot=True, cmap='Reds', xticklabels=tokens, yticklabels=["tower"])
plt.title("5. Attention Weights (Focus of 'tower')")
plt.savefig("5_attention_weights.png")
print("Saved plot: 5_attention_weights.png")

print("\nScript finished. Check the generated PNG files in your project directory.")
