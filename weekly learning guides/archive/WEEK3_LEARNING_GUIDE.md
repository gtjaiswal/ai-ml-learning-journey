# Week 3 Learning Schedule - LLMs & OpenAI API

## Overview

A comprehensive 7-day learning plan covering Large Language Models fundamentals, OpenAI API, tokenization, prompt engineering, and building AI-powered applications. Total commitment: ~12 hours.

---

## Week Schedule

| Day | Date | Topic | Time |
|-----|------|-------|------|
| Mon | Dec 1 | LLM Fundamentals - Karpathy Lecture | 1.5h |
| Tue | Dec 2 | OpenAI API Setup & First Calls | 1.5h |
| Wed | Dec 3 | Tokenization Deep Dive | 1h |
| Thu | Dec 4 | Prompt Engineering Fundamentals | 1h |
| Fri | Dec 5 | Advanced Prompting Techniques | 1h |
| Sat | Dec 6 | **Build Transaction Categorizer** | 3h |
| Sun | Dec 7 | **Build Smart Fraud Detector** | 3h |

**Total Week 3:** ~12 hours

---

## Day 1: LLM Fundamentals - Karpathy Lecture

### Primary Video Resources

#### Andrej Karpathy - Introduction to Large Language Models

**Video: "Intro to Large Language Models"**
- Link: https://www.youtube.com/watch?v=zjkBMFhNj_g
- Duration: 59:44
- What you'll learn: How LLMs work, training process, capabilities, limitations
- **WATCH THIS COMPLETELY** - Best introduction to LLMs

**Key Topics Covered:**
- What is an LLM?
- Neural network architecture
- Training process and data
- Inference and sampling
- Capabilities and limitations
- Safety and alignment

### Supplementary Video Resources

**Video: "State of GPT" by Andrej Karpathy**
- Link: https://www.youtube.com/watch?v=bZQun8Y4L2A
- Duration: 1:09:30
- Watch sections: 0:00-20:00 (Overview) and 40:00-55:00 (Practical tips)
- Optional: Watch full if you have extra time

### Reading Materials

**Article: "What Are Large Language Models (LLMs)?"**
- Link: https://www.nvidia.com/en-us/glossary/large-language-models/
- Duration: 10 min read
- High-level overview

**Article: "How ChatGPT Works: A Non-Technical Explanation"**
- Link: https://www.vox.com/technology/2023/4/6/23670237/chatgpt-ai-explained-language-model
- Duration: 15 min read
- For deeper understanding

**OpenAI Research: "Language Models are Few-Shot Learners" (GPT-3 Paper)**
- Link: https://arxiv.org/abs/2005.14165
- Read: Abstract and Introduction only
- Duration: 10 min
- Understand the breakthrough

### Day1's Schedule (90 minutes total)

**Option A: Full Karpathy Focus (Recommended)**

1. **Watch: Intro to LLMs** (60 min)
   - Take notes on key concepts
   - Pause when needed
   - Rewind confusing parts

2. **Read: NVIDIA LLM article** (10 min)
   - Reinforce concepts

3. **Reflection and Notes** (20 min)
   - Write summary in own words
   - List questions
   - Connect to your payments domain

**Option B: Broader Overview (If time limited)**

1. **Watch: Intro to LLMs first 30 min** (30 min)
   - Get core concepts

2. **Read: Both articles** (25 min)
   - Get multiple perspectives

3. **Watch: State of GPT sections** (15 min)
   - Practical understanding

4. **Reflection** (20 min)
   - Synthesize learning

### Key Concepts to Master

**What is an LLM?**
- Neural network trained on massive text data
- Predicts next token given context
- Emergent capabilities from scale
- Not a database, a pattern recognizer

**How LLMs Work:**
- Tokenization: Text → Numbers
- Transformer architecture: Attention mechanism
- Autoregressive generation: One token at a time
- Temperature: Controls randomness

**Training Process:**
1. Pre-training: Learn from internet text
2. Fine-tuning: Specialize on specific tasks
3. RLHF: Align with human preferences
4. Result: ChatGPT, GPT-4, etc.

**Key Capabilities:**
- Text generation and completion
- Question answering
- Summarization
- Translation
- Code generation
- Reasoning (to an extent)

