# WEEK 5: DAY 6-7 (WEEKEND DEEP DIVE)
## LLM Model Selection & Production Prompt Engineering

**Duration:** 6-7 hours (Saturday-Sunday split)  
**Goal:** Benchmark 3 LLM models, document speed/accuracy trade-offs, build production prompt templates

---

## 📚 LEARNING RESOURCES

### Primary Learning Resources

**Prompt Engineering for Production:**
- "Advanced Prompt Engineering" - OpenAI Developer Day
  - Link: https://www.youtube.com/watch?v=ahnGLM-RC1Y
  - Duration: 18:47
  - Focus: Structured outputs, error handling patterns

### Supplementary Reading

**Ollama Model Comparison:**
- Ollama Model Library: https://ollama.com/library
- Duration: 10 min browse
- Compare: llama3.2, mistral, phi3 specs

**Production Prompting Best Practices:**
- Anthropic Prompt Engineering Guide: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices
- Duration: 20 min read
- Focus: Role, task, constraints, format structure

**Temperature & Sampling Parameters:**
- "LLM Parameters Guide" - Prompt Engineering Guide
  - Link: https://www.promptingguide.ai/introduction/settings
  - Duration: 10 min read
  - Focus: Temperature, top-p, top-k with examples

- "Token Selection Strategies" - Peter Chng
  - Link: https://peterchng.com/blog/2023/05/02/token-selection-strategies-top-k-top-p-and-temperature/
  - Duration: 12 min read
  - Focus: Mathematical explanation with visualizations

- "How to Tune LLM Parameters" - phData
  - Link: https://www.phdata.io/blog/how-to-tune-llm-parameters-for-top-performance-understanding-temperature-top-k-and-top-p/
  - Duration: 15 min read
  - Focus: Practical tuning for performance

**Model Benchmarking Concepts:**
- "Evaluating LLMs" - Hugging Face Course
  - Link: https://huggingface.co/learn/nlp-course/chapter1/7
  - Duration: 12 min read
  - Focus: Accuracy, speed, consistency metrics

**Prompt Engineering for Production:**
- "Prompt Engineering Overview" - Anthropic
  - Link: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
  - Duration: 20 min read
  - Focus: Role, task, constraints, format structure

### Supplementary Reading

**Ollama Model Comparison:**
- Ollama Model Library: https://ollama.com/library
- Duration: 10 min browse
- Compare: llama3.2, mistral, phi3 specs

**Production Prompting Best Practices:**
- Anthropic Prompt Engineering Guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Duration: 20 min read
- Focus: Role, task, constraints, format structure

---

## 🎯 DAY 6 (SATURDAY) - MODEL BENCHMARKING

**Time:** 3.5-4 hours

---

### SESSION 1: Understanding Sampling Parameters (90 mins)

**Theory (30 mins):**
Watch temperature/sampling video above (15 mins), then read:
- Ollama API docs on parameters: https://github.com/ollama/ollama/blob/main/docs/api.md
- Focus on: temperature, top_p, top_k, seed

**What you need to understand:**
1. Why does low temperature (0.1-0.3) give consistent outputs?
2. When would you want high temperature (0.7-1.0)?
3. What's the difference between top_p and top_k?
4. For fraud classification, which parameter set is best?

**Hands-on Experimentation (60 mins):**

**Requirements:**
Create `test_sampling_params.py` that:
- Tests same prompt with 3 parameter combinations
- Runs each combination 3 times
- Logs all outputs for comparison

**Test prompt template:**
```
Analyze this transaction for fraud:
Amount: $7,500
Merchant: Electronics Store XYZ  
Time: 2:30 AM
Location: 500 miles from cardholder home
Cardholder pattern: Average $150, mostly groceries

Classify as LEGITIMATE or SUSPICIOUS with reasoning.
```

**Parameter combinations to test:**
1. Deterministic: temp=0.1, top_p=0.95
2. Balanced: temp=0.5, top_p=0.9
3. Creative: temp=0.9, top_p=0.85

**What you need to figure out:**
- How to call Ollama Python library with these parameters
- How to structure output comparison (CSV? JSON?)
- Which combination gives most consistent fraud classification
- How many runs needed to see consistency patterns

