# WEEK 5: LLM FUNDAMENTALS - Complete Day-wise Plan

## WEEK 5 OVERVIEW

**Duration:** 7 days (5 weekdays @ 1-1.5 hours each + 2 weekend days @ 3-4 hours each)
**Total Time:** ~11-13 hours
**Goal:** Master LLM fundamentals, transformer architecture, OpenAI API integration, and prompt engineering basics
**Deliverable:** Payment transaction Q&A chatbot using OpenAI API with fintech-optimized prompts

**Current Progress:** Week 4 completed (arXiv pipeline operational)
**Starting Date:** December 16, 2025 (Tuesday)

---

## DAY 1 (Tuesday Dec 16): LLM Fundamentals & Architecture - 90 minutes  ✅

### Primary Video Resources  ✅

**"Intro to Large Language Models" by Andrej Karpathy** 
- Link: https://www.youtube.com/watch?v=zjkBMFhNj_g  ✅
- Duration: 1:00:00
- Watch: Full video (essential foundation)
- What you'll learn: How LLMs work, capabilities, limitations, GPT architecture

**Introduction to Large Language Models** by Google Cloud Tech  
- Link: https://www.youtube.com/watch?v=zizonToFXDs    ✅
- Duration: 15:46  
- What LLMs are, next-token prediction, and how parameters capture knowledge  

**AI ML Training versus Inference** by New Machina  
- Link: https://www.youtube.com/watch?v=lsPucobtdDk   ✅
- Duration: 09:20  
- Clear distinction between training (learning) and inference (usage) phases

**What is the LLM's Context Window ?** by New Machina  
- https://www.youtube.com/watch?v=y5wBbDSe0cM  ✅

**What are Transformers (Machine Learning Model)?**
- Link: https://www.youtube.com/watch?v=ZXiruGOCn9s  ✅
- Link: https://www.youtube.com/watch?v=SZorAJ4I-sA   ✅ + https://www.daleonai.com/transformers-explained
- Learn more about Transformers → http://ibm.biz/ML-Transformers

**Transformer Neural Networks (ChatGPT’s Foundation)** by StatQuest with Josh Starmer  
- Link: https://www.youtube.com/watch?v=zxQyTK8quyY  🟡 
- Duration: 36:15  
- Tokenization, embeddings, positional encoding, self-attention, encoder/decoder, and parallelization

**Attention in Transformers, Step-by-Step** by 3Blue1Brown  
- Link: https://www.youtube.com/watch?v=lsPucobtdDk    ✅
- Duration: 26:10  
- Intuitive visual explanation of self-attention and contextual word representations  

**Self-Attention Explained Visually (Transformer Intuition)**  
- Link: https://www.youtube.com/watch?v=PSs6nxngL6k  
- Duration: ~15:00  
- Conceptual and visual intuition behind attention and transformer scalability

**"The Illustrated GPT-2" (Visual Walkthrough)**
- Link: https://www.youtube.com/watch?v=-QH8fRhqFHM&list=PLTx9yCaDlo1UlgZiSgEjq86Zvbo2yC87d&index=2  ✅
- Link https://www.youtube.com/watch?v=uSinkCeUg9U  ✅
- https://jalammar.github.io/illustrated-gpt2/
- Duration: 30 min read
- Visual step-by-step transformer architecture explanation

**Links for the "Data Privacy in LLMs" subtopic**
- Additional Resources for Day 1: Data Privacy & Security
    **"LLM or Large Liability Model? The risks of ChatGPT in Finance"**
        - https://www.globalrelay.com/resources/thought-leadership/large-language-model-or-large-liability-model-what-are-the-risks-of-chatgpt-in-financial-services/
        - Why relevant: This article specifically discusses why financial institutions like Bank of America and Goldman Sachs have restricted ChatGPT, citing risks of bias, hallucination, and data leakage.
    **"Data Privacy and Security Challenges in Using LLMs for Business"**
        - https://medium.com/@gurpreets_87390/data-privacy-and-security-challenges-in-using-llms-for-business-4a2945009847
        - Why relevant: It breaks down key risks such as "Data Leakage Through Prompts," "Retention of Input Data," and "Prompt Injection Attacks," which are critical for understanding why banks are cautious.
    **"Managing Privacy Risks in Large Language Models" - Securiti.ai Whitepaper**
        - https://securiti.ai/whitepapers/llm-privacy-risks/
        - Why relevant: Offers a more technical deep dive into privacy risks like sensitive data memorization and regulatory compliance (GDPR, etc.).
    **"The companies now banning their workers from using ChatGPT"**
        - https://www.semafor.com/article/05/19/2023/chatgpt-companies-banning-workers
        - Why relevant: Provides a list of major companies (including banks) that have banned or restricted ChatGPT and the specific reasons given (confidential data leaks, compliance).
    **Data Privacy for LLMs**
        - https://youtu.be/XmgXbqT7610
        - Why relevant: Visual explanation of how data privacy issues arise in LLM architectures and techniques like opaque prompts to mitigate them.

### Reading Materials  ✅

**"How GPT Models Work" by OpenAI**
- Link: https://platform.openai.com/docs/guides/text-generation  ✅
- Duration: 15 min read
- Official explanation of text generation

**"Attention Is All You Need" (Original Transformer Paper)** 🟡 
- Link: https://arxiv.org/abs/1706.03762
- Duration: Read abstract and introduction only (10 min)
- Historical context and innovation

**"Understanding Large Language Models" by Anthropic** 🟡 
- Link: https://www.anthropic.com/index/core-views-on-ai-safety
- Duration: 15 min read
- Safety, capabilities, and limitations perspective

### Schedule - 90 minutes total  ✅

**Part 1: High-Level Understanding (40 min)**
1. Watch: "GPT in 100 Seconds" (3 min)  ✅
2. Watch: Andrej Karpathy lecture first 30 min (30 min)  ✅
3. Read: OpenAI text generation guide (7 min)  ✅

**Part 2: Architecture Deep Dive (35 min)**
4. Read: Illustrated GPT-2 walkthrough (25 min)  ✅
5. Read: Transformer paper abstract (10 min)  ✅

**Part 3: Reflection & Application (15 min)**
6. Document key concepts  ✅
7. Identify payment domain applications  ✅

### Key Concepts to Master  ✅

**What are Large Language Models (LLMs)?**  ✅
    - Neural networks trained on massive text datasets
    - Learn statistical patterns in language
    - Predict next word/token based on previous context
    - Billions of parameters (weights) that encode knowledge
    - Transformer architecture enables long-range dependencies

**How LLMs Actually Work:?**  ✅

1. **Training Phase (Done Once):**  ✅
   - Read billions of web pages, books, code, articles
   - Learn task: "Given this text, predict next word"
   - Adjust billions of parameters to minimize errors
   - Takes weeks/months on thousands of GPUs
   - Cost: Millions of dollars
   - Result: Model file with learned patterns

2. **Inference Phase (When You Use It):**  ✅
   - You provide input text (prompt)
   - Model predicts most likely next token
   - Samples from probability distribution
   - Generates one token at a time
   - Uses attention to consider all previous tokens
   - Continues until stop condition or max length

**The Transformer Architecture:**  ✅

1. **Core Innovation: Self-Attention Mechanism**  ✅
   - Allows model to "look at" all previous words simultaneously
   - Weighs importance of each word for current prediction
   - Example: "The bank approved the loan application"
     - Word "bank" attends to "loan", "application" → financial institution
     - Not "river bank" because context clarifies meaning
  
2. **Key Components:**

   1. **Tokenization:**  ✅
      - Break text into smaller units (tokens)
      - Vocabulary of ~50,000 tokens
      - Each token has unique ID number

   2. **Embeddings:**  ✅
      - Convert token IDs to dense vectors
      - Similar meanings → similar vectors
      - Enables semantic understanding

   3. **Positional Encoding:**  ✅
      - Add position information to embeddings
      - Model understands word order
      - "Dog bites man" ≠ "Man bites dog"

   4. **Self-Attention Layers:**  ✅
      - Weigh relevance of all tokens
      - Multiple attention heads (8-96)
      - Each head captures different relationships

   5. **Feed-Forward Networks:**  ✅
      - Process each position independently
      - Add non-linearity and complexity
      - Transform representations

   6. **Layer Normalization:**  ✅
      - Stabilize training
      - Improve convergence

   7. **Output Layer:**  ✅
      - Convert to probability distribution
      - Over entire vocabulary
      - Sample next token from distribution

**Why Transformers Work So Well:**  ✅

1. **Parallelization:**  ✅
   - Process all positions simultaneously
   - Unlike RNNs that process sequentially
   - Trains much faster on GPUs

2. **Long-Range Dependencies:**  ✅
   - Attention connects distant words directly
   - No degradation over distance
   - Understands complex relationships

3. **Scalability:**  ✅
   - Larger models = better performance
   - More parameters = more knowledge
   - More data = better generalization  ✅

### Connection to Payments Domain  ✅

**Use Case 1: Transaction Description Understanding**
```
Raw Description: "SQ *COFFEE ROASTERS 123 MAIN ST LONDON"

LLM Understanding:
- Payment Processor: Square (SQ)
- Merchant: Coffee Roasters
- Location: 123 Main St, London
- Category: Food & Dining → Coffee Shop
- Type: Card-Present Transaction
```

**Use Case 2: Fraud Pattern Detection**
```
Transaction Pattern:
"$2,500 electronics at 3 AM from Nigeria, 
customer normally shops in USA, 
average transaction $50"

LLM Analysis:
- Amount anomaly: 50x typical
- Time anomaly: 3 AM unusual
- Location anomaly: International, high-risk country
- Category anomaly: First electronics purchase
- Velocity check: Multiple high-value in short time
Risk Score: 95/100 - CRITICAL
```

**Use Case 3: Regulatory Compliance Q&A**
```
Question: "What PCI-DSS requirements apply to storing card data?"

LLM Response:
- Requirement 3.2: Mask PAN when displayed
- Requirement 3.4: Encrypt cardholder data at rest
- Requirement 3.5: Document key management procedures
- Requirement 3.6: Secure cryptographic key management
[Cites specific requirement numbers]
```

**Use Case 4: Chargeback Dispute Analysis**
```
Customer Claim: "I never received the product I ordered"

LLM Processing:
- Dispute Category: Product/Service Issue
- Sub-category: Product not received
- Required Evidence: Tracking number, delivery confirmation
- Win Probability: 70% with proof of delivery
- Recommended Action: Fight if delivery confirmed
```

**Use Case 5: Customer Support Automation**
```
Customer: "Why was my card declined at the restaurant?"

LLM Response Generation:
- Check transaction history
- Identify decline reason
- Generate empathetic explanation
- Suggest resolution steps
- Offer escalation path if needed
```

### Attention Mechanism Deep Dive  ✅

**Analogy: Reading a Sentence Like a Human**

When you read: "The bank by the river has excellent loan rates"

Your brain:
1. Sees "bank"
2. Looks ahead to "river" and "loan"
3. Determines: financial institution (not riverbank)
4. Connects "excellent" with "loan rates"

Transformers do this with **attention scores**.

**How Self-Attention Works:**  ✅

**Input:** "The bank approved the loan application"

**Step 1: Create Query, Key, Value vectors**
- Each word gets 3 vectors
- Query: "What am I looking for?"
- Key: "What do I have?"
- Value: "What do I return?"

**Step 2: Calculate attention scores**
- For word "bank":
  - Compare query with all keys
  - "loan" key has high similarity → high score
  - "application" key has high similarity → high score
  - "the" key has low similarity → low score

**Step 3: Weighted sum**
- Multiply scores by values
- Sum to get context-aware representation
- "bank" now incorporates "loan" context

**Result:** "bank" representation now knows it means financial institution

**Multi-Head Attention:**  ✅

**Why Multiple Heads?**
- Different heads learn different patterns
- Head 1: Grammatical relationships (subject-verb)
- Head 2: Semantic relationships (word meanings)
- Head 3: Long-range dependencies (pronouns)
- Head 4-8: Other specialized patterns

**Combination:**
- Each head produces representation
- Concatenate all heads
- Linear transformation to combine
- Richer, more nuanced understanding

### LLM Capabilities & Limitations  ✅

**What LLMs Can Do Well:**  ✅
- Text generation (articles, emails, code)
- Summarization (long documents → key points)
- Translation (between languages)
- Classification (categorize text)
- Question answering (from provided context)
- Code generation (Python, SQL, JavaScript)
- Reasoning (step-by-step problem solving)
- Extraction (pull structured data from text)
- Sentiment analysis (positive/negative/neutral)
- Named entity recognition (find names, dates, amounts)

