# WEEK 8 LEARNING GUIDE: Chunking, Embeddings & Hybrid Search

**Pre-learning for Steps 13-16 (RAG Semantic Layer)**

**Time Investment:** 5-6 hours over the weekend before Week 8

---

## LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **Document Chunking** - Why and how to break documents into searchable segments
2. **Vector Embeddings** - How text is transformed into semantic representations
3. **Semantic Search** - k-NN and vector similarity concepts
4. **Hybrid Search** - Combining keyword (BM25) with semantic search
5. **Reciprocal Rank Fusion** - Algorithm for combining multiple rankings
6. **Production Patterns** - Real-world chunking and embedding strategies

**Goal:** Confident enough to implement Steps 13-16 without confusion

---

## WHAT YOU ALREADY KNOW (from Weeks 3-7)

[CHECK] **Weeks 3-4 (MOAI Weeks 1-2):**
- Docker, PostgreSQL, FastAPI fundamentals
- Airflow orchestration
- PDF parsing and data ingestion

[CHECK] **Week 7 (MOAI Week 3):**
- OpenSearch infrastructure
- BM25 keyword search
- Index creation and document indexing
- Basic search API endpoints

**You now have:**
- Papers stored in PostgreSQL with full text
- OpenSearch cluster running
- BM25 search working
- /api/v1/search endpoint functional

**Week 8 Focus:**
Adding the **semantic layer**:
- Breaking documents into chunks
- Generating embeddings
- Vector search capabilities
- Combining keyword + semantic search

---

## LEARNING SCHEDULE

### **Saturday/Sunday Before Week Starts (5-6 hours)**

**Recommended pre-learning:**
- Document chunking fundamentals (1.5 hours)
- Vector embeddings deep dive (1.5 hours)
- k-NN and vector search (1 hour)
- Hybrid search and RRF (1 hour)
- Production chunking patterns (45 minutes)
- Jina AI embedding service (30 minutes)

### **During Week (as needed)**

**Monday-Tuesday:**
- Chunking strategy decision making (30 min)
- Embedding model selection (30 min)

**Wednesday-Thursday:**
- k-NN algorithm deep dive (30 min)
- RRF implementation details (30 min)

**Friday:**
- Review and integration planning (1 hour)

---

## CORE LEARNING MODULES

### **MODULE 1: Document Chunking Fundamentals** [TIME] 90 minutes

#### **1.1 What is Chunking?** (30 min)

**The Problem:** Research papers are long (10,000+ words), but:
- Embedding models have token limits (512-8192)
- Long texts dilute semantic meaning
- Users ask specific questions, not about entire papers

**The Solution:** Break documents into chunks

**Simple Example:**
```
Paper (15,000 words)
    |
    v Chunking
    |
Chunk 1 (600 words): Introduction
Chunk 2 (600 words): Related Work  
Chunk 3 (600 words): Methodology
Chunk 4 (600 words): Results
...
```

**Why Chunk?**

1. **Fit embedding model limits:** Most models: 512-8192 tokens
2. **Improve retrieval precision:** Match specific sections, not entire papers
3. **Better LLM context:** Feed relevant chunks to LLM, not full papers
4. **Reduce noise:** Focus on relevant content only

**Video:**
[VIDEO] **"Chunking Strategies for RAG"** - LlamaIndex  
URL: https://www.youtube.com/results?search_query=chunking+strategies+RAG  
Watch: Any comprehensive video on chunking (15-20 min)

**Reading:**
[BOOK] **"Chunking Strategies for LLMs"** - Pinecone  
URL: https://www.pinecone.io/learn/chunking-strategies/  
Read: Complete guide (15 min)

#### **1.2 Chunking Strategies** (30 min)

**1. Fixed-Size Chunking:**
```
Split text every N words:
- Chunk 1: Words 0-600
- Chunk 2: Words 500-1100 (100-word overlap)
- Chunk 3: Words 1000-1600
```
[CHECK] Simple, predictable
[X] Splits mid-sentence, mid-thought

