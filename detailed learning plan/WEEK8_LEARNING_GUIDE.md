# ðŸ“š WEEK 8 LEARNING GUIDE: Chunking, Embeddings & Hybrid Search

**Pre-learning for Steps 13-16 (RAG Semantic Layer)**

**Time Investment:** 5-6 hours over the weekend before Week 8

---

## ðŸŽ¯ LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **Document Chunking** - Why and how to break documents into searchable segments
2. **Vector Embeddings** - How text is transformed into semantic representations
3. **Semantic Search** - k-NN and vector similarity concepts
4. **Hybrid Search** - Combining keyword (BM25) with semantic search
5. **Reciprocal Rank Fusion** - Algorithm for combining multiple rankings
6. **Production Patterns** - Real-world chunking and embedding strategies

**Goal:** Confident enough to implement Steps 13-16 without confusion

---

## ðŸ“– MODULE 1: Document Chunking Fundamentals (1.5 hours)

### **What is Chunking?**

**The Problem:** Research papers are long (10,000+ words), but:
- Embedding models have token limits (512-8192)
- Long texts dilute semantic meaning
- Users ask specific questions, not about entire papers

**The Solution:** Break documents into chunks

**Simple Example:**
```
Paper (15,000 words)
    â†“ Chunking
Chunk 1 (600 words): Introduction
Chunk 2 (600 words): Related Work  
Chunk 3 (600 words): Methodology
Chunk 4 (600 words): Results
...
```

### **Why Chunk?**

1. **Fit embedding model limits:** Most models: 512-8192 tokens
2. **Improve retrieval precision:** Match specific sections, not entire papers
3. **Better LLM context:** Feed relevant chunks to LLM, not full papers
4. **Reduce noise:** Focus on relevant content only

### **Chunking Strategies**

**1. Fixed-Size Chunking:**
```
Split text every N words:
- Chunk 1: Words 0-600
- Chunk 2: Words 500-1100 (100-word overlap)
- Chunk 3: Words 1000-1600
```
âœ… Simple, predictable
âŒ Splits mid-sentence, mid-thought

**2. Sentence-Based Chunking:**
```
Group complete sentences:
- Chunk 1: Sentences 1-15 (~600 words)
- Chunk 2: Sentences 12-27 (overlap)
```
âœ… Preserves sentence boundaries
âŒ Still arbitrary splits

**3. Section-Based Chunking (BEST for papers):**
```
Respect document structure:
- Chunk 1: Introduction section
- Chunk 2: Related Work section
- Chunk 3: Methodology section
```
âœ… Natural semantic boundaries
âœ… Preserves context
âœ… User-aligned (people think in sections)

**4. Semantic Chunking:**
```
Use embeddings to find natural breaks:
- Compare sentence embeddings
- Split when similarity drops
```
âœ… Most intelligent
âŒ Slow, complex

### **Chunking Parameters**

**Chunk Size:** How many words per chunk?
- Too small (100-200): Loss of context
- Too large (2000+): Diluted meaning
- **Sweet spot: 400-800 words**

**Overlap:** How much content repeated between chunks?
- Why? Preserves context across boundaries
- How much? 15-20% of chunk size (~100 words)
- Example: Chunk 1 ends with sentence A, Chunk 2 starts with sentence A

**Context Inclusion:**
```
Without context:
"Our approach uses multi-head attention..."

With context:
"Title: Attention Mechanisms in Neural Networks
Section: 3. Methodology
Our approach uses multi-head attention..."
```

Always include: Title, section heading, relevant metadata

### **Resources**

**Watch (30 min):**
- "Chunking Strategies for RAG" by LlamaIndex: https://www.youtube.com/results?search_query=chunking+strategies+RAG
- Focus on: Fixed vs semantic chunking

**Read (45 min):**
- "Chunking Strategies for LLMs": https://www.pinecone.io/learn/chunking-strategies/
- Research paper: "Late Chunking" (Jina AI): https://arxiv.org/abs/2409.04701

**Hands-on (15 min):**
- Think: How would you chunk a news article?
- Consider: Title, paragraphs, quotes, author

