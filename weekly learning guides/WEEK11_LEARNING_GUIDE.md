# WEEK 11 LEARNING GUIDE: LangGraph & Agentic RAG

**Pre-learning for Steps 25-28 (Agentic RAG System)**

**Time Investment:** 5-6 hours over the weekend before Week 11

---

## LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **AI Agents** - What makes an AI system "agentic"
2. **LangGraph** - Graph-based workflow orchestration for agents
3. **Multi-Agent Patterns** - Collaboration and task decomposition
4. **Tool Calling** - How agents use external tools
5. **Telegram Bots** - Building chat interfaces
6. **Langfuse** - LLM observability and monitoring

**Goal:** Build a production-grade agentic RAG system with observability

---

## WHAT YOU ALREADY KNOW (from Weeks 3-10)

[CHECK] **Weeks 3-5 (MOAI Weeks 1-2):**
- Docker, PostgreSQL, FastAPI fundamentals
- Airflow orchestration
- PDF parsing and data ingestion

[CHECK] **Weeks 7-9 (MOAI Weeks 3-5):**
- OpenSearch and BM25 search
- Semantic search with embeddings
- Hybrid search with RRF
- RAG system with Ollama
- Gradio web interface

[CHECK] **Week 10 (MOAI Week 6):**
- Redis caching
- Structured logging
- Rate limiting
- Production error handling

**You now have:**
- Complete RAG system
- Production-ready features
- Performance optimization
- Observability foundation

**Week 11 Focus:**
Adding **intelligence and automation**:
- Agentic reasoning and planning
- Multi-hop retrieval
- Self-reflection and critique
- Telegram bot interface
- LLM observability with Langfuse

---

## LEARNING SCHEDULE

### **Saturday/Sunday Before Week Starts (5-6 hours)**

**Recommended pre-learning:**
- AI agents fundamentals (1 hour)
- LangGraph framework (1.5 hours)
- Multi-agent patterns (1 hour)
- Telegram bots (1 hour)
- Langfuse observability (1.5 hours)

### **During Week (as needed)**

**Monday-Tuesday:**
- LangGraph API reference (45 min)
- State management patterns (45 min)

**Wednesday-Thursday:**
- Telegram Bot API deep dive (45 min)
- Langfuse integration (45 min)

**Friday:**
- Complete system testing (1 hour)

---

## CORE LEARNING MODULES

### **MODULE 1: AI Agents Fundamentals** [TIME] 60 minutes

#### **1.1 What are AI Agents?** (30 min)

**Video:**
[VIDEO] **"What are AI Agents?"** - IBM Technology  
URL: https://www.youtube.com/watch?v=F8NKVhkZZWI  
Watch: Full video (10 min)

[VIDEO] **"LLM Agents Explained"** - AI Explained  
URL: https://www.youtube.com/results?search_query=llm+agents+explained  
Watch: Any comprehensive explanation (15 min)

**Traditional RAG vs Agentic RAG:**

```
TRADITIONAL RAG:
User: "What improvements did BERT make?"
System:
  1. Search for "BERT improvements"
  2. Retrieve top 3 chunks
  3. Generate answer
  4. Return response

Limitations:
- Single search query
- No follow-up research
- Can't break down complex questions
- No self-verification
```

```
AGENTIC RAG:
User: "What improvements did BERT make?"
Agent:
  1. Planning: "Need to find: (a) What is BERT (b) What came before (c) What changed"
  2. Search 1: "BERT architecture"
  3. Search 2: "Transformer architecture" (for comparison)
  4. Synthesis: Compare findings
  5. Self-critique: "Do I have enough info?"
  6. Search 3: "BERT vs GPT" (if needed)
  7. Generate comprehensive answer
  8. Verify: Citations accurate?
  9. Return response

Benefits:
- Multi-hop reasoning
- Self-directed research
- Quality verification
- Comprehensive answers
```

**Key Agent Capabilities:**

1. **Planning:** Break complex task into subtasks
2. **Tool Use:** Call search, calculator, APIs
3. **Memory:** Track conversation context
4. **Reflection:** Evaluate own outputs
5. **Iteration:** Retry if answer insufficient

**Reading:**
[BOOK] **"What are AI Agents?"** - LangChain  
URL: https://python.langchain.com/docs/concepts/agents/  
Read: Core concepts (10 min)

