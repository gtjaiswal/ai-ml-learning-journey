# WEEK 5: LLM FUNDAMENTALS - Days 3-7 (Ollama Version)

## OVERVIEW OF CHANGES

**Replacing OpenAI API with Ollama:**
- ✅ Completely free (no API costs)
- ✅ Unlimited requests for learning
- ✅ Privacy - data stays local
- ✅ Same concepts apply (prompts, temperature, context)
- ✅ Integrates with Phase 1 RAG system (Week 9 already uses Ollama)

**Models You'll Use:**
- Llama 3.2 (3B) - Fast, good for categorization
- Phi-3 Mini - Efficient, good quality
- Mistral 7B - Higher quality when needed

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

## DAY 3 (Tuesday Dec 18): Ollama Setup & First Calls - 60 minutes

### Primary Resources

**"Ollama Documentation"**
- Link: https://ollama.com/
- Duration: 15 min read
- Official getting started guide

**"Ollama Python Library"**
- Link: https://github.com/ollama/ollama-python
- Duration: 10 min read
- Python client documentation

**"Ollama Model Library"**
- Link: https://ollama.com/library
- Duration: 10 min browsing
- Available models and sizes

### Video Resources

**"Ollama Tutorial - Local LLMs Made Easy"**
- Link: https://www.youtube.com/watch?v=Wjrdr0NU4Sk
- Duration: 15:00
- Installation and basic usage

**"Running LLMs Locally with Ollama"**
- Link: https://www.youtube.com/watch?v=rIRkxZSn-A8
- Duration: 12:00
- Practical walkthrough

### Reading Materials

**"Ollama vs OpenAI API - Key Differences"**
- Link: https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image
- Duration: 10 min read
- Understanding local vs cloud

**"Model Selection Guide"**
- Link: https://ollama.com/blog/how-to-prompt-code-llama
- Duration: 10 min read
- Choosing right model for task

### Schedule - 60 minutes total

**Part 1: Installation & Setup (20 min)**
1. Install Ollama (10 min)
2. Pull first model (5 min)
3. Test in terminal (5 min)

**Part 2: Python Integration (20 min)**
4. Install ollama-python library (5 min)
5. Watch: Tutorial video (15 min)

**Part 3: First API Calls (20 min)**
6. Make first programmatic calls
7. Test different models

### Key Concepts to Master

**Ollama vs OpenAI API:**

**Similarities:**
- Same API structure (messages, temperature, etc.)
- Same prompting techniques work
- Same conversation patterns
- JSON response format similar

**Differences:**
- Local execution (no network calls)
- No costs (unlimited usage)
- Slower inference (no GPUs in cloud)
- Smaller models (3B-13B vs 175B)
- Data privacy (stays on machine)

**How Ollama Works:**

**Architecture:**
```
Your Python Code
    ↓
Ollama Python Library
    ↓
Ollama Server (localhost:11434)
    ↓
Model loaded in RAM
    ↓
Inference on CPU/GPU
    ↓
Response back to Python
```

**Model Storage:**
- Models stored locally (~2-7 GB each)
- Location: `~/.ollama/models`
- Pull once, use forever
- Multiple models can coexist

### Installation Requirements

**Step 1: Install Ollama**

**For macOS:**
```bash
# Download from https://ollama.com/download
# Or use Homebrew
brew install ollama

# Start Ollama service
ollama serve
```

**For Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve
```

**For Windows:**
```bash
# Download installer from https://ollama.com/download
# Run installer
# Ollama runs as service automatically
```

**Step 2: Pull Models**

**Essential Models for Week 5:**
```bash
# Fast, efficient for categorization (1.7 GB)
ollama pull llama3.2:3b

# Good quality, general purpose (2.3 GB)
ollama pull phi3:mini

# Higher quality for complex tasks (4.1 GB)
ollama pull mistral:7b
```

**Step 3: Test in Terminal**
```bash
# Simple test
ollama run llama3.2:3b "Hello, explain what you are in one sentence"

# Should respond immediately
```

**Step 4: Install Python Library**
```bash
pip install ollama
```

**What to figure out:**
- Where models are stored on your system
- How to check running models
- How to stop/start Ollama service
- Memory usage per model
- How to list available models

### API Structure (Ollama Python)

**Basic Request:**
```python
import ollama

response = ollama.chat(
    model='llama3.2:3b',
    messages=[
        {
            'role': 'system',
            'content': 'You are a transaction categorizer'
        },
        {
            'role': 'user',
            'content': 'Categorize: STARBUCKS $5.50'
        }
    ]
)

print(response['message']['content'])
```

**Key Differences from OpenAI:**

**Authentication:**
- ❌ No API key needed
- ❌ No Authorization header
- ✅ Just works if Ollama running

**Endpoint:**
- ❌ No cloud URL
- ✅ localhost:11434 (automatic)

**Models:**
- ❌ No "gpt-4" or "gpt-3.5-turbo"
- ✅ Use "llama3.2:3b", "phi3:mini", etc.

**Cost:**
- ❌ No token counting needed
- ✅ Free, unlimited

**Response Structure:**
```python
{
    'model': 'llama3.2:3b',
    'created_at': '2024-12-17T10:30:00Z',
    'message': {
        'role': 'assistant',
        'content': 'Category: Food & Dining\nConfidence: 95%'
    },
    'done': True
}
```

### Available Parameters

**temperature (0-2)**
- Same as OpenAI
- 0: Deterministic
- 1: Balanced
- 2: Creative

**num_predict (integer)**
- Similar to max_tokens
- Maximum response length
- Default: 128 tokens

**top_p (0-1)**
- Nucleus sampling
- Same concept as OpenAI

**top_k (integer)**
- Alternative sampling method
- Limits vocabulary to top K tokens
- Default: 40

**repeat_penalty (float)**
- Reduces repetition
- Default: 1.1
- Higher = less repetition

**stop (array)**
- Stop sequences
- Same as OpenAI

### Model Selection Guide

**For Transaction Categorization:**
- Use: `llama3.2:3b`
- Why: Fast, accurate for simple tasks
- Speed: ~1-2s per request

**For Fraud Analysis:**
- Use: `mistral:7b` or `phi3:mini`
- Why: Better reasoning
- Speed: ~3-5s per request

**For Customer Support:**
- Use: `llama3.2:3b`
- Why: Natural language, fast
- Speed: ~2-3s per request

**Model Comparison:**

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| llama3.2:3b | 1.7GB | Fast | Good | Categorization |
| phi3:mini | 2.3GB | Fast | Good | General |
| mistral:7b | 4.1GB | Medium | Better | Complex reasoning |
| llama3.1:8b | 4.7GB | Slower | Best | High quality needed |

### Hands-On Requirements

**Exercise 1: Installation & First Call**

**Requirements:**
- Install Ollama successfully
- Pull at least 2 models
- Make successful API call from Python
- Verify response

**Tasks:**

**1. Installation Verification**
```bash
# Check Ollama is running
ollama list

# Should show pulled models
```

**2. Terminal Test**
```bash
# Test each model
ollama run llama3.2:3b "What is 2+2?"
ollama run phi3:mini "What is 2+2?"

# Compare speeds
```

**3. Python Integration**
```python
# Create test script: test_ollama.py
import ollama

# Test simple completion
response = ollama.chat(
    model='llama3.2:3b',
    messages=[
        {'role': 'user', 'content': 'Say hello in one sentence'}
    ]
)

print(response['message']['content'])
```

**What to figure out:**
- How to check if Ollama is running
- How to switch between models
- Memory usage per model (check Activity Monitor/Task Manager)
- Response time for each model
- How to handle connection errors

**Success criteria:**
- [ ] Ollama installed and running
- [ ] At least 2 models pulled
- [ ] Terminal test successful
- [ ] Python script works
- [ ] Response received and parsed
- [ ] Understand model selection

---

**Exercise 2: Model Comparison**

**Requirements:**
- Test same prompt across 3 models
- Compare speed, quality, consistency
- Document differences

**Test Prompt:**
```
System: You are a transaction categorization expert.

User: Categorize this transaction into a category and subcategory.
Provide confidence score 0-100.

