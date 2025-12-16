# WEEK 5: EMBEDDINGS & VECTOR DATABASES - Complete Day-wise Plan

## WEEK 5 OVERVIEW

**Duration:** 7 days (5 weekdays @ 1 hour each + 2 weekend days @ 3-4 hours each)
**Total Time:** ~11-12 hours
**Goal:** Master embeddings, semantic search, and vector databases
**Deliverable:** Production-ready payment regulations search system

---

## DAY 1 (Monday): Embeddings Concept - 60 minutes

### Primary Resources

**"What are Embeddings?" - Understanding the Basics**
- OpenAI Embeddings Guide: https://platform.openai.com/docs/guides/embeddings
- Duration: 15 min read
- Official explanation of embeddings and use cases

**"Embeddings: What they are and why they matter" by Simon Willison**
- Link: https://simonwillison.net/2023/Oct/23/embeddings/
- Duration: 20 min read
- Excellent intuitive explanation with real examples

**"Vector Embeddings Explained" by Pinecone**
- Link: https://www.pinecone.io/learn/vector-embeddings/
- Duration: 15 min read
- Visual explanations and technical details

### Video Resources

**"Embeddings Explained" by StatQuest**
- Link: https://www.youtube.com/watch?v=viZrOnJclY0
- Duration: 10:00
- Clear visual explanation
- Statistical foundations

**"Word Embeddings and Semantic Search"**
- Link: https://www.youtube.com/watch?v=5MaWmXwxFNQ
- Duration: 15:00
- Practical applications
- Search use cases

### Reading Materials

**"Understanding Embeddings in Machine Learning"**
- Link: https://machinelearningmastery.com/what-are-word-embeddings/
- Duration: 15 min read
- Comprehensive introduction

**OpenAI Embeddings Technical Guide**
- Link: https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
- Duration: 10 min read
- API details and implementation

### Schedule - 60 minutes total

**Part 1: Core Concepts (30 min)**
1. Watch: StatQuest video (10 min)
2. Read: Simon Willison article (20 min)

**Part 2: Technical Understanding (20 min)**
3. Read: OpenAI documentation (15 min)
4. Read: Pinecone visual guide (5 min)

**Part 3: Reflection and Application (10 min)**
5. Reflection and notes

### Key Concepts to Master

**What are Embeddings?**
- Numerical representations of text (vectors)
- Convert words/sentences into arrays of numbers
- Similar text → Similar vectors (close in vector space)
- Capture semantic meaning, not just keywords
- Enable mathematical operations on text

**Why Embeddings Matter:**
- Power semantic search (meaning-based vs keyword-based)
- Enable recommendation systems
- Support clustering and classification
- Foundation for RAG (Retrieval-Augmented Generation)
- Critical for modern AI applications

### Connection to Payments Domain

**Use Case 1: Transaction Search**
- User searches: "coffee shop"
- Embedding matches: "Starbucks", "Peet's Coffee", "Cafe Nero", "local cafe"

**Use Case 2: Similar Transaction Detection**
- Find transactions similar to: "Uber ride $45"
- Matches: "Lyft trip $38", "taxi service $52", "rideshare $41"

**Use Case 3: Payment Regulations Search**
- Search regulations by concept, not keywords
- Query: "What are rules for international transfers?"
- Finds relevant sections even without exact words

### Reflection Questions

1. What are embeddings in your own words?
2. Why are embeddings useful for payment processing? (Give 3 examples)
3. How would you use embeddings for transaction search?
4. What are the limitations of embeddings?
5. How do embeddings relate to the LLMs you learned in Week 3?

### Day 1 Deliverables

- [ ] Watched StatQuest video on embeddings
- [ ] Read Simon Willison's article
- [ ] Read OpenAI embeddings documentation
- [ ] Understand: what embeddings are, why they matter
- [ ] Can explain: embeddings vs keywords in simple terms
- [ ] Wrote reflection answers (5 questions)
- [ ] Listed 3+ payment use cases with details
- [ ] Spent approximately 60 minutes

---

## DAY 2 (Tuesday): Semantic Search - 60 minutes

### Primary Resources

**"Semantic Search with OpenAI Embeddings"**
- Link: https://platform.openai.com/docs/guides/embeddings/use-cases
- Duration: 15 min read

**"Building Semantic Search" by Pinecone**
- Link: https://www.pinecone.io/learn/semantic-search/
- Duration: 20 min read

### Video Resources

**"Semantic Search Explained"**
- Link: https://www.youtube.com/watch?v=OATCgQtNX2o
- Duration: 12:00

**"How Semantic Search Works"**
- Link: https://www.youtube.com/watch?v=vVMRY7r7FhQ
- Duration: 15:00

### Reading Materials

**"Introduction to Semantic Search" by Elastic**
- Link: https://www.elastic.co/what-is/semantic-search
- Duration: 10 min read

**"Semantic Search vs Keyword Search" by Qdrant**
- Link: https://qdrant.tech/articles/what-is-semantic-search/
- Duration: 15 min read

### Schedule - 60 minutes total

**Part 1: Understanding Semantic Search (22 min)**
1. Watch: "Semantic Search Explained" (12 min)
2. Read: Elastic introduction (10 min)

**Part 2: Technical Implementation (25 min)**
3. Read: OpenAI use cases (15 min)
4. Read: Pinecone comprehensive guide (10 min)

**Part 3: Design Exercise (13 min)**
5. Design payment regulation search system

### Key Concepts to Master

**What is Semantic Search?**
- Search by meaning, not exact keywords
- Understands user intent
- Finds conceptually similar results
- Better user experience

**How Semantic Search Works:**

**Step 1: Index Documents**
- Convert all documents to embeddings
- Store embeddings in database