**What LLMs Cannot Do:**  ✅
- Access real-time information (training cutoff date)
- Perform arithmetic reliably (use calculators/code)
- Remember previous conversations (stateless API)
- Access external databases (without integration)
- Execute actions (without tool integration)
- Understand images natively (need multimodal models)
- Guarantee 100% factual accuracy (can hallucinate)

**Hallucinations Explained:**

**What are hallucinations?**
- LLM generates plausible but false information
- Confidently states incorrect facts
- Makes up references, statistics, or events

**Why do they happen?**
- Model predicts based on patterns, not facts
- Training data contains errors
- No access to truth verification
- Optimized for fluency, not accuracy

**How to mitigate:**
- Retrieval-Augmented Generation (RAG) - Week 7-11
- Provide source documents for grounding
- Ask for citations and sources
- Use temperature=0 for consistency
- Verify critical information externally

### Important Terminology  ✅

**Token:**  
- Basic unit of text for LLMs
- Can be word, part of word, or character
- "transaction" = 1 token
- "unauthorized" = 2-3 tokens
- Affects cost and context limits

**Context Window:**  
- Maximum tokens model processes at once
- GPT-3.5-Turbo: 4K or 16K tokens
- GPT-4: 8K, 32K, or 128K tokens
- Includes prompt + response
- Exceeding causes error

**Temperature:**
- Controls randomness (0-2 scale)
- 0: Deterministic (same output every time)
- 1: Balanced creativity
- 2: Very random, creative
- Lower for factual tasks, higher for creative

**Prompt:**
- Input text given to LLM
- Includes instructions, context, examples
- Quality affects output quality
- "Prompt engineering" is key skill

**Fine-tuning:**
- Additional training on specific data
- Adapts model to domain/task
- Requires labeled examples
- Month 3 of your plan covers this

### Reflection Questions
1. What are transformers and how do they differ from previous architectures?
2. How does the attention mechanism help LLMs understand context?
3. What is a token and why does it matter for cost and limits?
4. What can LLMs do well for payment processing applications?
5. What are the key limitations of LLMs in fintech?
6. How would you use an LLM for transaction categorization?
7. What is hallucination and why is it a concern?
8. How does the context window constraint affect conversation design?

### Day 1 Deliverables  ✅

- [ ] Watched Andrej Karpathy LLM intro (full video or at least 30 min)
- [ ] Read Illustrated GPT-2 visual guide completely
- [ ] Read OpenAI text generation documentation
- [ ] Understand: What LLMs are and how they work at high level
- [ ] Understand: Transformer architecture key components
- [ ] Understand: Attention mechanism concept and purpose
- [ ] Can explain: Tokens, context windows, temperature
- [ ] Listed 5+ payment domain use cases for LLMs
- [ ] Wrote reflection answers (8 questions)
- [ ] Spent approximately 90 minutes on focused learning

---

## DAY 2 (Wednesday Dec 17): Tokenization & Cost Analysis - 60 minutes  ✅

### Primary Resources  ✅

**"Tokenization Explained" by OpenAI (Interactive)**  ✅
- Link: https://platform.openai.com/tokenizer
- Duration: 15 min hands-on experimentation
- Real-time tokenization visualization

**"Let's Build GPT Tokenizer" by Andrej Karpathy**  ✅
- Link: https://www.youtube.com/watch?v=zduSFxRajkE
- Duration: 2:18:00 total (watch first 20 minutes only)
- Understanding tokenization from first principles

**"Understanding Tokens and Pricing" - OpenAI Guide**  ✅
- Link: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- Duration: 10 min read
- Practical token counting and cost calculation

### Video Resources  ✅

**"How Tokenization Works in LLMs"**  ✅
- https://www.youtube.com/watch?v=nKSk_TiR8YA
- Duration: 12:00 

**Explanation of Byte Pair Encoding**  ✅
- https://www.youtube.com/watch?v=4A_nfXyBD08

### Reading Materials  ✅

**"Byte Pair Encoding (BPE) Explained"**
- Link: https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0  ✅
- Duration: 15 min read
- Algorithm behind modern tokenization

**"Managing Token Costs"**
- Link: https://platform.openai.com/docs/guides/realtime-costs#page-top  ✅
- Duration: 10 min read
- Cost optimization strategies

### Schedule - 60 minutes total  ✅

**Part 1: Understanding Tokenization (25 min)**  ✅
1. Watch: Tokenization video (12 min)
2. Read: OpenAI token guide (8 min)
3. Experiment: Tokenizer tool (5 min)

**Part 2: BPE Algorithm (15 min)**  ✅
4. Read: BPE explanation (15 min)

**Part 3: Cost Analysis (20 min)**
5. Calculate costs for payment scenarios
6. Build cost estimation framework

### Key Concepts to Master  ✅

**What is Tokenization?**  ✅
- Process of breaking text into tokens
- LLMs don't read text directly - they read token IDs
- Each token maps to a number in vocabulary
- Vocabulary size: ~50,000 tokens for GPT models
- Model predicts next token ID, converts back to text

**Why Tokenization Matters:**  ✅

1. **Cost Impact:**
   - Pricing based on tokens, not words or characters
   - More tokens = higher cost
   - Inefficient tokenization = wasted money

2. **Context Limits:**
   - Context window measured in tokens
   - Must fit prompt + response within limit
   - Exceeding limit causes request failure

3. **Performance:**
   - More tokens = longer processing time
   - Token count affects latency
   - Matters for real-time applications

4. **Quality:**
   - Poor tokenization can confuse model
   - Important for multilingual text
   - Affects model understanding

**How Byte Pair Encoding (BPE) Works:**  ✅

**Goal:** Balance vocabulary size vs. token efficiency  ✅

**Algorithm Steps:**  ✅

**Step 1: Start with character vocabulary**
    ```
    Text: "payment"
    Initial: ['p', 'a', 'y', 'm', 'e', 'n', 't']
    ```
    
**Step 2: Find most frequent adjacent pairs**
    ```
    Scan all text, find most common pairs
    Example: "pa" appears frequently
    ```
    
**Step 3: Merge frequent pair into single token**
    ```
    "pa" → single token
    Update: ['pa', 'y', 'm', 'e', 'n', 't']
    ```
    
**Step 4: Repeat until target vocabulary size**
    ```
    Merge "pay", then "payment"
    Common words become single tokens
    ```

**Result:**  ✅
  - Frequent words: 1 token ("payment", "transaction")
  - Rare words: Multiple tokens ("unauthorized" → 2-3 tokens)
  - Unknown words: Many character tokens

**Tokenization Examples:**  ✅

**Common Payment Terms:**  ✅
- "fraud" → 1 token
- "transaction" → 1 token
- "payment" → 1 token
- "merchant" → 1 token
- "chargeback" → 2 tokens: ["charge", "back"]

**Technical Terms:**  ✅
- "PCI-DSS" → 3 tokens: ["PC", "I", "-", "DSS"]
- "AML/KYC" → 4 tokens: ["AM", "L", "/", "KY", "C"]
- "3DS" → 2 tokens: ["3", "DS"]
- "EMV" → 2 tokens: ["E", "MV"]

**Numbers:**  ✅
- "123" → 1 token
- "1234" → 1 token
- "12345" → 2 tokens: ["123", "45"]
- "123456789" → 3-4 tokens
- "$1,234.56" → 5-6 tokens: ["$", "1", ",", "234", ".", "56"]

**Merchant Names:**  ✅
- "Starbucks" → 2 tokens: ["Star", "bucks"]
- "McDonald's" → 2 tokens: ["McDonald", "'s"]
- "Amazon" → 1 token
- "Netflix" → 1 token

**Whitespace and Punctuation:**  ✅
- Space before word often part of token
- " hello" = different token than "hello"
- Punctuation usually separate tokens
- "..." → 1 token
- "!!!" → 1 token

### Token Counting Rules of Thumb  ✅

**English Text:**
- 1 token ≈ 4 characters
- 1 token ≈ 0.75 words
- 100 words ≈ 75 tokens

**Code:**
- More tokens than English text
- Special characters = separate tokens
- Variable names = multiple tokens

**Numbers:**
- Grouped in 3-4 digit chunks
- More digits = more tokens
- Formatted numbers (commas, decimals) = extra tokens

### Context Window Management  ✅

**Model Limits:**  ✅

**GPT-3.5-Turbo:**
- Standard: 4,096 tokens
- Extended: 16,384 tokens
- Cost-effective for most tasks

**GPT-4:**
- Standard: 8,192 tokens
- Extended: 32,768 tokens  
- Turbo: 128,000 tokens
- Higher quality, higher cost

**What Counts Toward Limit:**
- System prompt (instructions)
- All previous user messages
- All previous assistant responses
- Current user message
- Function definitions (if using function calling)
- Response tokens

**Example Calculation:**
```
System prompt: 150 tokens
Previous conversation: 500 tokens
Current user message: 50 tokens
Total used: 700 tokens
Available for response: 4,096 - 700 = 3,396 tokens
```

**Strategies for Long Contexts:**  ✅

**Strategy 1: Summarization**
- Summarize old messages periodically
- Keep recent messages in full
- Reduces token count while preserving context
- Small cost for summarization API call

**Strategy 2: Sliding Window**
- Keep only last N messages
- Discard oldest when limit approached
- Simple to implement
- May lose important early context

**Strategy 3: Selective Memory**
- Identify and keep important messages
- Discard routine acknowledgments
- Preserve key decisions and data
- More complex logic required

**Strategy 4: RAG Approach**
- Store conversation in external database
- Retrieve relevant portions when needed
- Unlimited effective context
- Week 7-11 covers this extensively

### Cost Implications  ✅

**Pricing Structure (December 2024):**  ✅

**GPT-3.5-Turbo:**
- Input: $0.0005 per 1K tokens
- Output: $0.0015 per 1K tokens
- Good for: High-volume, simple tasks

**GPT-4:**
- Input: $0.01 per 1K tokens  
- Output: $0.03 per 1K tokens
- 20-30x more expensive than GPT-3.5
- Good for: Complex reasoning, high accuracy needs

**GPT-4 Turbo:**
- Input: $0.01 per 1K tokens
- Output: $0.03 per 1K tokens
- 128K context window
- Good for: Long documents, complex analysis

### Payment Domain Cost Analysis  ✅

**Scenario 1: Transaction Categorization**  ✅

**Requirements:**
- Categorize 10,000 transactions/day
- Simple task: merchant → category

**Prompt Structure:**
```
System: 100 tokens (category definitions)
User: 30 tokens (transaction description)
Response: 20 tokens (category + confidence)
Total per transaction: 150 tokens
```

**Daily Cost Calculation:**
```
Total tokens: 10,000 × 150 = 1,500,000 tokens
Input tokens: 10,000 × 130 = 1,300,000 tokens
Output tokens: 10,000 × 20 = 200,000 tokens

With GPT-3.5-Turbo:
Input: 1,300K × $0.0005/1K = $0.65
Output: 200K × $0.0015/1K = $0.30
Daily: $0.95
Monthly: $28.50
Annual: $346.75

With GPT-4:
Input: 1,300K × $0.01/1K = $13.00
Output: 200K × $0.03/1K = $6.00
Daily: $19.00
Monthly: $570.00
Annual: $6,935.00
```

**Decision:** Use GPT-3.5-Turbo for categorization

**Scenario 2: Fraud Analysis**  ✅

**Requirements:**
- Analyze 500 high-risk transactions/day
- Complex reasoning required

**Prompt Structure:**
```
System: 200 tokens (fraud rules, patterns)
User: 200 tokens (transaction + history + context)
Response: 150 tokens (detailed analysis)
Total per transaction: 550 tokens
```

**Daily Cost Calculation:**
```
Total tokens: 500 × 550 = 275,000 tokens
Input tokens: 500 × 400 = 200,000 tokens
Output tokens: 500 × 150 = 75,000 tokens

With GPT-4:
Input: 200K × $0.01/1K = $2.00
Output: 75K × $0.03/1K = $2.25
Daily: $4.25
Monthly: $127.50
Annual: $1,551.25
```

**Decision:** Use GPT-4 for fraud (accuracy > cost)

**Scenario 3: Customer Support**  ✅

**Requirements:**
- Handle 2,000 support queries/day
- Moderate complexity

**Prompt Structure:**
```
System: 150 tokens (support guidelines)
Conversation history: 300 tokens (avg)
User message: 100 tokens
Response: 200 tokens
Total per interaction: 750 tokens
```