#### **1.2 Agent Architecture Patterns** (30 min)

**ReAct Pattern (Reasoning + Acting):**
```
Thought: "I need to find what BERT improved over Transformers"
Action: search("BERT improvements over Transformer")
Observation: "BERT uses bidirectional training..."
Thought: "Now I need Transformer's approach for comparison"
Action: search("Transformer training approach")
Observation: "Transformer uses left-to-right..."
Thought: "I have enough info to answer"
Action: generate_answer()
```

**Plan-and-Execute Pattern:**
```
Step 1 - Planning:
  Task: "Compare BERT and GPT"
  Plan:
    1. Find BERT architecture
    2. Find GPT architecture
    3. Identify key differences
    4. Generate comparison

Step 2 - Execution:
  Execute each step sequentially
  Collect results
  Synthesize final answer
```

**Reflexion Pattern (Self-Critique):**
```
Generate initial answer
  |
  v
Critique: "Is this accurate? Complete? Well-cited?"
  |
  v
If issues found: Gather more info, regenerate
If satisfactory: Return answer
```

**Multi-Agent Pattern:**
```
Coordinator Agent: "User wants paper comparison"
  |
  +-> Searcher Agent: "Find relevant papers"
  |
  +-> Analyst Agent: "Analyze papers"
  |
  +-> Writer Agent: "Generate comparison"
  |
  v
Synthesize: Combine all results
```

**Reading:**
[BOOK] **"Agent Patterns"** - LangGraph  
URL: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/  
Read: ReAct and Plan-Execute (10 min)

---

### **MODULE 2: LangGraph Framework** [TIME] 90 minutes

#### **2.1 LangGraph Basics** (30 min)

**Video:**
[VIDEO] **"Introduction to LangGraph"** - LangChain  
URL: https://www.youtube.com/watch?v=HGRJLj5p0n8  
Watch: First 20 minutes

**What is LangGraph:**
- Framework for building agentic workflows
- Graph-based state machines
- Nodes = functions, Edges = transitions
- Handles state management
- Supports cycles (iteration/retry)

**LangGraph vs LangChain:**

```
LangChain                  LangGraph
---------                  ---------
Linear workflows           Graph workflows
Limited cycles             Full cycle support
Less control               Complete control
Good for: Chains           Good for: Agents
```

**Core Concepts:**

**1. State:**
```python
# REQUIREMENTS ONLY

# State defines what data flows through graph
# For RAG agent:
# - user_query: str
# - search_results: List[Paper]
# - answer: str
# - iterations: int
# - max_iterations: int = 3
```

**2. Nodes:**
```python
# REQUIREMENTS ONLY

# Each node is a function that:
# - Receives current state
# - Performs action
# - Returns updated state

# Example nodes for RAG:
# - query_planner: Break down query
# - searcher: Execute search
# - analyzer: Analyze results
# - generator: Create answer
# - critic: Evaluate quality
```

**3. Edges:**
```python
# REQUIREMENTS ONLY

# Edges connect nodes:

# Unconditional edge:
# searcher -> analyzer (always go here)

# Conditional edge:
# critic -> generator (if quality low, regenerate)
# critic -> END (if quality high, finish)
```

**Reading:**
[BOOK] **"LangGraph Tutorial"** - LangGraph Docs  
URL: https://langchain-ai.github.io/langgraph/tutorials/introduction/  
Read: Quick start (10 min)

#### **2.2 Building LangGraph Workflows** (35 min)

**Simple Agent Graph:**

```
                    START
                      |
                      v
              [Query Planner]
                      |
                      v
                [Searcher] <----+
                      |          |
                      v          |
                [Analyzer]       |
                      |          |
                      v          |
                [Generator]      |
                      |          |
                      v          |
                 [Critic]        |
                      |          |
            +---------+----------+
            |                    |
            v                    v
        (Good)                (Poor)
            |                    |
            v                    |
          END                    +
```

**State Management:**
```python
# REQUIREMENTS ONLY

# State flows through graph:

# Initial state:
# {
#   "query": "What are transformers?",
#   "results": [],
#   "answer": "",
#   "iteration": 0
# }

# After searcher:
# {
#   "query": "What are transformers?",
#   "results": [Paper1, Paper2, Paper3],
#   "answer": "",
#   "iteration": 0
# }

# After generator:
# {
#   "query": "What are transformers?",
#   "results": [Paper1, Paper2, Paper3],
#   "answer": "Transformers are neural networks...",
#   "iteration": 1
# }
```