**Step 2: Process Query**
- User enters search query
- Convert query to embedding

**Step 3: Find Similar**
- Compare query vector to all document vectors
- Calculate similarity scores

**Step 4: Return Results**
- Rank by similarity
- Show top N results

### Design Exercise: Payment Regulations Search System

**Component 1: Document Corpus**
- PCI-DSS compliance requirements
- AML/KYC regulations
- GDPR data protection rules
- Payment Services Directive requirements
- Regional regulations

**Component 2: Document Processing**
- Chunk size: 200-500 tokens recommended
- Overlap: 50-100 tokens to maintain context
- Metadata: source, category, importance, date, geography

**Component 3: Embedding Generation**
- Use OpenAI text-embedding-ada-002 or newer
- Generate embeddings for each chunk
- Store with original text and metadata

**Component 4: Search Interface**
- Natural language question input
- Optional filters (source, category, importance)
- Number of results desired (default: 3-5)

**Component 5: Result Presentation**
- Regulation text
- Source and reference
- Similarity score
- Related regulations

### Day 2 Deliverables

- [ ] Watched semantic search videos
- [ ] Read OpenAI and Pinecone guides
- [ ] Understand: how semantic search works end-to-end
- [ ] Designed payment regulation search system
- [ ] Identified all required components
- [ ] Spent approximately 60 minutes

---

## DAY 3 (Wednesday): Generate First Embeddings - 60 minutes

### Primary Resources

**OpenAI Embeddings API Documentation**
- Link: https://platform.openai.com/docs/api-reference/embeddings
- Duration: 15 min read

**OpenAI Embeddings Guide - How to Get Embeddings**
- Link: https://platform.openai.com/docs/guides/embeddings/how-to-get-embeddings
- Duration: 10 min read

### Code Resources (for reference only)

**OpenAI Cookbook - Embeddings Examples**
- Link: https://github.com/openai/openai-cookbook/blob/main/examples/Get_embeddings.ipynb
- Duration: 20 min review

### Reading Materials

**"Embeddings Best Practices" - OpenAI**
- Link: https://platform.openai.com/docs/guides/embeddings/use-cases
- Duration: 10 min read

### Schedule - 60 minutes total

**Part 1: API Understanding (15 min)**
1. Read: API documentation thoroughly

**Part 2: Hands-on Exercises (30 min)**
2. Exercise 1: Generate single embedding (10 min)
3. Exercise 2: Batch embeddings (10 min)
4. Exercise 3: Calculate similarities (10 min)

**Part 3: Review and Analysis (15 min)**
5. Review results and insights

### Exercise 1: Generate Single Embedding - 15 min

**Requirements:**

**Setup:**
- Use OpenAI API setup from Week 3
- Model: "text-embedding-3-small"

**Task:**
- Generate embedding for: "Bank transfer to John Smith $500"
- Store complete response

**What to figure out:**
- How to structure API request
- How to access embedding vector from response
- Vector properties (dimensions, data type, range)

**Success criteria:**
- [ ] Successful API call
- [ ] Received valid embedding vector
- [ ] Vector has expected dimensions
- [ ] Can print vector values
- [ ] Understand response structure

### Exercise 2: Batch Embeddings - 15 min

**Requirements:**

**Transaction list:**
1. "Coffee at Starbucks downtown $5.50"
2. "Latte at local coffee shop $6.00"
3. "Uber ride to airport $45.00"
4. "Taxi service to hotel $38.00"
5. "Electric bill payment monthly $89.00"
6. "Water utility bill $45.00"
7. "Netflix streaming subscription $15.99"
8. "Spotify music subscription $9.99"

**Task:**
- Send all 8 texts in single API request
- Store results in organized structure

**What to figure out:**
- How to send multiple texts in one request
- How to match embeddings to original texts
- How to organize storage
- Cost calculation

**Success criteria:**
- [ ] All 8 embeddings generated
- [ ] Stored in organized structure
- [ ] Know total tokens consumed
- [ ] Calculate exact cost

### Exercise 3: Calculate Similarities - 15 min

**Requirements:**

**Comparison pairs:**

**Pair 1:** Coffee vs Latte (expected: high similarity >0.8)
**Pair 2:** Uber vs Taxi (expected: high similarity >0.8)
**Pair 3:** Electric vs Water (expected: high similarity >0.7)
**Pair 4:** Netflix vs Spotify (expected: high similarity >0.8)
**Pair 5:** Coffee vs Electric (expected: low similarity <0.4)
**Pair 6:** Uber vs Netflix (expected: low similarity <0.4)

**What to figure out:**
- How to calculate cosine similarity
- Formula: cos(θ) = (A · B) / (||A|| × ||B||)
- Can use NumPy or sklearn

**Create similarity matrix:**
- Show all pairwise similarities

**Success criteria:**
- [ ] Calculated all similarities correctly
- [ ] Similar transactions have high scores
- [ ] Different transactions have low scores
- [ ] Results are intuitive

**Finctec Focused:**

### Exercise 1: Sanitization & Single Embedding (Fintech Data Privacy) — 15 min

#### Requirements

**Setup**
- Use OpenAI API setup from Week 3
- Model: `text-embedding-3-small`

**The Fintech Constraint (New)**
- You **must not** send PII (Personally Identifiable Information) to OpenAI.
- Create a `redact_pii(text)` function using simple string replacement or Regex.
- Rules:
  - Replace person names with `[PERSON]`
  - Replace account numbers with `[ACCOUNT]`

#### Task
- Raw Input:  
  `"Bank transfer to John Smith $500 from Acct 987654321"`
- Redacted Output:  
  `"Bank transfer to [PERSON] $500 from Acct [ACCOUNT]"`
- Generate an embedding **only for the redacted string**