**Daily Cost Calculation:**
```
Total tokens: 2,000 × 750 = 1,500,000 tokens
Input tokens: 2,000 × 550 = 1,100,000 tokens
Output tokens: 2,000 × 200 = 400,000 tokens

With GPT-3.5-Turbo:
Input: 1,100K × $0.0005/1K = $0.55
Output: 400K × $0.0015/1K = $0.60
Daily: $1.15
Monthly: $34.50
Annual: $419.75
```

**Decision:** Use GPT-3.5-Turbo for support

### Cost Optimization Strategies  ✅

**Strategy 1: Model Selection**
- GPT-3.5 for simple, high-volume tasks
- GPT-4 only for complex reasoning
- Can reduce costs by 95%

**Strategy 2: Prompt Optimization**
- Shorter, more focused prompts
- Remove unnecessary examples
- Clear, concise instructions
- Can reduce tokens by 30-50%

**Strategy 3: Caching**
- Store results for identical inputs
- Redis or database cache
- Avoid repeated API calls
- Near-zero cost for cache hits

**Strategy 4: Batch Processing**
- Process multiple items per request
- Share system prompt overhead
- Reduces total token count
- Requires careful prompt design

**Strategy 5: Smart Routing**
- Use GPT-3.5 first
- Escalate to GPT-4 only if needed
- Based on confidence scores
- Best of both worlds

### Hands-On Requirements  ✅

**Exercise 1: Token Counting Practice**  ✅

**Requirements:**
- Use OpenAI tokenizer tool
- Test payment-related text
- Build intuition for token counts

**Texts to Test:**
1. "STARBUCKS STORE #1234 $5.50" - 14/29
2. "Unauthorized transaction detected at electronics store" 8/56
3. "PCI-DSS Requirement 3.2.1: Mask PAN when displayed"
4. "Transaction ID: TXN-2024-12-15-ABC123XYZ for amount $1,234.56"
5. "Customer dispute: Product not received within 5-7 business days"

**What to figure out:**
- Exact token count for each
- Which has highest tokens-per-word ratio
- How special characters tokenize
- How numbers and IDs tokenize
- Patterns in tokenization

**Success criteria:**
- [ ] Tested all 5 examples in tokenizer
- [ ] Recorded exact token counts
- [ ] Identified why counts vary
- [ ] Can estimate tokens without tool (±20% accuracy)

---

**Exercise 2: Cost Calculation for Business Cases**

**Requirements:**
- Calculate realistic API costs
- Compare GPT-3.5 vs GPT-4
- Determine optimal model selection

**Business Scenario 1: Daily Categorization**
- Volume: 50,000 transactions/day
- Prompt: 120 tokens avg
- Response: 25 tokens avg
- Calculate: Daily, monthly, annual costs
- Both models: GPT-3.5 and GPT-4

**Business Scenario 2: Fraud Detection**
- Volume: 1,000 high-risk/day
- Prompt: 350 tokens avg
- Response: 120 tokens avg
- Calculate: Costs for GPT-4 only

**Business Scenario 3: Mixed Approach**
- Categorization: 50,000/day with GPT-3.5
- Fraud: 1,000/day with GPT-4
- Calculate: Total blended costs

**What to figure out:**
- Exact cost formulas
- Break-even points
- ROI calculations
- Cost per transaction
- Which scenarios justify GPT-4

**Success criteria:**
- [ ] Calculated all three scenarios
- [ ] Compared cost differences
- [ ] Identified optimal model per use case
- [ ] Can justify model selection decisions
- [ ] Built reusable cost calculator

---

**Exercise 3: Context Window Planning**  ✅

**Requirements:**
- Design conversation handling
- Manage token budgets
- Handle limit gracefully

**Conversation Scenario: Fraud Investigation**

**Initial State:**
```
System prompt: 250 tokens
User: "Investigate transaction TXN-123"
```

**10-Turn Conversation:**
- Each turn: User 80 tokens, Assistant 120 tokens
- Calculate cumulative tokens after each turn
- Identify when 4K limit approaches
- Design truncation/summarization strategy

**What to figure out:**
- Cumulative token tracking
- When to summarize
- What to keep vs. discard
- How to maintain context quality
- Error handling for exceeded limits

**Success criteria:**
- [ ] Tracked tokens across 10 turns
- [ ] Identified limit crossing point
- [ ] Designed management strategy
- [ ] Can prevent context overflow
- [ ] Maintains conversation quality

### Day 2 Deliverables  ✅

- [ ] Watched tokenization explanation video
- [ ] Used OpenAI tokenizer tool hands-on
- [ ] Read BPE algorithm explanation
- [ ] Understand: How tokenization works (BPE algorithm)
- [ ] Understand: Why token counts matter for cost
- [ ] Can estimate: Approximate token counts
- [ ] Completed: Token counting exercise (5 examples)
- [ ] Completed: Cost calculation exercise (3 scenarios)
- [ ] Completed: Context window planning
- [ ] Know: GPT-3.5 vs GPT-4 cost differences
- [ ] Can explain: Token vs word vs character
- [ ] Built: Cost calculator for payment scenarios
- [ ] Spent approximately 60 minutes

---

## DAY 3 (Thursday Dec 18): OpenAI API Setup & First Calls - 60 minutes

### Primary Resources

**"OpenAI API Quickstart Tutorial"**  ✅
- Link: https://platform.openai.com/docs/quickstart
- Duration: 20 min read
- Official getting started guide

**"Chat Completions API Reference"**  ✅
- Link: https://platform.openai.com/docs/guides/text-generation/chat-completions-api
- Duration: 25 min read
- Complete API documentation

**"API Best Practices for Production"**  ✅
- Link: https://platform.openai.com/docs/guides/production-best-practices
- Duration: 15 min read
- Production deployment guidelines

### Video Resources

**"OpenAI API Tutorial for Beginners"**
- Link: https://www.youtube.com/watch?v=xP_ZON_P4Ks
- Link: https://www.youtube.com/watch?v=9ZyHckE3iIo
- Link: https://www.youtube.com/watch?v=czvVibB2lRA (prequel - https://www.youtube.com/watch?v=tFHeUSJAYbE)
- Link: https://www.youtube.com/watch?v=YVFWBJ1WVF8
- Link: https://www.youtube.com/watch?v=CbpsDMwFG2g&pp=ugUEEgJlbg%3D%3D

### Reading Materials

**"Secure API Key Management"**
- Link: https://platform.openai.com/docs/guides/safety-best-practices/api-key-management
- Duration: 10 min read
- Security best practices

**"Error Codes and Troubleshooting"**
- Link: https://platform.openai.com/docs/guides/error-codes
- Duration: 10 min read
- Common errors and solutions

### Schedule - 60 minutes total

**Part 1: Account Setup (15 min)**
1. Create OpenAI account
2. Generate API key
3. Set up environment variables
4. Install required libraries

**Part 2: API Understanding (25 min)**
5. Read: Chat Completions API guide (15 min)
6. Watch: API tutorial video (10 min)

**Part 3: First API Calls (20 min)**
7. Make successful API call
8. Experiment with basic parameters
9. Handle errors gracefully

### Key Concepts to Master

**OpenAI API Overview:**

**API Type:** RESTful API
- Standard HTTP requests (POST method)
- JSON request and response format
- Bearer token authentication
- Rate limits enforced
- Usage-based billing

**Primary Endpoint:** Chat Completions
- URL: `https://api.openai.com/v1/chat/completions`
- Method: POST
- Purpose: Generate text completions
- Supports conversation context

**Authentication:**
- API key required for all requests
- Include in Authorization header
- Format: `Authorization: Bearer YOUR_API_KEY`
- Never expose in client-side code
- Rotate keys periodically

### API Request Structure

**Required Fields:**

**1. model (string)**
- Which LLM to use
- Options: "gpt-4", "gpt-3.5-turbo", "gpt-4-turbo"
- Different costs and capabilities

**2. messages (array)**
- Conversation history
- Array of message objects
- Each has 'role' and 'content'
- Order matters (chronological)

**Message Roles:**

**system (optional but recommended)**
- Sets AI behavior and personality
- Provides context and constraints
- Not visible to end user
- Example: "You are a payment fraud detection expert"

**user (required)**
- Human input or question
- What you're asking the model
- Example: "Analyze this transaction for fraud"

**assistant (optional)**
- Previous AI responses
- Maintains conversation context
- Enables multi-turn conversations
- Example: Previous model outputs

**Basic Request Example:**
```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a transaction categorization specialist"
    },
    {
      "role": "user",
      "content": "Categorize: STARBUCKS $5.50"
    }
  ]
}
```

### Optional Parameters

**temperature (number: 0-2)**
- Controls randomness
- 0: Deterministic, consistent
- 1: Balanced (default)
- 2: Very creative, random
- Payment apps: typically 0-0.3

**max_tokens (integer)**
- Maximum response length
- Limits output tokens
- Prevents runaway generation
- Default: Model-dependent
- Payment apps: set explicit limits

**top_p (number: 0-1)**
- Nucleus sampling
- Alternative to temperature
- 0.1: Very focused
- 1.0: Full vocabulary
- Don't combine with temperature

**n (integer)**
- Number of completions to generate
- Default: 1
- Cost multiplies by n
- Use for: Comparing alternatives

**stop (string or array)**
- Stop sequences
- Generation stops when encountered
- Example: ["\n", "###"]
- Useful for structured output

**presence_penalty (number: -2 to 2)**
- Encourages topic diversity
- Positive: Penalize used tokens
- Negative: Encourage repetition
- Default: 0

**frequency_penalty (number: -2 to 2)**
- Reduces repetition
- Positive: Penalize frequent tokens
- Negative: Encourage patterns
- Default: 0

### API Response Structure

**Success Response:**
```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1702890245,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Category: Food & Dining\nConfidence: 95%"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 45,
    "completion_tokens": 12,
    "total_tokens": 57
  }
}
```

**Key Fields to Extract:**

**choices[0].message.content**
- The generated text
- What you actually need
- Main output from API

**usage.total_tokens**
- Tokens consumed
- For cost tracking
- Sum of prompt + completion

**finish_reason**
- "stop": Normal completion
- "length": Hit max_tokens limit
- "content_filter": Filtered for safety
- "function_call": Called a function (advanced)

### Error Handling

**Common HTTP Status Codes:**

**401 Unauthorized**
- Invalid API key
- Expired key
- Missing Authorization header
- Fix: Verify API key, regenerate if needed

**429 Too Many Requests**
- Rate limit exceeded
- Quota exhausted
- Fix: Implement exponential backoff, upgrade plan

**400 Bad Request**
- Invalid request format
- Missing required fields
- Invalid parameter values
- Fix: Validate request structure

**500 Internal Server Error**
- OpenAI service issue
- Temporary outage
- Fix: Retry with exponential backoff

**503 Service Unavailable**
- Server overloaded
- Maintenance
- Fix: Retry later

**Context Length Error**
- Tokens exceed model limit
- Fix: Truncate messages, use shorter prompts

### Setup Requirements

**Step 1: Create OpenAI Account**
- Navigate to: https://platform.openai.com/signup
- Sign up with email
- Verify email address
- Set up billing (credit card required)

**Step 2: Generate API Key**
- Go to: https://platform.openai.com/api-keys
- Click "Create new secret key"
- Name it descriptively ("payment-chatbot")
- Copy key immediately (shown only once)
- Store securely

**Step 3: Environment Setup**
- Create `.env` file in project root
- Add: `OPENAI_API_KEY=your-key-here`
- Add `.env` to `.gitignore`
- Never commit API keys to git

**Step 4: Install Python Library**
- Install: `pip install openai`
- Install: `pip install python-dotenv`
- Verify installation

**What to figure out:**
- How to create virtual environment
- How to manage Python dependencies
- How to load environment variables
- How to structure project directories
- How to secure sensitive data

### Hands-On Requirements

**Exercise 1: First Successful API Call**

**Requirements:**
- Set up OpenAI credentials
- Make basic API request
- Extract and print response
- Log token usage

**Task:**
Make API call to categorize transaction:
- Transaction: "NETFLIX.COM $15.99"
- System message: "You are a transaction categorizer"
- Model: gpt-3.5-turbo
- Temperature: 0
- Expected: Category and confidence

**What to figure out:**
- How to structure HTTP POST request
- How to set headers (Authorization, Content-Type)
- How to send JSON body
- How to parse JSON response
- How to extract specific fields
- How to handle HTTP errors
- How to log requests/responses

**Success criteria:**
- [ ] API call completes successfully
- [ ] Response received and parsed
- [ ] Content extracted correctly
- [ ] Token usage logged
- [ ] No authentication errors
- [ ] Response makes sense

---

**Exercise 2: Parameter Experimentation**

**Requirements:**
- Test different API parameters
- Observe effects on outputs
- Document behavior patterns

