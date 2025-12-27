import numpy as np

# ==========================================
# 1. SETUP: INPUT DATA
# ==========================================
# Imagine we have 2 words ("The", "bank")
# Each word is represented by a vector of size 4.
input_embeddings = np.array([
    [1.0, 0.0, 1.0, 0.0],   # Word 1: "The"
    [0.0, 2.0, 0.0, 2.0]    # Word 2: "bank"
])

print(f"Step 1: Input Shape: {input_embeddings.shape} (2 words, 4 features)\n")

# ==========================================
# 2. THE WEIGHTS (The Brain)
# ==========================================
# In a real model, these are learned during training.
# Here, we initialize them randomly.
d_model = 4   # Input vector size
d_head = 3    # Output Q/K/V vector size

np.random.seed(42) # Fixed seed for consistent results
W_q = np.random.rand(d_model, d_head)  # Query Weights
W_k = np.random.rand(d_model, d_head)  # Key Weights
W_v = np.random.rand(d_model, d_head)  # Value Weights

# ==========================================
# 3. CALCULATE Q, K, V
# ==========================================
# Formula: Vector @ Weight_Matrix
Q = np.dot(input_embeddings, W_q)
K = np.dot(input_embeddings, W_k)
V = np.dot(input_embeddings, W_v)

print("Step 3: Calculated Q, K, V vectors.")
print(f"Q for 'The': {Q[0]}")
print(f"K for 'bank': {K[1]}\n")

# ==========================================
# 4. CALCULATE ATTENTION SCORES
# ==========================================
# Formula: (Q @ K_transpose) / sqrt(d_head)
# This is the "Dot Product" similarity check.

scores = np.dot(Q, K.T) / np.sqrt(d_head)

print("Step 4: Raw Attention Scores (The grid)")
print(f"Row 0 (The) vs [The, bank]: {scores[0]}")
# Example: If scores[0] is [2.5, 0.1], 'The' cares more about itself.
print("")

# ==========================================
# 5. SOFTMAX (Normalization)
# ==========================================
# Convert raw scores into probabilities (0 to 1)

def softmax(x):
    e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e_x / np.sum(e_x, axis=1, keepdims=True)

weights = softmax(scores)

print("Step 5: Probability Weights (Softmax)")
print(f"Row 0 (The) attention distribution: {weights[0]}")
# If this prints [0.9, 0.1], it means 'The' is focusing 90% on itself, 10% on 'bank'.
print("")

# ==========================================
# 6. WEIGHTED SUM (The Result)
# ==========================================
# Formula: Weights @ V
# Mix the Value vectors based on the probabilities.

output = np.dot(weights, V)

print("Step 6: Final Contextualized Output")
print(f"New Vector for 'The': {output[0]}")
print("(This new vector now contains a mix of 'The' info and 'bank' info)")