**Key Limitations:**
- No real-time knowledge (knowledge cutoff)
- Can hallucinate (make up facts)
- No true understanding
- Context window limits
- Biases from training data
- Cannot learn from conversations

### Connection to Your Domain

**How LLMs Apply to Payments/Banking:**

1. **Transaction Categorization**
   - "Coffee at Starbucks" → "Food & Dining"
   - Natural language understanding

2. **Fraud Detection**
   - Analyze transaction descriptions
   - Identify suspicious patterns
   - Generate risk assessments

3. **Customer Support**
   - Answer payment questions
   - Explain transaction details
   - Handle disputes

4. **Document Processing**
   - Extract data from invoices
   - Process receipts
   - Understand contracts

### Reflection Questions

Write detailed answers:

1. **What is an LLM in your own words?**
   - How is it different from traditional software?

2. **How does an LLM generate text?**
   - What role does "next token prediction" play?

3. **What are 3 capabilities and 3 limitations?**
   - Why do limitations matter?

4. **How can LLMs help in payment processing?**
   - Give 3 specific examples

5. **What concerns you about using LLMs in finance?**
   - Security, accuracy, compliance?

### End of Day1 Checklist

- [ ] Watched Karpathy's "Intro to LLMs" (at least 45 min)
- [ ] Read NVIDIA article on LLMs
- [ ] Read additional article or GPT-3 paper abstract
- [ ] Understand: tokenization, attention, autoregressive generation
- [ ] Can explain: How LLMs work in simple terms
- [ ] Wrote reflection answers (5 questions)
- [ ] Listed 3 payment/banking use cases
- [ ] Identified key limitations and concerns
- [ ] Spent approximately 90 minutes

---

## Day 2: OpenAI API Setup & First Calls

### Primary Resources

**OpenAI Documentation:**
- Main API Docs: https://platform.openai.com/docs/introduction
- Quickstart Guide: https://platform.openai.com/docs/quickstart
- API Reference: https://platform.openai.com/docs/api-reference

**OpenAI Cookbook (GitHub):**
- Link: https://github.com/openai/openai-cookbook
- Browse examples
- Payment processing examples if available

### Video Resources

**Video: "OpenAI API Tutorial for Beginners"**
- Link: https://www.youtube.com/watch?v=c-g6epk3fFE
- Duration: 20:00
- Practical walkthrough

**Video: "Getting Started with OpenAI API in Python"**
- Link: https://www.youtube.com/watch?v=tLe5R60ZEE4
- Duration: 15:00
- Hands-on examples

### Reading Materials

**Article: "OpenAI API Pricing Explained"**
- Link: https://openai.com/api/pricing/
- Duration: 10 min
- Understand costs before building

**Article: "Best Practices for OpenAI API"**
- Link: https://platform.openai.com/docs/guides/production-best-practices
- Duration: 15 min
- Important for production use

### Day2's Schedule (90 minutes total)

1. **Setup OpenAI Account** (15 min)
   - Create account: https://platform.openai.com/signup
   - Add payment method
   - Get API key
   - Set usage limits ($5-10 for learning)

2. **Install and Configure** (10 min)
   - Install OpenAI Python library
   - Set up environment variables
   - Test installation

3. **Watch Tutorial Video** (20 min)
   - See practical examples
   - Note key patterns

4. **Read API Documentation** (15 min)
   - Chat completions endpoint
   - Parameters: model, messages, temperature, max_tokens
   - Response format

5. **Hands-On Exercises** (25 min)
   - Complete 5 exercises below
   - Test each before moving on

6. **Reflection** (5 min)
   - Note what worked, what didn't

### Setup Instructions

**Step 1: Install OpenAI Library**
```bash
pip install openai python-dotenv
```

**Step 2: Create .env file**
```
OPENAI_API_KEY=your_api_key_here
```

