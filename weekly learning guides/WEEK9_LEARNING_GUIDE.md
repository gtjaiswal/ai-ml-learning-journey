# WEEK 9 LEARNING GUIDE: LLMs, RAG Systems & Web Interfaces

**Pre-learning for Steps 17-20 (Complete RAG System)**

**Time Investment:** 5-6 hours over the weekend before Week 9

---

## LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **Large Language Models** - How LLMs work and generate text
2. **Ollama** - Local LLM deployment and management
3. **Prompt Engineering** - Crafting effective prompts for RAG
4. **RAG Architecture** - Retrieval-Augmented Generation patterns
5. **Server-Sent Events** - Streaming responses to users
6. **Gradio** - Building web interfaces for AI applications

**Goal:** Build a production-grade conversational AI system over research papers

---

## WHAT YOU ALREADY KNOW (from Weeks 3-8)

[CHECK] **Weeks 3-4 (MOAI Weeks 1-2):**
- Docker, PostgreSQL, FastAPI fundamentals
- Airflow orchestration
- PDF parsing and data ingestion

[CHECK] **Week 7 (MOAI Week 3):**
- OpenSearch and BM25 search
- Full-text search and indexing

[CHECK] **Week 8 (MOAI Week 4):**
- Document chunking strategies
- Vector embeddings and semantic search
- Hybrid search with RRF fusion
- Jina AI embedding service

**You now have:**
- Papers stored with full text and chunks
- Hybrid search (BM25 + vector) working
- Retrieved chunks ready for LLM context
- Strong foundation for RAG

**Week 9 Focus:**
Adding the **intelligence layer**:
- Local LLM with Ollama
- RAG prompt engineering
- Streaming responses
- Web interface with Gradio
- Complete conversational AI

---

## LEARNING SCHEDULE

### **Saturday/Sunday Before Week Starts (5-6 hours)**

**Recommended pre-learning:**
- LLMs and Ollama basics (1.5 hours)
- Prompt engineering for RAG (2 hours)
- Streaming APIs and SSE (1 hour)
- Gradio framework (1.5 hours)

### **During Week (as needed)**

**Monday-Tuesday:**
- Ollama API reference (30 min)
- RAG prompt patterns (45 min)

**Wednesday-Thursday:**
- Server-Sent Events deep dive (30 min)
- Gradio components (45 min)

**Friday:**
- Review and system integration (1 hour)

---

## CORE LEARNING MODULES

### **MODULE 1: Large Language Models & Ollama** [TIME] 90 minutes

#### **1.1 LLM Fundamentals** (45 min)

**Video:**
[VIDEO] **"Intro to Large Language Models"** - Andrej Karpaty  
URL: https://www.youtube.com/watch?v=zjkBMFhNj_g  
Watch: Full video (1 hour) - focus on first 45 minutes

**Key Concepts:**

**What are LLMs:**
- Neural networks trained on massive text data
- Learn patterns, language structure, world knowledge
- Generate human-like text token by token
- Examples: GPT-4, Claude, Llama, Mistral

**How LLMs work:**
1. **Tokenization:** Text -> numbers
   ```
   "Hello world" -> [15496, 995]
   ```

2. **Transformer architecture:** Process tokens
   - Attention mechanisms (which words matter?)
   - Feed-forward layers (transform representations)
   - Multiple layers (build understanding)

3. **Next token prediction:**
   ```
   Input: "The cat sat on the"
   Model predicts: "mat" (highest probability)
   ```

**LLM Parameters:**

**Temperature (0-1):**
- Controls randomness in generation
- Low (0.1): Focused, deterministic, repeatable
- High (0.9): Creative, varied, unpredictable
- RAG typical: 0.3-0.5 (balanced)

**Top-p (nucleus sampling):**
- Controls diversity of token selection
- 0.9: Consider tokens up to 90% cumulative probability
- Prevents very unlikely tokens

**Max tokens:**
- Maximum length of generated response
- Includes input + output tokens
- Typical: 500-2000 for RAG

**Reading:**
[BOOK] **"What are Large Language Models?"** - AWS  
URL: https://aws.amazon.com/what-is/large-language-model/  
Read: Complete overview (15 min)