#### Success Criteria
- [ ] Redaction function works correctly  
- [ ] Embedding generated for sanitized text only  
- [ ] Clear understanding that embeddings capture **transaction patterns**, not user identity

---

### Exercise 2: Batch Embeddings with Redaction — 15 min

#### Requirements

**Raw Transaction List (Dirty Data)**
- `"Coffee at Starbucks with Sarah $5.50"`
- `"Latte at local cafe for Mike $6.00"`
- `"Uber ride for employee #4451 $45.00"`
- `"Taxi service for client mtg $38.00"`

#### Task
1. Sanitize the entire batch **before** sending data to OpenAI
2. Send the sanitized list in **one batch embedding request**
3. Map returned vectors back to original transaction IDs  
   - Raw data stays local  
   - Only sanitized data goes to the cloud

#### Success Criteria
- [ ] All PII removed before API call  
- [ ] Batch embedding request succeeds  
- [ ] Vectors correctly mapped back to original transactions 

### Day 3 Deliverables

- [ ] Generated first embedding successfully
- [ ] Created batch of transaction embeddings
- [ ] Calculated cosine similarities
- [ ] Understand API parameters and usage
- [ ] Know embedding costs
- [ ] Spent approximately 60 minutes

---

## DAY 4 (Thursday): Vector Similarity Metrics - 60 minutes

### Primary Resources

**"Understanding Vector Similarity" by Pinecone**
- Link: https://www.pinecone.io/learn/vector-similarity/
- Duration: 20 min read

**"Distance Metrics for Vector Embeddings" by Qdrant**
- Link: https://qdrant.tech/articles/vector-similarity-metrics/
- Duration: 15 min read

### Video Resources

**"Cosine Similarity Explained" by StatQuest**
- Link: https://www.youtube.com/watch?v=e9U0QAFbfLI
- Duration: 6:00

**"Distance Metrics in Machine Learning"**
- Link: https://www.youtube.com/watch?v=U5eUGESkXXE
- Duration: 12:00

### Reading Materials

**"Choosing the Right Similarity Metric" by Elastic**
- Link: https://www.elastic.co/blog/text-similarity-search-with-vectors-in-elasticsearch
- Duration: 15 min read

### Schedule - 60 minutes total

**Part 1: Visual Understanding (11 min)**
1. Watch: StatQuest cosine similarity (6 min)
2. Watch: Distance metrics overview (5 min)

**Part 2: Deep Dive (35 min)**
3. Read: Pinecone similarity guide (20 min)
4. Read: Qdrant technical comparison (15 min)

**Part 3: Hands-on Practice (14 min)**
5. Exercise: Implement and compare all metrics

### Key Concepts to Master

**Three Main Similarity Metrics:**

**1. Cosine Similarity**
- Measures angle between vectors
- Range: -1 to 1
- 1 = identical direction
- 0 = perpendicular (unrelated)
- Most common for text embeddings

**2. Euclidean Distance**
- Straight-line distance
- Range: 0 to infinity
- 0 = identical
- Lower = more similar

**3. Dot Product**
- Element-wise multiplication and sum
- Range: -infinity to infinity
- For normalized vectors: same as cosine
- Fastest to compute

### Exercise: Compare All Three Metrics - 14 min

**Requirements:**

Using yesterday's transaction embeddings, calculate all three metrics for:

1. Coffee vs Latte
2. Uber vs Taxi
3. Electric vs Netflix

**Create comparison table:**
```
Pair                | Cosine | Euclidean | Dot Product
--------------------|--------|-----------|------------
Coffee vs Latte     |  0.XX  |   0.XX    |    0.XX
Uber vs Taxi        |  0.XX  |   0.XX    |    0.XX
Electric vs Netflix |  0.XX  |   0.XX    |    0.XX
```

**Analysis questions:**
- Do all metrics agree on similarity ranking?
- Which is most intuitive for your use case?
- Are vectors normalized? (Check magnitude)

**Success criteria:**
- [ ] All three metrics calculated
- [ ] Results compared in table
- [ ] Understand when to use each
- [ ] Know which is best for payments use case

### When to Use Each Metric

**Use Cosine Similarity when:**
- Working with text embeddings
- Text has varying lengths
- Semantic similarity is goal
- OpenAI, Cohere, HuggingFace embeddings

**Use Euclidean Distance when:**
- Clustering similar items (K-means)
- K-Nearest Neighbors (KNN)
- Magnitude has meaning

**Use Dot Product when:**
- Vectors already normalized (OpenAI embeddings)
- Need maximum performance
- Large-scale applications

### Day 4 Deliverables

- [ ] Watched similarity metric videos
- [ ] Read comprehensive guides
- [ ] Understand all three metrics
- [ ] Implemented and compared metrics
- [ ] Know when to use each
- [ ] Spent approximately 60 minutes

---

## DAY 5 (Friday): Vector Databases Introduction - 60 minutes

### Primary Resources

**"What is a Vector Database?" by Pinecone**
- Link: https://www.pinecone.io/learn/vector-database/
- Duration: 20 min read

**"Vector Databases Explained" by Weaviate**
- Link: https://weaviate.io/blog/what-is-a-vector-database
- Duration: 15 min read

### Video Resources

**"Introduction to Vector Databases"**
- Link: https://www.youtube.com/watch?v=klTvEwg3oJ4
- Duration: 15:00

**"Why Do We Need Vector Databases?"**
- Link: https://www.youtube.com/watch?v=6jCm3aS1g3M
- Duration: 12:00

### Reading Materials

**"Comparing Vector Databases"**
- Link: https://lakefs.io/blog/12-vector-databases-2023/
- Duration: 15 min read

**ChromaDB Documentation**
- Link: https://docs.trychroma.com/
- Duration: 10 min browse