**Step 3: Basic Setup Code**
```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### Hands-On Exercises

**Exercise 1: Your First API Call**

**Requirements:**
- Make a chat completion request
- Use GPT-4o-mini model (cheaper for learning)
- Simple prompt: "Explain what an API is in one sentence"
- Print the response

**What to figure out:**
- How to structure messages
- How to extract response text
- How to handle the response object

**Success criteria:**
- Gets valid response
- Response is printed clearly
- No errors

**Key concepts:**
- `messages` list structure
- `role`: system, user, assistant
- `content`: the actual text
- Response structure

---

**Exercise 2: System Prompts**

**Requirements:**
- Create a transaction categorizer
- System prompt: "You are a financial expert who categorizes transactions into: Food, Transport, Shopping, Bills, Entertainment, Healthcare, or Other."
- User prompt: "Coffee at Starbucks $5.50"
- Get category as response

**What to figure out:**
- Difference between system and user messages
- How system prompts guide behavior
- Consistency of categorization

**Test with:**
- "Uber ride to airport $45"
- "Netflix monthly subscription $15.99"
- "Dr. Smith medical consultation $150"
- "Amazon purchase - books $35"

**Success criteria:**
- Correct categories returned
- Consistent format
- Reasonable categorization

---

**Exercise 3: Temperature Control**

**Requirements:**
- Same prompt: "Write a tagline for a payment app"
- Test with different temperatures: 0, 0.5, 1.0, 1.5
- Run each 3 times
- Compare outputs

**What to figure out:**
- How temperature affects creativity
- When to use low vs high temperature
- Consistency vs creativity tradeoff

**Observations to make:**
- Temperature = 0: Same output every time?
- Temperature = 1.5: More varied outputs?
- Which is best for transaction categorization?
- Which is best for marketing copy?

---

**Exercise 4: Token Limits and Costs**

**Requirements:**
- Make same request with different max_tokens: 10, 50, 100
- Track actual tokens used (in response metadata)
- Calculate cost for each

**Pricing (as of 2024):**
- GPT-4o-mini: $0.150 per 1M input tokens, $0.600 per 1M output tokens
- GPT-4o: $2.50 per 1M input tokens, $10.00 per 1M output tokens

**What to figure out:**
- How to access usage metadata
- Input vs output tokens
- Cost implications
- When to use which model

**Calculate:**
- Cost for 1000 transaction categorizations
- With GPT-4o-mini vs GPT-4o
- Which is better for production?

---

**Exercise 5: Error Handling**

**Requirements:**
- Implement comprehensive error handling
- Test error scenarios:
  - Invalid API key
  - Rate limit (make many rapid requests)
  - Invalid model name
  - Network timeout
  - Empty prompt

**What to figure out:**
- Try/except structure for API calls
- Different error types
- How to handle gracefully
- Retry logic

**Success criteria:**
- Program doesn't crash on errors
- Meaningful error messages
- Can recover from transient errors

---

### Key API Concepts

**Chat Completions Structure:**
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7,
    max_tokens=150
)
```

**Key Parameters:**

**model:**
- gpt-4o-mini: Fast, cheap, good for most tasks
- gpt-4o: Most capable, expensive
- gpt-4-turbo: Balanced

**temperature (0-2):**
- 0: Deterministic, focused
- 0.7: Balanced (default)
- 1.5+: Creative, varied

**max_tokens:**
- Limits response length
- Affects cost
- Set appropriately

**Messages roles:**
- system: Sets behavior/context
- user: Your input
- assistant: Model's response

### Best Practices

**Cost Management:**
1. Start with GPT-4o-mini
2. Set reasonable max_tokens
3. Monitor usage dashboard
4. Set monthly spending limits

**API Key Security:**
1. Never commit to Git
2. Use environment variables
3. Use .env files
4. Add .env to .gitignore

**Error Handling:**
1. Always use try/except
2. Handle rate limits
3. Implement retries
4. Log errors properly

**Prompt Design:**
1. Clear, specific instructions
2. Use system prompts for context
3. Provide examples when needed
4. Test variations

### End of Day2 Checklist

- [ ] OpenAI account created
- [ ] API key obtained and secured
- [ ] Python library installed
- [ ] Environment variables configured
- [ ] Completed Exercise 1 (First API call)
- [ ] Completed Exercise 2 (System prompts)
- [ ] Completed Exercise 3 (Temperature)
- [ ] Completed Exercise 4 (Token limits)
- [ ] Completed Exercise 5 (Error handling)
- [ ] Understand: messages structure, roles, parameters
- [ ] Can calculate costs for API usage
- [ ] Jupyter notebook with all exercises
- [ ] Spent approximately 90 minutes