#### **1.2 Ollama for Local LLMs** (45 min)

**Video:**
[VIDEO] **"Run LLMs Locally with Ollama"** - NetworkChuck  
URL: https://www.youtube.com/watch?v=Wjrdr0NU4Sk  
Watch: First 20 minutes (setup and basics)

**What is Ollama:**
- Tool to run LLMs locally on your machine
- Simple model management
- REST API for integration
- Docker-friendly
- CPU and GPU support

**Why Ollama vs Cloud APIs:**

```
Ollama (Local)              OpenAI API (Cloud)
--------------              ------------------
[CHECK] Free                [X] Pay per token
[CHECK] Complete privacy    [X] Data sent to cloud
[CHECK] No rate limits      [X] Rate limited
[CHECK] No API keys         [X] Requires API key
[X] Requires local compute  [CHECK] Always available
[X] Limited model size      [CHECK] Largest models
```

**For learning:** Ollama is perfect (free, private, sufficient quality)

**Ollama Models:**

1. **llama3.2:1b** (1.3GB)
   - Fast on CPU
   - Good for RAG
   - Recommended for this project

2. **llama3.2:3b** (2.0GB)
   - Better quality
   - Slower
   - Alternative if you have resources

3. **mistral:7b** (4.1GB)
   - High quality
   - Requires good hardware
   - Optional upgrade later

**Ollama API Endpoints:**

```
GET  /api/tags           # List installed models
POST /api/pull           # Download a model
POST /api/generate       # Generate text (streaming)
POST /api/chat           # Chat completion
```

**Docker Usage:**
```bash
# Pull Ollama image
docker pull ollama/ollama:0.5.4

# Run container
docker run -d -p 11434:11434 ollama/ollama

# Download model (inside container)
docker exec ollama ollama pull llama3.2:1b

# List models
docker exec ollama ollama list

# Test generation
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "What is machine learning?",
  "stream": false
}'
```

**Reading:**
[BOOK] **"Ollama Documentation"**  
URL: https://github.com/ollama/ollama/blob/main/docs/api.md  
Read: API reference (15 min)

---

### **MODULE 2: Prompt Engineering for RAG** [TIME] 120 minutes

#### **2.1 RAG Prompt Structure** (45 min)

**Video:**
[VIDEO] **"Prompt Engineering for RAG Systems"** - DeepLearning.AI  
URL: https://www.youtube.com/watch?v=T-D1OfcDW1M  
Watch: 30 minutes

**RAG Prompt Components:**

```
+------------------------------------------+
| 1. SYSTEM PROMPT                         |
|    Role definition, constraints          |
+------------------------------------------+
| 2. CONTEXT (Retrieved Chunks)            |
|    Relevant paper excerpts               |
+------------------------------------------+
| 3. USER QUESTION                         |
|    The actual query                      |
+------------------------------------------+
| 4. OUTPUT INSTRUCTIONS                   |
|    Format, citation requirements         |
+------------------------------------------+
```

**Example RAG Prompt:**

```
SYSTEM:
You are a helpful research assistant that answers questions 
about machine learning papers. Base your answers ONLY on the 
provided context. If the answer isn't in the context, say 
"I don't have enough information to answer that."

CONTEXT:
Paper: "Attention Is All You Need"
Section: Introduction
Text: "We propose the Transformer, a model architecture 
eschewing recurrence and instead relying entirely on an 
attention mechanism to draw global dependencies between 
input and output."

Paper: "BERT: Pre-training of Deep Bidirectional Transformers"
Section: Methodology  
Text: "BERT uses only the encoder part of the Transformer. 
Unlike directional models, BERT's denoising objective enables 
it to fuse the left and the right context."

QUESTION:
What is the main difference between Transformers and BERT?

INSTRUCTIONS:
Provide a clear, concise answer. Cite the paper titles you use.

EXPECTED OUTPUT:
The main difference is that BERT uses only the Transformer's 
encoder, while the original Transformer uses both encoder and 
decoder. Additionally, BERT is bidirectional, processing text 
in both directions simultaneously, unlike directional models.
(Sources: "Attention Is All You Need", "BERT: Pre-training...")
```

