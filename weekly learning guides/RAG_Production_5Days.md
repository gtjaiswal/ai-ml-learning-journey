# WEEK 6: RAG SYSTEMS & PRODUCTION DEPLOYMENT (5 DAYS)
## Transaction Intelligence with Retrieval-Augmented Generation

**Duration:** 5 days (Mon-Fri), ~2.5h/day = 12.5 hours total  
**Goal:** Build production RAG system for transaction analysis with batch processing and structured outputs

---

## 📚 CORE LEARNING RESOURCES

### Video Resources

**RAG Fundamentals:**
- "What is Retrieval Augmented Generation (RAG)?" - IBM Technology
  - Link: https://www.youtube.com/watch?v=T-D1OfcDW1M
  - Duration: 10:02
  - Watch: Full video (clear RAG explanation)

**Vector Databases Explained:**
- "Vector Databases Simply Explained" - Fireship
  - Link: https://www.youtube.com/watch?v=dN0lsF2cvm4
  - Duration: 4:33
  - Watch: Full video (quick overview)

**Embeddings & Similarity Search:**
- "Embeddings Explained in 5 Levels" - WIRED (AI expert)
  - Link: https://www.youtube.com/watch?v=l7_eOWGC-mE  
  - Duration: 17:41
  - Watch: Levels 3-5 (technical depth)

**ChromaDB Tutorial:**
- "ChromaDB Tutorial" - Tech with Tim
  - Link: https://www.youtube.com/watch?v=5WFMlGOk0_k
  - Duration: 24:36
  - Watch: 0:00-15:00 (basics + setup)

**Instructor Library (Structured Outputs):**
- "Structured Outputs with Instructor" - Jason Liu (creator)
  - Link: https://www.youtube.com/watch?v=yj-wSRJwrrc
  - Duration: 43:11
  - Watch: 0:00-20:00 (core concepts)

### Written Resources

**Pydantic Models:**
- Pydantic Docs: https://docs.pydantic.dev/latest/concepts/models/
- Duration: 15 min focused read
- Focus: BaseModel, Field validators, model validation

**ChromaDB Documentation:**
- Getting Started: https://docs.trychroma.com/getting-started
- Duration: 10 min read
- Focus: Collections, adding documents, querying

**Instructor GitHub:**
- README: https://github.com/jxnl/instructor
- Duration: 10 min scan
- Focus: Basic usage patterns

---

## 📅 DAY 1-2 (MON-TUE): RAG FUNDAMENTALS
**Time:** 4.5 hours total (2h + 2.5h)

---

### DAY 1: Understanding RAG & Vector Search (2 hours)

**Theory Session (60 mins):**

**Watch:**
1. RAG Fundamentals video (10 mins)
2. Vector Databases video (5 mins)
3. Embeddings video - Levels 3-5 (10 mins)

**Read:**
- ChromaDB getting started guide (10 min)
- Review: What is cosine similarity? (skim online)

**What you need to understand:**
- Why does LLM need external context for fraud detection?
- How do embeddings capture transaction "similarity"?
- What makes transactions "similar" in vector space?
- Why is ChromaDB better than storing vectors in lists?

**Concept Check Questions:**
1. If two transactions have similar embeddings (cosine similarity 0.95), what does that mean?
2. How would RAG help analyze: "$5,000 electronics, 2 AM" transaction?
3. What gets stored in vector database for transactions?

**Hands-On Exploration (60 mins):**

**Requirements:**
Create `simple_vector_search.py`

**What you need to figure out:**
- Install sentence-transformers library
- Generate embeddings for 10 sample transactions
- Calculate cosine similarity between transaction pairs
- Find top-3 most similar to a query transaction

**Sample transaction texts:**
```
1. "$50 grocery store, 3 PM, local area"
2. "$5,000 electronics, 2 AM, 500 miles away"
3. "$75 restaurant, 7 PM, nearby"
4. [Create 7 more diverse examples]
```

**What you need to discover:**
- Which transactions cluster together?
- Does "$60 supermarket, 4 PM" match transaction 1 or 2?
- How does embedding capture semantic meaning?