Transaction: UBER RIDE $45.00

Format:
Category: [category]
Subcategory: [type]
Confidence: [score]
```

**Models to Test:**
1. llama3.2:3b
2. phi3:mini
3. mistral:7b

**For Each Model, Measure:**
- Response time (seconds)
- Response quality (correct category?)
- Consistency (run 3 times, same result?)
- Response format (follows instructions?)

**What to figure out:**
- Which model is fastest
- Which gives best quality
- Which is most consistent
- Speed vs quality trade-off
- When to use which model

**Success criteria:**
- [ ] Tested all 3 models
- [ ] Measured response times
- [ ] Evaluated quality
- [ ] Tested consistency (3 runs each)
- [ ] Documented findings
- [ ] Can justify model selection

---

**Exercise 3: Error Handling**

**Requirements:**
- Test error scenarios
- Implement graceful handling
- Fallback strategies

**Error Scenarios:**

**Scenario 1: Ollama Not Running**
```python
# Stop Ollama service
# Try API call
# Should: Detect connection error
# Action: Clear error message
```

**Scenario 2: Model Not Found**
```python
# Use non-existent model name
# Should: Catch model error
# Action: Suggest available models
```

**Scenario 3: Timeout**
```python
# Set short timeout
# Long prompt
# Should: Handle timeout gracefully
# Action: Retry or return error
```

**Scenario 4: Invalid Response**
```python
# Prompt that might give invalid format
# Should: Parse defensively
# Action: Return default/error
```

**What to figure out:**
- How to detect Ollama not running
- Connection error handling
- Timeout configuration
- Response validation
- Fallback response design

**Success criteria:**
- [ ] All 4 scenarios tested
- [ ] Errors caught gracefully
- [ ] User-friendly messages
- [ ] No crashes
- [ ] Fallback strategies working

### Day 3 Deliverables

- [ ] Ollama installed successfully
- [ ] Pulled 2-3 models (llama3.2:3b, phi3:mini, mistral:7b)
- [ ] Made first successful API call
- [ ] Understand: Ollama vs OpenAI differences
- [ ] Understand: Model selection criteria
- [ ] Understand: Local vs cloud trade-offs
- [ ] Completed: Installation exercise
- [ ] Completed: Model comparison (3 models)
- [ ] Completed: Error handling exercise
- [ ] Can explain: When to use which model
- [ ] Can explain: How Ollama works locally
- [ ] Built: Reusable Ollama wrapper
- [ ] Spent approximately 60 minutes

---

## DAY 4 (Wednesday Dec 18): Advanced Parameters & Conversation Management - 60 minutes

### Primary Resources

**"Ollama API Reference"**
- Link: https://github.com/ollama/ollama/blob/main/docs/api.md
- Duration: 20 min read
- Complete parameter documentation

**"Modelfile Documentation"**
- Link: https://github.com/ollama/ollama/blob/main/docs/modelfile.md
- Duration: 15 min read
- Custom model configuration

### Video Resources

**"Advanced Ollama Features"**
- Link: https://www.youtube.com/watch?v=QWG_1r-L9x4
- Duration: 15:00
- Parameter tuning and optimization

### Reading Materials

**"Conversation Management with Ollama"**
- Link: https://github.com/ollama/ollama-python/blob/main/examples/chat.py
- Duration: 10 min read + code review
- Multi-turn conversation examples

### Schedule - 60 minutes total

**Part 1: Parameter Deep Dive (25 min)**
1. Read: API reference (15 min)
2. Watch: Advanced features video (10 min)

**Part 2: Conversation Patterns (20 min)**
3. Read: Conversation examples (10 min)
4. Experiment: Multi-turn conversations (10 min)

**Part 3: Hands-On Practice (15 min)**
5. Build conversation manager
6. Test with payment scenarios

### Key Concepts to Master

**Ollama-Specific Parameters:**

**seed (integer)**
- Controls randomness
- Same seed = same output
- Useful for testing consistency
- Similar to temperature=0 but different mechanism

**num_ctx (integer)**
- Context window size
- Default: 2048 tokens
- Can increase up to model's limit
- Llama3.2: up to 8K tokens
- More context = more memory

**num_gpu (integer)**
- Number of GPU layers
- Auto-detected by default
- Increase for faster inference
- Decrease if running out of VRAM

**num_thread (integer)**
- CPU threads for inference
- Default: auto-detect
- Tune for performance

**mirostat (0, 1, or 2)**
- Alternative sampling method
- 0: Disabled (default)
- 1: Mirostat 1.0
- 2: Mirostat 2.0 (recommended)
- Better quality for long text

### Conversation Management (Ollama)

**Same Stateless Principle:**
- Each request independent
- Must send full history
- Same as OpenAI API

**Conversation Pattern:**

**Turn 1:**
```python
messages = [
    {'role': 'system', 'content': 'You are a fraud analyst'},
    {'role': 'user', 'content': 'Check transaction TXN-123'}
]

response = ollama.chat(model='llama3.2:3b', messages=messages)
messages.append(response['message'])
```

**Turn 2:**
```python
# Add new user message
messages.append({
    'role': 'user',
    'content': 'Is it fraudulent?'
})

# Send full history
response = ollama.chat(model='llama3.2:3b', messages=messages)
messages.append(response['message'])
```

**Memory Management:**

**Ollama Considerations:**
- Models run in RAM
- Context uses RAM
- Longer conversations = more memory
- May need aggressive truncation
- Sliding window more important

**Recommended Limits:**
- Llama3.2 (3B): Keep under 4K tokens
- Phi3 Mini: Keep under 3K tokens
- Mistral (7B): Keep under 8K tokens

### Performance Optimization

**Speed Improvements:**

**1. Model Selection**
- Smaller model = faster
- 3B models: ~1-2s
- 7B models: ~3-5s
- Choose smallest that works

**2. GPU Acceleration**
- If you have GPU (NVIDIA/AMD/Apple M1+)
- Ollama auto-detects
- 5-10x faster than CPU
- Check GPU usage in task manager

**3. Context Management**
- Shorter context = faster
- Aggressive sliding window
- Summarization more important

**4. Batching (Advanced)**
- Process multiple simple requests
- Not native in Ollama
- Implement application-level queue

**Memory Management:**

**Current Usage:**
- Llama3.2 (3B): ~4GB RAM
- Phi3 Mini: ~5GB RAM
- Mistral (7B): ~8GB RAM

**If Running Multiple:**
- Models can coexist
- Load on first use
- Unload after idle timeout
- Configure timeout in Modelfile

### Hands-On Requirements

**Exercise 1: Parameter Experimentation**

**Requirements:**
- Test different parameters
- Understand effects
- Optimize for payment tasks

**Test Matrix:**

**Temperature Variation:**
```python
# Test categorization
prompt = "Categorize: STARBUCKS $5.50"

for temp in [0, 0.3, 0.7, 1.0]:
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': temp}
    )
    # Run 3 times each, compare consistency
```

**Seed Testing:**
```python
# Test reproducibility
for seed in [42, 42, 42]:  # Same seed
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': 0.7, 'seed': seed}
    )
    # Should get identical responses
```

**Context Window:**
```python
# Test different context sizes
for ctx_size in [1024, 2048, 4096]:
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[long_conversation_history],
        options={'num_ctx': ctx_size}
    )
    # Measure performance impact
```

**What to figure out:**
- Which temperature for categorization (0 vs 0.3)
- Does seed ensure reproducibility?
- Context size vs performance trade-off
- Best parameter combinations per task

**Success criteria:**
- [ ] Tested temperature (4 values)
- [ ] Verified seed reproducibility
- [ ] Tested context sizes
- [ ] Measured performance impact
- [ ] Documented optimal settings

---

**Exercise 2: Build Conversation Manager**

**Requirements:**
- Track conversation history
- Implement sliding window
- Manage memory limits
- Test with fraud investigation

**Features to Implement:**

**1. Message Storage**
```python
class ConversationManager:
    def __init__(self, model, max_messages=10):
        self.model = model
        self.messages = []
        self.max_messages = max_messages
    
    def add_message(self, role, content):
        # Add message
        # Check limit
        # Truncate if needed
        pass
    
    def get_history(self):
        # Return messages for API
        pass
    
    def chat(self, user_message):
        # Add user message
        # Call Ollama
        # Add assistant response
        # Return response
        pass