---

## Day 3: Tokenization Deep Dive

### Primary Video Resources

**Video: "Tokenization in LLMs" by Andrej Karpathy**
- Link: https://www.youtube.com/watch?v=zduSFxRajkE
- Duration: 1:58:00
- Watch sections: 0:00-30:00 (Core concepts)
- Optional: Full video if you have time

**Video: "Understanding Tokenization - Visual Explanation"**
- Link: https://www.youtube.com/watch?v=wK1N2nOBE0A
- Duration: 10:00
- Quick visual overview

### Interactive Tools

**OpenAI Tokenizer:**
- Link: https://platform.openai.com/tokenizer
- Duration: 15 min exploration
- **MUST USE** - See tokenization in action

**Tiktokenizer (Alternative):**
- Link: https://tiktokenizer.vercel.app/
- Compare different encodings

### Reading Materials

**Article: "What are Tokens?"**
- Link: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- Duration: 5 min read
- Official OpenAI explanation

**Article: "Understanding Tokenization in NLP"**
- Link: https://huggingface.co/docs/transformers/tokenizer_summary
- Duration: 15 min read
- Technical deep dive

**tiktoken GitHub Documentation:**
- Link: https://github.com/openai/tiktoken
- Duration: 10 min
- How to count tokens programmatically

### Day3's Schedule (60 minutes total)

1. **Watch: Karpathy tokenization** (30 min)
   - First 30 minutes covers essentials
   - Take notes on BPE algorithm

2. **Interactive: OpenAI Tokenizer** (15 min)
   - Test various inputs
   - See token boundaries
   - Understand token counts

3. **Read: OpenAI tokens article** (5 min)
   - Understand cost implications

4. **Hands-On Exercise** (10 min)
   - Use tiktoken library
   - Count tokens programmatically
   - Test edge cases

### Key Concepts to Master

**What is a Token?**
- Smallest unit LLMs process
- Not always a word
- Can be:
  - Whole word: "hello" = 1 token
  - Part of word: "tokenization" = 2-3 tokens
  - Single character: "🎉" = 1-2 tokens
  - Whitespace + word: " hello" = 1 token

**Why Tokenization Matters:**

1. **Cost:** Charged per token
   - Input tokens + output tokens
   - Need to estimate costs

2. **Context Window:** Limited by tokens
   - GPT-4o: 128K tokens
   - GPT-4o-mini: 128K tokens
   - Must fit: system + conversation + response

3. **Performance:** Token count affects speed
   - More tokens = slower response
   - Optimize prompts

**Byte Pair Encoding (BPE):**
- Most common tokenization algorithm
- Builds vocabulary from frequent pairs
- Balances vocabulary size and token length
- Language-agnostic

**Special Tokens:**
- <|endoftext|>: Marks document boundaries
- <|im_start|>, <|im_end|>: Chat format markers
- Usually hidden from users

### Hands-On Exercise

**Exercise: Token Counter Tool**

**Requirements:**

Build a Python function that:
1. Accepts text input
2. Counts tokens using tiktoken
3. Estimates cost for GPT-4o-mini
4. Shows token breakdown
5. Warns if approaching context limit

**Installation:**
```bash
pip install tiktoken
```

**Function Template:**
```python
import tiktoken

def analyze_tokens(text, model="gpt-4o-mini"):
    """
    Analyze token count and cost for given text
    
    Args:
        text: Input text
        model: Model name (default: gpt-4o-mini)
    
    Returns:
        dict with token_count, estimated_cost, warnings
    """
    # Your implementation here
    pass
```

**Test Cases:**

1. Simple text:
   - "Hello, world!"
   - Should be ~4 tokens

2. Transaction description:
   - "Purchase at Amazon.com for $45.99 - Order #12345 - Electronics category"
   - Count tokens, estimate cost

3. Long conversation:
   - System prompt + 10 message pairs
   - Check if within context window

