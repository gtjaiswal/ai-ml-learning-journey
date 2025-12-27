# ðŸ“š WEEK 9 LEARNING GUIDE (Career Transition Plan)

**Your Timeline:** Week 9 of 34-week transition  
**Corresponds to:** Week 5 MOAI - Complete RAG System  
**Focus:** Conversational AI with LLMs, RAG Endpoints, Web Interfaces

---

## ðŸŽ¯ WEEK 9 OVERVIEW

**What You'll Build:**
- Step 17: Ollama LLM service integration
- Step 18: RAG API endpoints (ask + stream)
- Step 19: Gradio web interface
- Step 20: Complete system verification

**What You'll Learn:**
- Local LLM deployment and management
- Prompt engineering for RAG
- API design for conversational AI
- Server-Sent Events (SSE) for streaming
- Web UI development with Gradio
- Production system integration

**Time Investment:** ~16-18 hours total
- Learning: 5-6 hours
- Implementation: 11-12 hours

---

## ðŸ“– WHAT YOU ALREADY KNOW (from Weeks 1-8)

âœ… **Weeks 1-2:** ML Math, NumPy, Python basics  
âœ… **Week 3:** FastAPI, Docker, PostgreSQL  
âœ… **Week 4:** Async Python, SQLAlchemy, Repository pattern  
âœ… **Weeks 5-6:** Data ingestion (arXiv API, PDF parsing, Airflow)  
âœ… **Week 7:** OpenSearch, BM25 search  
âœ… **Week 8:** Hybrid search, embeddings, chunking, RRF fusion

**Foundation is solid!** Week 9 adds the **intelligence layer** - the AI that actually answers questions.

---

## ðŸ—“ï¸ LEARNING SCHEDULE

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

## ðŸ“š CORE LEARNING MODULES

### **MODULE 1: Large Language Models & Ollama** â±ï¸ 90 minutes

#### **1.1 LLM Fundamentals** (45 min)

**Video:**
ðŸ“º **"Intro to Large Language Models"** - Andrej Karpathy  
URL: https://www.youtube.com/watch?v=zjkBMFhNj_g  
Watch: Full video (1 hour) - focus on first 45 minutes

**Key Concepts:**

**What are LLMs:**
- Neural networks trained on massive text data
- Learn patterns, language structure, knowledge
- Generate human-like text
- Examples: GPT, Claude, Llama

**How LLMs work:**
- Tokenization (text â†’ numbers)
- Transformer architecture
- Attention mechanisms
- Next token prediction

**LLM Parameters:**
- **Temperature:** Controls randomness (0-1)
  - Low (0.1): Focused, deterministic
  - High (0.9): Creative, varied
- **Top-p:** Nucleus sampling
  - Controls diversity of outputs
- **Max tokens:** Response length limit

**Reading:**
ðŸ“– **"What are Large Language Models?"** - AWS  
URL: https://aws.amazon.com/what-is/large-language-model/

#### **1.2 Ollama for Local LLMs** (45 min)

**Video:**
ðŸ“º **"Run LLMs Locally with Ollama"** - NetworkChuck  
URL: https://www.youtube.com/watch?v=Wjrdr0NU4Sk  
Watch: First 20 minutes (setup and basics)

**Reading:**
ðŸ“– **Ollama Documentation**  
URL: https://ollama.com/  
Read: Quick start, API documentation

**Key Concepts:**

**Why Ollama:**
- Run LLMs locally (no API costs)
- Complete data privacy
- Fast inference on CPU/GPU
- Simple model management
- Docker-friendly

**Ollama vs Cloud APIs:**
```
Ollama (Local)              OpenAI API (Cloud)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€              â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
âœ… Free (after hardware)    âŒ Pay per token
âœ… Complete privacy         âŒ Data sent to cloud
âœ… No rate limits           âŒ Rate limited
âŒ Requires local compute   âœ… Always available
âŒ Limited model size       âœ… Largest models
```

**Ollama API Endpoints:**
```
GET  /api/tags          # List models
POST /api/pull          # Download model
POST /api/generate      # Generate text
POST /api/chat          # Chat completion
```

**Ollama Models:**
- **llama3.2:1b** (1.3GB) - Fast, good for RAG
- **llama3.2:3b** (2.0GB) - Better quality
- **mistral:7b** (4.1GB) - High quality, slower

**Docker Usage:**
```bash
# Pull Ollama image
docker pull ollama/ollama

# Run container
docker run -d -p 11434:11434 ollama/ollama

# Download model
docker exec ollama ollama pull llama3.2:1b

# List models
docker exec ollama ollama list
```