```

**2. Sliding Window**
- Keep system prompt
- Keep last N messages
- Remove oldest user+assistant pairs
- Maintain conversation coherence

**3. Token Estimation**
- Count characters (rough estimate)
- 1 token ≈ 4 characters
- Alert when approaching limit
- Trigger truncation at threshold

**What to figure out:**
- Data structure for messages
- How to implement sliding window
- When to truncate
- How to preserve context quality
- Testing multi-turn scenarios

**Success criteria:**
- [ ] ConversationManager class implemented
- [ ] Sliding window working
- [ ] Tested with 20+ turn conversation
- [ ] Memory limits enforced
- [ ] Context quality maintained

---

**Exercise 3: Fraud Investigation Chatbot**

**Requirements:**
- Multi-turn fraud investigation
- Context maintenance
- Natural conversation flow

**Conversation Flow:**
```
Bot: "I'll help investigate. What's the transaction ID?"
User: "TXN-12345"
Bot: "Found: $500, Electronics Store, Nigeria, 3 AM
     This looks suspicious. Do you recognize this merchant?"
User: "No, never shopped there"
Bot: "Do you have your card with you?"
User: "Yes"
Bot: "When did you last use your card?"
User: "Yesterday at grocery store"
Bot: "Based on your answers, this appears to be fraud.
     Recommended action: Block card and file dispute.
     Shall I proceed?"
```

**Implementation Requirements:**
- System prompt: Fraud investigation role
- Maintain conversation state
- Ask relevant follow-up questions
- Provide clear recommendations
- Handle 8-10 turn conversations

**What to figure out:**
- System prompt design for investigation
- How to guide conversation flow
- When to conclude investigation
- Error handling in multi-turn
- Context preservation strategies

**Success criteria:**
- [ ] Investigation chatbot functional
- [ ] Handles 8-10 turn conversations
- [ ] Asks relevant questions
- [ ] Maintains context throughout
- [ ] Provides clear recommendations
- [ ] Tested with 3 different scenarios

### Day 4 Deliverables

- [ ] Tested Ollama parameters (temperature, seed, context)
- [ ] Understand: Parameter effects on output
- [ ] Understand: Performance vs quality trade-offs
- [ ] Built: ConversationManager class
- [ ] Implemented: Sliding window
- [ ] Built: Fraud investigation chatbot
- [ ] Tested: Multi-turn conversations (10+ turns)
- [ ] Can explain: Ollama-specific parameters
- [ ] Can explain: Memory management for local LLMs
- [ ] Spent approximately 60 minutes

---

## DAY 5 (Thursday Dec 19): Prompt Engineering for Local LLMs - 60 minutes

### Primary Resources

**"Prompting Local LLMs" - Best Practices**
- Link: https://github.com/ollama/ollama/blob/main/docs/prompts.md
- Duration: 15 min read
- Ollama-specific prompting tips

**"Llama 3 Prompt Format"**
- Link: https://llama.meta.com/docs/model-cards-and-prompt-formats/meta-llama-3/
- Duration: 10 min read
- Model-specific formatting

### Video Resources

**"Prompt Engineering for Open Source LLMs"**
- Link: https://www.youtube.com/watch?v=mwMT-vYOvJI
- Duration: 18:00
- Differences from GPT prompting

### Reading Materials

**"Few-Shot Learning with Smaller Models"**
- Link: https://arxiv.org/abs/2005.14165 (skim introduction)
- Duration: 10 min read
- Why examples matter more for small models

### Schedule - 60 minutes total

**Part 1: Local LLM Prompting (25 min)**
1. Read: Ollama prompting guide (15 min)
2. Watch: Open source LLM prompting (10 min - first half)

**Part 2: Model-Specific Techniques (20 min)**
3. Read: Llama 3 prompt format (10 min)
4. Experiment: Different prompt styles (10 min)

**Part 3: Practice Exercises (15 min)**
5. Build payment domain prompts

### Key Concepts to Master

**Local LLMs vs GPT: Key Differences**

**1. Need More Explicit Instructions**
- GPT: Infers context easily
- Local: Be very explicit
- Example: "Output ONLY JSON" not "Provide JSON"

**2. Examples Are Critical**
- GPT: Works well zero-shot
- Local: Almost always needs examples
- Rule: 3-5 examples minimum

**3. Shorter Context Better**
- GPT: Handles long context well
- Local: Quality degrades faster
- Keep system prompts under 500 tokens

**4. Simpler Language**
- GPT: Understands complex instructions
- Local: Use simple, clear language
- Avoid nested conditions

**5. Format Matters More**
- GPT: Flexible with format
- Local: Stick to one format consistently
- XML or JSON work best

### Effective Prompting Patterns for Ollama

**Pattern 1: Explicit Role + Task + Format**

**Structure:**
```
You are [role].

Task: [specific action]

Input: [data]

Output EXACTLY in this format:
[format specification]

Examples:
[2-3 examples]

Now process:
[actual input]
```

**Example - Transaction Categorization:**
```
You are a transaction categorizer.

Task: Categorize the transaction into category and subcategory.

Output EXACTLY in this format:
Category: [name]
Subcategory: [name]
Confidence: [number 0-100]

Examples:
Input: SHELL GAS STATION $45
Output:
Category: Transportation
Subcategory: Gas & Fuel
Confidence: 95

Input: NETFLIX.COM $15.99
Output:
Category: Entertainment
Subcategory: Streaming
Confidence: 98

Now process:
Input: STARBUCKS $5.50
Output:
```

**Pattern 2: Step-by-Step Instructions**

**For Complex Tasks:**
```
Task: Analyze transaction for fraud.

Step 1: Compare amount to customer average
Step 2: Check merchant location vs customer location
Step 3: Check transaction time (unusual hours?)
Step 4: Determine risk level based on steps 1-3
Step 5: Recommend action

Transaction: [details]
Customer: [profile]

Follow all 5 steps:
```

**Pattern 3: Constrained Output**

**Force Specific Format:**
```
Categorize this transaction.

RULES:
- Output ONLY the category name
- Choose from: Food, Transport, Shopping, Entertainment
- ONE WORD ONLY
- NO explanations

Transaction: UBER RIDE $25
Category:
```

### Model-Specific Prompting

**Llama 3.2 Best Practices:**

**1. Use Simple, Direct Language**
```
✅ Good: "Categorize this: STARBUCKS $5"
❌ Avoid: "Please assist me in determining the appropriate category..."
```

**2. One Task Per Prompt**
```
✅ Good: "Is this fraud? $5000 electronics, Nigeria"
❌ Avoid: "Analyze for fraud, then categorize, then suggest actions"
```

**3. Examples Over Explanations**
```
✅ Good: Show 3 examples
❌ Avoid: Long explanation of categories
```

**Mistral 7B Best Practices:**

**1. Handles More Complex Instructions**
- Can do multi-step reasoning
- Better with longer context
- More GPT-like behavior

**2. Good for Fraud Analysis**
- Better reasoning ability
- Understands nuance
- Worth slower speed

**Phi-3 Mini Best Practices:**

**1. Strong at Following Format**
- Excellent JSON output
- Consistent formatting
- Good for structured tasks

**2. Code-Focused**
- Originally trained on code
- Good with structured data
- Less creative than Llama

### Hands-On Requirements

**Exercise 1: Build Categorization Prompt (Local LLM)**

**Requirements:**
- Optimize for Llama 3.2
- Include 5 examples
- Test with 10 transactions
- Achieve >85% accuracy

**Prompt Template:**
```
You are a transaction categorizer. Categorize into ONE of these categories:

Categories: Food, Transport, Shopping, Entertainment, Bills, Healthcare, Travel, Other

Output format:
Category: [name]
Confidence: [0-100]

Examples:
[5 diverse examples]