### Schedule - 60 minutes total

**Part 1: Core Concepts (20 min)**
1. Watch: "Introduction to Vector Databases" (15 min)
2. Skim: Weaviate blog (5 min)

**Part 2: Deep Understanding (25 min)**
3. Read: Pinecone comprehensive guide (20 min)
4. Skim: Vector database comparison (5 min)

**Part 3: Preparation (15 min)**
5. Browse: ChromaDB documentation (10 min)
6. Plan: Tomorrow's implementation (5 min)

### Key Concepts to Master

**What is a Vector Database?**
- Specialized database optimized for vector embeddings
- Stores high-dimensional vectors efficiently
- Enables fast similarity search
- Scales to billions of vectors

**Why Traditional Databases Don't Work:**

PostgreSQL with 1M embeddings:
- Query time: 10+ seconds
- Must compare to ALL vectors

Vector Database with 1M embeddings:
- Query time: <100ms
- Uses specialized indexing
- 100x+ speedup

### Core Features

**1. Efficient Storage**
- Vector compression
- Optimized binary formats
- Memory mapping

**2. Fast Similarity Search**
- Specialized indexing (HNSW, IVF)
- Approximate Nearest Neighbors (ANN)
- Sub-millisecond queries

**3. Metadata Filtering**
- Store attributes with vectors
- Filter before similarity search
- Combine vector and traditional queries

**4. Scalability**
- Horizontal scaling
- Handle billions of vectors
- Production-ready

### Vector Database Options

**ChromaDB (Recommended for Week 5):**
- Easiest to start
- Python-native
- Local-first
- Great for learning
- Link: https://www.trychroma.com/

**Pinecone:**
- Managed service
- Very fast
- Good free tier
- Production-ready
- Link: https://www.pinecone.io/

**Qdrant:**
- Very fast (Rust-based)
- Open source + cloud
- Modern API
- Link: https://qdrant.tech/

**Weaviate:**
- Open source + cloud
- GraphQL API
- Modular
- Link: https://weaviate.io/

**Milvus:**
- Highly scalable
- Enterprise features
- More complex
- Link: https://milvus.io/

**FAISS:**
- Library, not database
- Extremely fast
- Research-oriented
- Link: https://github.com/facebookresearch/faiss

### Use Cases

1. **Semantic Search** - Search documents by meaning
2. **Recommendation Systems** - Find similar items
3. **Duplicate Detection** - Find near-duplicates
4. **Clustering** - Group similar items
5. **RAG Systems** - Retrieve context for LLMs
6. **Anomaly Detection** - Find outliers

### Day 5 Deliverables

- [ ] Watched vector database videos
- [ ] Read comprehensive guides
- [ ] Understand: what vector databases are, why needed
- [ ] Know different options
- [ ] Decided on ChromaDB for learning
- [ ] Bookmarked ChromaDB documentation
- [ ] Spent approximately 60 minutes

---

## DAY 6 (Saturday): ChromaDB Setup - 3-4 hours

### Overview

Install ChromaDB and build working payment regulations search system.

### Schedule - 3-4 hours total

**Hour 1:** Installation & Basic Operations (60 min)
**Hour 2:** Payment Regulations Indexing (60 min)
**Hour 3:** Search Implementation (60 min)
**Hour 4:** Advanced Features & Testing (60 min, optional)

### Resources

**ChromaDB Documentation:**
- Getting Started: https://docs.trychroma.com/getting-started
- Guides: https://docs.trychroma.com/guides
- API Reference: https://docs.trychroma.com/reference

**ChromaDB GitHub:**
- Repository: https://github.com/chroma-core/chroma
- Examples: https://github.com/chroma-core/chroma/tree/main/examples

---

### HOUR 1: Installation & Basic Operations

**Part 1: ChromaDB Installation - 15 min**

**Requirements:**

Install ChromaDB:
```bash
pip install chromadb
```

Verify installation:
- Import chromadb in Python
- Check version
- No errors

**Success criteria:**
- [ ] ChromaDB installed
- [ ] Can import successfully
- [ ] Ready to create collections

---

**Part 2: Understanding Basics - 20 min**

**Read Documentation:**
- Core Concepts: https://docs.trychroma.com/guides
- Collections Guide
- Querying Guide

**Key Concepts:**

**Client** - Entry point to ChromaDB
**Collection** - Stores embeddings with metadata
**Document** - Individual item (ID, embedding, metadata, text)
**Embedding Function** - How text → vector

---

**Part 3: First Operations - 25 min**

**Exercise 1: Create Collection and Add Documents**

**Requirements:**

Create collection: "test_transactions"

Add 5 sample transactions:
1. "Coffee at Starbucks $5.50" - Food, $5.50
2. "Uber ride to airport $45" - Transport, $45.00
3. "Netflix subscription $15.99" - Bills, $15.99
4. "Whole Foods groceries $87" - Food, $87.00
5. "Shell gas station $52" - Transport, $52.00

**What to figure out:**
- How to initialize client
- How to create collection
- How to add documents
- How embeddings generated automatically

**Success criteria:**
- [ ] Client initialized
- [ ] Collection created
- [ ] All 5 documents added
- [ ] Count shows 5

---

**Exercise 2: Query Similar Transactions**

**Requirements:**

**Query 1:** Find similar to "coffee shop"
- Expected: Returns Starbucks

**Query 2:** Find similar to "transportation"
- Expected: Returns Uber and Shell

**Query 3:** Find similar to "monthly bill"
- Expected: Returns Netflix

**What to figure out:**
- Query syntax
- How to specify number of results
- How to access returned data
- How similarity scores presented

**Success criteria:**
- [ ] All queries executed
- [ ] Results make sense
- [ ] Can access IDs, scores, metadata
- [ ] Understand result structure