**2. Sentence-Based Chunking:**
```
Group complete sentences:
- Chunk 1: Sentences 1-15 (~600 words)
- Chunk 2: Sentences 12-27 (overlap)
```
[CHECK] Preserves sentence boundaries
[X] Still arbitrary splits

**3. Section-Based Chunking (BEST for papers):**
```
Respect document structure:
- Chunk 1: Introduction section
- Chunk 2: Related Work section
- Chunk 3: Methodology section
```
[CHECK] Natural semantic boundaries
[CHECK] Preserves context
[CHECK] User-aligned (people think in sections)

**4. Semantic Chunking:**
```
Use embeddings to find natural breaks:
- Compare sentence embeddings
- Split when similarity drops
```
[CHECK] Most intelligent
[X] Slow, complex

**Reading:**
[BOOK] **"Late Chunking"** - Jina AI Research Paper  
URL: https://arxiv.org/abs/2409.04701  
Read: Abstract and Introduction (10 min)

#### **1.3 Chunking Parameters** (30 min)

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

**Metadata Tracking:**

**1. Chunk Identification:**
```
{
  "paper_id": "2304.12345",
  "chunk_id": 3,
  "chunk_index": 2  # 0-indexed position
}
```

**2. Position Information:**
```
{
  "section_heading": "Methodology",
  "start_char": 1250,
  "end_char": 1850,
  "word_count": 587
}
```

**3. Metadata:**
```
{
  "chunk_type": "section",  # vs "sliding_window"
  "position": "middle",  # "start", "middle", "end"
  "has_figures": true,
  "has_equations": false
}
```

**Chunking Best Practices:**

1. **Respect structure** when available (sections, paragraphs)
2. **Include context** (title, section, relevant metadata)
3. **Use overlap** (15-20% of chunk size)
4. **Reasonable size** (400-800 words for research papers)
5. **Track metadata** (section, type, position)
6. **Test retrieval quality** (does it answer questions?)

**Additional Reading:**
[BOOK] **"Advanced Chunking Strategies"** - LlamaIndex  
URL: https://www.llamaindex.ai/blog/evaluating-the-ideal-chunk-size-for-a-rag-system-using-llamaindex-6207e5d3fec5  
Read: Evaluation methodology (10 min)

---

### **MODULE 2: Vector Embeddings Deep Dive** [TIME] 90 minutes

#### **2.1 What are Embeddings?** (30 min)

**Definition:** Dense vector representations of text that capture semantic meaning

**Simple Analogy:**
```
Words as coordinates in space:
- "king" -> [0.8, 0.3, -0.1, ...]
- "queen" -> [0.7, 0.4, -0.1, ...]
- "car" -> [-0.2, 0.9, 0.5, ...]

Similar meaning = nearby in space
```

**Why Embeddings?**

Traditional search: Exact word matching
```
Query: "car"
Matches: "car" [CHECK]
Doesn't match: "automobile", "vehicle" [X]
```

Embedding search: Semantic matching
```
Query embedding: [0.1, 0.8, ...]
Similar: "automobile" (cosine: 0.92)
Similar: "vehicle" (cosine: 0.87)
Dissimilar: "banana" (cosine: 0.12)
```

**Video:**
[VIDEO] **"Embeddings Explained"** - 3Blue1Brown  
URL: https://www.youtube.com/watch?v=wjZofJX0v4M  
Watch: First 20 minutes (core concepts)

**Reading:**
[BOOK] **"What are Embeddings?"** - OpenAI  
URL: https://platform.openai.com/docs/guides/embeddings  
Read: "What are embeddings" and "Use cases" sections (10 min)

#### **2.2 How Embeddings Work** (30 min)

**1. Tokenization:**
```
"Machine learning" -> ["Machine", "learning"]
```

**2. Encode with neural network:**
```
Neural network (millions of parameters)
    |
    v
[0.123, -0.456, 0.789, ..., 0.234]  # 1024 dimensions
```

**3. Properties:**
- Same dimension for all texts (e.g., 1024)
- Normalized to unit length (length = 1)
- Semantic similarity = vector similarity

**Similarity Metrics:**