Categorize:
Input: [transaction]
Output:
```

**Test Transactions:**
1. STARBUCKS #1234 $5.50
2. AMAZON.COM $127.99
3. SHELL GAS $45.00
4. NETFLIX $15.99
5. CVS PHARMACY $32.10
6. UBER RIDE $67
7. WHOLE FOODS $156.43
8. SPOTIFY $9.99
9. DENTIST COPAY $40
10. ELECTRIC BILL $128.50

**What to figure out:**
- Minimum examples needed
- Best example diversity
- Output format consistency
- How to improve low-confidence cases
- When prompt is "good enough"

**Success criteria:**
- [ ] Prompt created with 5 examples
- [ ] Tested with all 10 transactions
- [ ] Accuracy >85% (8-9 correct)
- [ ] Consistent output format
- [ ] Confidence scores reasonable

---

**Exercise 2: Fraud Analysis Prompt (Local LLM)**

**Requirements:**
- Optimize for Mistral 7B
- Include risk factor checklist
- Test with 5 scenarios
- Clear recommendations

**Prompt Template:**
```
You are a fraud analyst. Analyze transaction for fraud.

Check these factors:
1. Amount vs customer average
2. Location (customer vs merchant)
3. Time of day
4. Merchant category
5. Velocity (multiple transactions)

Output format:
Risk: [Low/Medium/High/Critical]
Score: [0-100]
Factors: [comma-separated list]
Recommend: [Approve/Review/Decline]

Examples:
[2 examples: clear fraud + clear legitimate]

Analyze:
Transaction: [details]
Customer: [profile]
Output:
```

**Test Scenarios:**
1. **Clear Fraud:** $5000 electronics, 3 AM, Nigeria, customer USA, avg $50
2. **Clear Legit:** $35 restaurant, customer city, 6 PM, regular category
3. **Borderline:** $800 jewelry, midnight, new category, avg $300
4. **Travel:** $2500 hotel, Paris, customer has flight booking
5. **Velocity:** 5 transactions in 10 minutes, all different cities

**What to figure out:**
- How explicit to be about risk factors
- Example quality importance
- When Mistral gives better quality than Llama
- How to calibrate risk scores
- Handling edge cases

**Success criteria:**
- [ ] Prompt optimized for Mistral 7B
- [ ] Clear fraud detected (Scenario 1)
- [ ] Clear legit approved (Scenario 2)
- [ ] Edge cases handled reasonably (3-5)
- [ ] Recommendations actionable

---

**Exercise 3: Prompt Iteration & Optimization**

**Requirements:**
- Start with basic prompt
- Iterate to improve accuracy
- Document each change
- Measure improvement

**Task:** Merchant name normalization

**Iteration 1: Basic (Baseline)**
```
Clean merchant name: SQ *COFFEE ROASTERS NYC
```

**Measure:** Accuracy, format consistency

**Iteration 2: Add Role & Format**
```
You are a merchant name cleaner.

Remove: processor codes, location codes, extra info
Keep: main merchant name only

Input: SQ *COFFEE ROASTERS NYC
Output:
```

**Measure:** Improvement from iteration 1

**Iteration 3: Add Examples**
```
[Same as iteration 2]

Examples:
SQ *COFFEE SHOP → Coffee Shop
AMZN MKTP US → Amazon
TST* RESTAURANT → Restaurant

Input: SQ *COFFEE ROASTERS NYC
Output:
```

**Measure:** Improvement from iteration 2

**Iteration 4: Constrain Output**
```
[Same as iteration 3]

Output ONLY the cleaned name.
NO explanations.
NO extra text.

Input: SQ *COFFEE ROASTERS NYC
Cleaned:
```

**Measure:** Final accuracy

**Test Set (10 merchants):**
1. SQ *COFFEE ROASTERS NYC
2. AMZN MKTP US*123ABC
3. TST* RESTAURANT SOHO
4. PAYPAL *NETFLIX COM
5. SP* SPOTIFY NYC
6. SHELL OIL #1234
7. MCDONALD'S #567 NY
8. WHOLE FOODS MKT #89
9. CVS/PHARMACY #1234
10. UBER *TRIP PAYMENT

**What to figure out:**
- Which iteration provides best results
- Diminishing returns point
- When to stop iterating
- Cost vs quality for local LLMs
- Documentation importance

**Success criteria:**
- [ ] Completed 4 iterations
- [ ] Measured accuracy each iteration
- [ ] Documented improvements
- [ ] Identified optimal prompt
- [ ] Tested on all 10 merchants
- [ ] Achieved >80% accuracy

### Day 5 Deliverables

- [ ] Understand: Local LLM prompting differences
- [ ] Understand: Model-specific best practices
- [ ] Understand: Importance of examples for small models
- [ ] Built: Categorization prompt (>85% accuracy)
- [ ] Built: Fraud analysis prompt (Mistral optimized)
- [ ] Completed: Prompt iteration exercise
- [ ] Documented: Improvement per iteration
- [ ] Can explain: Why local LLMs need more explicit prompts
- [ ] Can explain: When to use which model
- [ ] Spent approximately 60 minutes

---

## DAY 6 (Saturday Dec 21): Build Payment Q&A System with Ollama - 180-240 minutes

### Goal
Build production-ready payment Q&A system using local LLMs with Ollama.

### Schedule - 180-240 minutes total

**HOUR 1: System Design (60 min)**
**HOUR 2: Core Implementation (60 min)**
**HOUR 3: Testing & Optimization (60 min)**
**HOUR 4 (Optional): Documentation (60 min)**

---

### HOUR 1: System Design

**Part 1: Requirements (20 min)**

**System Capabilities:**

**1. Transaction Categorization**
- Model: Llama 3.2 (3B)
- Speed: <2s per transaction
- Accuracy: >85%
- Volume: Unlimited (free!)

**2. Fraud Analysis**
- Model: Mistral 7B
- Speed: <5s per analysis
- Accuracy: >85%
- Quality: Multi-factor reasoning

**3. Customer Support**
- Model: Llama 3.2 (3B)
- Speed: <3s per response
- Quality: Natural conversation

**Non-Functional Requirements:**
- Cost: $0 (completely free)
- Privacy: All data stays local
- Offline: Works without internet
- Memory: <12GB RAM total
- Storage: ~8GB for models

**What to figure out:**
- Which tasks need which models
- Memory management strategy
- Performance optimization
- When to load/unload models
- Fallback strategies

**Success criteria:**
- [ ] Requirements documented
- [ ] Model selection justified
- [ ] Performance targets set
- [ ] Memory budget defined

---

**Part 2: Architecture (25 min)**

**System Components:**

**1. Ollama Manager**
- Check Ollama status
- Load models on demand
- Track loaded models
- Memory monitoring
- Error handling

**2. Model Router**
- Route requests to appropriate model
- Load model if needed
- Cache model instances
- Unload unused models

**3. Prompt Library**
- Categorization prompts
- Fraud analysis prompts
- Support prompts
- Few-shot examples
- Version control

**4. Transaction Processor**
- Categorization pipeline
- Fraud analysis pipeline
- Batch processing
- Result caching

**5. Conversation Manager**
- History tracking
- Sliding window
- Memory limits
- State persistence

**Architecture Diagram:**
```
┌─────────────────────────────────────┐
│     Payment Q&A System              │
│                                     │
│  ┌────────────┐  ┌───────────────┐│
│  │ Model      │  │ Conversation  ││
│  │ Router     │  │ Manager       ││
│  └─────┬──────┘  └───────┬───────┘│
│        │                  │        │
│  ┌─────▼──────────────────▼──────┐│
│  │     Ollama Manager            ││
│  └─────┬──────────────────────────┘│
│        │                          │
│  ┌─────▼────────┐  ┌────────────┐│
│  │ llama3.2:3b  │  │ mistral:7b ││
│  │ (Fast)       │  │ (Quality)  ││
│  └──────────────┘  └────────────┘│
└─────────────────────────────────────┘
```

**What to figure out:**
- Component interactions
- Data flow
- Error propagation
- State management
- Testing strategy

**Success criteria:**
- [ ] Architecture designed
- [ ] Components defined
- [ ] Diagram created
- [ ] Data flow documented

---

**Part 3: Prompt Library (15 min)**

**Prompts to Create:**

**1. Transaction Categorization**
```
Model: llama3.2:3b
Temperature: 0
Num_predict: 50
Examples: 5
Output: Structured (Category/Confidence)
```

**2. Merchant Normalization**
```
Model: llama3.2:3b
Temperature: 0
Num_predict: 20
Examples: 5
Output: Clean merchant name only
```

**3. Fraud Analysis**
```
Model: mistral:7b
Temperature: 0.3
Num_predict: 200
Examples: 2
Output: Risk/Score/Factors/Recommend
```

**4. Customer Support**
```
Model: llama3.2:3b
Temperature: 0.7
Num_predict: 150
Examples: 2
Output: Natural language response
```

**What to figure out:**
- Optimal examples per task
- Temperature settings
- Response length limits
- Format specifications

**Success criteria:**
- [ ] 4 prompt templates created
- [ ] Parameters specified
- [ ] Examples included
- [ ] Format defined

---

### HOUR 2: Core Implementation

**Part 1: Ollama Manager (25 min)**

**Requirements:**

**Class: OllamaManager**

**Methods:**

**1. `__init__()`**
- Initialize ollama client
- Track loaded models
- Set default parameters

**2. `is_ollama_running()`**
- Check if Ollama service is up
- Return bool
- Log status

**3. `list_available_models()`**
- Get models pulled locally
- Return list of model names

**4. `load_model(model_name)`**
- Preload model into memory
- Track in loaded_models set
- Handle errors

**5. `chat(model, messages, options)`**
- Make Ollama API call
- Handle errors with retry
- Log request/response
- Return parsed result

**6. `count_tokens(text)`**
- Estimate tokens (chars / 4)
- Return approximate count

**Features:**
- Retry logic (3 attempts)
- Connection error handling
- Model not found handling
- Response validation
- Logging

**What to figure out:**
- How to check Ollama status
- Connection error detection
- Retry strategy
- Logging approach
- Error message design

**Success criteria:**
- [ ] OllamaManager class implemented
- [ ] All methods working
- [ ] Error handling comprehensive
- [ ] Logging in place
- [ ] Tested with 2 models

---

**Part 2: Transaction Categorization (20 min)**

**Requirements:**

**Function: `categorize_transaction(description)`**

**Implementation:**
1. Load categorization prompt template
2. Insert transaction description
3. Select model: llama3.2:3b, temp=0
4. Call Ollama via manager
5. Parse response
6. Extract category, confidence
7. Return structured result

**Prompt (Complete):**
```
You are a transaction categorizer.