4. Special characters:
   - "Payment 💰 received ✓ from user 👤"
   - See how emojis are tokenized

5. Code snippet:
   - Python function (20 lines)
   - Code often uses more tokens

**What to figure out:**
- How to load encoding for specific model
- How to count tokens
- How to handle different input types
- Context window limits

**Success criteria:**
- Accurate token counts
- Cost calculations correct
- Warnings for long inputs
- Handles edge cases

### Token Optimization Tips

**For Transaction Categorization:**

❌ **Inefficient:**
```
"You are a highly skilled financial expert with years of experience in payment processing and transaction categorization. Please carefully analyze the following transaction and provide a detailed category."
```
~30 tokens

✅ **Efficient:**
```
"Categorize transaction into: Food, Transport, Shopping, Bills, Entertainment, Healthcare, Other."
```
~15 tokens

**Savings:** 50% fewer tokens, same result!

**General Optimization:**
1. Remove filler words
2. Use abbreviations where clear
3. Avoid repetition
4. Be direct and specific
5. Use structured formats (JSON)

### Token Counting Examples

**Example 1: English Text**
```
Text: "The quick brown fox jumps over the lazy dog"
Tokens: ["The", " quick", " brown", " fox", " jumps", " over", " the", " lazy", " dog"]
Count: 9 tokens
```

**Example 2: Numbers**
```
Text: "Total: $1,234.56"
Tokens: ["Total", ":", " $", "1", ",", "234", ".", "56"]
Count: 8 tokens
Note: Numbers can be split unexpectedly!
```

**Example 3: Code**
```python
Text: "def hello():\n    print('hi')"
Tokens: ["def", " hello", "()", ":", "\n", "    ", "print", "('", "hi", "')"]
Count: ~10 tokens
Note: Whitespace counts!
```

### End of Day3 Checklist

- [ ] Watched Karpathy video (at least first 30 min)
- [ ] Used OpenAI tokenizer tool extensively
- [ ] Read OpenAI article on tokens
- [ ] Installed tiktoken library
- [ ] Built token counter function
- [ ] Tested with 5 different inputs
- [ ] Understand: BPE, token boundaries, counting
- [ ] Can estimate costs from token counts
- [ ] Know how to optimize prompts
- [ ] Understand context window implications
- [ ] Spent approximately 60 minutes

---

## Day 4: Prompt Engineering Fundamentals

### Primary Resources

**OpenAI Prompt Engineering Guide:**
- Link: https://platform.openai.com/docs/guides/prompt-engineering
- Duration: 30 min read
- **MUST READ** - Official best practices

**Anthropic Prompt Engineering Guide:**
- Link: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Duration: 20 min read
- Excellent techniques, applicable to OpenAI

### Video Resources

**Video: "Prompt Engineering Tutorial"**
- Link: https://www.youtube.com/watch?v=_ZvnD73m40o
- Duration: 15:00
- Practical examples

**Video: "ChatGPT Prompt Engineering for Developers" (DeepLearning.AI)**
- Link: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
- Duration: ~1 hour course (free)
- Optional: Watch sections 1-3

### Reading Materials

**Article: "The Prompt Engineering Guide"**
- Link: https://www.promptingguide.ai/
- Read sections: Introduction, Basic Prompting, Advanced Techniques
- Duration: 20 min

**Paper: "Chain-of-Thought Prompting" (Optional)**
- Link: https://arxiv.org/abs/2201.11903
- Read abstract and introduction
- Duration: 10 min

### Day4's Schedule (60 minutes total)

1. **Read: OpenAI Prompt Engineering Guide** (30 min)
   - Take notes on each technique
   - Note examples

2. **Read: Prompting Guide sections** (15 min)
   - Focus on basics and few-shot

3. **Hands-On Practice** (15 min)
   - Apply techniques to transaction processing
   - Test different approaches

### Core Prompting Techniques

**1. Clear Instructions**

❌ **Bad:**
```
"Look at this transaction"
```

✅ **Good:**
```
"Categorize this transaction into exactly one category: Food, Transport, Shopping, Bills, Entertainment, Healthcare, or Other. Return only the category name."
```

**Why:** Specific, unambiguous, clear output format

---

**2. Provide Context**