**Success criteria:**
✅ Embeddings generated for all transactions  
✅ Similarity scores calculated  
✅ Can explain why certain transactions are "similar"

---

### DAY 2: ChromaDB & RAG Pipeline (2.5 hours)

**Theory Session (30 mins):**

**Watch:**
- ChromaDB Tutorial (0:00-15:00)

**Read:**
- ChromaDB docs on collections and querying

**What you need to understand:**
- How do collections organize data?
- What's the difference between documents and metadata?
- How does automatic embedding work?

**ChromaDB Setup & Operations (90 mins):**

**Requirements:**
Create `transaction_vector_db.py`

**What you need to implement:**
1. Initialize ChromaDB with persistent storage
2. Create "transactions" collection
3. Add 20 test transactions with metadata
4. Query for similar transactions

**What you need to figure out:**
- How to structure transaction data for ChromaDB?
- What goes in document vs metadata?
- How to set up persistence (data survives restarts)?
- How many results to retrieve (top-3? top-5?)?

**Metadata structure:**
```
{
  "amount": float,
  "merchant": str,
  "category": str,
  "timestamp": str,
  "label": "LEGITIMATE" | "FRAUD"
}
```

**Build Complete RAG Pipeline (60 mins):**

**Requirements:**
Create `fraud_rag_pipeline.py`

**Workflow to implement:**
1. Receive new transaction
2. Query vector DB for top-5 similar historical transactions
3. Build prompt with retrieved context
4. Call LLM (using Week 5 client)
5. Return classification with reasoning

**What you need to figure out:**
- How to convert transaction dict to search query?
- How to format retrieved transactions in prompt?
- How to structure prompt: [CONTEXT] vs [NEW TRANSACTION]?
- Does RAG improve accuracy over no-context baseline?

**Testing:**
- Run 5 test transactions through RAG pipeline
- Compare: RAG accuracy vs standalone LLM
- Document improvement (expect 10-15% boost)

**Success criteria:**
✅ ChromaDB collection persists between runs  
✅ RAG pipeline works end-to-end  
✅ Retrieved context visible in LLM responses  
✅ Measurable accuracy improvement

---

## 📅 DAY 3 (WED): BATCH PROCESSING PIPELINE
**Time:** 2.5 hours

---

**Theory Session (30 mins):**

**Learning Resources:**
- Python Concurrency: https://realpython.com/python-concurrency/
  - Duration: 15 min focused read
  - Focus: ThreadPoolExecutor basics

**What you need to understand:**
- Why batch processing vs real-time?
- When to use threads vs processes?
- How to handle errors without failing entire batch?

**Concept questions:**
1. Why process 1000 transactions in batch overnight?
2. What happens if transaction #237 fails in batch?
3. How many parallel workers optimal? (too many = problems)

**Build Batch Processor (120 mins):**

**Requirements:**
Create `batch_fraud_processor.py`

**What you need to implement:**
1. Load transactions from file (CSV/JSON)
2. Process using ThreadPoolExecutor (configurable workers)
3. Track progress (X/Y completed)
4. Handle individual failures gracefully
5. Export results with summary statistics

**What you need to figure out:**
- How to use ThreadPoolExecutor with your RAG pipeline?
- How to track which transactions processed/failed?
- What summary statistics matter? (total, success rate, fraud rate, avg time)
- How to export results (CSV format with headers)?

**Testing requirements:**
- Process 100 test transactions
- Simulate 2-3 failures (bad data)
- Measure total time
- Generate summary report

**Optimization (30 mins):**

**What you need to test:**
Different configurations:
- 1 worker vs 2 vs 4 vs 8
- With/without connection reuse
- Batch vector search vs individual queries

**What you need to document:**
- Which configuration fastest?
- What's the bottleneck?
- Optimal worker count for your machine?

**Success criteria:**
✅ Batch 100 transactions in < 2 minutes  
✅ Errors logged but don't stop batch  
✅ Results exported to CSV  
✅ Summary statistics generated