Categories: Food, Transport, Shopping, Entertainment, Bills, Healthcare, Travel, Other

Output format:
Category: [name]
Confidence: [0-100]

Examples:
Input: SHELL GAS STATION $45
Output:
Category: Transport
Confidence: 95

Input: NETFLIX.COM $15.99
Output:
Category: Entertainment
Confidence: 98

Input: CVS PHARMACY $32.10
Output:
Category: Healthcare
Confidence: 90

Input: UBER RIDE $67
Output:
Category: Transport
Confidence: 95

Input: WHOLE FOODS $156.43
Output:
Category: Food
Confidence: 98

Categorize:
Input: {transaction_description}
Output:
```

**Error Handling:**
- Ollama not running → Return error + instructions
- Parse failure → Return "Other" with low confidence
- Timeout → Retry once, then fail gracefully

**What to figure out:**
- Response parsing (extract category/confidence)
- Default behavior on errors
- Validation of category names
- Handling low confidence (<50%)

**Success criteria:**
- [ ] Function implemented
- [ ] Tested with 10 merchants
- [ ] >85% accuracy
- [ ] Parse working reliably
- [ ] Errors handled

---

**Part 3: Fraud Analysis (15 min)**

**Requirements:**

**Function: `analyze_fraud(transaction, customer_profile)`**

**Implementation:**
1. Load fraud prompt template
2. Insert transaction + profile
3. Select model: mistral:7b, temp=0.3
4. Call Ollama
5. Parse: risk, score, factors, recommendation
6. Return structured result

**Prompt (Complete):**
```
You are a fraud analyst.

Check these factors:
1. Amount vs customer average
2. Merchant location vs customer location
3. Transaction time (unusual hours?)
4. Merchant category (first time?)
5. Velocity (multiple quick transactions?)

Output format:
Risk: [Low/Medium/High/Critical]
Score: [0-100]
Factors: [list]
Recommend: [Approve/Review/Decline]

Example 1:
Transaction: $5000 electronics, 3 AM, Nigeria
Customer: Avg $50, USA, never electronics
Output:
Risk: Critical
Score: 95
Factors: Amount 100x typical, High-risk country, Unusual time, New category
Recommend: Decline

Example 2:
Transaction: $35 restaurant, 7 PM, customer's city
Customer: Avg $40, regular dining category
Output:
Risk: Low
Score: 5
Factors: Normal amount, Local, Expected time, Regular category
Recommend: Approve

Analyze:
Transaction: {transaction_details}
Customer: {customer_profile}
Output:
```

**What to figure out:**
- How to structure transaction + profile in prompt
- Parse multi-line factors
- Risk level mapping
- When Mistral 7B is worth the speed trade-off

**Success criteria:**
- [ ] Function implemented
- [ ] Tested with 5 scenarios
- [ ] Correctly identifies clear fraud
- [ ] Handles legitimate transactions
- [ ] Structured output parsing

---

### HOUR 3: Testing & Optimization

**Part 1: Accuracy Testing (30 min)**

**Categorization Test (20 transactions):**
1. STARBUCKS $5.50 → Food
2. AMAZON $127.99 → Shopping
3. SHELL GAS $45 → Transport
4. NETFLIX $15.99 → Entertainment
5. CVS PHARMACY $32.10 → Healthcare
6. UBER $67 → Transport
7. WHOLE FOODS $156.43 → Food
8. SPOTIFY $9.99 → Entertainment
9. DENTIST $40 → Healthcare
10. ELECTRIC BILL $128.50 → Bills
11. APPLE.COM $99.99 → Shopping
12. MCDONALD'S $12.50 → Food
13. LYFT RIDE $42 → Transport
14. HULU $14.99 → Entertainment
15. WALGREENS $28 → Healthcare
16. UNKNOWN_MERCH $50 → ? (test edge case)
17. 123456 $100 → ? (test garbage input)
18. @#$%^ $5 → ? (test special chars)
19. Very long merchant name... (200 chars) → ?
20. MÚLTIPLÉ SPËCIÅL ÇHÅRS → ? (test unicode)

**Fraud Test (10 scenarios):**
1. Clear fraud (high amount, bad location, odd time)
2. Clear legitimate (normal amount, local, expected time)
3. Borderline (slightly unusual, needs review)
4. Legitimate travel (different location, has context)
5. Velocity pattern (multiple in short time)
6. Low-value fraud ($5 test transaction)
7. High-value legitimate (customer traveling)
8. New merchant category (first time luxury)
9. Geographic anomaly (customer location jumped)
10. Time pattern (consistent odd-hour purchases)

**Metrics to Calculate:**
- Accuracy: Correct predictions / Total
- Precision per category
- False positive rate (legitimate flagged as fraud)
- False negative rate (fraud missed)
- Average response time
- Memory usage

**What to figure out:**
- Ground truth dataset creation
- Accuracy measurement methodology
- When accuracy is "good enough"
- Error analysis approach

**Success criteria:**
- [ ] 20 categorization tests complete
- [ ] 10 fraud scenarios tested
- [ ] Accuracy >85% for categorization
- [ ] Fraud detection >85% correct
- [ ] Edge cases handled
- [ ] Metrics documented

---

**Part 2: Performance Optimization (20 min)**

**Current Baseline:**
- Categorization: ~2s (llama3.2:3b)
- Fraud: ~5s (mistral:7b)
- Memory: ~4GB (llama) + ~8GB (mistral) = 12GB

**Optimization 1: Model Preloading**
```python
# Load models at startup
manager.load_model('llama3.2:3b')
# First request: 2s
# Subsequent: 1.5s (already loaded)
```

**Optimization 2: Prompt Compression**
- Remove unnecessary words from system prompts
- Reduce examples from 5 to 3
- Shorter = faster processing
- Target: -0.3s per request

**Optimization 3: Response Length Limits**
```python
options = {
    'num_predict': 50,  # Strict limit for categorization
    'stop': ['\n\n']     # Stop at double newline
}
# Prevents long rambling responses
```

**Optimization 4: Batch Processing (If Needed)**
- Process 10 categorizations sequentially
- Keep model in memory
- Amortize load time
- Target: 15s for 10 (1.5s each)

**What to figure out:**
- When to preload models
- When to unload to save memory
- Minimum prompt length for quality
- Batch vs real-time trade-off

**Success criteria:**
- [ ] Models preloaded at startup
- [ ] Prompts compressed 20%
- [ ] Response length limited
- [ ] Latency reduced 10-20%
- [ ] Memory usage monitored

---

**Part 3: Error Recovery (10 min)**

**Error Scenarios:**

**1. Ollama Not Running**
```python
try:
    response = manager.chat(...)