**Conditional Routing:**
```python
# REQUIREMENTS ONLY

# Function signature needed:
# - Input: Current state
# - Output: Next node name

# Logic:
# if state["iteration"] >= MAX_ITERATIONS:
#     return "END"
# elif answer_quality_high(state["answer"]):
#     return "END"
# else:
#     return "searcher"  # Try again with refined query
```

**Reading:**
[BOOK] **"LangGraph How-To Guides"**  
URL: https://langchain-ai.github.io/langgraph/how-tos/  
Read: State management and conditional edges (15 min)

#### **2.3 Advanced LangGraph Patterns** (25 min)

**Subgraphs:**
```
Main Graph:
  Coordinator
    |
    v
  [Research Subgraph] <- Complex multi-step research
    |
    v
  Synthesizer
```

**Parallel Execution:**
```
Query: "Compare BERT, GPT, and T5"
    |
    +-> [Search BERT] ----+
    |                      |
    +-> [Search GPT] ------+-> [Combine]
    |                      |
    +-> [Search T5] -------+
```

**Human-in-the-Loop:**
```
Generator -> [Human Review] -> Approve/Edit -> Continue
                              |
                              v
                           Reject -> Regenerate
```

**Checkpointing:**
```
# Save state at each node
# Resume from checkpoint if failure
# Useful for long-running agents
```

**Reading:**
[BOOK] **"Advanced LangGraph"** - LangGraph Docs  
URL: https://langchain-ai.github.io/langgraph/concepts/low_level/  
Read: Checkpointing and subgraphs (10 min)

---

### **MODULE 3: Multi-Agent Orchestration** [TIME] 60 minutes

#### **3.1 Multi-Agent Patterns** (25 min)

**Hierarchical:**
```
Manager Agent
    |
    +-> Researcher Agent (finds papers)
    |
    +-> Analyst Agent (analyzes content)
    |
    +-> Writer Agent (creates response)
```

**Collaborative:**
```
Agent 1: "I found 5 papers on transformers"
Agent 2: "I analyzed their methodologies"
Agent 3: "I compared their results"
Shared Memory: All agents can see each other's outputs
```

**Sequential:**
```
Query -> Agent A -> Agent B -> Agent C -> Final Answer
         (search)   (analyze) (generate)
```

**Debate:**
```
Agent A: "BERT is better because..."
Agent B: "No, GPT is better because..."
Moderator: "Let's synthesize both views..."
```

**Video:**
[VIDEO] **"Multi-Agent Systems"**  
URL: https://www.youtube.com/results?search_query=multi+agent+systems+llm  
Watch: Any overview (15 min)

#### **3.2 Agent Communication** (20 min)

**Shared State:**
```python
# REQUIREMENTS ONLY

# All agents read/write to shared state:
# {
#   "query": "...",
#   "searcher_results": [...],
#   "analyst_insights": [...],
#   "writer_draft": "..."
# }

# Advantages:
# - Simple coordination
# - All agents see full context

# Disadvantages:
# - Can get messy with many agents
# - Harder to debug
```

**Message Passing:**
```python
# REQUIREMENTS ONLY

# Agents send messages to each other:
# Searcher -> Analyst: {"papers": [...]}
# Analyst -> Writer: {"key_points": [...]}
# Writer -> END: {"answer": "..."}

# Advantages:
# - Clear communication
# - Easier to test

# Disadvantages:
# - More complex orchestration
```

#### **3.3 Tool Calling in Agents** (15 min)

**What are Tools:**
```python
# REQUIREMENTS ONLY

# Tools are functions agents can call:
# - search_papers(query: str) -> List[Paper]
# - calculate(expression: str) -> float
# - fetch_url(url: str) -> str
# - send_email(to: str, subject: str, body: str) -> bool

# Agent decides:
# 1. Which tool to use
# 2. What parameters to pass
# 3. How to use the result
```

**Tool Selection:**
```
Agent thought: "User wants paper count"
Available tools:
  - search_papers: "Search academic papers"
  - count_papers: "Count papers in database"
  - calculate: "Perform calculation"

Agent decision: Use count_papers() <- Most relevant
```