**Experiment 1: Temperature Variation**
- Same prompt: "Describe this transaction: UBER $45"
- Test temperatures: 0, 0.5, 1.0, 1.5
- Run 3 times each temperature
- Document: Consistency vs. creativity

**Experiment 2: Max Tokens Limit**
- Prompt: "Explain PCI-DSS compliance"
- Test max_tokens: 20, 50, 100, 200
- Document: When responses truncate

**Experiment 3: System Prompt Impact**
- Same user message
- Test different system prompts:
  - No system prompt
  - "You are helpful"
  - "You are a fraud expert"
  - "You are a compliance officer"
- Document: How behavior changes

**What to figure out:**
- Which parameters affect consistency most
- How temperature affects payment tasks
- When max_tokens should be set
- How system prompts shape responses
- Optimal settings for categorization

**Success criteria:**
- [ ] Completed all 3 experiments
- [ ] Documented observations
- [ ] Understand parameter effects
- [ ] Can choose appropriate settings
- [ ] Built testing framework

---

**Exercise 3: Error Handling Implementation**

**Requirements:**
- Test different error scenarios
- Implement robust error handling
- Log errors appropriately

**Error Scenario 1: Invalid API Key**
- Use intentionally wrong key
- Catch 401 error
- Log error details
- Display user-friendly message

**Error Scenario 2: Context Too Long**
- Send request exceeding 4K tokens
- Catch length error
- Implement truncation
- Retry with shorter input

**Error Scenario 3: Rate Limit**
- Make rapid consecutive requests
- Catch 429 error
- Implement exponential backoff
- Retry with delays

**Error Scenario 4: Network Timeout**
- Set short timeout (1 second)
- Catch timeout error
- Implement retry logic
- Max 3 retries

**What to figure out:**
- How to catch specific HTTP errors
- When to retry vs. fail permanently
- Exponential backoff algorithm
- How many retries appropriate
- What to log for debugging
- User-friendly error messages

**Success criteria:**
- [ ] Handled all 4 error types
- [ ] Implemented retry logic
- [ ] Exponential backoff working
- [ ] Errors logged properly
- [ ] User-friendly messages
- [ ] Production-ready error handling

### Day 3 Deliverables

- [ ] Created OpenAI account
- [ ] Generated and secured API key
- [ ] Set up environment variables
- [ ] Installed OpenAI Python library
- [ ] Made first successful API call
- [ ] Understand: Request structure (model, messages, params)
- [ ] Understand: Response structure (choices, usage, finish_reason)
- [ ] Understand: Message roles (system, user, assistant)
- [ ] Completed: First API call exercise
- [ ] Completed: Parameter experimentation (3 experiments)
- [ ] Completed: Error handling exercise (4 scenarios)
- [ ] Can explain: Authentication process
- [ ] Can explain: How to extract response content
- [ ] Can explain: Token usage tracking
- [ ] Built: Reusable API wrapper with error handling
- [ ] Spent approximately 60 minutes

---

## DAY 4 (Friday Dec 19): Advanced Parameters & Conversation Management - 60 minutes

### Primary Resources

**"Text Generation Parameters Guide"**
- Link: https://platform.openai.com/docs/guides/text-generation
- Duration: 20 min read
- Detailed parameter explanations

**"Managing Conversations and Context"**
- Link: https://platform.openai.com/docs/guides/text-generation/managing-tokens
- Duration: 15 min read
- Context management strategies

### Video Resources

**"Understanding LLM Parameters"**
- Link: https://www.youtube.com/watch?v=0a8pz7FJwZU
- Duration: 12:00
- Visual parameter effects

### Reading Materials

**"Conversation Design Patterns"**
- Link: https://platform.openai.com/docs/guides/chat
- Duration: 15 min read
- Building conversational apps

**"Prompt Engineering for Chat"**
- Link: https://www.promptingguide.ai/introduction/settings
- Duration: 15 min read
- Chat-specific prompting

### Schedule - 60 minutes total

**Part 1: Advanced Parameters (25 min)**
1. Read: Text generation parameters (15 min)
2. Watch: LLM parameters video (10 min)

**Part 2: Conversation Management (20 min)**
3. Read: Managing tokens guide (10 min)
4. Read: Conversation design patterns (10 min)

**Part 3: Hands-On Practice (15 min)**
5. Build multi-turn conversation handler

### Key Concepts to Master

**Stateless API Nature:**

**Critical Understanding:**
- Each API call is independent
- Model doesn't remember previous requests
- No automatic conversation memory
- You must send full history each time

**Multi-Turn Conversation:**

**Turn 1:**
```
messages: [
  {role: "system", content: "You are a fraud analyst"},
  {role: "user", content: "Check transaction TXN-123"}
]
Response: "Transaction TXN-123: $500, Electronics, Nigeria"
```

**Turn 2 (WRONG - No Context):**
```
messages: [
  {role: "system", content: "You are a fraud analyst"},
  {role: "user", content: "Is it fraudulent?"}
]
Response: "I don't have information about which transaction"
```

**Turn 2 (CORRECT - With Context):**
```
messages: [
  {role: "system", content: "You are a fraud analyst"},
  {role: "user", content: "Check transaction TXN-123"},
  {role: "assistant", content: "Transaction TXN-123: $500, Electronics, Nigeria"},
  {role: "user", content: "Is it fraudulent?"}
]
Response: "High risk - amount unusual, high-risk country, electronics category"
```

### Conversation History Strategies

**Strategy 1: Full History (Simple)**

**Implementation:**
- Store all messages in array
- Append new messages
- Send entire array each call
- No truncation

**Pros:**
- Simple to implement
- Complete context available
- No information loss

**Cons:**
- Token count grows linearly
- Eventually exceeds limit
- Increasingly expensive
- Slower with large histories

**When to use:**
- Short conversations (<10 turns)
- Within budget constraints
- Context limit not reached

**Strategy 2: Sliding Window**

**Implementation:**
- Keep only last N messages
- Discard oldest messages
- System prompt always included
- Fixed memory footprint

**Example (N=6):**
```
messages: [
  {system},
  {last 6 user+assistant messages}
]
```

**Pros:**
- Bounded token usage
- Won't exceed limits
- Simple logic
- Predictable cost

**Cons:**
- Loses old context
- Can't reference early conversation
- May lose important details

**When to use:**
- Long conversations
- Recent context sufficient
- Memory not critical

**Strategy 3: Summarization**

**Implementation:**
- Periodically summarize old messages
- Replace old messages with summary
- Keep recent messages full
- Trigger: Token threshold

**Example:**
```
messages: [
  {system},
  {summary: "Customer disputed $500 charge from Dec 10"},
  {last 4 messages in full}
]
```

**Pros:**
- Retains key information
- Bounded tokens
- Better than sliding window
- Context quality maintained

**Cons:**
- More complex
- Extra API calls for summaries
- Slight information loss
- Requires logic to trigger

**When to use:**
- Long conversations
- Context quality important
- Can afford summary costs

**Strategy 4: Selective Memory (Advanced)**

**Implementation:**
- Identify important messages
- Keep important, discard routine
- Tag messages by importance
- Retrieve relevant on demand

**Importance Criteria:**
- Contains transaction data
- User explicitly said "remember"
- Decision points
- Error or issues
- Preferences stated

**When to use:**
- Complex applications
- Multiple topics in conversation
- Cost optimization critical

### Token Budget Management

**Fixed Budget Approach:**

**Total Limit:** 4,096 tokens (GPT-3.5)

**Allocation:**
```
System prompt:     300 tokens (fixed)
History:         2,300 tokens (variable)
Current message:   200 tokens (estimated)
Response buffer: 1,296 tokens (for output)
-----------------
Total:           4,096 tokens
```

**Enforcement Logic:**
```
before_request():
  current_total = count_tokens(system + history + message)
  if current_total > (LIMIT - RESPONSE_BUFFER):
    trigger_truncation()
    # or trigger_summarization()
    # or return_error()
```

**What to figure out:**
- How to count tokens accurately (tiktoken library)
- When to trigger truncation
- How much buffer for responses
- How to handle exceeding limit
- Where to store conversation history

### Payment Support Conversation Patterns

**Pattern 1: Transaction Investigation**

**Flow:**
```
User: "Why was my card declined?"
Bot: "I'll help investigate. Can you provide:
     - Date and time
     - Merchant name
     - Approximate amount?"

User: "Yesterday, 3pm, Target, about $130"
Bot: [Search] "Found: $127.43 at Target, 12/17/2025 3:14pm
     Decline reason: Insufficient funds
     Current balance: $95.18"

User: "How can I fix this?"
Bot: "Options:
     1. Transfer from savings
     2. Use different card
     3. Call to increase limit"
```

**Context Management:**
- Remember transaction being discussed
- Track investigation stage
- Maintain user's original question

**Pattern 2: Dispute Resolution**

**Flow:**
```
User: "I didn't make this $500 purchase"
Bot: "I'll help dispute this.
     Transaction: $500, ElectronicsStore, 12/15/2025
     Do you recognize this merchant?"

User: "No, never shopped there"
Bot: "Understood. Additional questions:
     - Do you have your card with you?
     - Last time you used the card?
     - Shared card details recently?"

[Collect information over multiple turns]

Bot: "Based on your answers, filing fraud claim.
     Claim ID: CLM-2025-001
     Card will be blocked
     New card ships in 5-7 days"
```

**Context Management:**
- Store dispute details
- Track investigation progress
- Remember user responses
- Build case documentation

**Pattern 3: Regulatory Q&A**

**Flow:**
```
User: "What are PCI-DSS requirements?"
Bot: "PCI-DSS has 12 main requirements:
     1. Install firewalls
     2. Change vendor defaults
     [list continues]
     Which area interests you?"

User: "Number 3"
Bot: "Requirement 3: Protect stored cardholder data
     Key points:
     - Mask PAN when displayed
     - Encrypt data at rest
     - Secure key management
     Want details on any specific point?"

User: "How to mask PAN?"
Bot: "PAN masking best practices:
     - Show only last 4 digits
     - Format: XXXX-XXXX-XXXX-1234
     [detailed guidance]"
```

**Context Management:**
- Remember regulation being discussed
- Track drill-down path
- Maintain topic focus

### Hands-On Requirements

**Exercise 1: Build Conversation Manager**

**Requirements:**
- Implement conversation history tracking
- Handle multi-turn interactions
- Manage token budget
- Test with payment scenarios

**Features to Implement:**

**1. Message Storage**
- Store messages in list/array
- Include role, content, timestamp
- Track token count per message
- Persist across turns

**2. History Management**
- Add new messages
- Remove old messages (sliding window)
- Summarize when threshold reached
- Reset conversation

**3. Token Tracking**
- Count tokens before each request
- Track cumulative usage
- Alert when approaching limit
- Enforce maximum budget

**4. API Integration**
- Send full history with each call
- Append assistant responses
- Handle errors gracefully
- Log all interactions

**What to figure out:**
- Data structure for messages
- How to count tokens accurately
- When to truncate history
- How to persist state
- Testing multi-turn conversations

**Success criteria:**
- [ ] Stores conversation history
- [ ] Sends context with each request
- [ ] Tracks token usage
- [ ] Handles 10+ turn conversations
- [ ] Enforces token budget
- [ ] Tested with payment scenarios

---

**Exercise 2: Implement Sliding Window**

**Requirements:**
- Keep only last N messages
- Maintain system prompt
- Test boundary conditions

**Implementation Steps:**

**1. Configure Window Size**
- Set max messages (e.g., 8)
- Always keep system prompt
- Count user+assistant pairs

**2. Add Message Logic**
- Append new message
- Check if exceeds limit
- Remove oldest if needed
- Keep system prompt

**3. Boundary Testing**
- Test with window size 2, 4, 8
- Verify oldest removed first
- System prompt never removed
- Context maintains coherence

**Payment Scenario:**
- Fraud investigation (8+ turns)
- Track which context is lost
- Verify system still functional
- Test context quality degradation

**What to figure out:**
- How to implement circular buffer
- Which messages to count (user+assistant pairs?)
- How to handle odd numbers
- Testing context loss impact

**Success criteria:**
- [ ] Sliding window working
- [ ] System prompt preserved
- [ ] Oldest messages removed
- [ ] Tested with multiple window sizes
- [ ] Context quality acceptable
- [ ] Payment scenario functional

---

**Exercise 3: Payment Investigation Chatbot**

**Requirements:**
- Build multi-turn payment support bot
- Handle common investigation flows
- Manage context appropriately

**Scenarios to Support:**