**Success criteria:**
✅ 9 total outputs (3 params × 3 runs each)  
✅ Clear winner for "most consistent"  
✅ One-paragraph explanation: "For fraud detection, I choose temp=X because..."

---

### SESSION 2: Model Benchmarking Framework (150 mins)

**Preparation - Create Test Dataset (30 mins):**

**Requirements:**
Build `transaction_test_data.json` with 20 transactions:
- 10 clearly LEGITIMATE (normal patterns)
- 5 clearly SUSPICIOUS (obvious red flags)
- 5 EDGE CASES (ambiguous)

**What you need to figure out:**
- What fields are essential? (amount, merchant, time, location, pattern)
- What makes a transaction "clearly fraudulent" vs "edge case"?
- How to structure for automated testing?
- Should you include expected classification (ground truth)?

**Benchmark 3 Models (60 mins):**

**Models to test:**
1. **llama3.2** (3B params - Meta's latest)
2. **mistral** (7B params - Mistral AI)  
3. **phi3** (3.8B params - Microsoft)

**Watch first:** Model comparison video (15 mins from resources)

**Requirements:**
Create `benchmark_models.py` that:
- Pulls all 3 models via Ollama
- Tests each model on all 20 transactions
- Measures: accuracy, speed, consistency
- Outputs results to CSV

**Metrics to capture:**
- **Accuracy**: % matching ground truth
- **Speed**: Average ms per transaction
- **Consistency**: Agreement across repeat runs
- **Output quality**: Follows format?

**What you need to figure out:**
- How to install multiple Ollama models
- How to measure response time accurately
- How to calculate accuracy programmatically
- How to test "consistency" (run same transaction 3 times?)

**Analysis & Documentation (60 mins):**

**Requirements:**
Create `MODEL_SELECTION.md` documenting:

1. **Results Table:**
```
| Model     | Accuracy | Avg Time | P95 Time | Consistency |
|-----------|----------|----------|----------|-------------|
| llama3.2  |    %     |    ms    |    ms    |    %        |
| mistral   |    %     |    ms    |    ms    |    %        |
| phi3      |    %     |    ms    |    ms    |    %        |
```

2. **Speed vs Accuracy Trade-offs:**
- Which model is fastest?
- Which is most accurate?
- What's the "sweet spot" for production?

3. **Use Case Recommendations:**
- Real-time fraud screening (< 100ms): Model X because...
- Batch processing (accuracy priority): Model Y because...
- Edge case investigation (balanced): Model Z because...

4. **Interview Story** (2-3 paragraphs):
Write narrative: "I benchmarked three models... here's what I found... for production I'd choose X because..."

**What you need to figure out:**
- How to visualize results (simple table? chart?)
- What trade-offs matter for fintech
- How to explain technical decisions to non-technical stakeholders

**Success criteria:**
✅ Complete comparison data for 3 models  
✅ Clear recommendation with data backing  
✅ Interview-ready narrative (practice saying it!)

---

## 🎯 DAY 7 (SUNDAY) - PRODUCTION PROMPT ENGINEERING

**Time:** 2.5-3 hours

---

### SESSION 1: Compliance-Focused Prompts (90 mins)

**Theory (30 mins):**
Watch prompt engineering video from resources, read Anthropic guide sections on:
- Role definition
- Task clarity
- Constraints/rules
- Output formatting

**What you need to understand:**
- Why are fintech prompts different from general prompts?
- What does "compliance-ready" mean?
- How do structured outputs help auditing?

**Build Prompt Template Library (60 mins):**

**Requirements:**
Create `prompt_templates.py` with 3 templates:

**Template 1: FRAUD_CLASSIFIER**
Purpose: Binary classification with confidence

**What you need to figure out:**
- What role description sets fraud detection context?
- What constraints prevent hallucination?
- What output format ensures parseability?
- How to handle "insufficient data" cases?

**Template 2: TRANSACTION_EXPLAINER**  
Purpose: Customer-facing fraud alert explanations

**What you need to figure out:**
- How to ensure plain language (8th grade level)?
- Maximum length for customer messages?
- How to be factual without speculation?

**Template 3: PATTERN_ANALYZER**
Purpose: Behavioral anomaly detection

**What you need to figure out:**
- How to structure historical pattern description?
- What deviation types matter? (amount, category, time, location)
- How to quantify anomaly severity?

**Testing Requirements:**
- Test each template with 3 sample transactions
- Document: when to use which template
- Measure: does output follow format 100% of time?

**Success criteria:**
✅ 3 working prompt templates  
✅ Each tested on 3 transactions  
✅ Clear usage documentation

---

### SESSION 2: Structured Output Handling (90 mins)

**Learning Resources (20 mins):**

**Instructor Library Overview:**
- GitHub: https://github.com/jxnl/instructor  
- Duration: 10 min read
- Focus: Why structured outputs matter

**Pydantic Basics:**
- Pydantic docs: https://docs.pydantic.dev/latest/concepts/models/
- Duration: 10 min read
- Focus: BaseModel, Field, validators

**What you need to understand:**
- Why is string parsing unreliable?
- How does Instructor guarantee structure?
- When to use Pydantic validators?

**Build Response Parser (40 mins):**

**Requirements:**
Create `parse_llm_response.py` with:

**What you need to implement:**
1. JSON extraction from markdown code blocks
2. Response validation (required fields present?)
3. Retry logic for invalid responses

**What you need to figure out:**
- How to handle LLMs wrapping JSON in ```json blocks?
- How to validate classification values (only LEGITIMATE/SUSPICIOUS)?
- How to retry when LLM doesn't follow format?
- When to give up and log error?

**Production Integration (30 mins):**

**Requirements:**
Create `fraud_llm_client.py` class with:
- Model configuration (which model, what temperature)
- Request/response logging
- Automatic retries
- Performance metrics tracking

**What you need to figure out:**
- What should be logged for audit trail?
- How to measure performance (avg time, p95, p99)?
- How to handle errors gracefully?
- How to make client reusable?

**Success criteria:**
✅ Parser handles messy LLM outputs  
✅ Retry logic tested (simulate failures)  
✅ Client logs all requests/responses  
✅ Metrics tracked accurately

---

## 🎯 WEEKEND DELIVERABLES

### What You Built:
✅ Temperature/sampling experiment results  
✅ 3-model benchmark comparison  
✅ MODEL_SELECTION.md with trade-offs  
✅ 3 production prompt templates  
✅ Response parser with retry logic  
✅ Reusable LLM client class

### What You Documented:
✅ Parameter selection rationale  
✅ Model selection criteria  
✅ Speed vs accuracy trade-offs  
✅ Prompt design patterns

### What You Can Explain:
✅ "I benchmarked 3 models and chose X for production because..."  
✅ "For fraud detection, I use low temperature because..."  
✅ "My prompts are compliance-ready because..."  
✅ "I handle errors with retry logic and logging for audit trails"

---

## 📊 TIME BREAKDOWN

**Day 6 (Saturday):**
- Sampling parameters: 1.5h
- Model benchmarking: 2.5h
- Total: 4h

**Day 7 (Sunday):**
- Prompt engineering: 1.5h
- Output handling: 1.5h
- Total: 3h

**Weekend Total:** 7 hours

---

## 🔗 CONNECTS TO WEEK 6

Next week builds on this:
- Week 6 Day 1-2: RAG uses your LLM client
- Week 6 Day 3: Batch processing scales benchmarking
- Week 6 Day 5: Instructor formalizes structured outputs

Your MODEL_SELECTION.md becomes part of project documentation!

---

## 💡 PORTFOLIO IMPACT

**Resume bullet:**
"Benchmarked llama3.2, mistral, and phi3 models on fraud detection dataset; documented speed vs accuracy trade-offs for model selection"

**GitHub README:**
"Production-ready LLM integration with model benchmarking, compliance-focused prompts, and structured output parsing"

**Interview talking point:**
"I chose llama3.2 for the sweet spot of 85ms latency with 92% accuracy, over mistral's higher accuracy but slower speed"