**Reading:**
[BOOK] **"Tool Calling in LangChain"**  
URL: https://python.langchain.com/docs/concepts/tool_calling/  
Read: Function calling (10 min)

---

### **MODULE 4: Telegram Bot Development** [TIME] 60 minutes

#### **4.1 Telegram Bot Basics** (25 min)

**Video:**
[VIDEO] **"Python Telegram Bot Tutorial"**  
URL: https://www.youtube.com/results?search_query=python+telegram+bot+tutorial  
Watch: Any beginner tutorial (20 min)

**What is a Telegram Bot:**
- Automated account in Telegram
- Responds to messages
- Can send text, images, buttons
- Free API (no limits)
- Good for: Demos, internal tools, notifications

**Creating a Bot:**
1. Talk to @BotFather on Telegram
2. Use /newbot command
3. Choose name and username
4. Receive bot token (like API key)
5. Use token to send/receive messages

**Bot Capabilities:**
- Receive messages from users
- Send text responses
- Send formatted messages (markdown/HTML)
- Send inline buttons
- Handle commands (/start, /help, /search)
- Group chat support

**Reading:**
[BOOK] **"Telegram Bot API"**  
URL: https://core.telegram.org/bots/api  
Read: Getting started (10 min)

#### **4.2 python-telegram-bot Library** (20 min)

**Installation:**
```bash
pip install python-telegram-bot
```

**Core Concepts:**

**1. Application:**
```python
# REQUIREMENTS ONLY

# Main bot application:
# - Handle updates (messages, commands)
# - Route to handlers
# - Manage conversation state
```

**2. Handlers:**
```python
# REQUIREMENTS ONLY

# Different handler types:
# - CommandHandler: /start, /help, /search
# - MessageHandler: Regular text messages
# - CallbackQueryHandler: Button presses

# Each handler:
# - Matches specific pattern
# - Calls function when matched
# - Can access message context
```

**3. Context:**
```python
# REQUIREMENTS ONLY

# Update object contains:
# - message.text: User's message
# - message.from_user: User info
# - message.chat: Chat info

# Context object provides:
# - bot: Send messages
# - user_data: Per-user storage
# - chat_data: Per-chat storage
```

**Webhook vs Polling:**

```
Polling (Good for Development):
- Bot asks Telegram: "Any new messages?"
- Every 1-2 seconds
- Simple to set up
- Works on localhost

Webhook (Good for Production):
- Telegram sends messages to your URL
- Real-time delivery
- More efficient
- Requires public HTTPS endpoint
```

**For learning:** Polling is sufficient

**Reading:**
[BOOK] **"python-telegram-bot Wiki"**  
URL: https://docs.python-telegram-bot.org/  
Read: Introduction and Your First Bot (10 min)

#### **4.3 Integrating with RAG** (15 min)

**Bot Workflow:**
```
User sends message to bot
    |
    v
Bot receives update
    |
    v
Extract message text
    |
    v
Call RAG endpoint (/api/v1/ask)
    |
    v
Get answer + sources
    |
    v
Format response with markdown
    |
    v
Send back to user
```

**Response Formatting:**
```
# REQUIREMENTS ONLY

# Telegram supports markdown:
# *bold*
# _italic_
# [link text](URL)
# `code`

# Good RAG response format:
# Answer: [answer text]
#
# Sources:
# 1. [Paper Title](arxiv_url)
# 2. [Paper Title](arxiv_url)
```

**Commands to Implement:**
```
/start - Welcome message
/help - How to use the bot
/search [query] - Search papers (without RAG)
/ask [question] - Ask question (with RAG)
/settings - Configure preferences
```

**Reading:**
[BOOK] **"Formatting Telegram Messages"**  
URL: https://core.telegram.org/bots/api#formatting-options  
Read: Markdown and HTML modes (10 min)

---

### **MODULE 5: Langfuse Observability** [TIME] 90 minutes

#### **5.1 Why LLM Observability?** (30 min)

**Video:**
[VIDEO] **"LLM Observability Explained"**  
URL: https://www.youtube.com/watch?v=bG5pOqhIFME  
Watch: Langfuse overview (10 min)

**The Problem:**

Without observability:
```
User: "Answer is wrong"
You: [Check logs]
Logs: "LLM generated answer"
You: "???" (No idea what happened inside LLM)
```