**Scenario 1: Declined Transaction**
- User reports decline
- Bot asks for details
- Bot looks up transaction (simulated)
- Bot explains reason
- Bot suggests solutions

**Scenario 2: Unrecognized Charge**
- User questions charge
- Bot retrieves transaction
- Bot asks verification questions
- Bot determines fraud likelihood
- Bot initiates appropriate action

**Scenario 3: Balance Inquiry**
- User asks balance
- Bot provides balance (simulated)
- Bot offers related services
- Bot handles follow-up questions

**What to figure out:**
- Conversation flow design
- Context requirements per scenario
- How to simulate backend systems
- Error handling in conversations
- When to escalate to human

**Success criteria:**
- [ ] Handles all 3 scenarios
- [ ] Maintains context across turns
- [ ] Natural conversation flow
- [ ] Appropriate responses
- [ ] Tested end-to-end
- [ ] Error handling functional

### Day 4 Deliverables

- [ ] Read text generation parameters guide
- [ ] Watched LLM parameters video
- [ ] Read conversation management guide
- [ ] Understand: Stateless API nature
- [ ] Understand: History management strategies
- [ ] Understand: Token budget management
- [ ] Completed: Conversation manager implementation
- [ ] Completed: Sliding window implementation
- [ ] Completed: Payment investigation chatbot
- [ ] Can explain: Why context must be sent each time
- [ ] Can explain: Sliding window vs summarization
- [ ] Can explain: Token budgeting
- [ ] Built: Reusable conversation manager
- [ ] Tested: Multi-turn payment scenarios
- [ ] Spent approximately 60 minutes

---

## DAY 5 (Saturday Dec 20): Prompt Engineering Basics - 60 minutes

### Primary Resources

**"Prompt Engineering Guide" by OpenAI**
- Link: https://platform.openai.com/docs/guides/prompt-engineering
- Duration: 25 min read
- Official best practices

**"Introduction to Prompt Engineering"**
- Link: https://www.promptingguide.ai/
- Duration: 20 min read (Introduction + Techniques)
- Comprehensive guide

### Video Resources

**"Prompt Engineering Crash Course"**
- Link: https://www.youtube.com/watch?v=_ZvnD73m40o
- Duration: Watch first 20 minutes
- Practical techniques

### Reading Materials

**"Prompting Techniques" by Anthropic**
- Link: https://www.anthropic.com/index/prompting-guide
- Duration: 15 min read
- Advanced patterns

**"Few-Shot Learning"**
- Link: https://www.promptingguide.ai/techniques/fewshot
- Duration: 10 min read
- Example-based prompting

### Schedule - 60 minutes total

**Part 1: Fundamentals (25 min)**
1. Read: OpenAI prompting guide (15 min)
2. Watch: Crash course (first 10 min)

**Part 2: Techniques (20 min)**
3. Read: Prompting guide intro (15 min)
4. Read: Few-shot learning (5 min)

**Part 3: Practice (15 min)**
5. Write prompts for payment scenarios

### Key Concepts to Master

**What is Prompt Engineering?**
- Crafting inputs to get desired outputs
- Instructions + Context + Examples
- Systematic approach to guide LLM
- Iterative refinement process
- Critical for production quality

**Why Prompt Engineering Matters:**
- Determines output quality
- Affects consistency
- Controls behavior
- Reduces costs (fewer retries)
- Enables complex tasks

**Core Prompting Principles:**

**Principle 1: Be Specific and Clear**

**Bad:**
"Analyze this transaction"

**Good:**
"Analyze this transaction for fraud. Provide:
1. Risk score (0-100)
2. Three specific risk factors identified
3. Recommendation (approve/review/decline)
4. Confidence level (0-100)"

**Principle 2: Provide Context**

**Bad:**
"Is this fraudulent? $2000 electronics"

**Good:**
"You are analyzing a credit card transaction for fraud.
Customer profile:
- Average transaction: $50
- Location: USA
- Card age: 5 years
Transaction to analyze:
- Amount: $2000
- Category: Electronics  
- Location: Nigeria
- Time: 3 AM local
Is this fraudulent?"

**Principle 3: Use Examples (Few-Shot)**

**Zero-Shot (No Examples):**
"Categorize: STARBUCKS $5.50"

**Few-Shot (With Examples):**
"Categorize these transactions:

Example 1:
Input: SHELL GAS STATION $45
Output: Transportation > Gas & Fuel

Example 2:
Input: WHOLE FOODS MARKET $127
Output: Food & Dining > Grocery

Example 3:
Input: NETFLIX.COM $15.99
Output: Entertainment > Streaming

Now categorize:
Input: STARBUCKS $5.50
Output:"

**Principle 4: Specify Output Format**

**Bad:**
"Tell me about this transaction"

**Good:**
"Analyze this transaction and respond in JSON:
{
  \"category\": \"string\",
  \"confidence\": 0-100,
  \"risk_level\": \"low|medium|high\",
  \"reasoning\": \"brief explanation\"
}"

### Prompting Techniques

**Technique 1: Instruction Prompting**

**Structure:**
```
[Task Description]
[Constraints/Requirements]
[Input Data]
[Output Format]
```

**Example - Fraud Detection:**
```
Task: Analyze the following transaction for fraud indicators.

Requirements:
- Identify at least 3 specific risk factors
- Assign risk score (0-100)
- Provide clear reasoning
- Recommend action (approve/review/decline)

Transaction:
Amount: $3,500
Merchant: Electronics Store
Location: Different country from customer
Time: 2 AM
Customer avg: $75

Output Format:
Risk Score: [0-100]
Factors: [list]
Recommendation: [action]
Reasoning: [explanation]
```

**Technique 2: Role Prompting**

**Pattern:**
"You are a [specific role] with [expertise/experience]..."

**Examples:**

**Fraud Analyst:**
"You are a senior fraud analyst with 15 years of experience in credit card fraud detection. You specialize in behavioral analysis and pattern recognition."

**Compliance Officer:**
"You are a PCI-DSS compliance officer responsible for ensuring payment security standards are met."

**Customer Support:**
"You are an empathetic customer support specialist for a payment company. You explain complex payment issues in simple terms."

**Technique 3: Chain-of-Thought (CoT)**

**Pattern:**
"Let's think step by step:"

**Example:**
```
Determine if this transaction is fraudulent.
Think step-by-step:

1. First, compare amount to customer's typical spending
2. Second, check the merchant location vs customer location
3. Third, examine the transaction time
4. Fourth, consider the merchant category
5. Finally, calculate overall risk score

Transaction: [details]
```

**Technique 4: Few-Shot Learning**

**Pattern:**
Provide 2-5 examples of input-output pairs

**Best Practices:**
- 2-5 examples optimal
- Cover diverse cases
- Include edge cases
- Match desired output format exactly

**Example - Categorization:**
```
Categorize transactions:

UBER RIDE $25 → Transportation > Rideshare
PHARMACY CVS $43.21 → Healthcare > Pharmacy
STEAM GAMES $59.99 → Entertainment > Gaming
TARGET STORE $156 → Shopping > General Retail

Now categorize:
SPOTIFY PREMIUM $9.99 → ?
```

**Technique 5: Constraints and Guardrails**

**Pattern:**
Explicitly state what NOT to do

**Example:**
```
Analyze this transaction.

DO:
- Provide specific evidence
- Cite risk factors
- Quantify risk (0-100)
- Recommend clear action

DO NOT:
- Make assumptions without evidence
- Use vague language ("might", "could")
- Recommend approval for high-risk
- Include sensitive customer data in output
```

### Payment Domain Prompt Templates

**Template 1: Transaction Categorization**
```
You are a transaction categorization expert.

Task: Categorize the transaction below into a category and subcategory.

Categories:
- Food & Dining (Restaurants, Groceries, Coffee Shops, Fast Food)
- Transportation (Gas, Public Transit, Rideshare, Parking)
- Shopping (Clothing, Electronics, General Retail, Online)
- Entertainment (Streaming, Gaming, Movies, Events)
- Bills & Utilities (Electric, Water, Internet, Phone)
- Healthcare (Medical, Dental, Pharmacy, Insurance)
- Travel (Hotels, Flights, Car Rental)
- Other

Transaction: {transaction_description}

Output Format:
Category: [primary category]
Subcategory: [specific type]
Confidence: [0-100]
Reasoning: [brief explanation]
```

**Template 2: Fraud Analysis**
```
You are a fraud detection analyst. Analyze the transaction below for fraud risk.

Risk Factors to Check:
1. Amount relative to customer history
2. Geographic location (customer vs merchant)
3. Transaction time (unusual hours)
4. Merchant category (first time or high-risk)
5. Velocity (multiple transactions quickly)

Customer Profile:
- Average transaction: {avg_amount}
- Typical location: {location}
- Typical categories: {categories}

Transaction to Analyze:
- Amount: {amount}
- Merchant: {merchant}
- Location: {location}
- Time: {time}
- Category: {category}

Output Format:
Risk Score: [0-100]
Risk Level: [low/medium/high/critical]
Factors: [list of specific indicators]
Recommendation: [approve/review/decline]
Confidence: [0-100]
Reasoning: [detailed explanation]
```

**Template 3: Customer Support**
```
You are a helpful and empathetic customer support specialist for a payment company.

Guidelines:
- Explain complex issues in simple terms
- Be understanding of customer frustration
- Provide clear next steps
- Offer alternatives when possible
- Escalate to human if you cannot resolve

Customer Issue: {customer_message}

Context (if available):
- Transaction history: {transactions}
- Account status: {status}
- Previous interactions: {history}

Respond with:
1. Empathetic acknowledgment of issue
2. Clear explanation of what happened
3. Specific steps to resolve
4. Timeline for resolution
5. Escalation option if needed
```

### Hands-On Requirements

**Exercise 1: Build Categorization Prompt**

**Requirements:**
- Create effective categorization prompt
- Test with 10 diverse transactions
- Achieve >90% accuracy

**Prompt Components to Include:**
- Clear role definition
- Category taxonomy (10+ categories)
- Output format specification
- Few-shot examples (3-5)
- Confidence scoring instruction

**Test Transactions:**
1. "STARBUCKS #1234 $5.50"
2. "AMAZON.COM $127.99"
3. "SHELL GAS STATION $45.00"
4. "NETFLIX MONTHLY $15.99"
5. "CVS PHARMACY $32.10"
6. "UBER TRIP TO AIRPORT $67"
7. "WHOLE FOODS $156.43"
8. "SPOTIFY PREMIUM $9.99"
9. "DENTIST OFFICE COPAY $40"
10. "ELECTRIC BILL AUTOPAY $128.50"

**What to figure out:**
- How many examples needed
- Which categories to include
- How specific to be
- What output format works best
- How to improve accuracy

**Success criteria:**
- [ ] Created complete prompt
- [ ] Tested with all 10 transactions
- [ ] Achieved >90% accuracy
- [ ] Consistent output format
- [ ] Confidence scores reasonable

---

**Exercise 2: Fraud Detection Prompt**

**Requirements:**
- Create comprehensive fraud analysis prompt
- Include specific risk factors
- Test with various scenarios

**Scenarios to Test:**

**Scenario 1: Clear Fraud**
- $5,000 electronics, 3 AM, Nigeria, customer in USA, avg $50

**Scenario 2: Legitimate Unusual**
- $2,500 hotel, Paris, customer traveling, hotel booking

**Scenario 3: Borderline**
- $800 jewelry, midnight, new merchant category, customer avg $300

**Scenario 4: Clear Legitimate**
- $35 restaurant, customer's city, typical time, regular category

**What to figure out:**
- What risk factors to check
- How to weight different factors
- When to flag for review vs decline
- How to explain reasoning clearly
- Balancing false positives/negatives

**Success criteria:**
- [ ] Identifies clear fraud (Scenario 1)
- [ ] Approves legitimate (Scenario 4)
- [ ] Handles edge cases reasonably (Scenarios 2-3)
- [ ] Provides specific reasoning
- [ ] Consistent risk scoring
- [ ] Actionable recommendations

---

**Exercise 3: Prompt Iteration**

**Requirements:**
- Start with basic prompt
- Iteratively improve
- Document improvements

**Task:** Create merchant normalization prompt
- Input: Raw merchant description
- Output: Clean merchant name

**Iteration 1: Basic**
```
Clean this merchant name: {raw_merchant}
```

**Iteration 2: Add Context**
```
You are a payment processor. Clean and standardize this merchant name.
Remove processor codes, location codes, and extra information.

Merchant: {raw_merchant}
```

**Iteration 3: Add Examples**
```
[Add few-shot examples]

SQ *COFFEE SHOP → Coffee Shop
AMZN MKTP US*AB12 → Amazon
TST* RESTAURANT NYC → Restaurant
```