**Cosine Similarity (Most Common):**
```
cosine_sim(A, B) = dot(A, B) / (||A|| x ||B||)

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

**Hands-on Calculation:**

Calculate cosine similarity by hand:
```
A = [1, 0, 0]
B = [0.7, 0.7, 0]

dot(A, B) = 1×0.7 + 0×0.7 + 0×0 = 0.7
||A|| = 1
||B|| = sqrt(0.7² + 0.7²) = 0.99
cosine = 0.7 / (1 × 0.99) = 0.707
```

**Reading:**
[BOOK] **"Vector Similarity Search"** - Weaviate  
URL: https://weaviate.io/developers/weaviate/concepts/vector-index  
Read: Similarity metrics section (10 min)

#### **2.3 Embedding Models** (30 min)

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

**Task-Specific Embeddings (Important!)**

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
    -> [0.1, 0.8, ...]

embed_document("Transformers are...")
    task="retrieval.passage"
    -> [0.11, 0.79, ...]
```

Both optimized for matching across query-document gap.

**Reading:**
[BOOK] **"Jina AI Embeddings Documentation"**  
URL: https://jina.ai/embeddings  
Read: Task-specific embeddings section (10 min)

---

### **MODULE 3: k-NN and Vector Search** [TIME] 60 minutes

#### **3.1 What is k-NN?** (20 min)

**k-Nearest Neighbors:** Find the k closest vectors to a query vector

**Simple Example:**
```
Query: "transformers in ML"
Query embedding: [0.8, 0.2, 0.1]

Documents in database:
Doc 1: [0.7, 0.3, 0.1] -> similarity: 0.95 (very close!)
Doc 2: [0.1, 0.8, 0.5] -> similarity: 0.32 (far)
Doc 3: [0.75, 0.25, 0.1] -> similarity: 0.98 (very close!)

k=2 nearest neighbors: Doc 3, Doc 1
```

**The Challenge:** Searching millions of vectors is slow

**Naive approach:**
```
For each document:
  Calculate similarity with query
  
With 1M documents: 1M calculations per search
Too slow for production!
```

**Video:**
[VIDEO] **"Vector Search Explained"** - Pinecone  
URL: https://www.youtube.com/results?search_query=vector+search+explained  
Watch: Any comprehensive overview (15 min)

#### **3.2 Approximate Nearest Neighbor (ANN)** (20 min)

**Solution:** Approximate algorithms that trade accuracy for speed

**HNSW (Hierarchical Navigable Small World):**
- Most popular ANN algorithm
- Used by OpenSearch, Pinecone, Weaviate
- 100-1000x faster than exact search
- 95-99% accuracy

**How HNSW works (conceptual):**
```
Build a graph where similar vectors are connected:

Layer 2 (sparse):   A -------- B
                    |          |
Layer 1 (medium):   A -- C -- B -- D
                    |    |    |    |
Layer 0 (dense):    A-C-E-F-B-D-G-H

Search:
1. Start at top layer (fast jumps)
2. Navigate to approximate region
3. Drill down to lower layers
4. Find exact nearest neighbors
```

**Trade-offs:**
- **ef_construction:** Build quality (higher = slower build, better search)
- **ef_search:** Search quality (higher = slower search, better accuracy)
- **M:** Connections per node (higher = more memory, better recall)

**Reading:**
[BOOK] **"HNSW Explained"** - Pinecone  
URL: https://www.pinecone.io/learn/series/faiss/hnsw/  
Read: Algorithm overview and trade-offs (15 min)

#### **3.3 Vector Search in OpenSearch** (20 min)

**OpenSearch k-NN Plugin:**
- Uses HNSW algorithm
- Integrated with OpenSearch index
- Supports filtering with BM25

**Index Configuration:**
```
{
  "mappings": {
    "properties": {
      "embedding": {
        "type": "knn_vector",
        "dimension": 1024,
        "method": {
          "name": "hnsw",
          "engine": "nmslib",
          "parameters": {
            "ef_construction": 128,
            "m": 16
          }
        }
      }
    }
  }
}
```