With observability:
```
User: "Answer is wrong"
You: [Check Langfuse]
Langfuse shows:
  - Prompt used: "..."
  - Context chunks: [Paper A, Paper B]
  - LLM response: "..."
  - Token count: 1234
  - Latency: 15.2s
  - Cost: $0.05
You: "Ah! Wrong chunks retrieved, search query needs refinement"
```

**What Langfuse Tracks:**

**Traces:** Complete request flow
```
Search Query Trace:
  |
  +-> Embedding Generation (500ms, $0.001)
  |
  +-> Hybrid Search (200ms, $0)
  |
  +-> LLM Generation (15s, $0.05)
      |
      +-> Prompt: "..."
      +-> Completion: "..."
      +-> Tokens: input=500, output=200
```

**Generations:** Individual LLM calls
```
Model: llama3.2:1b
Input tokens: 500
Output tokens: 200
Latency: 15.2s
Temperature: 0.3
```

**Scores:** Quality metrics
```
User feedback: thumbs_up
Correctness: 0.85 (auto-evaluated)
Relevance: 0.92
Hallucination: 0.05 (low is good)
```

**Reading:**
[BOOK] **"Why Observability for LLMs"** - Langfuse  
URL: https://langfuse.com/blog/2024-04-python-decorator  
Read: Introduction section (10 min)

#### **5.2 Langfuse Setup** (30 min)

**What is Langfuse:**
- Open-source LLM observability platform
- Self-hostable (Docker)
- Tracks prompts, completions, costs
- User feedback collection
- Analytics dashboard

**Architecture:**
```
Your RAG Application
    |
    v
Langfuse SDK (Python decorator)
    |
    v
Langfuse Server (Docker)
    |
    v
PostgreSQL (traces storage)
    |
    v
Web UI (analytics dashboard)
```

**Docker Setup:**
```yaml
# REQUIREMENTS ONLY

# Services needed in docker-compose:
# - langfuse-web: Web interface (port 3000)
# - langfuse-worker: Background processing
# - langfuse-postgres: Data storage
# - langfuse-redis: Caching
# - langfuse-minio: S3-compatible storage (for exports)
# - clickhouse: Analytics database
```

**Integration:**
```python
# REQUIREMENTS ONLY

# Decorator pattern:
# @observe() on any function to track it
# @observe(as_type="generation") for LLM calls

# Automatically captures:
# - Function inputs/outputs
# - Execution time
# - Nested calls (parent-child traces)
# - Errors and exceptions
```

**Reading:**
[BOOK] **"Langfuse Quickstart"**  
URL: https://langfuse.com/docs/get-started  
Read: Self-hosting and Python SDK (15 min)

#### **5.3 Langfuse in Production** (30 min)

**Key Metrics to Track:**

**Performance:**
- Average latency per endpoint
- p95, p99 latencies
- Throughput (requests/second)

**Cost:**
- Token usage (input + output)
- Cost per request
- Daily/monthly costs
- Cost by user

**Quality:**
- User feedback (thumbs up/down)
- Hallucination rate
- Citation accuracy
- Answer completeness

**Usage:**
- Requests per day
- Popular queries
- User retention
- Error rate

**Dashboard Views:**

**1. Traces Dashboard:**
- See all requests
- Filter by user, date, status
- Drill down into specific traces

**2. Analytics Dashboard:**
- Charts: latency over time
- Token usage trends
- Cost breakdown
- User activity

**3. Prompt Management:**
- Version prompts
- A/B test different prompts
- Track prompt performance

**Alerting:**
```
Alert if:
- Average latency >10s
- Error rate >5%
- Daily cost >$50
- Hallucination score >0.2
```

**Reading:**
[BOOK] **"Langfuse Features"**  
URL: https://langfuse.com/docs/analytics  
Read: Analytics and scores (10 min)

**Example:**
[BOOK] **"Langfuse Demo"**  
URL: https://cloud.langfuse.com/  
Browse: Public demo dashboard (10 min)

---

## HANDS-ON EXERCISES

### **Exercise 1: Design Agent Workflow**

**Task:** Design LangGraph workflow for this query:

"Which papers improved upon the Transformer architecture and what were the key innovations?"

**Requirements:**
1. Plan: What steps needed?
2. Nodes: What functions?
3. Edges: How to connect?
4. Routing: When to iterate vs finish?