**Iteration 4: Add Output Format**
```
[Add structured output requirement]

Output:
Cleaned Name: [result]
Removed: [what was removed]
Confidence: [0-100]
```

**What to figure out:**
- What each iteration improves
- When to stop iterating
- How to measure improvement
- What elements are essential
- Cost vs quality trade-off

**Success criteria:**
- [ ] Completed 4+ iterations
- [ ] Each iteration better than previous
- [ ] Documented improvements
- [ ] Final version production-ready
- [ ] Understand iteration process

### Day 5 Deliverables

- [ ] Read OpenAI prompt engineering guide
- [ ] Watched prompt engineering crash course
- [ ] Read comprehensive prompting guide
- [ ] Understand: Core prompting principles
- [ ] Understand: Key techniques (few-shot, CoT, role)
- [ ] Understand: Importance of specificity
- [ ] Completed: Categorization prompt (tested with 10)
- [ ] Completed: Fraud detection prompt (4 scenarios)
- [ ] Completed: Prompt iteration exercise
- [ ] Can explain: When to use few-shot vs zero-shot
- [ ] Can explain: How to structure effective prompts
- [ ] Built: 3 production-ready prompt templates
- [ ] Know: How to iterate and improve prompts
- [ ] Spent approximately 60 minutes

---

## DAY 6 (Sunday Dec 21): Build Payment Q&A System - 180-240 minutes

### Goal
Build production-ready payment transaction Q&A system using OpenAI API with optimized prompts.

### Schedule - 180-240 minutes total

**HOUR 1: System Design & Architecture (60 min)**
**HOUR 2: Core Implementation (60 min)**
**HOUR 3: Testing & Optimization (60 min)**
**HOUR 4 (Optional): Polish & Documentation (60 min)**

---

### HOUR 1: System Design & Architecture

**Part 1: Requirements Definition - 20 min**

**System Capabilities:**

**1. Transaction Categorization**
- Input: Raw transaction description
- Output: Category, subcategory, confidence
- Volume: 1,000+ transactions/day
- Latency: <1 second per transaction
- Accuracy: >95% for common merchants

**2. Fraud Analysis**
- Input: Transaction + customer context
- Output: Risk score, factors, recommendation
- Volume: 500 suspicious transactions/day
- Latency: <2 seconds per analysis
- Accuracy: >90% fraud detection

**3. Customer Support Q&A**
- Input: Customer question about payment
- Output: Clear answer with context
- Volume: 500 questions/day
- Latency: <3 seconds per response
- Quality: Natural, empathetic responses

**Non-Functional Requirements:**
- Cost: <$5/day for 2,000 operations
- Error handling: Graceful degradation
- Logging: All requests logged
- Monitoring: Track success rate, latency
- Security: API keys secure

**What to figure out:**
- Which models for which tasks
- Cost optimization strategies
- Error recovery approach
- How to measure quality
- Where to store conversations

**Success criteria:**
- [ ] Requirements documented
- [ ] Success metrics defined
- [ ] Cost budget established
- [ ] Quality targets set

---

**Part 2: Architecture Design - 25 min**

**System Components:**

**1. API Wrapper Module**
- Handles OpenAI API calls
- Implements retry logic
- Tracks token usage
- Manages rate limits
- Logs all interactions

**2. Prompt Manager**
- Stores prompt templates
- Manages few-shot examples
- Version control for prompts
- A/B testing support

**3. Conversation Manager**
- Tracks message history
- Implements sliding window
- Manages token budget
- Persists conversations

**4. Transaction Processor**
- Categorization pipeline
- Fraud analysis pipeline
- Batch processing support
- Result caching

**5. Response Formatter**
- Parse API responses
- Extract structured data
- Format for presentation
- Error message generation

**What to figure out:**
- Module dependencies
- Data flow between components
- Where to cache results
- How to handle failures
- Testing strategy

**Success criteria:**
- [ ] Architecture diagram created
- [ ] Component responsibilities defined
- [ ] Data flow documented
- [ ] Error handling strategy
- [ ] Testing approach planned

---

**Part 3: Prompt Library Creation - 15 min**

**Prompts to Create:**

**1. Transaction Categorization Prompt**
- System message with role
- Category taxonomy
- 5 few-shot examples
- Output format specification
- Confidence requirement

**2. Fraud Analysis Prompt**
- Fraud analyst role
- Risk factors checklist
- Customer context template
- Scoring methodology
- Output format (JSON)

**3. Merchant Normalization Prompt**
- Processor code removal
- Location code stripping
- Standardization rules
- Few-shot examples

**4. Customer Support Prompt**
- Support specialist role
- Empathy guidelines
- Response structure
- Escalation criteria

**What to figure out:**
- Optimal prompt structure
- How many examples needed
- Best output formats
- Version management
- Testing approach

**Success criteria:**
- [ ] 4 prompt templates created
- [ ] Each tested with examples
- [ ] Output formats validated
- [ ] Few-shot examples included
- [ ] Ready for implementation

---

### HOUR 2: Core Implementation

**Part 1: API Wrapper Implementation - 25 min**

**Requirements:**

**Class: OpenAIWrapper**

**Methods:**

**1. __init__(api_key, model, default_temp)**
- Initialize with configuration
- Set up logging
- Validate API key
- Set default parameters

**2. complete(messages, temperature, max_tokens, etc.)**
- Make API request
- Handle errors with retry
- Track token usage
- Log request/response
- Return parsed result

**3. count_tokens(text)**
- Use tiktoken library
- Return accurate token count
- Cache results

**4. batch_complete(message_list)**
- Process multiple requests
- Respect rate limits
- Aggregate results
- Return all responses

**Features:**
- Exponential backoff retry (3 attempts)
- Token usage tracking
- Cost calculation
- Request/response logging
- Error handling for all error types

**What to figure out:**
- Retry logic implementation
- Token counting with tiktoken
- How to log effectively
- Rate limiting approach
- Error message formatting

**Success criteria:**
- [ ] OpenAIWrapper class functional
- [ ] All methods working
- [ ] Retry logic tested
- [ ] Token counting accurate
- [ ] Logging comprehensive

---

**Part 2: Transaction Categorization - 20 min**

**Requirements:**

**Function: categorize_transaction(description)**

**Steps:**
1. Load categorization prompt template
2. Insert transaction description
3. Call OpenAI API (GPT-3.5, temp=0)
4. Parse response
5. Extract category, confidence
6. Return structured result

**Input:**
```
"STARBUCKS STORE #1234 NEW YORK $5.50"
```

**Output:**
```
{
  "category": "Food & Dining",
  "subcategory": "Coffee Shop",
  "confidence": 95,
  "reasoning": "Starbucks is a coffee shop chain"
}
```

**Edge Cases:**
- Unknown merchant
- Ambiguous category
- Very low confidence (<50%)
- API error

**What to figure out:**
- Response parsing logic
- Error handling approach
- Default category for failures
- When to retry vs return error
- How to validate output

**Success criteria:**
- [ ] Function implemented
- [ ] Tested with 10 merchants
- [ ] >90% accuracy achieved
- [ ] Edge cases handled
- [ ] Error handling working

---

**Part 3: Fraud Analysis - 15 min**

**Requirements:**

**Function: analyze_fraud(transaction, customer_context)**

**Inputs:**
```
transaction: {
  "amount": 2500,
  "merchant": "Electronics Store",
  "location": "Nigeria",
  "time": "3:00 AM",
  "category": "Electronics"
}

customer_context: {
  "avg_transaction": 50,
  "location": "USA",
  "typical_categories": ["Food", "Gas", "Groceries"]
}
```

**Output:**
```
{
  "risk_score": 95,
  "risk_level": "critical",
  "factors": [
    "Amount 50x typical",
    "International location (high-risk country)",
    "Unusual time (3 AM)",
    "First electronics purchase"
  ],
  "recommendation": "decline",
  "confidence": 90
}
```

**What to figure out:**
- How to structure context in prompt
- Risk score calculation validation
- Factor extraction from response
- When to use GPT-4 vs GPT-3.5
- Output consistency checking

**Success criteria:**
- [ ] Function implemented
- [ ] Tested with 5 scenarios
- [ ] Identifies clear fraud
- [ ] Handles borderline cases
- [ ] Returns structured output

---

### HOUR 3: Testing & Optimization

**Part 1: Comprehensive Testing - 30 min**

**Test Suite:**

**1. Unit Tests (10 transactions)**
- STARBUCKS $5.50
- AMAZON.COM $127.99
- SHELL GAS $45.00
- NETFLIX $15.99
- Unknown merchant "ABCD123"
- Very long description (200 chars)
- Numbers only "123456 $50"
- Special characters "@@@ $$$"
- International merchant "東京レストラン"
- Misspelled "WALLMART"

**Expected:**
- 8/10 correct categories
- Confidence scores reasonable
- Unknown merchants handled
- No crashes on edge cases

**2. Fraud Scenarios (6 tests)**
- Clear fraud (score >80)
- Clear legitimate (score <20)
- Borderline case (score 40-60)
- Customer traveling (context matters)
- High-value legitimate purchase
- Low-value fraudulent pattern

**Expected:**
- Correct risk levels
- Specific factors listed
- Appropriate recommendations
- Confidence scores reasonable

**3. Error Handling (5 tests)**
- Invalid API key
- Network timeout
- Rate limit hit
- Context too long
- Invalid input format

**Expected:**
- Graceful error messages
- Retry attempts logged
- Fallback responses
- No crashes

**What to figure out:**
- How to automate tests
- Success criteria per test
- How to measure accuracy
- Regression testing approach
- CI/CD integration later

**Success criteria:**
- [ ] All unit tests passing
- [ ] Fraud scenarios correct
- [ ] Error handling robust
- [ ] Test coverage >80%
- [ ] Documented test results

---

**Part 2: Cost Optimization - 15 min**

**Analysis:**

**Current Costs (Baseline):**
- Categorization: 10,000/day × 150 tokens = 1.5M tokens/day
- Fraud: 500/day × 550 tokens = 275K tokens/day
- Support: 500/day × 750 tokens = 375K tokens/day
- Total: ~2.15M tokens/day

**Cost Calculation:**
```
With GPT-3.5 (all tasks):
Input: ~1.6M × $0.0005/1K = $0.80
Output: ~550K × $0.0015/1K = $0.82
Daily: $1.62

With GPT-4 (fraud only):
Cat+Support: $1.30 (GPT-3.5)
Fraud: $4.25 (GPT-4)
Daily: $5.55
```

**Optimization Strategies:**

**1. Caching**
- Cache categorization for identical merchants
- Expected: 60% cache hit rate
- Savings: ~$0.50/day

**2. Prompt Compression**
- Reduce system prompts by 30%
- Remove unnecessary words
- Savings: ~$0.20/day

**3. Smart Batching**
- Batch categorizations (5 per request)
- Share system prompt
- Savings: ~$0.15/day

**4. Temperature=0 for Caching**
- Deterministic outputs enable caching
- Identical inputs → identical outputs
- Better cache hit rates

**What to figure out:**
- Cache implementation (Redis?)
- Prompt optimization techniques
- Batching logic
- Cost tracking dashboard

**Success criteria:**
- [ ] Cost baseline calculated
- [ ] Optimization strategies identified
- [ ] Caching implemented
- [ ] Reduced costs by >30%
- [ ] Cost monitoring in place

---

**Part 3: Performance Optimization - 15 min**

**Metrics to Optimize:**

**1. Latency**
- Target: <1s categorization
- Target: <2s fraud analysis
- Target: <3s support responses

**Optimization:**
- Async API calls where possible
- Connection pooling
- Timeout configuration
- Parallel processing for batch

**2. Accuracy**
- Target: >95% categorization
- Target: >90% fraud detection
- Target: >85% support quality

**Optimization:**
- Prompt refinement
- Few-shot example selection
- Model selection per task
- A/B testing prompts

**3. Reliability**
- Target: >99% uptime
- Target: <0.1% error rate

**Optimization:**
- Retry logic (3 attempts)
- Circuit breaker pattern
- Fallback responses
- Health checks

**What to figure out:**
- How to measure latency accurately
- Accuracy testing methodology
- Reliability monitoring
- Performance benchmarking

**Success criteria:**
- [ ] Latency targets met
- [ ] Accuracy targets met
- [ ] Reliability >99%
- [ ] Performance monitored
- [ ] Bottlenecks identified

---

### HOUR 4 (Optional): Polish & Documentation

**Part 1: Code Quality - 20 min**

**Improvements:**

**1. Error Messages**
- User-friendly messages
- Technical details logged
- Action suggestions
- Support contact info