---

### **MODULE 2: Prompt Engineering for RAG** â±ï¸ 120 minutes

#### **2.1 RAG Prompt Structure** (45 min)

**Reading:**
ðŸ“– **"Prompt Engineering Guide - RAG"** - Anthropic  
URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview  
Read: RAG best practices section

**Video:**
ðŸ“º **"Prompt Engineering for RAG Systems"** - DeepLearning.AI  
URL: https://www.youtube.com/watch?v=T-D1OfcDW1M  
Watch: 30 minutes

**Key Concepts:**

**RAG Prompt Components:**
```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ 1. SYSTEM PROMPT                        â”‚
â”‚    Role definition, constraints         â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ 2. CONTEXT (Retrieved Chunks)           â”‚
â”‚    Relevant paper excerpts              â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ 3. USER QUESTION                        â”‚
â”‚    The actual query                     â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ 4. INSTRUCTIONS                         â”‚
â”‚    Format, length, citations            â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

**Example RAG Prompt:**
```
SYSTEM:
You are an AI assistant specialized in academic papers.
Answer based ONLY on the provided context.
If the answer is not in the context, say "I cannot find...".

CONTEXT:
[2401.00001] Attention is All You Need
The Transformer model architecture relies entirely on attention...

[2401.00002] BERT: Pre-training
Building on the transformer architecture, BERT introduces...

QUESTION:
What are transformers in machine learning?

INSTRUCTIONS:
Answer in maximum 300 words. Be accurate and cite paper IDs.
```

**Prompt Engineering Principles:**
1. **Be specific:** Clear role, clear task
2. **Provide context:** Give relevant information
3. **Set constraints:** Length, format, style
4. **Prevent hallucination:** "Use ONLY provided context"
5. **Request citations:** "Cite paper IDs"

#### **2.2 Optimizing RAG Prompts** (45 min)

**Reading:**
ðŸ“– **"The Art of Asking ChatGPT for High-Quality Answers"** - OpenAI  
URL: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api

**Key Concepts:**

**Prompt Size Matters:**
```
Large Prompt (10KB)           Small Prompt (2KB)
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€               â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
âŒ Slow (120s)                âœ… Fast (20s)
âŒ High cost                  âœ… Low cost
âŒ Noise in context           âœ… Focused context
âŒ Token limit issues         âœ… Fits easily
```

**Optimization Strategies:**
1. **Remove redundancy**
   - Don't repeat metadata
   - Minimize formatting
   - Focus on content

2. **Chunk wisely**
   - Quality over quantity
   - Top 3-5 chunks usually enough
   - More chunks â‰  better answers

3. **Format efficiently**
   ```
   âŒ Verbose:
   "The following paper titled 'Attention is All You Need' 
   written by authors Vaswani et al. published in 2017 states..."
   
   âœ… Concise:
   "[2401.00001] Attention is All You Need
   Transformer architecture relies on attention..."
   ```

4. **Set response limits**
   - "Answer in maximum 300 words"
   - Prevents verbose responses
   - Improves response time

**Week 5 Optimization Result:**
- Before: 10KB prompts, 120s responses
- After: 2KB prompts, 15-20s responses
- **6x performance improvement!**

#### **2.3 Preventing Hallucination** (30 min)

**Reading:**
ðŸ“– **"How to Reduce Hallucination in Language Models"**  
URL: https://help.openai.com/en/articles/6825453-chatgpt-release-notes

**Key Techniques:**

**1. Explicit Constraints:**
```
âŒ Weak: "Answer the question based on context"

âœ… Strong: 
"Answer based ONLY on the provided excerpts.
If the answer is not in the context, respond with:
'I cannot find information about that in the papers.'"
```

**2. Source Attribution:**
```
âœ… "Cite paper IDs when relevant"
âœ… "Reference specific papers in your answer"
âœ… "If unsure, indicate uncertainty"
```

**3. Factual Focus:**
```
âŒ "Be creative and helpful"
âœ… "Be accurate and concise"
âœ… "Stick to facts from the papers"
```

**4. Testing:**
- Ask questions NOT in context
- Verify model says "I cannot find..."
- Don't reward hallucination

---

### **MODULE 3: Streaming APIs & Server-Sent Events** â±ï¸ 60 minutes

#### **3.1 Why Streaming for AI** (20 min)

**Concept:**

**Standard API (No Streaming):**
```
User sends question
       â†“
[Wait 15-20 seconds...]
       â†“
Complete answer appears
```

**Streaming API (SSE):**
```
User sends question
       â†“