**Reading:**
[BOOK] **"Prompt Engineering Guide - RAG"** - Anthropic  
URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview  
Read: RAG best practices (15 min)

#### **2.2 RAG Prompt Best Practices** (45 min)

**1. Clear Instructions:**

Bad:
```
Here's some context. Answer the question.
```

Good:
```
You are a research assistant. Use ONLY the provided context 
to answer. If unsure, say "I don't know." Always cite sources.
```

**2. Context Formatting:**

Bad:
```
[chunk1 chunk2 chunk3]
```

Good:
```
CONTEXT 1:
Paper: "Attention Is All You Need"
Section: Introduction
Text: "We propose the Transformer..."

CONTEXT 2:
Paper: "BERT"
Section: Methodology
Text: "BERT uses only the encoder..."
```

**3. Handling Citations:**

Bad:
```
Answer the question.
```

Good:
```
Answer the question and cite which papers you used. 
Format: (Source: Paper Title)
```

**4. Controlling Hallucination:**

Bad:
```
Be helpful and creative.
```

Good:
```
CRITICAL: Base your answer ONLY on the provided context.
Do NOT use external knowledge.
If the context doesn't contain the answer, explicitly state:
"The provided papers don't contain information about [topic]."
```

**5. Output Formatting:**

```
Provide your answer in this format:

ANSWER: [your 2-3 sentence answer]

EXPLANATION: [brief elaboration if needed]

SOURCES: [list paper titles used]

CONFIDENCE: [high/medium/low based on context quality]
```

**Testing Prompts:**

Test with these scenarios:
1. Question WITH answer in context -> Should answer correctly
2. Question WITHOUT answer -> Should say "I don't know"
3. Ambiguous question -> Should ask for clarification
4. Multiple conflicting sources -> Should note disagreement

**Reading:**
[BOOK] **"RAG Prompt Engineering"** - LangChain  
URL: https://python.langchain.com/docs/use_cases/question_answering/  
Read: Prompt templates section (15 min)

#### **2.3 Advanced RAG Patterns** (30 min)

**Query Rewriting:**

User asks: "How does it work?"

Bad (send as-is):
```
"How does it work?"
```

Good (rewrite for clarity):
```
Original: "How does it work?"
Rewritten: "How does the Transformer architecture work?"
```

**Context Compression:**

If retrieved chunks are too long:
1. Extract most relevant sentences
2. Summarize less critical parts
3. Prioritize sections matching query

**Multi-hop Reasoning:**

For complex questions:
```
Question: "What improvements did BERT make over Transformers?"

Step 1: Find Transformer capabilities
Step 2: Find BERT capabilities  
Step 3: Compare and contrast
```

**Confidence Scoring:**

Add to prompt:
```
Rate your confidence (high/medium/low) based on:
- How directly the context answers the question
- How complete the information is
- Whether multiple sources agree
```

**Reading:**
[BOOK] **"Advanced RAG Techniques"** - LlamaIndex  
URL: https://docs.llamaindex.ai/en/stable/  
Read: Advanced patterns (10 min)

---

### **MODULE 3: Server-Sent Events (SSE)** [TIME] 60 minutes

#### **3.1 What are Server-Sent Events?** (20 min)

**The Problem:**

Traditional HTTP:
```
Client: "Answer this question"
Server: [waits 20 seconds]
Server: "Here's the complete answer"
```

User sees: Loading spinner for 20 seconds, then complete answer

**The Solution - Streaming:**

```
Client: "Answer this question"
Server: "Transform" [200ms]
Server: "ers" [200ms]
Server: " are" [200ms]
Server: " neural" [200ms]
...
```

User sees: Text appearing word-by-word (like ChatGPT)

**Why SSE?**
- Better user experience (immediate feedback)
- Perceived speed (starts showing results instantly)
- Works over HTTP (no special protocol)
- Simple to implement
- Built into browsers

**Video:**
[VIDEO] **"Server-Sent Events Explained"** - Web Dev Simplified  
URL: https://www.youtube.com/results?search_query=server+sent+events+explained  
Watch: Any clear explanation (15 min)

#### **3.2 SSE Format and Protocol** (20 min)