except ConnectionError:
    return {
        'error': 'Ollama not running',
        'message': 'Start Ollama with: ollama serve',
        'fallback': 'Other'  # Safe default
    }
```

**2. Model Not Pulled**
```python
if model not in manager.list_available_models():
    return {
        'error': 'Model not found',
        'message': f'Pull model: ollama pull {model}',
        'available': manager.list_available_models()
    }
```

**3. Response Parse Failure**
```python
try:
    category = parse_category(response)
except ValueError:
    # Return safe default
    return {
        'category': 'Other',
        'confidence': 50,
        'note': 'Parse failed, default category'
    }
```

**4. Timeout/Slow Response**
```python
# Set timeout (30s)
try:
    response = manager.chat(..., timeout=30)
except TimeoutError:
    return {'error': 'Request timed out', 'retry': True}
```

**What to figure out:**
- Appropriate timeouts
- Fallback strategies
- Error message design
- When to retry vs fail

**Success criteria:**
- [ ] All 4 error types handled
- [ ] User-friendly error messages
- [ ] Fallback values defined
- [ ] No crashes on errors

---

### HOUR 4 (Optional): Documentation

**Part 1: README Creation (30 min)**

**README.md Structure:**
```markdown
# Payment Q&A System (Ollama)

Local LLM-powered transaction analysis system.

## Features
- ✅ Transaction categorization (>85% accuracy)
- ✅ Fraud detection (>85% accuracy)
- ✅ Customer support Q&A
- ✅ 100% free (no API costs)
- ✅ Complete privacy (data stays local)
- ✅ Works offline

## Performance
- Categorization: <2s (llama3.2:3b)
- Fraud analysis: <5s (mistral:7b)
- Memory: ~12GB RAM
- Storage: ~8GB models

## Prerequisites
- Python 3.8+
- Ollama installed
- 12GB+ RAM
- 8GB disk space

## Quick Start
1. Install Ollama: https://ollama.com
2. Pull models:
   ```
   ollama pull llama3.2:3b
   ollama pull mistral:7b
   ```
3. Install dependencies:
   ```
   pip install ollama
   ```
4. Run:
   ```
   python main.py
   ```

## Architecture
[Include component diagram]

## Models Used
- llama3.2:3b - Fast categorization
- mistral:7b - Quality fraud analysis

## Testing
- Categorization: 20 tests, 87% accuracy
- Fraud: 10 scenarios, 90% accuracy

## Troubleshooting
[Common issues and solutions]

## Why Local LLMs?
- $0 cost (vs $50-200/month API)
- Complete privacy
- No internet required
- Unlimited requests
- Full control
```

**What to document:**
- Installation steps
- Model requirements
- Performance metrics
- Troubleshooting
- Limitations

**Success criteria:**
- [ ] README comprehensive
- [ ] Installation clear
- [ ] Performance documented
- [ ] Examples included

---

**Part 2: Code Documentation (15 min)**

**Docstrings:**
```python
def categorize_transaction(description: str) -> dict:
    """
    Categorize payment transaction using local LLM.
    
    Args:
        description: Raw transaction description
                    Example: "STARBUCKS $5.50"
    
    Returns:
        dict: {
            'category': str,      # One of 8 categories
            'confidence': int,    # 0-100
            'model': str,         # Model used
            'time_ms': int        # Response time
        }
    
    Raises:
        ConnectionError: If Ollama not running
        ValueError: If invalid input
    
    Example:
        >>> categorize_transaction("UBER $45")
        {'category': 'Transport', 'confidence': 95}
    """
```

**Success criteria:**
- [ ] All functions documented
- [ ] Parameters explained
- [ ] Return types specified
- [ ] Examples included

---

**Part 3: Comparison Guide (15 min)**

**Create: OLLAMA_VS_OPENAI.md**

**Comparison:**
```markdown
# Ollama vs OpenAI API

## Cost
- Ollama: $0 forever
- OpenAI: ~$50-200/month for this system

## Performance
- Ollama: 1-5s per request (local CPU/GPU)
- OpenAI: 0.5-2s per request (cloud GPUs)

## Quality
- Ollama (llama3.2): ~85% accuracy
- OpenAI (gpt-3.5): ~95% accuracy

## Privacy
- Ollama: 100% local, no data sent
- OpenAI: Data sent to cloud

## When to use Ollama:
- Learning (unlimited free practice)
- Privacy-sensitive applications
- Offline requirements
- Budget constraints
- Good enough quality (>85%)

## When to use OpenAI:
- Need >95% accuracy
- Speed critical (<1s)
- Complex reasoning required
- Production at scale

## Hybrid Approach:
- Development: Ollama (free testing)
- Production: OpenAI (pay for quality)
```

**Success criteria:**
- [ ] Comparison documented
- [ ] Trade-offs explained
- [ ] Use cases clear
- [ ] Hybrid approach described

---

### Day 6 Deliverables

**System Built:**
- [ ] Ollama Manager class
- [ ] Transaction categorization (>85%)
- [ ] Fraud analysis (>85%)
- [ ] Conversation manager
- [ ] Error handling comprehensive

**Testing:**
- [ ] 20 categorization tests
- [ ] 10 fraud scenarios
- [ ] Edge cases covered
- [ ] Performance measured

**Optimization:**
- [ ] Models preloaded
- [ ] Prompts compressed
- [ ] Latency optimized
- [ ] Memory monitored

**Documentation:**
- [ ] README complete
- [ ] Code documented
- [ ] Comparison guide
- [ ] Troubleshooting included

**Performance Achieved:**
- [ ] Categorization: <2s, >85% accuracy
- [ ] Fraud: <5s, >85% accuracy
- [ ] Memory: <12GB
- [ ] Cost: $0
- [ ] Errors handled gracefully

---

## DAY 7 (Sunday Dec 22): Advanced Testing & Polish - 180 minutes

### Goal
Comprehensive testing, performance tuning, and production-ready documentation.

### Schedule - 180 minutes total

**HOUR 1: Comprehensive Testing (60 min)**
**HOUR 2: Performance Tuning (60 min)**
**HOUR 3: Final Polish & Docs (60 min)**

---

### HOUR 1: Comprehensive Testing

**Part 1: Extended Accuracy Test (25 min)**

**Create 50-Transaction Test Set:**

**Categories Distribution:**
- Food & Dining: 10 transactions
- Transportation: 8 transactions
- Shopping: 10 transactions
- Entertainment: 5 transactions
- Bills & Utilities: 5 transactions
- Healthcare: 5 transactions
- Travel: 4 transactions
- Other/Edge Cases: 3 transactions

**Include:**
- Common merchants (Starbucks, Amazon, Uber)
- Unknown merchants
- Misspellings (WALLMART, MACDONALDS)
- Special characters
- Very long names
- Non-English characters
- Ambiguous categories

**Ground Truth Required:**
- Manual labeling of all 50
- Expected category for each
- Confidence threshold (>70% = accept)

**Metrics to Calculate:**
```python
correct = 0
total = 50

for transaction in test_set:
    result = categorize_transaction(transaction)
    if result['category'] == transaction['expected']:
        correct += 1

accuracy = correct / total * 100
print(f"Accuracy: {accuracy}%")