**Expected workflow:**
```
START
  |
  v
[Query Analyzer]
  |
  v
[Multi-Query Planner]
  |  "Transformer architecture"
  |  "Improvements over Transformer"
  |  "BERT GPT T5 innovations"
  v
[Parallel Searcher] (3 searches)
  |
  v
[Result Aggregator]
  |
  v
[Comparison Generator]
  |
  v
[Quality Checker]
  |
  +-> Good -> END
  |
  +-> Poor -> [Refine Query] -> Back to Search
```

---

### **Exercise 2: Telegram Bot Commands**

**Task:** Design bot command handlers

**Commands:**
1. /start - What to show?
2. /help - What instructions?
3. /ask - How to handle question?
4. /settings - What options?

**Expected responses:**
```
/start:
"Welcome to arXiv RAG Bot!
Ask questions about ML papers.
Use /help for more info."

/help:
"Commands:
/ask [question] - Ask about papers
/search [terms] - Find papers
/settings - Configure preferences"

/ask What are transformers:
"[Searching papers...]
Answer: Transformers are neural...
Sources:
1. Attention Is All You Need
2. BERT: Pre-training..."
```

---

### **Exercise 3: Trace Design**

**Task:** Design Langfuse trace for RAG request

**Request:** User asks "What are transformers?"

**Expected trace structure:**
```
Trace: rag_request
  |
  +-> Span: query_processing (50ms)
  |
  +-> Span: hybrid_search (300ms)
  |   |
  |   +-> Generation: embedding (100ms, $0.001)
  |   +-> Search: bm25 (50ms)
  |   +-> Search: vector (150ms)
  |
  +-> Generation: llm_answer (15s, $0.05)
      |
      +-> Input: 500 tokens
      +-> Output: 200 tokens
      +-> Model: llama3.2:1b
      +-> Temperature: 0.3

Total: 15.35s, $0.051
```

---

## RESEARCH QUESTIONS

### **Conceptual Questions:**

1. **What makes an AI system "agentic"?**
   - How is it different from traditional RAG?
   - What capabilities define an agent?

2. **What is LangGraph?**
   - How is it different from LangChain?
   - When to use each?

3. **What is multi-agent orchestration?**
   - When to use multiple agents vs single agent?
   - How do agents communicate?

4. **Why use Telegram for bots?**
   - What are advantages vs web interface?
   - What are limitations?

5. **What is LLM observability?**
   - What's different from regular logging?
   - Why is it necessary?

6. **What is a trace?**
   - How is it different from a log entry?
   - What does it track?

### **Practical Questions:**

1. **How do you design an agent workflow?**
   - What nodes to include?
   - How to handle failures?
   - When to iterate?

2. **How do you prevent infinite loops in agents?**
   - Maximum iterations?
   - Quality thresholds?

3. **How do you test agent behavior?**
   - What scenarios to test?
   - How to verify quality?

4. **How do you handle errors in Telegram bots?**
   - Network failures?
   - Invalid commands?

5. **How do you optimize LLM costs?**
   - Token reduction strategies?
   - Caching opportunities?

6. **How do you evaluate agent performance?**
   - What metrics matter?
   - How to improve over time?

---

## KEY TAKEAWAYS

**Remember these 12 things:**

1. **Agents = Autonomous decision-making**
   - Plan, act, observe, reflect
   - Use tools independently
   - Iterate until satisfied

2. **LangGraph = State machines for agents**
   - Nodes are functions
   - Edges are transitions
   - State flows through graph

3. **ReAct = Thought -> Action -> Observation**
   - Agent reasoning pattern
   - Balances thinking and doing

4. **Multi-hop = Complex question decomposition**
   - Break into subtasks
   - Execute sequentially or parallel
   - Synthesize results

5. **Reflection = Self-critique**
   - Evaluate own outputs
   - Identify gaps
   - Improve iteratively

6. **Tool calling = Agent capabilities**
   - Search, calculate, fetch data
   - Agent chooses which tool
   - Uses results to inform next step

7. **Telegram bots = Easy chat interface**
   - Free, no hosting needed for small scale
   - Rich formatting (markdown, buttons)
   - Good for demos and internal tools

8. **Langfuse = LLM observability**
   - Track prompts and completions
   - Monitor costs and latency
   - Collect user feedback
   - Debug production issues