[2-3 seconds...]
       â†“
First words appear âœ“
More words... âœ“
More words... âœ“
Complete answer (15-20s total)
```

**Benefits:**
- **Better UX:** Immediate feedback
- **Perceived speed:** Feels faster
- **Interruptible:** Can stop generation
- **Progressive:** Show results as available

**Use Cases:**
- Chat interfaces
- Content generation
- Real-time updates
- Progress indicators

#### **3.2 Server-Sent Events (SSE)** (40 min)

**Video:**
ðŸ“º **"Server-Sent Events Explained"** - Fireship  
URL: https://www.youtube.com/watch?v=4HlNv1qpZFY  
Watch: Full video (5 min)

**Reading:**
ðŸ“– **"Using Server-Sent Events"** - MDN  
URL: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events  
Read: Complete guide

**Key Concepts:**

**SSE Format:**
```
data: {"chunk": "Hello"}\n\n
data: {"chunk": " world"}\n\n
data: {"type": "done"}\n\n
```

**SSE vs WebSocket:**
```
Server-Sent Events (SSE)     WebSocket
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€         â”€â”€â”€â”€â”€â”€â”€â”€â”€
âœ… Simple, HTTP-based        Complex, new protocol
âœ… Auto-reconnect            Manual reconnect
âœ… Server â†’ Client only      âœ… Bidirectional
âœ… Built into browsers       Library needed
âœ… Perfect for streaming     Perfect for chat
```

**FastAPI SSE Example:**
```python
from fastapi.responses import StreamingResponse

async def event_generator():
    yield 'data: {"chunk": "Hello"}\n\n'
    yield 'data: {"chunk": " world"}\n\n'
    yield 'data: {"type": "done"}\n\n'

@app.post("/stream")
async def stream():
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
```

**Client-Side (JavaScript):**
```javascript
const eventSource = new EventSource('/stream');
eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    console.log(data);
};
```

**Event Types for RAG:**
```
{"type": "start"}                    # Stream started
{"chunk": "Transformers"}            # Answer chunk
{"chunk": " are"}                    # Another chunk
{"type": "sources", "sources": [...]}# Paper sources
{"type": "done"}                     # Complete
{"type": "error", "message": "..."}  # Error occurred
```

---

### **MODULE 4: Gradio for Web Interfaces** â±ï¸ 90 minutes

#### **4.1 Gradio Basics** (30 min)

**Video:**
ðŸ“º **"Build Machine Learning Apps with Gradio"**  
URL: https://www.youtube.com/watch?v=RiCQzBluTxU  
Watch: First 20 minutes

**Reading:**
ðŸ“– **Gradio Quickstart**  
URL: https://www.gradio.app/guides/quickstart  
Read: Complete guide

**Key Concepts:**

**What is Gradio:**
- Python library for ML/AI interfaces
- Fast prototyping
- Automatic UI generation
- Built-in components
- Easy deployment

**Simple Example:**
```python
import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text"
)

demo.launch()
```

**Gradio vs Streamlit:**
```
Gradio                       Streamlit
â”€â”€â”€â”€â”€â”€                       â”€â”€â”€â”€â”€â”€â”€â”€â”€
âœ… ML/AI focused             General dashboards
âœ… Chat interfaces           Data visualization
âœ… Quick prototypes          Complex apps
âœ… Auto component layout     Manual layout control
```

#### **4.2 Gradio Blocks for Custom UIs** (30 min)

**Reading:**
ðŸ“– **Gradio Blocks Documentation**  
URL: https://www.gradio.app/docs/blocks  
Read: Blocks guide and examples

**Key Concepts:**

**Blocks API:**
- More control than Interface
- Custom layouts
- Multiple components
- Complex interactions
- Event handling

**Example Structure:**
```python
import gradio as gr

with gr.Blocks() as app:
    gr.Markdown("# My App")
    
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            submit = gr.Button("Submit")
        
        with gr.Column(scale=1):
            slider = gr.Slider(1, 10, value=3)
            dropdown = gr.Dropdown(["A", "B"])
    
    submit.click(
        fn=my_function,
        inputs=[msg, slider, dropdown],
        outputs=chatbot
    )

app.launch()
```

**Key Components:**
- **Chatbot:** Chat interface
- **Textbox:** Text input
- **Button:** Click actions
- **Slider:** Numeric input
- **Dropdown:** Selection
- **Checkbox:** Boolean toggle

#### **4.3 Streaming in Gradio** (30 min)

**Reading:**
ðŸ“– **Gradio Streaming Guide**  
URL: https://www.gradio.app/guides/streaming-outputs  
Read: Complete guide

**Key Concepts:**

**Generator Pattern:**
```python
async def chat(message, history):
    # Yield partial responses
    response = ""
    for chunk in generate_chunks():
        response += chunk
        yield response  # Update UI