---

### HOUR 2: Payment Regulations Indexing

**Part 1: Prepare Documents - 25 min**

**Requirements:**

Create 40-50 payment regulation documents:

**PCI-DSS (10 documents):**
1. "Credit card data must be encrypted during transmission using TLS 1.2 or higher."
2. "Card verification value (CVV) must never be stored after authorization."
3. "Access to cardholder data must be restricted on need-to-know basis."
4. "All access to payment systems must be logged and monitored."
5. "Network segmentation required to isolate payment processing systems."
6. "Passwords must meet complexity requirements: 7+ characters, changed every 90 days."
7. "Multi-factor authentication required for remote access to cardholder data."
8. "Quarterly vulnerability scans must be performed on payment systems."
9. "Maintain vulnerability management program to remediate security issues."
10. "Physical security controls required for systems handling cardholder data."

**AML/KYC (10 documents):**
1. "Identity verification required for all new customers using government-issued ID."
2. "Transactions over $10,000 must be reported to financial authorities."
3. "Suspicious activity must be flagged and investigated within 24 hours."
4. "Customer due diligence performed annually for high-risk customers."
5. "Source of funds verification required for large transactions exceeding $5,000."
6. "Enhanced due diligence required for politically exposed persons (PEPs)."
7. "Transaction monitoring systems must detect unusual money laundering patterns."
8. "Customer risk rating based on occupation, transaction patterns, geography."
9. "Sanctions screening required against OFAC, UN, EU sanctions lists."
10. "Beneficial ownership information must be collected for business accounts."

**GDPR/Privacy (10 documents):**
1. "Personal financial data must be retained for minimum 7 years."
2. "Customer consent required before sharing payment data with third parties."
3. "Right to data deletion applies except for legal retention requirements."
4. "Data breach notification must occur within 72 hours of awareness."
5. "Privacy policy must be clearly displayed before collecting customer data."
6. "Customers have right to access personal data in portable format."
7. "Data processing limited to purposes stated at time of collection."
8. "Children under 16 require parental consent for payment data processing."
9. "Data protection impact assessment required for high-risk activities."
10. "Cross-border transfers require Standard Contractual Clauses."

**Payment Services (10 documents):**
1. "Strong customer authentication required for payments exceeding 30 EUR under PSD2."
2. "Payment service providers must maintain minimum capital based on volume."
3. "Transaction disputes must be resolved within 15 business days."
4. "Refund processing must begin within 5 business days."
5. "Payment initiation requires explicit customer consent for each transaction."
6. "Account information service providers must be authorized and registered."
7. "E-money issuers must safeguard customer funds separately."
8. "Payment providers liable for unauthorized transactions unless customer negligent."
9. "SEPA credit transfers must not exceed 1 business day execution time."
10. "Users must be informed of fees and exchange rates before authorization."

**Regional (10 documents):**
1. "UK FCA requires authorization for all firms conducting payment activities."
2. "EU PSD mandates passporting rights for authorized payment institutions."
3. "US ACH network requires Same Day ACH capability for participants."
4. "SEPA transactions must use IBAN and BIC codes."
5. "CFPB oversight applies to all US payment service providers."
6. "Reserve Bank of India mandates additional factor authentication for CNP."
7. "Australia's NPP enables real-time payments 24/7 across banks."
8. "Hong Kong's FPS supports instant transfers across banks."
9. "Singapore requires MAS license for payment service providers."
10. "Canadian Payment Association governs clearing and settlement."

**Metadata structure:**
- id: Unique identifier
- source: PCI-DSS, AML, GDPR, etc.
- category: Security, Compliance, Privacy, Operations
- importance: Critical, High, Medium
- geography: Global, EU, UK, US, Asia

**Success criteria:**
- [ ] 40-50 documents prepared
- [ ] Metadata designed
- [ ] Ready to index

---

**Part 2: Create Regulations Collection - 20 min**

**Requirements:**

Create collection: "payment_regulations"
- Distance metric: Cosine
- Embedding function: Default

Add all documents in batch:
- Prepare lists: ids, documents, metadatas
- Single collection.add() call

**Success criteria:**
- [ ] Collection created
- [ ] All documents added
- [ ] Count matches number
- [ ] Can query collection

---

**Part 3: Test Queries - 15 min**

**Requirements:**

**Test 1:** "How should we protect credit card numbers?"
- Expected: PCI-DSS encryption rules

**Test 2:** "What are reporting requirements for large transactions?"
- Expected: AML $10,000 threshold

**Test 3:** "Can we share customer payment data?"
- Expected: GDPR consent rules

**Test 4:** "International wire transfer requirements?"
- Expected: SEPA/SWIFT rules

**Test 5:** "What to do if data breach?"
- Expected: GDPR 72-hour notification

**Success criteria:**
- [ ] All 5 queries tested
- [ ] Results documented
- [ ] Relevance evaluated
- [ ] Quality thresholds determined

**Fintech FocusLed**

### HOUR 2: Payment Regulations Indexing (Hierarchy Aware) — 25 min

#### The Fintech Constraint
Legal documents are **hierarchical**.  
A clause like *Section 4.1* is meaningless without its parent context (e.g., GDPR).

#### Required Change
- Chunk individual sections
- Store **parent context** in metadata for every chunk

#### Updated Metadata Structure

```json
{
  "id": "GDPR_4_1",
  "text": "The actual regulation clause text",
  "metadata": {
    "source": "GDPR",
    "section_id": "4.1",
    "parent_context": "Article 4: Definitions and Penalties",
    "importance": "Critical"
  }
}
```
----

**Success Criteria:**
 Documents chunked but linked to parent context

 Section IDs stored for precise citation
---