---

## 📅 DAY 4 (THU): CONTEXT ASSEMBLY ENGINE
**Time:** 2 hours

---

**Multi-Source Context (90 mins):**

**Requirements:**
Create `context_assembler.py`

**Context sources to implement:**
1. **Similar transactions** (vector search)
2. **Merchant profile** (fraud statistics)
3. **Temporal patterns** (time-of-day norms)

**What you need to figure out:**
- How to gather context from multiple sources efficiently?
- How to structure multi-source context in prompt?
- What if some context sources unavailable?
- How much context is too much? (token limits)

**Merchant profile structure (mock data):**
```
{
  "merchant_id": "MERCHANT_123",
  "name": "Electronics Store XYZ",
  "category": "Electronics",
  "fraud_rate": 0.023,  # 2.3%
  "total_transactions": 5420,
  "risk_level": "MEDIUM"
}
```

**Temporal patterns (mock data):**
```
{
  "hour": 2,  # 2 AM
  "day_of_week": "Saturday",
  "fraud_rate_this_hour": 0.087,  # 8.7%
  "normal_for_category": false
}
```

**Adaptive Context Selection (30 mins):**

**Requirements:**
Implement logic to select context depth based on transaction complexity.

**Context levels:**
- **Minimal**: Simple case → 2 similar transactions only
- **Moderate**: Unclear case → 4 similar + merchant profile
- **Rich**: Edge case → 5 similar + merchant + temporal

**What you need to figure out:**
- What makes a transaction "simple" vs "edge case"?
- How to classify automatically?
- Does adaptive approach save time vs always using "rich"?

**Success criteria:**
✅ Context assembled from 2+ sources  
✅ Adaptive selection logic working  
✅ Faster than always using maximum context

---

## 📅 DAY 5 (FRI): STRUCTURED OUTPUTS (INSTRUCTOR + PYDANTIC)
**Time:** 2.5 hours

---

**Theory Session (45 mins):**

**Watch:**
- Instructor library video (0:00-20:00)

**Read:**
- Pydantic BaseModel docs (15 min)
- Instructor README examples (10 min)

**What you need to understand:**
- Why is string parsing unreliable?
- How does Instructor guarantee structure?
- What are Pydantic validators?
- When to use Field() constraints?

**Build Three Production Models (105 mins):**

**Requirements:**
Create `fraud_models.py` with Pydantic models:

**MODEL 1: SanitizedTransaction (Input Validator)**

**What you need to implement:**
- Required fields: id, amount, merchant, timestamp, location
- Validators: amount > 0, timestamp not future
- Optional fields: cardholder_pattern

**What you need to figure out:**
- How to use Pydantic's @validator decorator?
- How to validate timestamp format?
- What's reasonable max amount? ($1M+ probably error)

**MODEL 2: FraudAnalysis (LLM Output Structure)**

**What you need to implement:**
- classification: Literal["LEGITIMATE", "SUSPICIOUS", "INSUFFICIENT_DATA"]
- confidence: Literal["HIGH", "MEDIUM", "LOW"]
- risk_factors: List[str]
- risk_score: int (0-100)
- reasoning: str (min 10 chars)
- recommended_action: Literal["APPROVE", "REVIEW", "DECLINE", "REQUEST_VERIFICATION"]

**What you need to figure out:**
- How to use Literal for enum-like fields?
- How to ensure LLM returns exact values?
- How to validate risk_score range (0-100)?

**MODEL 3: FraudAuditRecord (Complete Trail)**

**What you need to implement:**
- audit_id, transaction_id, timestamp_analyzed
- input_transaction: SanitizedTransaction
- analysis_result: FraudAnalysis
- model_used, model_parameters
- context_sources: List[str]
- processing_time_ms: int

**What you need to figure out:**
- How to nest Pydantic models?
- How to capture all metadata for audit?
- What format for export (JSON)?

**Integration with Instructor (45 mins):**

**Requirements:**
Update RAG pipeline to use Instructor