---

## ðŸ“– MODULE 2: Vector Embeddings Deep Dive (1.5 hours)

### **What are Embeddings?**

**Definition:** Dense vector representations of text that capture semantic meaning

**Simple Analogy:**
```
Words as coordinates in space:
- "king" â†’ [0.8, 0.3, -0.1, ...]
- "queen" â†’ [0.7, 0.4, -0.1, ...]
- "car" â†’ [-0.2, 0.9, 0.5, ...]

Similar meaning = nearby in space
```

**Why Embeddings?**

Traditional search: Exact word matching
```
Query: "car"
Matches: "car" âœ“
Doesn't match: "automobile", "vehicle" âœ—
```

Embedding search: Semantic matching
```
Query embedding: [0.1, 0.8, ...]
Similar: "automobile" (cosine: 0.92)
Similar: "vehicle" (cosine: 0.87)
Dissimilar: "banana" (cosine: 0.12)
```

### **How Embeddings Work**

**1. Tokenization:**
```
"Machine learning" â†’ ["Machine", "learning"]
```

**2. Encode with neural network:**
```
Neural network (millions of parameters)
    â†“
[0.123, -0.456, 0.789, ..., 0.234]  # 1024 dimensions
```

**3. Properties:**
- Same dimension for all texts (e.g., 1024)
- Normalized to unit length (length = 1)
- Semantic similarity = vector similarity

### **Similarity Metrics**

**Cosine Similarity (Most Common):**
```python
cosine_sim(A, B) = dot(A, B) / (||A|| Ã— ||B||)

Range: [-1, 1]
- 1.0: Identical meaning
- 0.0: Unrelated
- -1.0: Opposite meaning
```

**Example:**
```
"neural networks" vs "deep learning": 0.85 (very similar)
"neural networks" vs "pasta recipe": 0.05 (unrelated)
```

**Other Metrics:**
- **L2 Distance:** Euclidean distance (smaller = more similar)
- **Dot Product:** Raw similarity (unnormalized)

### **Embedding Models**

**Popular Models:**
1. **OpenAI text-embedding-3-large:**
   - Dimensions: 3072
   - Context: 8191 tokens
   - Cost: $$

2. **Jina AI jina-embeddings-v3:**
   - Dimensions: 1024
   - Context: 8192 tokens
   - Task-specific: retrieval.passage, retrieval.query
   - FREE tier: 1M tokens/month

3. **Sentence-Transformers (Open-source):**
   - Various models
   - Run locally
   - No API costs

### **Task-Specific Embeddings (Important!)**

**Why different tasks?**

Query: "What are transformers?"
- Short, question form
- User intent

Document: "Transformers are neural network architectures that use attention mechanisms to process sequential data efficiently..."
- Long, informative
- Contains answer

**Asymmetric Search:**
```
embed_query("What are transformers?")
    task="retrieval.query"
    â†’ [0.1, 0.8, ...]

embed_document("Transformers are...")
    task="retrieval.passage"
    â†’ [0.11, 0.79, ...]
```

Both optimized for matching across query-document gap.

### **Resources**

**Watch (45 min):**
- "Embeddings Explained" by 3Blue1Brown: https://www.youtube.com/watch?v=wjZofJX0v4M
- "Vector Similarity Search" by Weaviate: https://www.youtube.com/results?search_query=vector+similarity+search

**Read (30 min):**
- OpenAI Embeddings Guide: https://platform.openai.com/docs/guides/embeddings
- Jina AI Embeddings: https://jina.ai/embeddings

**Hands-on (15 min):**
- Calculate cosine similarity by hand:
  ```
  A = [1, 0, 0]
  B = [0.7, 0.7, 0]
  
  dot(A, B) = 1Ã—0.7 + 0Ã—0.7 + 0Ã—0 = 0.7
  ||A|| = 1
  ||B|| = sqrt(0.7Â² + 0.7Â²) = 0.99
  cosine = 0.7 / (1 Ã— 0.99) = 0.707
  ```

---