**SSE Message Format:**

```
data: {"chunk": "Hello"}\n\n
data: {"chunk": " world"}\n\n
data: {"type": "done"}\n\n
```

**Rules:**
- Each message starts with "data: "
- Each message ends with "\n\n" (two newlines)
- Can send any text (usually JSON)
- Messages arrive in order

**SSE vs WebSocket:**

```
Server-Sent Events (SSE)     WebSocket
------------------------     ----------
[CHECK] Simple HTTP          Complex protocol
[CHECK] Auto-reconnect       Manual reconnect
[CHECK] Server -> Client     [CHECK] Bidirectional
[CHECK] Built into browsers  Needs library
[CHECK] Perfect for RAG      Better for chat apps
[X] One-way only             [CHECK] Two-way
```

**For RAG:** SSE is perfect (server pushes tokens to client)

**FastAPI SSE Example:**

```python
# REQUIREMENTS ONLY - NOT IMPLEMENTATION

# Endpoint should:
# - Return StreamingResponse
# - Set media_type to "text/event-stream"
# - Use async generator to yield events

# Each yielded message should:
# - Start with "data: "
# - End with "\n\n"
# - Contain JSON with chunk or status

# Event types needed:
# - {"type": "start"} - stream beginning
# - {"chunk": "text"} - answer token
# - {"type": "sources", "sources": [...]} - paper list
# - {"type": "done"} - stream complete
# - {"type": "error", "message": "..."} - error occurred
```

**Reading:**
[BOOK] **"Using Server-Sent Events"** - MDN  
URL: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events  
Read: Complete guide (15 min)

#### **3.3 Client-Side SSE Handling** (20 min)

**JavaScript EventSource:**

```javascript
// REQUIREMENTS ONLY - NOT IMPLEMENTATION

// Create EventSource connection:
// - URL: POST endpoint that returns SSE
// - Handle: onmessage, onerror, onopen events

// Message handling:
// - Parse JSON from event.data
// - Route based on type (start/chunk/sources/done/error)
// - Update UI accordingly

// Error handling:
// - Automatic reconnection (built-in)
// - Manual reconnection on failure
// - Display errors to user
```

**Testing SSE:**

Use curl:
```bash
curl -X POST "http://localhost:8000/api/v1/stream" \
  -H "Content-Type: application/json" \
  -d '{"query": "What are transformers?"}' \
  --no-buffer
```

Expected output:
```
data: {"type": "start"}

data: {"chunk": "Transform"}

data: {"chunk": "ers"}

data: {"chunk": " are"}

...

data: {"type": "sources", "sources": [...]}

data: {"type": "done"}
```

**Reading:**
[BOOK] **"EventSource API"** - MDN  
URL: https://developer.mozilla.org/en-US/docs/Web/API/EventSource  
Read: API reference (10 min)

---

### **MODULE 4: Gradio for Web Interfaces** [TIME] 90 minutes

#### **4.1 Gradio Basics** (30 min)

**Video:**
[VIDEO] **"Build ML Apps with Gradio"** - Official Gradio  
URL: https://www.youtube.com/watch?v=RiCQzBluTxU  
Watch: First 20 minutes

**What is Gradio:**
- Python library for ML/AI web interfaces
- Automatic UI generation
- Built-in components (textbox, slider, etc.)
- Fast prototyping
- Easy sharing and deployment

**Simple Example (REQUIREMENTS):**

```python
# REQUIREMENTS ONLY - NOT IMPLEMENTATION

# Interface needs:
# - Input: Textbox for user question
# - Output: Textbox for AI answer
# - Function: Call RAG endpoint
# - Submit button automatically created

# When user types and clicks submit:
# 1. Get text from input
# 2. Call backend API
# 3. Display response in output

# Should launch on: http://localhost:7860
```

**Gradio Advantage:**

Without Gradio:
- Write HTML, CSS, JavaScript
- Handle form submission
- Manage state
- Deploy web server
- Handle errors
- Total: Many hours

With Gradio:
- Write 5 lines of Python
- Automatic UI
- Built-in error handling
- Automatic deployment
- Total: 10 minutes