### HOUR 3: Search Implementation

**Part 1: Build Search Function - 25 min**

**Requirements:**

Create function: `search_regulations()`

**Parameters:**
- question: User query (required)
- n_results: Number of results (default: 3)
- source_filter: Filter by source (optional)
- category_filter: Filter by category (optional)
- importance_filter: Filter by importance (optional)
- min_similarity: Minimum threshold (default: 0.0)

**Returns:**
- List of matching regulations with metadata and scores

**What to figure out:**
- Function signature
- Filter dictionary building
- Result formatting
- Error handling

**Success criteria:**
- [ ] Function accepts all parameters
- [ ] Can query with/without filters
- [ ] Returns formatted results
- [ ] Handles errors gracefully

---

**Part 2: Enhanced Filtering - 20 min**

**Requirements:**

**Test filtering:**

**Test 1:** Filter by source = "PCI-DSS"
**Test 2:** Filter by importance = "Critical"
**Test 3:** Combined: source = "GDPR" AND category = "Privacy"
**Test 4:** Filter by category = "Security"
**Test 5:** Minimum similarity = 0.7

**What to figure out:**
- ChromaDB where filter syntax
- Single and multiple filters
- Filter performance

**Success criteria:**
- [ ] All filter types working
- [ ] Can combine filters
- [ ] Results correctly filtered

---

**Part 3: Result Formatting - 15 min**

**Requirements:**

Create display function: `format_results()`

**Display for each result:**
- Result number and similarity score
- Source, category, importance
- Regulation text
- Reference number

**Example format:**
=== Search Results for: "credit card storage" ===
- Result 1 (Similarity: 0.92 | Importance: Critical)
- Source: PCI-DSS | Category: Security
- "Card verification value (CVV) must never be stored after authorization..."
- Reference: PCI-DSS 3.2.2

**Success criteria:**
- [ ] Results formatted clearly
- [ ] Professional appearance
- [ ] Easy to scan

---

**Fintech Focused:**

**Part 1: Build Search Function (Strict Mode) — 25 min**

The Fintech Constraint
Hallucination = Compliance Violation

You must enforce a confidence cutoff.

Updated Function Logic
def search_regulations(query, min_similarity=0.75):
    # 1. Vector Search
    results = collection.query(query_embeddings=[vec], n_results=5)

    # 2. Apply Threshold (Fintech Filter)
    valid_results = []
    for doc, score in zip(results["documents"][0], results["distances"][0]):
        # Adjust logic depending on similarity vs distance
        if score > min_similarity:
            valid_results.append(doc)

    # 3. Handle Empty Results
    if not valid_results:
        return ["NO_RELEVANT_REGULATION_FOUND. Please refine your query."]

    return valid_results

Success Criteria

 Threshold logic implemented

 Query like “Crypto mining rules on Mars” returns zero results, not a random closest match

**Part 2: Hybrid Search Implementation — 20 min (Core Requirement)**
Requirements

Pure semantic search fails on exact references like Section 10.3.

Implement a Keyword Booster:

Run vector search (top 10)

Check for exact keywords or IDs from the query (e.g., PCI-DSS, 10.3)

If keyword exists, boost score by +0.2

Re-rank and return Top 3

Success Criteria

 Searching “Section 10.3” returns Section 10.3 as the top result

 Exact identifiers override purely semantic similarity

### HOUR 4: Advanced Features (Optional)

**Part 1: Hybrid Search - 20 min**

**Requirements:**

Combine:
- Vector similarity
- Keyword matching
- Metadata filtering

**Approach:**
1. Semantic search (top 10)
2. Keyword boosting for regulation terms
3. Importance weighting
4. Re-rank and return top N

**Success criteria:**
- [ ] Hybrid search implemented
- [ ] Results improved
- [ ] Performance acceptable

---

**Part 2: Comprehensive Testing - 20 min**

**Requirements:**

**Edge cases (10 tests):**
1. Empty query
2. Very long query
3. No matches
4. Matches everything
5. Special characters
6. Different case
7. Very short query
8. Misspelled query
9. Question format
10. Statement format

**Performance tests:**
- Single query latency (<200ms target)
- Batch queries (10 queries)
- Memory usage

**Accuracy tests:**
- 20 test questions with known answers
- Calculate accuracy (>85% target)

**Success criteria:**
- [ ] All edge cases handled
- [ ] Performance acceptable
- [ ] Accuracy >85%
- [ ] Test report complete

---

### Day 6 Overall Deliverables

**Technical:**
- [ ] ChromaDB installed and configured
- [ ] 40-50 regulations indexed
- [ ] Search function with filtering
- [ ] Results formatted professionally

**Functional:**
- [ ] Can search regulations by natural language
- [ ] Returns relevant results
- [ ] Supports metadata filtering
- [ ] Handles edge cases
- [ ] Performance <200ms

**Testing:**
- [ ] Edge cases tested
- [ ] Performance benchmarked
- [ ] Accuracy measured
- [ ] Known limitations identified

**Portfolio Ready:**
- [ ] Clean, professional code
- [ ] Demonstrates practical AI
- [ ] Real-world use case
- [ ] Can demo in interviews

---

## DAY 7 (Sunday): Production CLI Tool - 3 hours

### Project Overview

Build complete production-ready command-line tool for payment regulations search.

### Schedule - 3 hours total

**Hour 1:** Enhanced Features & Analytics (60 min)
**Hour 2:** Production CLI Tool (60 min)
**Hour 3:** Documentation & Testing (60 min)

---

### HOUR 1: Enhanced Features

** Part 1: Search Analytics - 20 min**

**Requirements:**

Track search usage:
- Query text and timestamp
- Number of results returned
- Top result similarity score
- Filters applied
- Response time