## ðŸ“– MODULE 3: k-NN and Vector Search (1 hour)

### **What is k-NN?**

**k-Nearest Neighbors:** Find k most similar vectors

**Example:**
```
Query embedding: [0.5, 0.8, ...]

All document embeddings:
doc_1: [0.51, 0.79, ...] â†’ cosine: 0.98 âœ“
doc_2: [0.1, 0.2, ...]   â†’ cosine: 0.23
doc_3: [0.49, 0.81, ...] â†’ cosine: 0.96 âœ“
doc_4: [-0.3, 0.1, ...]  â†’ cosine: 0.15
doc_5: [0.52, 0.78, ...] â†’ cosine: 0.97 âœ“

k=3 â†’ Return: doc_1, doc_5, doc_3
```

### **Exact vs Approximate k-NN**

**Exact k-NN:**
- Compare query to ALL vectors
- Guaranteed to find true k-nearest
- Slow for large datasets (millions of vectors)

**Approximate k-NN (ANN):**
- Use index structure (HNSW, IVF)
- Fast (milliseconds)
- ~95% recall (finds 95% of true k-nearest)

### **HNSW Algorithm**

**Hierarchical Navigable Small World**

**Concept:** Multi-layer graph for fast search

```
Layer 2:  o â†â†’ o â†â†’ o       (Sparse, long jumps)
          â†“    â†“    â†“
Layer 1:  oâ†’oâ†’oâ†’oâ†’oâ†’oâ†’o     (Medium density)
          â†“ â†“ â†“ â†“ â†“ â†“ â†“
Layer 0:  oâ†’oâ†’oâ†’oâ†’oâ†’oâ†’oâ†’oâ†’o (Dense, all vectors)

Search: Start at top layer, navigate down
```

**Parameters:**
- `M`: Connections per node (16-32)
  - Higher = better recall, more memory
- `ef_construction`: Build quality (128-512)
  - Higher = better index, slower build
- `ef_search`: Search quality (100-500)
  - Higher = better recall, slower search

**Trade-offs:**
```
Higher M & ef:
âœ… Better recall (find true nearest)
âœ… Better accuracy
âŒ More memory
âŒ Slower search
```

### **Resources**

**Watch (20 min):**
- "HNSW Algorithm Explained": https://www.youtube.com/results?search_query=HNSW+algorithm+explained

**Read (40 min):**
- HNSW paper (skim): https://arxiv.org/abs/1603.09320
- OpenSearch k-NN: https://opensearch.org/docs/latest/search-plugins/knn/

---

## ðŸ“– MODULE 4: Hybrid Search & RRF Fusion (1 hour)

### **Why Hybrid Search?**

**The Reality:** Neither BM25 nor vector search is perfect

**BM25 Strengths:**
âœ… Exact term matching ("GPT-4", "BERT")
âœ… Named entities (authors, organizations)
âœ… Acronyms, technical terms
âœ… Fast (~50ms)

**BM25 Weaknesses:**
âŒ Synonym problem ("automobile" vs "car")
âŒ Paraphrasing ("What is attention?" vs "Explain attention mechanisms")
âŒ No semantic understanding

**Vector Search Strengths:**
âœ… Semantic similarity
âœ… Handles synonyms
âœ… Understands paraphrasing
âœ… Conceptual matching

**Vector Search Weaknesses:**
âŒ Exact term matching harder
âŒ Slower (~200ms)
âŒ More expensive (embedding generation)

**Solution: Hybrid = BM25 + Vector**

### **Combining Rankings: RRF**

**Reciprocal Rank Fusion (RRF)**

**Problem:** How to combine two different rankings?

BM25 results:
1. doc_A (score: 8.2)
2. doc_B (score: 7.1)
3. doc_C (score: 6.8)

Vector results:
1. doc_C (score: 0.95)
2. doc_A (score: 0.92)
3. doc_D (score: 0.88)

**Can't average scores!** Different scales (BM25: 0-10, Vector: 0-1)