❌ **Bad:**
```
User: "Is this fraud?"
```

✅ **Good:**
```
System: "You are a fraud detection system. Analyze transactions for suspicious patterns."

User: "Transaction: $5000 to 'Electronics Store' at 3 AM from new device in foreign country. User's typical transaction: $50 groceries."
```

**Why:** Context helps model make better decisions

---

**3. Few-Shot Learning**

❌ **Zero-shot (no examples):**
```
"Categorize: Coffee at Starbucks"
```

✅ **Few-shot (with examples):**
```
Examples:
- "Uber to downtown" → Transport
- "Netflix subscription" → Entertainment
- "Whole Foods groceries" → Food

Now categorize: "Coffee at Starbucks"
```

**Why:** Examples guide the model's understanding

---

**4. Chain of Thought**

❌ **Direct answer:**
```
"Is this transaction fraudulent: $5000 electronics purchase?"
```

✅ **Ask for reasoning:**
```
"Analyze this transaction for fraud. First, list suspicious factors. Second, list normal factors. Third, provide risk score (0-100) with reasoning."
```

**Why:** Makes model "think" through the problem

---

**5. Specify Output Format**

❌ **Unstructured:**
```
"Analyze this transaction"
```

✅ **Structured (JSON):**
```
"Analyze transaction and return JSON:
{
  'category': '...',
  'confidence': 0.95,
  'reasoning': '...'
}"
```

**Why:** Easier to parse programmatically

---

**6. Iterative Refinement**

**Process:**
1. Start with simple prompt
2. Test on examples
3. Identify failures
4. Add specificity
5. Repeat

**Example Evolution:**

**V1:** "Categorize transaction"
- Problem: Too vague

**V2:** "Categorize into: Food, Transport, Other"
- Problem: Limited categories

**V3:** "Categorize into: Food, Transport, Shopping, Bills, Entertainment, Healthcare, Other"
- Problem: Inconsistent format

**V4:** "Categorize into exactly one: Food, Transport, Shopping, Bills, Entertainment, Healthcare, Other. Return only category name, no explanation."
- Problem: Sometimes wrong

**V5:** Add examples + "If uncertain, use 'Other'"
- ✓ Works well!

### Hands-On Exercises

**Exercise 1: Transaction Categorization**

Build a categorizer with:
- Clear system prompt
- Few-shot examples (5)
- Specific output format
- Confidence scoring

**Test with:**
1. "Starbucks coffee $5.50"
2. "Amazon Prime monthly fee"
3. "Dr. Smith consultation"
4. "Unclear merchant XYZ"

**Measure:**
- Accuracy
- Consistency (run 5 times)
- Cost (tokens used)

---

**Exercise 2: Fraud Detection Prompt**

Create prompt that:
- Takes transaction details
- User's normal pattern
- Returns risk score (0-100)
- Provides reasoning
- Suggests action

**Test scenarios:**
1. Normal: $45 grocery store, usual location
2. Suspicious: $5000 electronics, new country
3. Edge case: Large but legitimate (house down payment)

---

**Exercise 3: Prompt Comparison**

Take same task, create 3 different prompts:
1. Minimal (very short)
2. Detailed (with examples)
3. Structured (JSON output)

**Compare:**
- Which is most accurate?
- Which is most consistent?
- Which is most cost-effective?
- Which is easiest to parse?

---

### Prompt Patterns for Payments

**Pattern 1: Classification**
```
You are a transaction classifier.

Categories: [list]
Rules: [specific rules]
Examples: [2-3 examples]
Edge cases: [how to handle]

Transaction: [input]
Output format: [JSON schema]
```

**Pattern 2: Risk Assessment**
```
You are a fraud analyst.

Analyze transaction for risk factors:
1. Amount vs user's typical
2. Location vs usual locations
3. Merchant vs purchase history
4. Time of transaction
5. Device/IP information

Provide:
- Risk score (0-100)
- Key risk factors
- Recommendation (approve/decline/review)

Transaction: [input]
User profile: [normal behavior]
```

**Pattern 3: Extraction**
```
Extract information from transaction description.

Required fields:
- Merchant name
- Amount
- Category
- Location (if mentioned)
- Date/time (if mentioned)

Transaction: [input]
Output: JSON with extracted fields
```