**Storage:** JSON log file

**Analytics to generate:**
- Total searches
- Most common queries
- Average response time
- Most accessed regulations
- Filter usage patterns

**Success criteria:**
- [ ] Logging implemented
- [ ] Analytics generated
- [ ] Actionable insights

**Fintech Focused**

### HOUR 1: Enhanced Features & Audit Logging
**Part 1: Audit Logging (Compliance-Focused) — 20 min**
The Fintech Constraint

Regulators require full traceability of who searched for what and when.

Requirements

Create an append-only audit log (audit_logs.jsonl or SQL table).

Required Fields

timestamp: UTC ISO format

user_id: Mocked (e.g., analyst_01)

search_query: Raw query text

results_count: Number of documents returned

top_result_id: ID of the regulation shown

access_granted: true / false (mock RBAC decision)

Task

Log every search request to audit_logs.jsonl

Append-only (no overwrites)

Success Criteria

 Every search appends a new audit record

 Each entry contains user_id and timestamp

 Demonstrates regulator-ready auditability
---

**Part 2: Query Expansion - 20 min**

**Requirements:**

**Synonym expansion:**
```python
SYNONYMS = {
    "wire transfer": ["bank transfer", "SWIFT payment"],
    "fraud": ["suspicious activity", "unauthorized"],
    "customer data": ["personal information", "PII"],
    # Add 10-15 more
}
```

**Acronym handling:**
```python
ACRONYMS = {
    "PCI": "Payment Card Industry",
    "AML": "Anti-Money Laundering",
    "KYC": "Know Your Customer",
    "GDPR": "General Data Protection Regulation",
    # Add more
}
```

**Question reformulation:**
- "How do I..." → "procedures requirements"
- "What are rules for..." → "regulations requirements"
- "Is it allowed..." → "rules restrictions permissions"

**Success criteria:**
- [ ] Synonym expansion working
- [ ] Acronym expansion working
- [ ] Question reformulation implemented

---

**Part 3: Result Explanation - 20 min**

**Requirements:**

For each result, provide:
- Why result was returned
- Key matching concepts
- Relevance summary
- Related regulations

**Example:**
```
Result 1: PCI-DSS Encryption Requirements
Similarity: 0.89

Why relevant: Your query about "protecting card data" 
matches encryption and data protection concepts.
Key topics: encryption, TLS, data security.

Related regulations:
- Key Management Standards (PCI-DSS 3.6)
- Data Retention Policies (PCI-DSS 3.1)
```

**Success criteria:**
- [ ] Explanations generated
- [ ] Matching concepts highlighted
- [ ] Related regulations shown

---

### HOUR 2: Production CLI Tool

**Part 1: Build CLI - 30 min**

**Requirements:**

**Project structure:**
```
payment-regulations-search/
├── regulations_search.py
├── search_engine.py
├── analytics.py
├── config.py
├── requirements.txt
├── README.md
├── data/chroma/
├── logs/
└── tests/
```

**Basic commands:**
```bash
# Simple search
python regulations_search.py "How to encrypt card data?"

# With filters
python regulations_search.py "data retention" --source PCI-DSS

# Number of results
python regulations_search.py "authentication" --results 5

# Output formats
python regulations_search.py "encryption" --format json
python regulations_search.py "encryption" --format markdown
```

**Advanced commands:**
```bash
# Analytics
python regulations_search.py --analytics

# List sources
python regulations_search.py --list-sources

# Search history
python regulations_search.py --history

# Export results
python regulations_search.py "GDPR" --export results.json

# Interactive mode
python regulations_search.py --interactive
```

**Interactive mode:**
```
> search How to encrypt card data?
[Results]

> filter PCI-DSS
Filter applied

> search authentication
[Filtered results]

> exit
```

**Success criteria:**
- [ ] All commands working
- [ ] Interactive mode functional
- [ ] Error handling robust
- [ ] Professional UX

---

**Part 2: Output Formats - 15 min**

**Requirements:**

**Format 1: Table (default)**
```
╔════════════════════════════════════════╗
║ Search Results: "encryption"          ║
╚════════════════════════════════════════╝

Result 1 - Similarity: 0.92
Source: PCI-DSS | Category: Security
"Credit card data must be encrypted..."
```

**Format 2: JSON**
```json
{
  "query": "encryption",
  "results": [
    {
      "rank": 1,
      "similarity": 0.92,
      "source": "PCI-DSS",
      "text": "..."
    }
  ]
}
```

**Format 3: Markdown**
```markdown
# Search Results

**Query:** "encryption"

## Result 1 (0.92)
**Source:** PCI-DSS
> Credit card data must...
```

**Format 4: CSV**
```csv
rank,similarity,source,text
1,0.92,PCI-DSS,"Credit card..."
```

**Success criteria:**
- [ ] All 4 formats implemented
- [ ] Format selection working
- [ ] Export to file working

---

**Part 3: Configuration - 15 min**

**Requirements:**

**config.py:**
```python
CHROMA_PERSIST_DIRECTORY = "./data/chroma"
COLLECTION_NAME = "payment_regulations"
DEFAULT_NUM_RESULTS = 3
MIN_SIMILARITY_THRESHOLD = 0.5
ANALYTICS_LOG_FILE = "./logs/searches.json"
```

**requirements.txt:**
```
chromadb>=0.4.0
python-dotenv>=1.0.0
click>=8.1.0
tabulate>=0.9.0
colorama>=0.4.6
```

**Success criteria:**
- [ ] Configuration system implemented
- [ ] Environment variables supported
- [ ] requirements.txt complete
- [ ] Setup documented

---

### HOUR 3: Documentation & Testing

**Part 1: Documentation - 30 min**

**Requirements:**

**README.md **
# Payment Regulations Search System