**RRF Formula:**
```
For each document d:
  RRF_score(d) = Î£ (1 / (k + rank(d)))

Where:
- k = constant (typically 60)
- rank(d) = position in ranking (1, 2, 3, ...)
- Î£ = sum across all rankings
```

**Example Calculation:**
```
doc_A:
  BM25 rank: 1 â†’ 1/(60+1) = 0.0164
  Vector rank: 2 â†’ 1/(60+2) = 0.0161
  RRF total: 0.0325

doc_B:
  BM25 rank: 2 â†’ 1/(60+2) = 0.0161
  Vector rank: not in top 3 â†’ 0
  RRF total: 0.0161

doc_C:
  BM25 rank: 3 â†’ 1/(60+3) = 0.0159
  Vector rank: 1 â†’ 1/(60+1) = 0.0164
  RRF total: 0.0323

doc_D:
  BM25 rank: not in top 3 â†’ 0
  Vector rank: 3 â†’ 1/(60+3) = 0.0159
  RRF total: 0.0159

Final ranking: doc_A (0.0325) > doc_C (0.0323) > doc_B > doc_D
```

**Why k=60?**
- Empirically tested
- Balances top vs lower ranks
- Not too sensitive to small rank differences

### **Hybrid Search Performance**

**Benchmarks (typical):**

| Metric | BM25 | Vector | Hybrid |
|--------|------|--------|--------|
| Precision@10 | 0.67 | 0.72 | **0.84** |
| Recall@10 | 0.71 | 0.78 | **0.89** |
| Latency | 50ms | 200ms | 400ms |

Hybrid = Best accuracy, slower speed

### **Resources**

**Read (45 min):**
- "Hybrid Search Explained" by Pinecone: https://www.pinecone.io/learn/hybrid-search-intro/
- "Reciprocal Rank Fusion": Original paper (skim)

**Watch (15 min):**
- "Hybrid Search in Practice": https://www.youtube.com/results?search_query=hybrid+search+explained

---

## ðŸ“– MODULE 5: Production Chunking Strategies (45 min)

### **Real-World Considerations**

**1. Context Preservation:**
```
Bad chunk:
"Our approach achieved 95% accuracy."

Good chunk:
"Title: Novel Attention Mechanism
Section: 4. Results
Our approach achieved 95% accuracy on the ImageNet dataset..."
```

**2. Overlap Strategy:**
```
Chunk 1: Sentences 1-20
Chunk 2: Sentences 18-38  (overlap: 18-20)
Chunk 3: Sentences 36-56  (overlap: 36-38)
```

Why? Query might span boundary.

**3. Metadata:**
```python
{
  "chunk_id": 3,
  "section_heading": "Methodology",
  "chunk_type": "section",  # vs "sliding_window"
  "word_count": 587,
  "position": "middle"  # "start", "middle", "end"
}
```

### **Chunking Best Practices**

1. **Respect structure** when available (sections, paragraphs)
2. **Include context** (title, section, relevant metadata)
3. **Use overlap** (15-20% of chunk size)
4. **Reasonable size** (400-800 words for research papers)
5. **Track metadata** (section, type, position)
6. **Test retrieval quality** (does it answer questions?)

### **Resources**

**Read (30 min):**
- "Advanced Chunking Strategies": https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5

**Watch (15 min):**
- "Production RAG Tips": https://www.youtube.com/results?search_query=production+RAG+tips

---

## ðŸ“– MODULE 6: Jina AI & Production Embeddings (30 min)

### **Jina AI Overview**

**What:** Commercial embedding API
**Models:** jina-embeddings-v3 (1024 dimensions)
**Free Tier:** 1M tokens/month
**Features:**
- Task-specific embeddings
- High quality
- 8192 token context

### **API Usage**

**Endpoint:**
```
POST https://api.jina.ai/v1/embeddings
```

**Request:**
```json
{
  "model": "jina-embeddings-v3",
  "task": "retrieval.passage",
  "dimensions": 1024,
  "input": ["Text to embed"]
}
```

**Response:**
```json
{
  "model": "jina-embeddings-v3",
  "data": [
    {
      "embedding": [0.123, -0.456, ..., 0.789],
      "index": 0
    }
  ]
}
```