**What you need to implement:**
1. Patch Ollama client with Instructor
2. Force LLM to return FraudAnalysis model
3. Handle validation errors (retry?)
4. Generate complete FraudAuditRecord

**What you need to figure out:**
- How does Instructor integrate with Ollama?
- What if LLM can't match structure after retries?
- How to log audit records to file?

**Testing:**
- Process 10 transactions through new pipeline
- Verify 100% structured outputs
- Export sample audit record JSON

**Success criteria:**
✅ All 3 Pydantic models working  
✅ Instructor integration successful  
✅ Zero parsing errors on test set  
✅ Audit records exportable

---

## 📅 DAY 7 (WEEKEND): DOCUMENTATION
**Time:** 2 hours

---

**Create Professional README.md:**

**Requirements:**
GitHub-ready documentation with:

**Sections to write:**
1. **Overview** (2-3 sentences: what + why)
2. **Architecture** (simple text diagram)
3. **Key Features** (bullet points with checkmarks)
4. **Tech Stack** (LLM, vector DB, libraries)
5. **Performance Metrics** (latency, throughput, accuracy)
6. **Quick Start** (installation steps)
7. **Project Structure** (directory tree with explanations)
8. **Design Decisions** (why RAG? why Instructor? why local LLM?)
9. **Future Enhancements** (3-5 items)

**What you need to figure out:**
- How to make technical yet accessible?
- What metrics to highlight?
- How to explain value to non-technical reader?

**Performance metrics to document:**
- Average latency: ___ ms
- Batch throughput: ___ transactions/minute
- Accuracy: ___% on test dataset
- Model choice: ___ because ___

**Design decisions to explain:**
- Why RAG over fine-tuning?
- Why ChromaDB over alternatives?
- Why Instructor for structured outputs?
- Why local LLM over API?

**Success criteria:**
✅ README < 300 lines  
✅ Non-technical person understands value  
✅ Technical recruiter sees depth  
✅ Professional tone throughout

---

## 🎯 WEEK 6 COMPLETE DELIVERABLES

### Code Artifacts:
✅ Vector search implementation  
✅ ChromaDB transaction database  
✅ Complete RAG pipeline  
✅ Batch processing engine  
✅ Context assembler (multi-source)  
✅ Three Pydantic models  
✅ Instructor integration  

### Documentation:
✅ BATCH_PROCESSING.md (optimization results)  
✅ CONTEXT_ASSEMBLY.md (design decisions)  
✅ Professional README.md  

### Skills Demonstrated:
✅ RAG architecture implementation  
✅ Vector database operations  
✅ Parallel processing patterns  
✅ Structured output validation  
✅ Production error handling  
✅ Technical writing  

---

## 📊 TIME BREAKDOWN

**Day 1:** RAG fundamentals - 2h  
**Day 2:** ChromaDB + pipeline - 2.5h  
**Day 3:** Batch processing - 2.5h  
**Day 4:** Context assembly - 2h  
**Day 5:** Structured outputs - 2.5h  
**Day 7:** Documentation - 2h  

**Total:** 13.5 hours over 6 days

---

## 💡 PORTFOLIO IMPACT

**GitHub README highlights:**
- "RAG system with multi-source context assembly"
- "Batch processing: 1000 transactions in 2 minutes"
- "Structured outputs with Pydantic validation"
- "Complete audit trail for regulatory compliance"

**Resume bullets:**
- "Built RAG-powered transaction intelligence system with ChromaDB vector database"
- "Implemented batch processing pipeline with parallel execution and error recovery"
- "Designed structured output models ensuring 100% parseable LLM responses"

**Interview talking points:**
1. "I chose RAG over fine-tuning because..."
2. "My batch processor handles failures gracefully by..."
3. "Instructor guarantees structured outputs, critical for compliance..."

---

## 🔗 CONNECTS TO NEXT STEPS

**Month 2 Preview:**
- Week 7-8: Airflow orchestration of batch jobs
- Week 9: AWS deployment
- Week 10: Monitoring and observability

Your RAG system becomes the core production workload!