**2. Logging**
- Structured logging (JSON)
- Log levels (DEBUG, INFO, ERROR)
- Request IDs for tracing
- Performance metrics

**3. Configuration**
- Environment variables
- Config file support
- Different configs per environment
- Validation on startup

**4. Code Organization**
- Modular structure
- Clear naming conventions
- Documentation strings
- Type hints

**Success criteria:**
- [ ] Clean, readable code
- [ ] Comprehensive logging
- [ ] Configuration externalized
- [ ] Error messages helpful

---

**Part 2: Documentation - 20 min**

**Documents to Create:**

**README.md:**
```markdown
# Payment Q&A System

LLM-powered transaction analysis and customer support.

## Features
- Transaction categorization (>95% accuracy)
- Fraud detection (>90% accuracy)  
- Customer support Q&A
- Cost: ~$5/day for 2,000 operations

## Quick Start
[Installation and usage]

## Architecture
[Component diagram]

## API Reference
[Function documentation]

## Testing
[How to run tests]
```

**API_USAGE.md:**
- Function signatures
- Input/output examples
- Error handling
- Best practices

**PROMPT_LIBRARY.md:**
- All prompt templates
- Version history
- Performance metrics
- A/B test results

**Success criteria:**
- [ ] README complete
- [ ] API documented
- [ ] Prompts documented
- [ ] Examples included

---

**Part 3: Deployment Prep - 20 min**

**Checklist:**

**1. Environment Setup**
- Requirements.txt complete
- .env.example provided
- Setup script working
- Dependencies documented

**2. Configuration**
- API keys via environment
- Model selection configurable
- Costs monitored
- Logging configured

**3. Monitoring**
- Request/response logging
- Token usage tracking
- Error rate monitoring
- Cost dashboards

**4. Security**
- API keys secure
- Input validation
- Output sanitization
- Rate limiting

**What to figure out:**
- Deployment target (local/cloud)
- Environment management
- Secrets management
- Monitoring tools

**Success criteria:**
- [ ] Ready for deployment
- [ ] Configuration complete
- [ ] Monitoring in place
- [ ] Security validated

---

### Day 6 Deliverables

**System Components:**
- [ ] OpenAI API wrapper with retry logic
- [ ] Transaction categorization (>95% accuracy)
- [ ] Fraud analysis (>90% accuracy)
- [ ] Conversation manager
- [ ] Error handling comprehensive

**Testing:**
- [ ] Unit tests (20+ tests)
- [ ] Integration tests
- [ ] Edge case handling
- [ ] Error scenario coverage

**Optimization:**
- [ ] Cost <$5/day target
- [ ] Caching implemented
- [ ] Latency optimized
- [ ] Prompts refined

**Documentation:**
- [ ] README comprehensive
- [ ] API reference complete
- [ ] Architecture documented
- [ ] Deployment guide

**Quality Metrics:**
- [ ] Categorization: >95% accuracy
- [ ] Fraud detection: >90% accuracy
- [ ] Latency: <2s average
- [ ] Cost: ~$5/day for 2K operations
- [ ] Reliability: >99%

---

## DAY 7 (Monday Dec 22): Testing, Optimization & Documentation - 180 minutes

### Goal
Comprehensive testing, cost optimization, performance tuning, and professional documentation.

### Schedule - 180 minutes total

**HOUR 1: Advanced Testing (60 min)**
**HOUR 2: Production Optimization (60 min)**
**HOUR 3: Final Documentation & Polish (60 min)**

---

### HOUR 1: Advanced Testing

**Part 1: Accuracy Testing - 25 min**

**Requirements:**

**Create Test Dataset:**
- 50 transactions with ground truth categories
- 20 fraud scenarios with expected risk levels
- 10 edge cases

**Categorization Test:**
```
Transaction: "STARBUCKS #1234 $5.50"
Expected: Food & Dining > Coffee Shop
Actual: [run through system]
Match: Yes/No
```

**Metrics to Calculate:**
- Accuracy: Correct / Total
- Precision per category
- Recall per category
- F1 Score
- Confusion matrix

**Fraud Test:**
```
Scenario: High-value electronics, 3 AM, Nigeria
Expected Risk: >80 (Critical)
Actual: [run through system]
Within Range: Yes/No
```

**Metrics:**
- True Positives (fraud caught)
- False Positives (legitimate flagged)
- False Negatives (fraud missed)
- True Negatives (legitimate approved)

**What to figure out:**
- How to build ground truth dataset
- Accuracy calculation methods
- When accuracy is "good enough"
- How to improve false positives/negatives
- Testing automation

**Success criteria:**
- [ ] 50-transaction test set created
- [ ] Categorization accuracy measured
- [ ] Fraud detection accuracy measured
- [ ] Metrics calculated
- [ ] Improvement areas identified

---

**Part 2: Stress Testing - 20 min**

**Requirements:**

**Volume Test:**
- Process 1,000 transactions
- Measure throughput (trans/sec)
- Monitor memory usage
- Track error rate
- Calculate total cost

**Latency Test:**
- Measure P50, P95, P99 latency
- Categorization response time
- Fraud analysis response time
- Identify slowest operations

**Concurrency Test:**
- 10 simultaneous requests
- 50 simultaneous requests
- 100 simultaneous requests
- Monitor for failures
- Check rate limit handling

**What to figure out:**
- Load testing tools
- How to generate test data
- Acceptable latency levels
- Concurrency limits
- Bottleneck identification

**Success criteria:**
- [ ] Processed 1,000 transactions
- [ ] Measured latencies (P50, P95, P99)
- [ ] Tested concurrency (10, 50, 100)
- [ ] No failures under load
- [ ] Bottlenecks documented

---

**Part 3: Edge Case Testing - 15 min**

**Edge Cases:**

**1. Unusual Inputs:**
- Empty string
- Very long input (10,000 chars)
- Special characters only "!@#$%^&*()"
- Non-English text "日本語"
- Numbers only "123456789"

**2. Boundary Conditions:**
- Token limit exactly at max
- Token limit exceeded by 1
- Zero tokens
- Very small response (<10 tokens)

**3. API Errors:**
- Simulate all HTTP error codes
- Network timeout
- Invalid JSON response
- Partial response

**4. Data Quality:**
- Missing fields
- Invalid field types
- Null values
- Unexpected formats

**What to figure out:**
- How to handle each edge case
- Default behaviors
- Error messages
- Recovery strategies

**Success criteria:**
- [ ] All edge cases tested
- [ ] Graceful handling verified
- [ ] No crashes or hangs
- [ ] Error messages helpful
- [ ] Recovery working

---

### HOUR 2: Production Optimization

**Part 1: Cost Optimization Deep Dive - 25 min**

**Current Cost Analysis:**

**Detailed Breakdown:**
```
Categorization:
- Volume: 10,000/day
- Avg tokens: 150 per request
- Model: GPT-3.5-Turbo
- Daily cost: $1.62

Fraud Analysis:
- Volume: 500/day
- Avg tokens: 550 per request
- Model: GPT-4
- Daily cost: $4.25

Total: $5.87/day
Monthly: $176/month
Annual: $2,142/year
```

**Optimization Strategies:**

**1. Aggressive Caching**
- Cache all categorization results
- Cache key: merchant name hash
- Expected hit rate: 70%
- Savings: $1.13/day ($410/year)

**2. Prompt Compression**
- Reduce system prompts 40%
- Remove redundant instructions
- Shorter examples
- Savings: $0.35/day ($128/year)

**3. Selective GPT-4 Usage**
- Use GPT-3.5 for fraud first-pass
- Escalate to GPT-4 only if borderline
- 60% stay with GPT-3.5
- Savings: $2.55/day ($930/year)

**4. Batch Processing**
- Batch 10 categorizations per request
- Share system prompt overhead
- Savings: $0.25/day ($91/year)

**Total Potential Savings: $4.28/day ($1,559/year)**
**New Daily Cost: $1.59/day ($580/year)**
**Reduction: 73%**

**What to figure out:**
- Cache implementation (Redis/in-memory)
- Prompt optimization without quality loss
- GPT-3.5 → GPT-4 escalation logic
- Batching implementation
- Cost monitoring dashboard

**Success criteria:**
- [ ] Caching implemented
- [ ] Prompts optimized
- [ ] Selective GPT-4 logic
- [ ] Batching working
- [ ] Cost reduced >50%

---

**Part 2: Performance Tuning - 20 min**

**Latency Optimization:**

**Current Performance:**
- Categorization: 1.2s average
- Fraud: 2.8s average
- Support: 3.5s average

**Targets:**
- Categorization: <1s
- Fraud: <2s
- Support: <3s

**Improvements:**

**1. Connection Pooling**
- Reuse HTTP connections
- Reduce handshake overhead
- Expected: -200ms per request

**2. Async Processing**
- Non-blocking API calls
- Parallel processing where possible
- Expected: -300ms for batches

**3. Local Caching**
- In-memory cache for frequent queries
- Skip API call entirely
- Expected: <50ms for cache hits

**4. Timeout Optimization**
- Set appropriate timeouts
- Fail fast on issues
- Retry only when useful

**What to figure out:**
- Connection pool configuration
- Async implementation approach
- Cache eviction policy
- Optimal timeout values

**Success criteria:**
- [ ] All latency targets met
- [ ] Connection pooling implemented
- [ ] Cache hit rate >60%
- [ ] P95 latency improved

---

**Part 3: Reliability Improvements - 15 min**

**Current Issues:**
- Occasional timeouts
- Rate limit errors
- Token overflow errors
- Response parsing failures

**Improvements:**

**1. Circuit Breaker**
- Detect repeated failures
- Stop making requests temporarily
- Auto-recover when service healthy
- Prevents cascading failures

**2. Exponential Backoff**
- Retry with increasing delays
- 1s, 2s, 4s, 8s
- Max 3-5 retries
- Jitter to prevent thundering herd

**3. Fallback Responses**
- Default categories for failures
- Conservative fraud scores
- Generic support responses
- Maintain service availability

**4. Health Checks**
- Periodic API health checks
- Monitor success rate
- Alert on degradation
- Dashboard for monitoring

**What to figure out:**
- Circuit breaker thresholds
- Retry strategy tuning
- Fallback response design
- Health check implementation

**Success criteria:**
- [ ] Circuit breaker implemented
- [ ] Exponential backoff working
- [ ] Fallback responses defined
- [ ] Health monitoring active
- [ ] Reliability >99.5%

---

### HOUR 3: Final Documentation & Polish

**Part 1: Comprehensive Documentation - 30 min**

**README.md Updates:**
```markdown
# Payment Q&A System with OpenAI

Production-ready LLM system for payment processing.

## Performance Metrics
- Categorization: 96% accuracy, <1s latency
- Fraud Detection: 92% accuracy, <2s latency
- Cost: $1.59/day for 10,500 operations
- Reliability: 99.6% uptime

## Features
✅ Transaction categorization
✅ Real-time fraud detection
✅ Customer support Q&A
✅ Conversation management
✅ Cost optimization (73% reduction)
✅ Comprehensive error handling

## Quick Start
[Installation steps]

## Architecture
[Component diagram with data flow]

## Cost Optimization
- Caching: 70% hit rate
- Selective GPT-4: 40% of fraud analysis
- Batch processing: 10 per request
- Prompt compression: 40% reduction

## Testing
- Unit tests: 50+ tests
- Integration tests: 20+ scenarios
- Load testing: 1,000 transactions
- Accuracy: >95% categorization

## Deployment
[Production deployment guide]

## Monitoring
[Dashboard screenshots/links]

## Troubleshooting
[Common issues and solutions]
```

**API_REFERENCE.md:**
- All function signatures
- Input/output schemas
- Error codes
- Rate limits
- Examples

**COST_ANALYSIS.md:**
- Detailed cost breakdown
- Optimization strategies
- ROI calculations
- Scaling projections

**Success criteria:**
- [ ] README comprehensive
- [ ] API reference complete
- [ ] Cost analysis detailed
- [ ] All docs professional

---

**Part 2: Code Review & Cleanup - 15 min**

**Cleanup Tasks:**

**1. Code Quality**
- Remove dead code
- Fix TODO comments
- Consistent naming
- Add type hints
- Improve comments

**2. Error Messages**
- Clear and actionable
- Include error codes
- Suggest solutions
- Contact information

**3. Logging**
- Structured logging
- Appropriate log levels
- Performance metrics
- Security considerations

**4. Configuration**
- All hardcoded values moved to config
- Environment variable support
- Validation on startup
- Sensible defaults

**Success criteria:**
- [ ] No dead code
- [ ] Consistent style
- [ ] Type hints added
- [ ] Error messages clear
- [ ] Configuration complete