Semantic search for payment regulations using embeddings.

## Features
- 🔍 Semantic search across 40+ regulations
- 🎯 Filter by source, category, importance
- 📊 Search analytics
- 💻 CLI and interactive modes
- 📄 Multiple output formats

## Quick Start

### Installation
```bash
pip install -r requirements.txt
python setup.py
```

### Usage
```bash
python regulations_search.py "How to encrypt card data?"
```

## Covered Regulations
- PCI-DSS (10)
- AML/KYC (10)
- GDPR (10)
- Payment Services (10)
- Regional (10)

## Performance
- Query time: <150ms
- Accuracy: >85%
- Storage: ~10MB

## Architecture
[Diagram or description]

## License
MIT
```

**USAGE_EXAMPLES.md:**
- 10-15 real-world examples
- Finding encryption requirements
- Checking thresholds
- Understanding retention rules
- Breach notification
- Authentication requirements

**ARCHITECTURE.md:**
- System design
- ChromaDB integration
- Search algorithm
- Future improvements

**Success criteria:**
- [ ] README comprehensive
- [ ] Usage examples helpful
- [ ] Architecture documented

---

**Part 2: Testing - 20 min**

**Requirements:**

**Test suite:**

**Unit tests:**
- search_regulations() function
- format_results() function
- build_filter() function

**Integration tests:**
- End-to-end search
- Search with filters
- Export functionality

**Edge case tests:**
- Empty queries
- Long queries
- Special characters
- No results

**Performance tests:**
- Query latency
- Memory usage

**Accuracy tests:**
- 20 test questions
- Measure correct in top 3
- Calculate accuracy %

**Success criteria:**
- [ ] Test suite complete
- [ ] All tests passing
- [ ] Coverage >80%
- [ ] Performance benchmarked

---

**Part 3: GitHub Prep - 10 min**

**Requirements:**

**Code cleanup:**
- Remove debug statements
- Add docstrings
- Consistent formatting
- Meaningful names

**.gitignore:**
```
__pycache__/
*.pyc
data/chroma/
logs/
.env
.vscode/
.DS_Store


**Git setup:**
```
git init
git add .
git commit -m "Initial commit: Payment Regulations Search"
```

**Success criteria:**
- [ ] Code clean and professional
- [ ] Git initialized
- [ ] Ready for GitHub
- [ ] Portfolio-ready

---

### Day 7 Overall Deliverables

**Complete System:**
- [ ] 40-50 regulations indexed
- [ ] Production CLI tool
- [ ] Interactive mode
- [ ] Multiple output formats
- [ ] Search analytics
- [ ] Query expansion

**Code Quality:**
- [ ] Clean, documented code
- [ ] Type hints added
- [ ] Consistent style
- [ ] Best practices

**Documentation:**
- [ ] README comprehensive
- [ ] Usage examples
- [ ] Architecture docs
- [ ] Installation guide

**Testing:**
- [ ] Test suite (30+ tests)
- [ ] All tests passing
- [ ] >80% coverage
- [ ] >85% accuracy

**Portfolio:**
- [ ] Professional presentation
- [ ] Real-world application
- [ ] Well-documented
- [ ] GitHub ready
- [ ] Interview-ready

---

## WEEK 5 COMPLETE SUMMARY

### Accomplishments

**Day 1:** Embeddings Concept ✅
**Day 2:** Semantic Search ✅
**Day 3:** Generate Embeddings ✅
**Day 4:** Vector Similarity ✅
**Day 5:** Vector Databases ✅
**Day 6:** ChromaDB Implementation ✅
**Day 7:** Production System ✅

### Skills Gained

**Technical:**
- Embeddings generation
- Vector similarity calculations
- ChromaDB usage
- Metadata filtering
- CLI development
- Search analytics

**Conceptual:**
- Embeddings vs keywords
- Semantic search principles
- Vector database architecture
- Similarity metrics
- Production considerations

### Portfolio Project

**Payment Regulations Search:**
- 40-50 regulations indexed
- <200ms query performance
- Multiple output formats
- Search analytics
- Production CLI
- >85% accuracy
- GitHub-ready

### Connection to RAG (Week 6)

**Week 5 (Search):**
```
Question → Embedding → Vector Search → Documents
```

**Week 6 (RAG):**
```
Question → Embedding → Vector Search → Documents
                                           ↓
                                       Feed to LLM
                                           ↓
                                   Generated Answer
                                           ↓
                                        Performance
                                            Query: <150ms average
                                            Accuracy: >85% (top 3)
                                            Cost: ~$1 (embeddings)
                                            Storage: ~10MB
```                                      
### Time & Cost
**Week 5:**

- Weekdays: 5 hours
- Weekend: 6-7 hours
- Total: ~11-12 hours
- Cost: ~$1

**Cumulative (Weeks 1-5):**

- Time: ~55-60 hours
- Cost: ~$7-15
- Projects: 3 portfolio pieces

### Ready for Week 6: RAG Systems
**What you'll learn:**

- RAG architecture
- LangChain fundamentals
 -Document loaders
- Retrieval + Generation 
- Q&A systems

**What you'll build:**

- Regulations Q&A System
- Uses Week 5 vector database
- Adds LLM generation
- Natural answers

You're prepared:

✅ Working semantic search
✅ Vector database expertise
✅ Search quality evaluation
✅ Ready for next level


Congratulations! 🎉
You've mastered embeddings and vector search!
Progress:

✅ Week 1: Math & Python
✅ Week 2: APIs & Calculus
✅ Week 3: LLMs & OpenAI
✅ Week 4: Prompt Engineering
✅ Week 5: Embeddings & Vector Search

Next: Week 6 - RAG with LangChain 🚀

End of Week 5 Learning Guide