### Best Practices

**DO:**
- Be specific and clear
- Provide examples
- Specify output format
- Test thoroughly
- Iterate and improve
- Use system prompts for context
- Ask for reasoning when needed

**DON'T:**
- Be vague or ambiguous
- Assume model knows your context
- Ignore edge cases
- Use one-size-fits-all prompts
- Forget to validate outputs
- Over-engineer (start simple)

### End of Day4 Checklist

- [ ] Read OpenAI prompt engineering guide
- [ ] Read Prompting Guide basics
- [ ] Understand: clear instructions, context, few-shot, CoT
- [ ] Completed Exercise 1 (Categorization)
- [ ] Completed Exercise 2 (Fraud detection)
- [ ] Completed Exercise 3 (Prompt comparison)
- [ ] Built 3 prompts for payment tasks
- [ ] Tested prompts with multiple examples
- [ ] Documented what works vs doesn't
- [ ] Can explain: when to use each technique
- [ ] Spent approximately 60 minutes

---

## Day 5: Advanced Prompting Techniques

### Primary Resources

**OpenAI Advanced Techniques:**
- Link: https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results
- Duration: 20 min read

**LangChain Prompt Engineering:**
- Link: https://python.langchain.com/docs/modules/model_io/prompts/
- Duration: 15 min
- Learn about prompt templates

### Video Resources

**Video: "Advanced Prompt Engineering"**
- Link: https://www.youtube.com/watch?v=T9aRN5JkmL8
- Duration: 25:00

### Reading Materials

**Article: "Prompt Injection and Security"**
- Link: https://simonwillison.net/2023/Apr/14/worst-that-can-happen/
- Duration: 10 min
- **IMPORTANT** for production systems

**Article: "Function Calling in OpenAI"**
- Link: https://platform.openai.com/docs/guides/function-calling
- Duration: 15 min
- Structured outputs

### Day5's Schedule (60 minutes total)

1. **Read: Advanced techniques** (20 min)
   - OpenAI strategies
   - Note techniques applicable to payments

2. **Read: Security article** (10 min)
   - Understand risks
   - Plan mitigations

3. **Hands-On: Function Calling** (25 min)
   - Implement structured outputs
   - Build transaction analyzer

4. **Reflection** (5 min)
   - Document learnings

### Advanced Techniques

**1. Function Calling (Structured Outputs)**

**Why:** Get reliable, parseable JSON responses

**Example:**
```python
functions = [
    {
        "name": "categorize_transaction",
        "description": "Categorize a financial transaction",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Healthcare", "Other"]
                },
                "confidence": {
                    "type": "number",
                    "description": "Confidence score 0-1"
                },
                "reasoning": {
                    "type": "string",
                    "description": "Brief explanation"
                }
            },
            "required": ["category", "confidence", "reasoning"]
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Categorize: Coffee at Starbucks"}],
    functions=functions,
    function_call={"name": "categorize_transaction"}
)
```

**Benefits:**
- Guaranteed structure
- Type safety
- No parsing errors
- Validation built-in

---

**2. Self-Consistency**

**Technique:** Run same prompt multiple times, take majority vote

**Use case:** High-stakes decisions (fraud detection)

**Example:**
```python
def fraud_check_with_consistency(transaction, n=5):
    results = []
    for _ in range(n):
        result = analyze_fraud(transaction)
        results.append(result)
    
    # Take majority vote
    return most_common(results)
```

**Benefits:**
- More reliable for critical decisions
- Reduces random errors
- Identifies uncertain cases

**Tradeoff:**
- 5x cost
- 5x latency
- Use selectively

---

**3. Prompt Chaining**

**Technique:** Break complex task into steps

**Example: Transaction Analysis Pipeline**

**Step 1:** Extract information
```
Extract merchant, amount, date from: "Starbucks 123 Main St $5.50 on 2024-12-01"
```

**Step 2:** Categorize
```
Given merchant='Starbucks', amount=5.50, categorize this transaction
```

**Step 3:** Risk assessment
```
Given category='Food', amount=5.50, assess fraud risk