9. **Traces = Request flow visualization**
   - See every step
   - Find bottlenecks
   - Debug errors

10. **Observability = Production requirement**
    - Can't improve what you can't measure
    - Essential for LLM applications
    - Helps justify costs

11. **State management = Critical for agents**
    - Shared state vs message passing
    - Persistence for long workflows
    - Checkpointing for reliability

12. **Iteration limits = Prevent infinite loops**
    - Max 3-5 iterations typical
    - Quality threshold for early exit
    - Timeout for safety

**If you understand these 12:** Agentic RAG ready! [CHECK]

---

## ADDITIONAL RESOURCES (Optional Deep Dives)

### **AI Agents:**
- "Building LLM Agents" - DeepLearning.AI: https://www.deeplearning.ai/short-courses/
- AutoGPT: https://github.com/Significant-Gravitas/AutoGPT
- Agent Papers: https://github.com/AGI-Edgerunners/LLM-Agents-Papers

### **LangGraph:**
- Official Docs: https://langchain-ai.github.io/langgraph/
- Tutorials: https://langchain-ai.github.io/langgraph/tutorials/
- Examples: https://github.com/langchain-ai/langgraph/tree/main/examples

### **Multi-Agent Systems:**
- CAMEL: https://github.com/camel-ai/camel
- AutoGen: https://github.com/microsoft/autogen
- CrewAI: https://github.com/joaomdmoura/crewAI

### **Telegram Bots:**
- python-telegram-bot: https://docs.python-telegram-bot.org/
- Bot Examples: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
- Telegram Bot API: https://core.telegram.org/bots/api

### **Langfuse:**
- Documentation: https://langfuse.com/docs
- Cookbook: https://langfuse.com/docs/cookbook
- GitHub: https://github.com/langfuse/langfuse
- Discord: https://discord.gg/7NXusRtqYU

---

## AFTER LEARNING

### **You're ready to build Steps 25-28 when you can:**

**Knowledge Check:**
- [ ] Explain what makes a system "agentic"
- [ ] Understand LangGraph state machines
- [ ] Design multi-step agent workflows
- [ ] Implement ReAct pattern conceptually
- [ ] Create Telegram bot handlers
- [ ] Integrate Langfuse tracking
- [ ] Design effective traces
- [ ] Understand tool calling

**Practical Check:**
- [ ] Can design agent workflow for complex question
- [ ] Can choose appropriate agent pattern
- [ ] Can handle Telegram bot commands
- [ ] Can set up Langfuse tracing
- [ ] Can analyze traces to debug issues
- [ ] Can calculate LLM costs from traces
- [ ] Can prevent infinite agent loops

**Then proceed to:**
- **STEP25_COMPLETE.md** - LangGraph agent foundation
- **STEP26_COMPLETE.md** - Multi-hop agentic retrieval
- **STEP27_COMPLETE.md** - Telegram bot integration
- **STEP28_COMPLETE.md** - Langfuse observability

---

## WEEK 11 SUCCESS METRICS

**By end of this week, you'll have:**
- [TARGET] LangGraph agent with multi-hop retrieval
- [TARGET] Self-reflection and quality checking
- [TARGET] Telegram bot interface
- [TARGET] Langfuse observability tracking all operations
- [TARGET] Complete agentic RAG system
- [TARGET] Production-ready with full monitoring

**Quality Targets:**
- Agent successfully answers complex questions (>2 hops)
- Reflection improves answer quality >20%
- Telegram bot responds <30s
- All LLM calls traced in Langfuse
- Cost tracking accurate to $0.01

**User Experience:**
- Ask complex question via Telegram
- Bot shows "thinking..." indicator
- Multi-step research visible
- Comprehensive answer with sources
- Observable in Langfuse dashboard

**System Capabilities:**
- Handle multi-part questions
- Iterate if initial answer insufficient
- Self-verify answer quality
- Provide detailed traces
- Track costs per request

---

**Time estimate:** 5-6 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Total week time:** ~18-20 hours (learning + implementation)

---

**Document Generated:** December 28, 2025  
**For:** Career Transition Week 11 (MOAI Week 7)  
**Status:** Agentic RAG with Observability - Ready for Steps 25-28  
**Format:** Clean ASCII - No Character Corruption  
**Completes:** Full MOAI Project Implementation Path