# Also calculate per-category accuracy
# Identify which categories struggle
```

**What to figure out:**
- Which categories most accurate
- Common failure patterns
- Edge cases needing attention
- When to improve prompts vs accept limits

**Success criteria:**
- [ ] 50-transaction test set created
- [ ] All manually labeled
- [ ] Tested through system
- [ ] Accuracy calculated (target: >85%)
- [ ] Per-category metrics
- [ ] Failure analysis done

---

**Part 2: Stress Testing (20 min)**

**Volume Test:**
```python
import time

# Test 100 transactions
start = time.time()
results = []

for i in range(100):
    result = categorize_transaction(f"TEST MERCHANT #{i} $50")
    results.append(result)

end = time.time()
total_time = end - start
avg_time = total_time / 100

print(f"Total: {total_time}s")
print(f"Average: {avg_time}s per transaction")
print(f"Throughput: {100/total_time} trans/sec")
```

**Measure:**
- Total time for 100
- Average per transaction
- Memory usage during run
- CPU/GPU utilization
- Any errors or timeouts

**Concurrency Test:**
```python
import concurrent.futures

def process_batch(transactions):
    return [categorize_transaction(t) for t in transactions]

# Test sequential vs concurrent
# (Note: Ollama handles one at a time usually)
```

**What to figure out:**
- Sequential processing speed
- Memory stability over 100+ requests
- Model stays loaded
- Error rate over volume
- Performance degradation

**Success criteria:**
- [ ] Processed 100 transactions
- [ ] Average time <2s
- [ ] No memory leaks
- [ ] No errors
- [ ] Performance stable

---

**Part 3: Edge Case Validation (15 min)**

**Edge Cases:**

**1. Empty/Invalid Input**
```python
test_cases = [
    "",
    "   ",
    None,
    "$0",
    "UNKNOWN",
    "123456789",
    "!@#$%^&*()",
]

for case in test_cases:
    result = categorize_transaction(case)
    # Should: Not crash, return default
```

**2. Extreme Length**
```python
very_long = "MERCHANT " * 500  # 4000+ chars
result = categorize_transaction(very_long)
# Should: Handle gracefully, truncate if needed
```

**3. Multiple Languages**
```python
test_cases = [
    "東京レストラン $50",  # Japanese
    "CAFÉ MÜNCHEN $30",   # German
    "МОСКВА МАГАЗИН $40", # Russian
]
# Should: Handle or return "Other"
```

**4. Model Switching**
```python
# Test rapid model changes
categorize_transaction("TEST 1")  # llama3.2
analyze_fraud(txn, profile)       # mistral
categorize_transaction("TEST 2")  # llama3.2
# Should: Switch cleanly, no errors
```

**What to figure out:**
- Graceful degradation
- Default behaviors
- Error messages
- When to give up vs retry

**Success criteria:**
- [ ] All edge cases tested
- [ ] No crashes
- [ ] Reasonable defaults
- [ ] Error messages helpful

---

### HOUR 2: Performance Tuning

**Part 1: Latency Optimization (25 min)**

**Current Baseline:**
- Categorization: ~2s
- Fraud: ~5s

**Optimization Attempts:**

**1. Prompt Length Reduction**
```python
# Before: 800 tokens
# After: 400 tokens (remove verbose parts)
# Measure improvement
```

**2. num_predict Tuning**
```python
# Test different limits
for limit in [30, 50, 100]:
    # Measure: time vs quality trade-off
```

**3. Temperature = 0 (Caching Benefit)**
```python
# Same input always produces same output
# Can cache results
# Measure cache hit benefits
```

**4. Model Warm-up**
```python
# Preload by running dummy request
manager.chat(model='llama3.2:3b', 
             messages=[{'role': 'user', 'content': 'Hi'}])
# Subsequent requests faster
```

**Measure P50, P95, P99:**
```python
import numpy as np

times = []
for i in range(20):
    start = time.time()
    categorize_transaction(f"TEST {i}")
    times.append(time.time() - start)

print(f"P50: {np.percentile(times, 50)}s")
print(f"P95: {np.percentile(times, 95)}s")
print(f"P99: {np.percentile(times, 99)}s")
```

**What to figure out:**
- Which optimization has most impact
- Quality vs speed trade-off
- Acceptable latency levels
- When optimizations diminishing returns

**Success criteria:**
- [ ] Baseline measured
- [ ] 4 optimizations attempted
- [ ] Impact quantified each
- [ ] P50/P95/P99 calculated
- [ ] Best settings identified

---

**Part 2: Memory Optimization (20 min)**

**Current Memory Usage:**
- llama3.2:3b: ~4GB
- mistral:7b: ~8GB
- Total: ~12GB

**Optimization Strategies:**

**1. Model Unloading**
```python
# After inactivity, unload model
import psutil

def check_memory():
    return psutil.virtual_memory().percent

if check_memory() > 80:
    # Unload least recently used model
    manager.unload_model('mistral:7b')
```

**2. Selective Loading**
```python
# Load models only when needed
# Don't preload all at startup
# Trade: First request slower

def categorize_transaction(desc):
    if 'llama3.2:3b' not in manager.loaded_models:
        manager.load_model('llama3.2:3b')
    # Then proceed
```

**3. Context Window Reduction**
```python
# Reduce num_ctx from 2048 to 1024
# Less memory per request
# Test if quality acceptable
```

**Monitor Memory:**
```python
import psutil

before = psutil.virtual_memory().used
# Run operation
after = psutil.virtual_memory().used

print(f"Memory used: {(after - before) / 1024 / 1024}MB")
```

**What to figure out:**
- When to unload models
- Memory vs convenience trade-off
- Minimum context window for quality
- Monitoring approach

**Success criteria:**
- [ ] Memory usage measured
- [ ] Unloading strategy implemented
- [ ] Tested selective loading
- [ ] Monitored peak memory
- [ ] Reduced usage if possible

---

**Part 3: Quality Improvements (15 min)**

**Identify Weak Points:**
```python
# Analyze failures from Hour 1 testing
failures = [t for t in test_results if t['correct'] == False]

# Group by category
from collections import Counter
failure_categories = Counter([f['expected'] for f in failures])

print("Most failures in:", failure_categories.most_common(3))
```

**Improvement Strategies:**

**1. Add More Examples**
- Weak category: Add 2-3 more examples
- Test improvement

**2. Clarify Instructions**
- Ambiguous category: Add definition
- Test improvement

**3. Try Different Model**
- Phi3 vs Llama3.2 for categorization
- Measure quality difference

**4. Adjust Temperature**
- Test 0 vs 0.1 vs 0.3
- Impact on consistency

**A/B Testing:**
```python
# Test two prompt versions
results_v1 = test_with_prompt(prompt_v1, test_set)
results_v2 = test_with_prompt(prompt_v2, test_set)

print(f"V1 accuracy: {results_v1['accuracy']}%")
print(f"V2 accuracy: {results_v2['accuracy']}%")
```

**What to figure out:**
- Most impactful improvements
- Diminishing returns point
- Cost of quality (latency, memory)
- When "good enough"

**Success criteria:**
- [ ] Failures analyzed
- [ ] 2-3 improvements tried
- [ ] Impact measured each
- [ ] Best version identified
- [ ] Accuracy improved 2-5%

---

### HOUR 3: Final Polish & Documentation

**Part 1: Code Cleanup (20 min)**

**Tasks:**

**1. Remove Dead Code**
- Delete unused functions
- Remove commented code
- Clean imports

**2. Consistent Naming**
- Functions: snake_case
- Classes: PascalCase
- Constants: UPPER_CASE

**3. Add Type Hints**
```python
def categorize_transaction(description: str) -> dict:
    ...

def analyze_fraud(
    transaction: dict,
    profile: dict
) -> dict:
    ...
```

**4. Docstrings**
- All public functions
- Include examples
- Specify return types

**5. Error Messages**
- User-friendly
- Actionable
- Include context

**What to figure out:**
- Consistent code style
- Documentation standards
- Error message format

**Success criteria:**
- [ ] No dead code
- [ ] Naming consistent
- [ ] Type hints added
- [ ] Docstrings complete
- [ ] Error messages clear

---

**Part 2: Final Documentation (25 min)**

**README.md Updates:**
```markdown
# Payment Q&A System with Ollama