### **Batch Processing**

**Limits:**
- Max 32 texts per request
- Max 8192 tokens per text

**Strategy:**
```python
# Don't do this (slow):
for chunk in chunks:
    embed(chunk)  # 100 API calls

# Do this (fast):
batches = chunks[0:32], chunks[32:64], ...
for batch in batches:
    embed(batch)  # 4 API calls
```

### **Resources**

**Read (20 min):**
- Jina AI Docs: https://jina.ai/embeddings
- API Reference: https://api.jina.ai/redoc

**Try (10 min):**
- Get free API key
- Test embedding API with curl

---

## ðŸŽ“ LEARNING SCHEDULE

**Weekend Before Week 8:**

**Saturday (3 hours):**
- Module 1: Chunking Fundamentals (1.5h)
- Module 2: Vector Embeddings (1.5h)

**Sunday (3 hours):**
- Module 3: k-NN & Vector Search (1h)
- Module 4: Hybrid Search & RRF (1h)
- Module 5: Production Chunking (45min)
- Module 6: Jina AI (30min)
- Hands-on exercises (30min)

**Total:** 5-6 hours

---

## ðŸŽ¯ KEY TAKEAWAYS

**Remember these 8 things:**

1. **Chunking = Breaking documents into searchable pieces**
   - Sweet spot: 400-800 words
   - Always include context (title, section)

2. **Embeddings = Semantic vectors**
   - Similar meaning = nearby in vector space
   - Cosine similarity measures closeness

3. **k-NN = Find k nearest vectors**
   - Approximate (HNSW) is fast enough
   - Trade-off: speed vs accuracy

4. **BM25 = Keyword precision**
   - Fast, exact matching
   - Misses synonyms

5. **Vector = Semantic understanding**
   - Handles paraphrasing
   - Slower, more expensive

6. **Hybrid = Best of both worlds**
   - Combine with RRF
   - Best accuracy

7. **Task-specific embeddings**
   - retrieval.passage for documents
   - retrieval.query for queries

8. **Batch processing = Efficiency**
   - 32 texts per API call
   - Huge performance gain

**If you understand these 8:** You're 90% ready! âœ…

---

## ðŸš€ NEXT STEPS

After completing this guide:

1. **Review key concepts** (8 takeaways above)
2. **Get Jina API key** (free tier)
3. **Start Step 13** (Text Chunking)
4. **Reference this guide** during Steps 13-16

**Remember:** Understanding concepts > memorizing code

---

## ðŸ§ª HANDS-ON EXERCISES

### **Exercise 1: Chunking Practice**

Take this text and chunk it:
```
Title: Machine Learning Fundamentals

Introduction:
Machine learning is a subset of artificial intelligence that enables computers to learn from data. Unlike traditional programming, ML systems improve their performance through experience.

Methodology:
We used a neural network with three hidden layers. Each layer contained 128 neurons with ReLU activation. Training took 50 epochs on the MNIST dataset.

Results:
Our model achieved 98.5% accuracy on the test set, outperforming the baseline by 12%. Training time was approximately 2 hours on a single GPU.
```

**Questions:**
1. How would you chunk this with section-based strategy?
2. How would you add context to each chunk?
3. Where would you add overlap?

### **Exercise 2: Cosine Similarity**

Given these embeddings (simplified to 3D):
```
query = [0.8, 0.2, 0.1]
doc_1 = [0.7, 0.3, 0.1]
doc_2 = [0.1, 0.8, 0.5]
```

Calculate cosine similarity for both documents.
Which is more relevant?

### **Exercise 3: RRF Calculation**

Given:
```
BM25 ranking: [doc_A, doc_B, doc_C]
Vector ranking: [doc_C, doc_A, doc_D]
```

Calculate RRF scores (k=60) and final ranking.

---

**Document Generated:** December 25, 2024  
**Purpose:** Pre-learning for Week 8 (Steps 13-16)  
**Time Required:** 5-6 hours  
**Format:** Self-paced learning modules