**Reading:**
[BOOK] **"Gradio Quickstart"**  
URL: https://www.gradio.app/guides/quickstart  
Read: Complete quickstart (15 min)

#### **4.2 Gradio Components** (30 min)

**Key Components for RAG:**

**1. Textbox (Input/Output):**
```python
# REQUIREMENTS ONLY

# Input textbox needs:
# - Label: "Ask a question about machine learning papers"
# - Placeholder: Example question
# - Lines: 3 (multiline)

# Output textbox needs:
# - Label: "Answer"
# - Lines: 10
# - Show copy button
```

**2. Chatbot (Alternative to Textbox):**
```python
# REQUIREMENTS ONLY

# Chatbot component provides:
# - Chat history display
# - Message bubbles (user vs assistant)
# - Better UX for conversations
# - Automatic scroll

# Requires:
# - List of [user_msg, assistant_msg] tuples
# - Append new exchanges to history
```

**3. Examples:**
```python
# REQUIREMENTS ONLY

# Examples component needs:
# - List of sample questions
# - Click to populate input
# - Helps users get started

# Sample questions:
# - "What are transformers in ML?"
# - "Explain attention mechanisms"
# - "How does BERT differ from GPT?"
```

**4. Additional Components:**
```python
# REQUIREMENTS ONLY

# Slider for top_k:
# - Min: 1, Max: 10, Default: 3
# - Label: "Number of papers to search"

# Checkbox for use_hybrid:
# - Label: "Use hybrid search"
# - Default: True

# Dropdown for model:
# - Options: ["llama3.2:1b", "llama3.2:3b"]
# - Default: "llama3.2:1b"
```

**Reading:**
[BOOK] **"Gradio Components"**  
URL: https://www.gradio.app/docs/gradio/textbox  
Read: Textbox, Chatbot, Examples (15 min)

#### **4.3 Gradio Blocks (Advanced Layout)** (30 min)

**Interface vs Blocks:**

**Interface:** Simple, automatic layout
```python
# REQUIREMENTS ONLY

# Single function, single UI
# Good for: Simple demos
# Limited: Can't customize layout
```

**Blocks:** Custom layout
```python
# REQUIREMENTS ONLY

# Multiple functions, custom UI
# Good for: Production apps
# Flexible: Complete control over layout

# Layout components:
# - Row: Horizontal layout
# - Column: Vertical layout
# - Tab: Tabbed interface
# - Accordion: Collapsible sections
```

**RAG Interface Layout (REQUIREMENTS):**

```
+------------------------------------------+
| HEADER: "arXiv Paper Research Assistant" |
+------------------------------------------+
|                                          |
| [Row]                                    |
|   [Column - Left 70%]                    |
|     Input: Question textbox              |
|     Output: Answer textbox               |
|                                          |
|   [Column - Right 30%]                   |
|     Settings:                            |
|     - top_k slider                       |
|     - use_hybrid checkbox                |
|     - model dropdown                     |
|                                          |
| [Row]                                    |
|   Submit button | Clear button           |
|                                          |
| [Row]                                    |
|   Sources: Papers used (formatted)       |
|                                          |
| [Accordion - Collapsed]                  |
|   Example questions                      |
+------------------------------------------+
```

**Streaming in Gradio:**

```python
# REQUIREMENTS ONLY

# For streaming responses:
# - Use async function
# - Yield partial results
# - Update UI incrementally

# User sees:
# - "Transform" (100ms)
# - "Transformers" (200ms)
# - "Transformers are" (300ms)
# - "Transformers are neural" (400ms)
# ...

# Implementation:
# - Connect to SSE endpoint
# - Parse streaming chunks
# - Yield each update to Gradio
```

**Reading:**
[BOOK] **"Gradio Blocks Tutorial"**  
URL: https://www.gradio.app/guides/blocks-and-event-listeners  
Read: Blocks basics and layout (15 min)

**Examples:**
[BOOK] **"Gradio Examples Gallery"**  
URL: https://www.gradio.app/demos  
Browse: Chat and QA examples (10 min)

---

## HANDS-ON EXERCISES

### **Exercise 1: Prompt Engineering**

**Task:** Improve this RAG prompt:

```
Bad Prompt:
"Here are some papers. Answer the question."

Context:
[chunk1] [chunk2] [chunk3]

Question: What are transformers?
```

**Requirements for improved prompt:**
1. Clear role definition
2. Formatted context with paper titles
3. Citation requirements
4. Hallucination prevention
5. Output format specification

**Expected structure:**
```
SYSTEM: [role and constraints]
CONTEXT: [formatted excerpts]
QUESTION: [user query]
INSTRUCTIONS: [output format and citations]
```

---

### **Exercise 2: SSE Message Design**

**Task:** Design SSE message format for RAG streaming

**Requirements:**
1. Start event (stream beginning)
2. Chunk events (answer tokens)
3. Sources event (paper list)
4. Done event (completion)
5. Error event (if something fails)

**Expected format:**
```json
# Each message should be valid JSON
# Each message should have "type" field
# Content should be in appropriate fields
```

**Test scenarios:**
1. Successful generation with 3 sources
2. Error during LLM generation
3. No sources found (empty results)

---

### **Exercise 3: Gradio Interface Design**

**Task:** Design Gradio interface for RAG system

**Requirements:**
1. Input: Question textbox
2. Output: Answer display
3. Settings: top_k, use_hybrid, model
4. Sources: Paper list with titles and URLs
5. Examples: 3 sample questions

**Layout considerations:**
- Where should settings go?
- How to display sources clearly?
- When to show examples?
- Submit vs Enter key behavior?

**Bonus:** How would you add streaming?

---

## RESEARCH QUESTIONS

### **Conceptual Questions:**

1. **How do LLMs generate text?**
   - What is next token prediction?
   - What role does temperature play?

2. **What is RAG?**
   - How does it differ from fine-tuning?
   - When to use RAG vs fine-tuning?

3. **Why use Ollama locally?**
   - What are the tradeoffs vs cloud APIs?
   - When is local better?

4. **How does SSE work?**
   - How is it different from WebSocket?
   - When to use each?

5. **What makes a good RAG prompt?**
   - How to prevent hallucination?
   - How to ensure citation?

6. **Why stream responses?**
   - What's the UX benefit?
   - What's the technical cost?

### **Practical Questions:**

1. **How do you choose an LLM model?**
   - Size vs quality tradeoff?
   - Speed vs accuracy?

2. **How do you test RAG quality?**
   - What metrics to use?
   - How to evaluate answers?

3. **How do you handle LLM errors?**
   - Timeout scenarios?
   - Model unavailable?
   - Out of context?

4. **How do you design for streaming?**
   - Frontend considerations?
   - Error handling?

5. **What makes a good Gradio interface?**
   - Layout best practices?
   - Component selection?

6. **How do you debug RAG issues?**
   - Poor quality answers?
   - Wrong sources?
   - Slow responses?

---

## KEY TAKEAWAYS

**Remember these 12 things:**

1. **LLMs = Next token prediction**
   - Generate text word by word
   - Temperature controls randomness
   - Context window has limits

2. **Ollama = Local LLM deployment**
   - Free and private
   - Good for learning and development
   - llama3.2:1b sufficient for RAG

3. **RAG = Retrieval + Generation**
   - Search finds relevant context
   - LLM generates answer from context
   - Better than pure LLM (no hallucination)

4. **Prompt engineering = Critical for quality**
   - Clear instructions prevent errors
   - Context formatting matters
   - Citation requirements must be explicit

5. **Hallucination prevention = Primary concern**
   - "Use ONLY provided context"
   - "Say 'I don't know' if unsure"
   - Always require source citations

6. **SSE = Server-Sent Events**
   - One-way streaming (server to client)
   - Perfect for RAG responses
   - Better UX than loading spinners

7. **Streaming = Better user experience**
   - Users see results immediately
   - Perceived speed improvement
   - Like ChatGPT interface

8. **Gradio = Fast web interfaces**
   - Python-only (no HTML/CSS/JS)
   - Automatic UI generation
   - Perfect for ML/AI demos

9. **Blocks = Custom layouts**
   - More control than Interface
   - Production-ready apps
   - Row/Column layout system

10. **Context limits matter**
    - 8K tokens typical for llama3.2
    - Must fit: prompt + context + answer
    - Chunk count affects this