**Search Query:**
```
{
  "query": {
    "knn": {
      "embedding": {
        "vector": [0.1, 0.8, ...],
        "k": 10
      }
    }
  }
}
```

**Reading:**
[BOOK] **"OpenSearch k-NN Plugin"**  
URL: https://opensearch.org/docs/latest/search-plugins/knn/index/  
Read: Getting started and k-NN search sections (10 min)

---

### **MODULE 4: Hybrid Search & RRF** [TIME] 60 minutes

#### **4.1 Why Hybrid Search?** (20 min)

**BM25 (Keyword) Strengths:**
- [CHECK] Exact term matching
- [CHECK] Fast (no embedding needed)
- [CHECK] Handles rare terms well
- [X] Misses paraphrasing
- [X] No semantic understanding

**Vector (Semantic) Strengths:**
- [CHECK] Understands meaning
- [CHECK] Handles synonyms
- [CHECK] Cross-language potential
- [X] Slower (embedding + ANN)
- [X] Can miss exact terms

**Example:**

Query: "attention mechanism"

**BM25 finds:**
1. Paper with "attention mechanism" 20 times [CHECK]
2. Paper mentioning "self-attention" [CHECK]
3. Misses: "query-key-value architecture" [X]

**Vector finds:**
1. "query-key-value architecture" (semantically similar) [CHECK]
2. "multi-head attention layers" [CHECK]
3. Misses: Exact term "attention mechanism" might rank lower [X]

**Hybrid = Best of both worlds**

**Video:**
[VIDEO] **"Hybrid Search Explained"** - Weaviate  
URL: https://www.youtube.com/results?search_query=hybrid+search+weaviate  
Watch: Concept and benefits (15 min)

#### **4.2 Reciprocal Rank Fusion (RRF)** (25 min)

**The Problem:** How to combine two ranked lists?

**BM25 ranking:**
```
1. Paper A (score: 15.2)
2. Paper B (score: 12.1)
3. Paper C (score: 8.5)
```

**Vector ranking:**
```
1. Paper C (score: 0.95)
2. Paper A (score: 0.87)
3. Paper D (score: 0.82)
```

**How to merge?** Can't just add scores (different scales!)

**RRF Algorithm:**

For each paper, calculate:
```
RRF_score = sum(1 / (k + rank))

Where:
- k = constant (typically 60)
- rank = position in that ranking (1, 2, 3, ...)
```

**Example Calculation:**

Paper A:
- BM25 rank: 1 -> 1/(60+1) = 0.0164
- Vector rank: 2 -> 1/(60+2) = 0.0161
- RRF score: 0.0164 + 0.0161 = 0.0325

Paper B:
- BM25 rank: 2 -> 1/(60+2) = 0.0161
- Vector rank: not in top 3 -> 0
- RRF score: 0.0161

Paper C:
- BM25 rank: 3 -> 1/(60+3) = 0.0159
- Vector rank: 1 -> 1/(60+1) = 0.0164
- RRF score: 0.0159 + 0.0164 = 0.0323

**Final ranking:** Paper A, Paper C, Paper B

**Why RRF works:**
- Scale-independent (uses ranks, not scores)
- Favors papers appearing in both lists
- Constant k controls blend (lower = more fusion)
- Simple, fast, effective

**Reading:**
[BOOK] **"Reciprocal Rank Fusion"** - Original Paper  
URL: https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf  
Read: Abstract and Section 2 (10 min)

#### **4.3 Implementing Hybrid Search** (15 min)

**Workflow:**

```
1. User query: "What are transformers?"
   |
2. Generate query embedding
   |
3. Parallel search:
   |
   +-> BM25 search -> [Paper A, Paper B, Paper C]
   |
   +-> Vector search -> [Paper C, Paper A, Paper D]
   |
4. Apply RRF
   |
5. Return merged ranking -> [Paper A, Paper C, Paper B, Paper D]
```

**Configuration Decisions:**

1. **Top-k per method:** How many results from each?
   - Typically: 10-20 from each
   - Then merge to final top-k (e.g., 5)

2. **RRF constant k:**
   - Default: 60
   - Lower (30): More aggressive blending
   - Higher (100): More conservative