## Performance Metrics (Week 5 Final)

### Accuracy
- Transaction Categorization: 87% (50-test set)
- Fraud Detection: 90% (10-scenario set)
- Edge Cases: 100% handled gracefully

### Speed
- Categorization: 1.8s average (P95: 2.3s)
- Fraud Analysis: 4.5s average (P95: 6.2s)
- Throughput: 0.5 trans/sec (sequential)

### Resource Usage
- Memory: 8GB active, 12GB peak
- Storage: 8GB (models)
- CPU: 40-60% during inference
- Cost: $0 (completely free)

## Limitations
- Quality: 85-90% (vs 95%+ with GPT-4)
- Speed: 2-5s (vs 0.5-1s with cloud API)
- Local only: Needs Ollama running
- Sequential: One request at a time

## When to Use This
✅ Learning AI/ML (unlimited free practice)
✅ Privacy-critical applications
✅ Offline requirements
✅ Budget constraints
✅ Prototyping before cloud

## When to Use OpenAI API Instead
✅ Need >95% accuracy
✅ Need <1s latency
✅ Complex reasoning required
✅ Production at scale

## Week 5 Learning Outcomes
- ✅ LLM fundamentals mastered
- ✅ Local LLM deployment
- ✅ Prompt engineering
- ✅ Production system built
- ✅ Testing methodology
- ✅ Performance optimization
```

**Create: LESSONS_LEARNED.md**
```markdown
# Week 5: Lessons Learned

## Key Insights

### 1. Local LLMs vs Cloud APIs
- Quality gap: ~10% (87% vs 95-97%)
- Speed gap: 4x slower (2s vs 0.5s)
- Cost: $0 vs $50-200/month
- For learning: Local is perfect

### 2. Prompt Engineering
- Examples critical for local LLMs
- Need 3-5 examples minimum
- Format instructions must be explicit
- Simpler language than GPT

### 3. Model Selection
- 3B models: Fast, good for simple tasks
- 7B models: Better reasoning, worth wait
- Right model for right task matters

### 4. Performance Optimization
- Preloading saves 0.5s per request
- Prompt compression: 20% faster
- Context limits more important
- Memory management crucial

### 5. Error Handling
- Ollama connection failures common
- Parsing failures need defaults
- Timeouts must be handled
- User-friendly errors critical

## Challenges Faced

1. **Accuracy Lower Than Expected**
   - Solution: More examples, better prompts
   - Accepted: 85% good enough for learning

2. **Speed Slower Than OpenAI**
   - Solution: Optimized prompts, preloading
   - Accepted: 2s acceptable for development

3. **Memory Usage High**
   - Solution: Selective loading, unloading
   - Accepted: 12GB reasonable for local

## What Worked Well

- ✅ Unlimited experimentation (free)
- ✅ Complete privacy (local)
- ✅ Fast iteration (no API delays)
- ✅ Good enough quality (85-90%)
- ✅ Valuable learning experience

## What Would I Change

- ⚠️ Start with smaller test sets
- ⚠️ Set realistic expectations (not GPT-4)
- ⚠️ More time on prompt optimization
- ⚠️ Better error handling earlier
- ⚠️ Memory monitoring from start

## Preparing for Week 6+

Week 6 will dive deeper into prompt engineering:
- Advanced techniques (CoT, ReAct)
- Meta-prompting
- Optimization frameworks
- A/B testing methodology

Week 7-11 will use Ollama for RAG:
- Already have LLM running locally
- Will add vector database
- Combine retrieval + generation
- Complete RAG system
```

**Success criteria:**
- [ ] README updated with metrics
- [ ] Lessons learned documented
- [ ] Limitations clear
- [ ] Use cases defined
- [ ] Next steps outlined

---

**Part 3: GitHub Preparation (15 min)**

**Repository Structure:**
```
payment-qa-ollama/
├── README.md
├── LESSONS_LEARNED.md
├── OLLAMA_VS_OPENAI.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── ollama_manager.py
│   ├── categorization.py
│   ├── fraud_detection.py
│   ├── conversation_manager.py
│   └── prompts/
│       ├── categorization.txt
│       ├── fraud_analysis.txt
│       └── support.txt
├── tests/
│   ├── test_categorization.py
│   ├── test_fraud.py
│   ├── test_edge_cases.py
│   └── test_data/
│       └── 50_transactions.json
├── examples/
│   ├── demo.py
│   └── demo.ipynb
└── docs/
    ├── ARCHITECTURE.md
    └── PERFORMANCE.md
```

**requirements.txt:**
```
ollama>=0.1.0
psutil>=5.9.0
```

**. gitignore:**
```
__pycache__/
*.pyc
.venv/
venv/
.env
.DS_Store
*.ipynb_checkpoints
```

**Success criteria:**
- [ ] Directory structure created
- [ ] All files in place
- [ ] requirements.txt complete
- [ ] .gitignore configured
- [ ] Ready to commit

---

### Day 7 Deliverables

**Testing Complete:**
- [ ] 50-transaction accuracy test (>85%)
- [ ] 100-transaction stress test
- [ ] Edge cases validated
- [ ] P50/P95/P99 latency measured
- [ ] Memory usage profiled

**Optimization Complete:**
- [ ] Latency reduced 10-20%
- [ ] Memory managed effectively
- [ ] Quality improved 2-5%
- [ ] Best settings documented

**Documentation Complete:**
- [ ] README with final metrics
- [ ] Lessons learned documented
- [ ] Code fully commented
- [ ] GitHub structure ready

**Production Ready:**
- [ ] All tests passing
- [ ] Code clean and organized
- [ ] Error handling comprehensive
- [ ] Performance acceptable
- [ ] Documentation complete
- [ ] GitHub ready to push

---

## WEEK 5 COMPLETE - OLLAMA VERSION

### What You Built

**Production System:**
- Transaction categorization (87% accuracy, <2s)
- Fraud detection (90% accuracy, <5s)
- Customer support Q&A
- Conversation management
- Comprehensive error handling

**Performance:**
- Cost: $0 (completely free)
- Latency: 2-5s (acceptable for learning)
- Memory: ~12GB
- Throughput: 0.5 trans/sec
- Reliability: >99%

**Testing:**
- 50-transaction accuracy suite
- 10 fraud scenarios
- Edge case coverage
- Stress testing (100 requests)
- Performance profiling

### Skills Gained

**Technical:**
- Local LLM deployment (Ollama)
- Model selection strategy
- Prompt optimization for small models
- Performance tuning
- Memory management
- Error handling patterns

**System Design:**
- Model routing
- Resource management
- Caching strategies
- Testing methodologies
- Documentation practices

**Domain:**
- Payment transaction processing
- Fraud detection patterns
- Customer support automation
- Fintech applications

### Key Learnings

**Local LLMs:**
- 85-90% quality (vs 95%+ cloud)
- Free and unlimited
- Privacy preserved
- Good for learning
- Production may need cloud

**Prompt Engineering:**
- Examples critical (3-5 minimum)
- Explicit instructions needed
- Simple language better
- Format matters more
- Iteration essential

**Performance:**
- Model size impacts speed
- Preloading saves time
- Memory is limiting factor
- Optimization yields 10-20% gains

### Week 5 Complete!

**Time Invested:** ~13 hours
**System Built:** ✅ Production-ready
**Tests Passing:** ✅ All
**Documentation:** ✅ Complete
**GitHub Ready:** ✅ Yes

**Next:** Week 6 - Advanced Prompt Engineering
- Meta-prompting strategies
- Chain-of-thought mastery
- Self-consistency methods
- ReAct patterns
- A/B testing frameworks

**Phase 1 Prep:**
- Week 9 already uses Ollama ✅
- LLM skills transferable to RAG ✅
- Prompt engineering applies to retrieval ✅
- System design patterns reusable ✅

---

## End of Week 5 Learning Guide (Ollama Version)

**Congratulations! You've mastered LLM fundamentals with local models and built a production-ready payment Q&A system - all for free! 🎉**