```

**Streaming vs Non-Streaming:**
```
Non-Streaming:
def chat(message):
    return complete_response  # Wait for all

Streaming:
async def chat(message):
    partial = ""
    for chunk in stream:
        partial += chunk
        yield partial  # Show progress
```

**Event Handlers:**
- `.click()` - Button clicks
- `.submit()` - Enter key
- `.change()` - Value changes
- `.select()` - Selection events

---

## ðŸ”¬ RESEARCH QUESTIONS

**Conceptual:**
- [ ] How do LLMs generate text?
- [ ] What is prompt engineering?
- [ ] Why use local LLMs vs APIs?
- [ ] What is RAG and how does it work?
- [ ] How does streaming improve UX?
- [ ] What are Server-Sent Events?
- [ ] Why use Gradio vs custom frontend?
- [ ] How to prevent LLM hallucination?

**Practical:**
- [ ] How to run Ollama in Docker?
- [ ] How to pull and manage models?
- [ ] How to build effective RAG prompts?
- [ ] How to implement SSE in FastAPI?
- [ ] How to create streaming generators?
- [ ] How to parse SSE on client side?
- [ ] How to build Gradio Blocks app?
- [ ] How to handle async in Gradio?

---

## ðŸ“š ADDITIONAL RESOURCES (Optional)

**LLMs:**
- Stanford CS324: https://stanford-cs324.github.io/winter2022/
- Hugging Face NLP Course: https://huggingface.co/learn/nlp-course

**Ollama:**
- Official Docs: https://ollama.com/docs
- GitHub: https://github.com/ollama/ollama
- Model Library: https://ollama.com/library

**Prompt Engineering:**
- OpenAI Guide: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic Guide: https://docs.anthropic.com/en/docs/prompt-engineering
- Prompt Engineering Guide: https://www.promptingguide.ai/

**Gradio:**
- Official Docs: https://www.gradio.app/docs
- Examples: https://www.gradio.app/demos
- Discord Community: https://discord.gg/feTf9x3ZSB

---

## ðŸš€ AFTER LEARNING

**You're ready to build Steps 17-20 when you can:**
1. Explain how LLMs generate text
2. Run Ollama locally and manage models
3. Build effective RAG prompts
4. Implement Server-Sent Events
5. Create async generators in Python
6. Build Gradio Blocks applications
7. Handle streaming in web interfaces
8. Debug LLM integration issues

**Then proceed to:**
- **STEP17_OLLAMA_LLM_SERVICE.md** - LLM client
- **STEP18_RAG_ENDPOINTS.md** - API endpoints
- **STEP19_GRADIO_INTERFACE.md** - Web UI
- **STEP20_COMPLETE_SYSTEM.md** - Integration

---

## ðŸŽ¯ WEEK 9 GOALS

**By end of week, you'll have:**
- âœ… Ollama running with llama3.2:1b
- âœ… RAG prompt engineering mastery
- âœ… /ask endpoint (standard response)
- âœ… /stream endpoint (SSE streaming)
- âœ… Gradio web interface on port 7861
- âœ… Complete RAG system end-to-end
- âœ… 15-20s response times (6x faster!)

**This completes Week 5 MOAI - Mother of AI Project!** ðŸŽ‰

**Next (Week 10):**
- Redis caching (150-400x speedup)
- Langfuse monitoring
- Production optimization

---

## ðŸ’¡ LEARNING TIPS

**For LLM Concepts:**
- Watch videos at 1.5x speed
- Take notes on key concepts
- Try Ollama hands-on immediately
- Experiment with different prompts

**For Streaming:**
- Build simple SSE example first
- Test with curl --no-buffer
- Understand event format thoroughly
- Debug with network inspector

**For Gradio:**
- Start with Interface API
- Move to Blocks for custom layout
- Test components individually
- Read component documentation

**Time Management:**
- Pre-learn on weekend: 5-6 hours
- Implement Mon-Fri: 2-3 hours/day
- Total week: 16-18 hours
- Take breaks every 90 minutes

---

**Time estimate:** 5-6 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Note:** Week 9 is exciting - you're building the AI layer!

---

**Document Generated:** December 26, 2025  
**For:** Career Transition Week 9 (MOAI Week 5)  
**Status:** Complete RAG System Learning Guide