3. **Boosting:**
   - BM25 weight: 0.5
   - Vector weight: 0.5
   - Adjust based on use case

**Reading:**
[BOOK] **"Hybrid Search Best Practices"** - Elastic  
URL: https://www.elastic.co/blog/improving-search-relevance-with-hybrid-search  
Read: Implementation patterns (10 min)

---

### **MODULE 5: Production Chunking Patterns** [TIME] 45 minutes

#### **5.1 Chunking for Different Content Types** (15 min)

**Research Papers:**
- Strategy: Section-based
- Size: 400-800 words
- Overlap: 100 words
- Context: Title + section + authors

**News Articles:**
- Strategy: Paragraph-based
- Size: 200-400 words
- Overlap: 50 words
- Context: Title + date + author

**Books:**
- Strategy: Chapter + section
- Size: 800-1200 words
- Overlap: 150 words
- Context: Book title + chapter + section

**Code Documentation:**
- Strategy: Function/class-based
- Size: 100-300 words
- Overlap: Minimal
- Context: Module + class + function name

#### **5.2 Quality Evaluation** (15 min)

**How to test chunk quality:**

1. **Retrieval Precision:**
   - Ask 10 sample questions
   - Check if relevant chunks are retrieved
   - Target: >80% precision

2. **Chunk Coherence:**
   - Read random chunks
   - Do they make sense standalone?
   - Is context preserved?

3. **Coverage:**
   - Are all sections represented?
   - No important content lost?

4. **LLM Context Quality:**
   - Feed chunks to LLM
   - Does it generate good answers?
   - Are citations accurate?

**Metrics to Track:**

- **Average chunk size:** Should be consistent
- **Chunk count per document:** Reasonable distribution?
- **Overlap percentage:** 15-20% target
- **Empty chunks:** Should be 0
- **Very small chunks (<100 words):** Minimize these

#### **5.3 Common Pitfalls** (15 min)

**What NOT to do:**

[X] **Don't ignore structure:**
- Bad: Fixed 500-word windows
- Good: Respect sections, paragraphs

[X] **Don't use zero overlap:**
- Bad: Hard boundaries between chunks
- Good: 15-20% overlap preserves context

[X] **Don't omit metadata:**
- Bad: Just text content
- Good: Title, section, position

[X] **Don't chunk too small:**
- Bad: 50-word chunks
- Good: 400-800 words for papers

[X] **Don't chunk too large:**
- Bad: 5000-word chunks
- Good: Fit within embedding model limits

[X] **Don't forget context:**
- Bad: "Our approach uses..."
- Good: "Title: X, Section: Methods - Our approach uses..."

**Best Practices Checklist:**

- [ ] Respect document structure
- [ ] Include 15-20% overlap
- [ ] Add metadata (title, section, position)
- [ ] Target 400-800 words for papers
- [ ] Test with sample questions
- [ ] Validate chunk coherence
- [ ] Track quality metrics
- [ ] Iterate based on retrieval results

---

### **MODULE 6: Jina AI & Production Embeddings** [TIME] 30 minutes

#### **6.1 Jina AI Overview** (10 min)

**What:** Commercial embedding API  
**Models:** jina-embeddings-v3 (1024 dimensions)  
**Free Tier:** 1M tokens/month  

**Features:**
- Task-specific embeddings
- High quality (state-of-the-art)
- 8192 token context
- Fast inference
- Simple REST API

**Why Jina AI for this project:**
- Free tier sufficient for learning
- Production-grade quality
- Task-specific optimization
- Well-documented API
- Good community support

**Reading:**
[BOOK] **"Jina AI Embeddings"**  
URL: https://jina.ai/embeddings  
Read: Overview and features (5 min)

#### **6.2 API Usage** (10 min)

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
  ],
  "usage": {
    "total_tokens": 15,
    "prompt_tokens": 15
  }
}
```

**Reading:**
[BOOK] **"Jina AI API Documentation"**  
URL: https://api.jina.ai/redoc  
Read: Embeddings endpoint reference (5 min)

#### **6.3 Batch Processing** (10 min)

**Limits:**
- Max 32 texts per request
- Max 8192 tokens per text

**Strategy:**
```
# DON'T do this (slow):
for chunk in chunks:
    embed(chunk)  # 100 API calls