11. **Response time = User expectation**
    - Target: <20 seconds for answer
    - Streaming helps perception
    - Monitor and optimize

12. **Testing = Essential**
    - Test with/without answers in context
    - Test error scenarios
    - Test different question types

**If you understand these 12:** You're ready to build! [CHECK]

---

## ADDITIONAL RESOURCES (Optional Deep Dives)

### **LLMs:**
- Stanford CS324: https://stanford-cs324.github.io/winter2022/
- Hugging Face NLP Course: https://huggingface.co/learn/nlp-course
- "Attention Is All You Need" paper: https://arxiv.org/abs/1706.03762

### **Ollama:**
- Official Docs: https://ollama.com/docs
- GitHub: https://github.com/ollama/ollama
- Model Library: https://ollama.com/library
- Community Models: https://ollama.com/search

### **Prompt Engineering:**
- OpenAI Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic Guide: https://docs.anthropic.com/en/docs/prompt-engineering
- Prompt Engineering Guide: https://www.promptingguide.ai/

### **RAG Systems:**
- LangChain RAG Tutorial: https://python.langchain.com/docs/use_cases/question_answering/
- LlamaIndex Guides: https://docs.llamaindex.ai/en/stable/
- RAG Evaluation (RAGAS): https://docs.ragas.io/

### **Gradio:**
- Official Docs: https://www.gradio.app/docs
- Examples Gallery: https://www.gradio.app/demos
- Discord Community: https://discord.gg/feTf9x3ZSB
- Custom Components: https://www.gradio.app/custom-components

### **Streaming:**
- FastAPI Streaming: https://fastapi.tiangolo.com/advanced/custom-response/
- JavaScript EventSource: https://javascript.info/server-sent-events

---

## AFTER LEARNING

### **You're ready to build Steps 17-20 when you can:**

**Knowledge Check:**
- [ ] Explain how LLMs generate text
- [ ] Run Ollama locally and manage models
- [ ] Build effective RAG prompts
- [ ] Implement Server-Sent Events concept
- [ ] Create async generators in Python concept
- [ ] Design Gradio Blocks applications
- [ ] Handle streaming in web interfaces
- [ ] Debug LLM integration issues

**Practical Check:**
- [ ] Can choose appropriate LLM model
- [ ] Can write RAG prompts that prevent hallucination
- [ ] Understand SSE message format
- [ ] Can design Gradio layouts
- [ ] Know how to test RAG quality
- [ ] Can handle LLM errors gracefully
- [ ] Understand streaming tradeoffs

**Then proceed to:**
- **STEP17_OLLAMA_LLM_SERVICE.md** - Ollama client service
- **STEP18_RAG_ENDPOINTS.md** - /ask and /stream endpoints
- **STEP19_GRADIO_INTERFACE.md** - Web UI implementation
- **STEP20_COMPLETE_SYSTEM.md** - End-to-end integration

---

## WEEK 9 SUCCESS METRICS

**By end of this week, you'll have:**
- [TARGET] Ollama running with llama3.2:1b model
- [TARGET] RAG prompts preventing hallucination
- [TARGET] /api/v1/ask endpoint (non-streaming)
- [TARGET] /api/v1/stream endpoint (SSE streaming)
- [TARGET] Gradio interface on port 7861
- [TARGET] Complete RAG system end-to-end
- [TARGET] <20s response times (streaming feels instant!)

**Quality Targets:**
- Answer accuracy: >85% based on context
- Hallucination rate: <5% (answers only from context)
- Citation accuracy: 100% (all sources valid)
- Streaming delay: <200ms per token
- UI responsiveness: Immediate feedback

**User Experience:**
- Type question -> see results streaming immediately
- Clear source citations with paper titles
- Handles "I don't know" appropriately
- Professional-looking interface

---

**Time estimate:** 5-6 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Total week time:** ~16-18 hours (learning + implementation)

---

**Document Generated:** December 28, 2025  
**For:** Career Transition Week 9 (MOAI Week 5)  
**Status:** Complete RAG System - Ready for Steps 17-20  
**Format:** Clean ASCII - No Character Corruption