---

**Part 3: Final Testing & Validation - 15 min**

**Pre-Production Checklist:**

**Functionality:**
- [ ] All core features working
- [ ] Error handling comprehensive
- [ ] Edge cases handled
- [ ] Performance targets met

**Quality:**
- [ ] >95% categorization accuracy
- [ ] >90% fraud detection accuracy
- [ ] <2s average latency
- [ ] >99% reliability

**Cost:**
- [ ] <$2/day for target volume
- [ ] Caching working (>60% hit rate)
- [ ] Monitoring in place
- [ ] Alerts configured

**Security:**
- [ ] API keys secure (environment vars)
- [ ] Input validation
- [ ] Output sanitization
- [ ] No secrets in code/logs

**Documentation:**
- [ ] README complete
- [ ] API documented
- [ ] Examples provided
- [ ] Troubleshooting guide

**Deployment:**
- [ ] Requirements.txt complete
- [ ] Setup script working
- [ ] Environment configs ready
- [ ] Health checks implemented

**Success criteria:**
- [ ] All checklist items passed
- [ ] Ready for production
- [ ] Documentation complete
- [ ] Monitoring active

---

### Day 7 Deliverables

**Testing Completed:**
- [ ] Accuracy: >95% categorization, >90% fraud
- [ ] Load tested: 1,000 transactions
- [ ] Latency: All targets met
- [ ] Edge cases: All handled gracefully
- [ ] Reliability: >99% uptime

**Optimization Completed:**
- [ ] Cost reduced by 73% ($5.87 → $1.59/day)
- [ ] Caching: 70% hit rate
- [ ] Performance: All latency targets met
- [ ] Reliability: Circuit breaker + backoff

**Documentation Completed:**
- [ ] README comprehensive with metrics
- [ ] API reference complete
- [ ] Cost analysis detailed
- [ ] Architecture documented
- [ ] Troubleshooting guide

**Production Ready:**
- [ ] All tests passing
- [ ] Code clean and documented
- [ ] Configuration externalized
- [ ] Monitoring active
- [ ] Security validated
- [ ] Deployment ready

---

## WEEK 5 SUMMARY

### What You've Completed

**LLM Fundamentals:**
- ✅ Transformer architecture understanding
- ✅ Attention mechanism concepts
- ✅ Token-based text processing
- ✅ Context window management
- ✅ Temperature and sampling parameters

**OpenAI API Mastery:**
- ✅ API authentication and setup
- ✅ Request/response structure
- ✅ Message roles (system, user, assistant)
- ✅ Error handling and retry logic
- ✅ Token usage tracking

**Prompt Engineering:**
- ✅ Core prompting principles
- ✅ Few-shot learning technique
- ✅ Chain-of-thought reasoning
- ✅ Role-based prompting
- ✅ Output format specification

**Conversation Management:**
- ✅ Stateless API handling
- ✅ Conversation history tracking
- ✅ Sliding window implementation
- ✅ Token budget management
- ✅ Multi-turn conversation flows

**Production System:**
- ✅ Transaction categorization (>95% accuracy)
- ✅ Fraud detection system (>90% accuracy)
- ✅ Customer support Q&A
- ✅ Cost optimization (73% reduction)
- ✅ Comprehensive error handling
- ✅ Performance monitoring
- ✅ Production-ready documentation

### Key Achievements

**Technical Skills:**
- Built production LLM system from scratch
- Implemented cost-effective API usage patterns
- Created reusable conversation management
- Developed comprehensive error handling
- Achieved industry-standard accuracy metrics

**Business Value:**
- $1.59/day operating cost for 10,500 operations
- <2s average latency for all operations
- 99.6% reliability/uptime
- ROI: ~$1,500/year savings vs. baseline
- Scalable architecture for growth

**Payment Domain Expertise:**
- Transaction categorization system
- Real-time fraud detection
- Customer support automation
- Merchant normalization
- Regulatory compliance Q&A capability

### Skills Gained for Interviews

**Can Explain:**
- "How do transformers work?" → Attention mechanism, parallel processing
- "What are tokens and why do they matter?" → Cost, limits, efficiency
- "How do you optimize LLM costs?" → Caching, batching, model selection
- "What is prompt engineering?" → Instructions + context + examples
- "How do you handle context limits?" → Sliding window, summarization
- "What's the difference between GPT-3.5 and GPT-4?" → Cost, quality, use cases
- "How do you ensure LLM reliability?" → Retry logic, fallbacks, monitoring

**Can Demonstrate:**
- Working payment Q&A system with GitHub repo
- Cost optimization strategies (73% reduction)
- Production error handling patterns
- Multi-turn conversation management
- Performance metrics and monitoring
- Testing methodology (accuracy, latency, reliability)

**Can Discuss Trade-offs:**
- GPT-3.5 vs GPT-4: Cost vs. quality
- Temperature 0 vs. higher: Consistency vs. creativity
- Caching: Cost savings vs. staleness
- Context length: Quality vs. token budget
- Synchronous vs. async: Simplicity vs. performance

### Total Time Investment

**Weekday Learning:**
- Monday-Friday: 5 days × 60-90 min = 5-7.5 hours

**Weekend Projects:**
- Saturday: 3-4 hours (system building)
- Sunday: 3 hours (testing & optimization)

**Total Week 5:** ~11-14.5 hours

**Cumulative (Weeks 1-5):**
- Week 1-2: Math, Python, basics (~24 hours)
- Week 3-4: Infrastructure, data pipeline (~28 hours)
- Week 5: LLM fundamentals (~13 hours)
- **Total: ~65 hours** across 5 weeks

### Looking Ahead: Week 6 (December 22-28)

**Week 6: Prompt Engineering Mastery**

**Focus Areas:**
- Advanced prompting techniques
- Chain-of-thought reasoning
- Self-consistency methods
- ReAct (Reasoning + Acting)
- Meta-prompting strategies
- Prompt optimization frameworks

**Deliverable:**
- Comprehensive fintech prompt library
- 50+ production-ready prompts
- Categorization, fraud, compliance, support
- A/B testing framework
- Performance benchmarking

**Why This Matters:**
- Prompt quality directly affects system quality
- Can improve accuracy 10-20% with better prompts
- Reduces costs through efficiency
- Critical for production systems
- Interview differentiator

### Week 5 Reflection Questions

**Technical Understanding:**
1. Can you explain how attention mechanism works to a non-technical person?
2. Why does tokenization matter for cost and performance?
3. How would you design a conversation system for 100-turn dialogues?
4. What's the trade-off between caching and freshness?
5. When should you use GPT-4 vs. GPT-3.5?

**System Design:**
1. How did you optimize costs from $5.87 to $1.59/day?
2. What error handling strategies did you implement?
3. How do you measure system quality (accuracy, latency, cost)?
4. What would you change if volume increased 10x?
5. How would you add new features (e.g., receipt parsing)?

**Business Application:**
1. What payment problems can LLMs solve effectively?
2. What are the limitations of LLMs in fintech?
3. How do you justify LLM costs to business stakeholders?
4. What compliance/security concerns exist with LLMs?
5. How do LLMs compare to traditional ML for categorization?

**Career Transition:**
1. What from this week would you highlight in interviews?
2. How does this connect to your payments domain expertise?
3. What GitHub projects can you create from this?
4. How would you explain this to technical recruiters?
5. What questions would you ask in an AI Engineer interview?

### Resources for Continued Learning

**Advanced Topics (Optional):**

**Function Calling:**
- OpenAI Function Calling Guide
- When LLMs need external tools
- Structured outputs
- Week 13+ covers this in agents

**Fine-Tuning:**
- When to fine-tune vs. prompt engineering
- Cost-benefit analysis
- Your Month 3 covers this extensively

**Embeddings:**
- Week 6 covers in depth
- Semantic search foundation
- RAG systems (Week 7-11)

**LangChain:**
- Framework for LLM applications
- Useful but not essential
- Many concepts you already learned

**Community Resources:**

**Discord Servers:**
- OpenAI Developer Community
- LangChain Discord
- Prompt Engineering discussions

**Twitter Follows:**
- @OpenAI
- @AndrewYNg
- @karpathy
- @simonw

**Newsletters:**
- The Batch (Andrew Ng)
- Import AI (Jack Clark)
- TLDR AI

**Blogs:**
- OpenAI Blog
- Anthropic Blog
- Hugging Face Blog
- Simon Willison's Blog

### Interview Preparation

**Portfolio Project:**
"Payment Q&A System with OpenAI"

**Elevator Pitch:**
"I built a production LLM system that categorizes 10,000 transactions daily with 96% accuracy at $1.59/day. It includes real-time fraud detection, customer support automation, and conversation management. I optimized costs by 73% through caching, selective GPT-4 usage, and prompt compression. The system handles 99.6% uptime with comprehensive error handling and monitoring."

**GitHub Repository Structure:**
```
payment-qa-system/
├── README.md (comprehensive with metrics)
├── src/
│   ├── api_wrapper.py
│   ├── categorization.py
│   ├── fraud_detection.py
│   ├── conversation_manager.py
│   └── prompt_templates.py
├── tests/
│   ├── test_accuracy.py
│   ├── test_performance.py
│   └── test_edge_cases.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COST_ANALYSIS.md
│   └── API_REFERENCE.md
├── examples/
│   └── demo_notebook.ipynb
├── requirements.txt
└── .env.example
```

**Technical Interview Questions You Can Now Answer:**

**Architecture:**
- "Design a fraud detection system using LLMs"
- "How would you handle 100K transactions/day?"
- "Explain your cost optimization strategy"
- "How do you ensure 99.9% reliability?"

**Implementation:**
- "How do you manage conversation context?"
- "Explain your error handling approach"
- "How do you monitor LLM system performance?"
- "Walk through your testing strategy"

**Trade-offs:**
- "When would you use GPT-4 vs. GPT-3.5?"
- "Caching vs. real-time API calls - discuss"
- "Temperature 0 vs. 0.7 for production?"
- "Synchronous vs. asynchronous processing?"

**Business:**
- "How do you measure ROI for LLM systems?"
- "What are compliance concerns in fintech LLMs?"
- "How do you handle hallucinations in production?"
- "Explain costs to non-technical stakeholders"

### Common Pitfalls to Avoid

**Technical:**
- ❌ Not tracking token usage (runaway costs)
- ❌ No retry logic (poor reliability)
- ❌ Hardcoding API keys (security issue)
- ❌ Ignoring context limits (runtime errors)
- ❌ No caching (unnecessary costs)

**Prompt Engineering:**
- ❌ Vague instructions (poor outputs)
- ❌ No examples (inconsistent results)
- ❌ No output format (parsing nightmares)
- ❌ Too verbose prompts (wasted tokens)
- ❌ No testing (production surprises)

**System Design:**
- ❌ No error handling (crashes in production)
- ❌ No monitoring (blind to issues)
- ❌ No testing (unknown accuracy)
- ❌ Overengineering (wasted time)
- ❌ No documentation (unmaintainable)

**Cost Management:**
- ❌ Using GPT-4 for everything (10x costs)
- ❌ No caching strategy (repeated calls)
- ❌ Long system prompts (token waste)
- ❌ No cost alerts (budget surprises)
- ❌ Inefficient prompts (wasted tokens)

### Success Metrics Achieved

**✅ Technical Metrics:**
- Categorization accuracy: 96% (target: >95%)
- Fraud detection accuracy: 92% (target: >90%)
- Average latency: 1.5s (target: <2s)
- P95 latency: 2.3s (target: <3s)
- Reliability: 99.6% (target: >99%)
- Test coverage: 85% (target: >80%)

**✅ Business Metrics:**
- Daily operating cost: $1.59 (budget: <$5)
- Cost per transaction: $0.00015
- ROI: $1,500/year savings
- Processing capacity: 10,500/day
- Cache hit rate: 70% (target: >60%)

**✅ Learning Metrics:**
- Time invested: 13 hours (planned: 11-13)
- Concepts mastered: 25+
- Exercises completed: 15+
- Production system: ✅ Deployed
- Portfolio piece: ✅ GitHub ready

### Week 5 Completion Checklist

**Day 1 (Sunday):**
- [x] Watched Andrej Karpathy LLM intro
- [x] Read Illustrated GPT-2
- [x] Understand transformer architecture
- [x] Identified payment use cases

**Day 2 (Monday):**
- [x] Understand tokenization (BPE)
- [x] Cost analysis for payment scenarios
- [x] Context window management
- [x] Token counting practice

**Day 3 (Tuesday):**
- [x] OpenAI API setup complete
- [x] First successful API calls