# DO this (fast):
batches = chunks[0:32], chunks[32:64], ...
for batch in batches:
    embed(batch)  # 4 API calls
```

**Error Handling:**

Must handle:
- Rate limits (429 status)
- Token limits (400 status)
- Network errors
- Invalid input

**Best Practices:**
- Batch requests (max 32)
- Retry with exponential backoff
- Monitor token usage
- Cache embeddings (don't re-embed)
- Validate input length

**Quick Setup:**
1. Get API key from https://jina.ai
2. Store in .env file
3. Test with sample text
4. Verify embedding dimensions

---

## HANDS-ON EXERCISES

### **Exercise 1: Chunking Practice**

Take this text and chunk it:
```
Title: Machine Learning Fundamentals

Introduction:
Machine learning is a subset of artificial intelligence that enables 
computers to learn from data. Unlike traditional programming, ML systems 
improve their performance through experience. This paper explores core
ML concepts and their applications.

Methodology:
We used a neural network with three hidden layers. Each layer contained 
128 neurons with ReLU activation. Training took 50 epochs on the MNIST 
dataset with batch size 32. We applied dropout (0.3) for regularization.

Results:
Our model achieved 98.5% accuracy on the test set, outperforming the 
baseline by 12%. Training time was approximately 2 hours on a single GPU.
The confusion matrix showed strong performance across all digit classes.
```

**Questions:**
1. How would you chunk this with section-based strategy?
2. How would you add context to each chunk?
3. Where would you add overlap?
4. What metadata would you track?

**Expected Answer:**
```
Chunk 1:
Title: Machine Learning Fundamentals
Section: Introduction
Text: "Machine learning is a subset... explores core ML concepts and 
their applications."
Word count: ~40
Metadata: {section: "Introduction", position: "start"}

Chunk 2:
Title: Machine Learning Fundamentals
Section: Methodology  
Text: "We used a neural network... dropout (0.3) for regularization."
Word count: ~45
Metadata: {section: "Methodology", position: "middle"}

Chunk 3:
Title: Machine Learning Fundamentals
Section: Results
Text: "Our model achieved 98.5%... performance across all digit classes."
Word count: ~45
Metadata: {section: "Results", position: "end"}
```

---

### **Exercise 2: Cosine Similarity**

Given these embeddings (simplified to 3D):
```
query = [0.8, 0.2, 0.1]
doc_1 = [0.7, 0.3, 0.1]
doc_2 = [0.1, 0.8, 0.5]
doc_3 = [0.75, 0.25, 0.12]
```

**Tasks:**
1. Calculate cosine similarity for doc_1, doc_2, doc_3
2. Rank documents by relevance
3. Which document is most relevant? Why?

**Calculation Steps:**

For doc_1:
```
dot(query, doc_1) = 0.8×0.7 + 0.2×0.3 + 0.1×0.1
                  = 0.56 + 0.06 + 0.01 = 0.63

||query|| = sqrt(0.8² + 0.2² + 0.1²) = sqrt(0.69) = 0.83
||doc_1|| = sqrt(0.7² + 0.3² + 0.1²) = sqrt(0.59) = 0.77

cosine = 0.63 / (0.83 × 0.77) = 0.63 / 0.64 = 0.98
```

For doc_2:
```
dot(query, doc_2) = 0.8×0.1 + 0.2×0.8 + 0.1×0.5
                  = 0.08 + 0.16 + 0.05 = 0.29

||doc_2|| = sqrt(0.1² + 0.8² + 0.5²) = sqrt(0.90) = 0.95

cosine = 0.29 / (0.83 × 0.95) = 0.29 / 0.79 = 0.37
```

For doc_3:
```
dot(query, doc_3) = 0.8×0.75 + 0.2×0.25 + 0.1×0.12
                  = 0.60 + 0.05 + 0.012 = 0.662

||doc_3|| = sqrt(0.75² + 0.25² + 0.12²) = sqrt(0.64) = 0.80

cosine = 0.662 / (0.83 × 0.80) = 0.662 / 0.664 = 0.997
```

**Ranking:**
1. doc_3 (0.997) - Most similar
2. doc_1 (0.98) - Very similar  
3. doc_2 (0.37) - Less similar

---

### **Exercise 3: RRF Calculation**

Given:
```
BM25 ranking: [Paper_A, Paper_B, Paper_C, Paper_D]
Vector ranking: [Paper_C, Paper_A, Paper_D, Paper_E]
```

**Task:** Calculate RRF scores (k=60) and final ranking

**Calculation:**

Paper_A:
- BM25 rank: 1 -> 1/(60+1) = 0.0164
- Vector rank: 2 -> 1/(60+2) = 0.0161
- RRF: 0.0164 + 0.0161 = 0.0325

Paper_B:
- BM25 rank: 2 -> 1/(60+2) = 0.0161
- Vector rank: none -> 0
- RRF: 0.0161

Paper_C:
- BM25 rank: 3 -> 1/(60+3) = 0.0159
- Vector rank: 1 -> 1/(60+1) = 0.0164
- RRF: 0.0159 + 0.0164 = 0.0323

Paper_D:
- BM25 rank: 4 -> 1/(60+4) = 0.0156
- Vector rank: 3 -> 1/(60+3) = 0.0159
- RRF: 0.0156 + 0.0159 = 0.0315

Paper_E:
- BM25 rank: none -> 0
- Vector rank: 4 -> 1/(60+4) = 0.0156
- RRF: 0.0156

**Final Ranking:**
1. Paper_A (0.0325)
2. Paper_C (0.0323)
3. Paper_D (0.0315)
4. Paper_B (0.0161)
5. Paper_E (0.0156)

---

## RESEARCH QUESTIONS

### **Conceptual Questions:**

Answer these to verify understanding:

1. **Why chunk documents?**
   - What problems does chunking solve?
   - What happens without chunking?

2. **What is an embedding?**
   - How does it differ from keyword matching?
   - Why use 1024 dimensions instead of 3?

3. **What is cosine similarity?**
   - Why use cosine instead of Euclidean distance?
   - What does a score of 0.95 mean?

4. **Why use HNSW?**
   - What's the problem with exact k-NN?
   - What's the trade-off?

5. **Why hybrid search?**
   - What does BM25 miss?
   - What does vector search miss?
   - How does RRF help?

6. **What is task-specific embedding?**
   - Why different tasks for query vs document?
   - How does it improve search?

### **Practical Questions:**

Test your application knowledge:

1. **How would you chunk a 20-page research paper?**
   - What strategy?
   - What chunk size?
   - How much overlap?

2. **How do you choose k for k-NN?**
   - What if k=1? k=100?
   - How to decide?

3. **How do you evaluate chunk quality?**
   - What metrics?
   - What tests?

4. **When would you use BM25 only?**
   - What use cases?
   - When is embedding unnecessary?

5. **How do you debug poor search results?**
   - What to check first?
   - How to improve?

6. **How do you handle very long documents (100+ pages)?**
   - Chunking strategy?
   - Performance considerations?

---

## KEY TAKEAWAYS

**Remember these 10 things:**

1. **Chunking = Breaking documents into searchable pieces**
   - Sweet spot: 400-800 words for research papers
   - Always include context (title, section)
   - Use 15-20% overlap

2. **Embeddings = Semantic vectors**
   - Similar meaning = nearby in vector space
   - Cosine similarity measures closeness (0-1)
   - 1024 dimensions is standard

3. **k-NN = Find k nearest vectors**
   - Approximate (HNSW) is fast enough for production
   - Trade-off: speed vs accuracy (95-99% accurate)

4. **BM25 = Keyword precision**
   - Fast, exact matching
   - Misses synonyms and paraphrasing

5. **Vector = Semantic understanding**
   - Handles paraphrasing and synonyms
   - Slower, more expensive

6. **Hybrid = Best of both worlds**
   - Combine with RRF algorithm
   - Best overall accuracy
   - Industry standard for production

7. **Task-specific embeddings**
   - retrieval.passage for documents
   - retrieval.query for queries
   - Optimizes for query-document matching

8. **Batch processing = Efficiency**
   - 32 texts per API call
   - Huge performance gain over individual calls

9. **Test chunk quality**
   - Ask sample questions
   - Check retrieval precision
   - Iterate based on results

10. **Production patterns**
    - Cache embeddings (don't re-embed)
    - Handle errors gracefully
    - Monitor token usage
    - Track quality metrics

**If you understand these 10:** You're 95% ready! [CHECK]

---

## ADDITIONAL RESOURCES (Optional Deep Dives)

### **Advanced Chunking:**
- Semantic chunking with embeddings
- Hierarchical chunking strategies
- Dynamic chunk sizing

**Resources:**
- "Semantic Chunking" - LlamaIndex: https://docs.llamaindex.ai/en/stable/
- "Hierarchical Chunking" - LangChain: https://python.langchain.com/docs/

### **Embedding Models:**
- Model comparison (quality vs speed)
- Fine-tuning embeddings
- Multi-lingual embeddings

**Resources:**
- "MTEB Leaderboard" (model rankings): https://huggingface.co/spaces/mteb/leaderboard
- "Sentence Transformers": https://www.sbert.net/

### **Vector Databases:**
- Pinecone, Weaviate, Qdrant comparison
- When to use dedicated vector DB
- Scaling considerations

**Resources:**
- "Vector Database Comparison": https://benchmark.vectorview.ai/
- "Choosing a Vector Database": https://www.pinecone.io/learn/vector-database/

### **Advanced RAG:**
- Re-ranking strategies
- Query expansion
- Contextual compression

**Resources:**
- "Advanced RAG Techniques": https://blog.langchain.dev/
- "RAG Evaluation": https://docs.ragas.io/

---

## AFTER LEARNING

### **You're ready to build Steps 13-16 when you can:**

**Knowledge Check:**
- [ ] Explain chunking strategies and choose appropriate one
- [ ] Understand how embeddings represent meaning
- [ ] Calculate cosine similarity
- [ ] Explain HNSW algorithm benefits
- [ ] Describe hybrid search advantages
- [ ] Implement RRF algorithm conceptually
- [ ] Use Jina AI API effectively
- [ ] Design chunking strategy for research papers

**Practical Check:**
- [ ] Can decide chunk size for a given document
- [ ] Know when to use BM25 vs vector vs hybrid
- [ ] Can evaluate chunk quality
- [ ] Understand task-specific embedding usage
- [ ] Can debug poor search results
- [ ] Know how to batch API requests

**Then proceed to:**
- **STEP13_COMPLETE.md** - Text Chunking Implementation
- **STEP14_COMPLETE.md** - Embedding Generation Service
- **STEP15_COMPLETE.md** - Vector Search Implementation
- **STEP16_COMPLETE.md** - Hybrid Search with RRF

---

## WEEK 8 SUCCESS METRICS

**By end of this week, you'll have:**
- [TARGET] Chunking service that creates 400-800 word chunks
- [TARGET] Jina AI integration generating 1024-dim embeddings
- [TARGET] Vector search in OpenSearch (k-NN)
- [TARGET] Hybrid search combining BM25 + Vector
- [TARGET] RRF fusion producing final rankings
- [TARGET] Improved search quality over BM25-only
- [TARGET] Production-ready semantic search layer

**Performance Targets:**
- Chunk creation: <1s for 10,000-word paper
- Embedding generation: <2s for 20 chunks (batched)
- Hybrid search: <500ms response time
- Search quality: >80% precision on test queries

---

**Time estimate:** 5-6 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Total week time:** ~16-18 hours (learning + implementation)

---

**Document Generated:** December 28, 2025  
**For:** Career Transition Week 8 (MOAI Week 4)  
**Status:** Complete - Ready for Steps 13-16 Implementation  
**Format:** Clean ASCII - No Character Corruption
