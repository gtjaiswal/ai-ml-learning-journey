# WEEK 15 LEARNING GUIDE: Agent Foundations

**Timeline:** February 23 - March 1, 2026  
**Total Time:** ~11-12 hours  
**Focus:** ReAct pattern, tool use basics, LangChain/LangGraph fundamentals

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Basic ReAct agent with reasoning traces
- Tool-calling agent with function execution
- LangChain agent with memory
- First multi-step agent workflow

**What You'll Learn:**
- ReAct (Reasoning + Acting) pattern
- Tool/function calling mechanics
- LangChain agent architecture
- LangGraph state machines
- Agent evaluation and debugging

**Time Allocation:**
- Mon-Fri: 1-1.5 hours/day (7-7.5h total)
- Weekend: 4-4.5 hours (2-2.5h Sat, 2h Sun)
- Total: 11-12 hours

---

## DAY 1 (MONDAY): ReAct Pattern Fundamentals

**Time:** 1.5 hours

---

### SESSION 1: Understanding ReAct (45 min)

**Video 1: "What are AI Agents?"** - IBM Technology  
- URL: https://www.youtube.com/watch?v=F8NKVhkZZWI
- Duration: 7:31
- What you'll learn: Agent vs LLM, autonomy, tool use

**Video 2: "ReAct: Reasoning and Acting"** - Yannic Kilcher  
- URL: https://www.youtube.com/watch?v=Eug2clsLtFs
- Duration: 23:17
- Watch: First 15 minutes (ReAct framework explanation)

**Reading:**
📖 **ReAct Paper (Original)**  
- URL: https://arxiv.org/abs/2210.03629
- Duration: 20 min read
- Focus: Abstract, Introduction, Figure 1 (ReAct example)

**What you need to understand:**

**Traditional LLM:**
```
User: What's the weather in London?
LLM: I don't have access to real-time data...
```

**ReAct Agent:**
```
User: What's the weather in London?

Thought: I need to check current weather data
Action: search("London weather today")
Observation: Sunny, 18°C

Thought: I have the information needed
Final Answer: It's currently sunny and 18°C in London
```

**Key Components:**

1. **Thought:** Internal reasoning
2. **Action:** Tool to execute
3. **Observation:** Tool result
4. **Repeat** until answer found

**Why ReAct Works:**
- Makes reasoning explicit (debuggable)
- Grounds responses in real data
- Prevents hallucination
- Enables complex multi-step tasks

---

### SESSION 2: ReAct Pattern Design (45 min)

**Hands-On Exercise: ReAct Prompt Design**

**Requirements:**
Create `REACT_PATTERN.md` documenting:

**1. ReAct Prompt Template:**

Design prompt structure:
```
You are an AI assistant that uses the ReAct pattern.
For each query, you should:

1. **Thought:** Analyze what you need to do
2. **Action:** Choose a tool to use (if needed)
3. **Observation:** Process the tool result
4. Repeat until you have enough information
5. **Final Answer:** Provide the complete response

Available tools:
- search(query): Search the web
- calculator(expression): Perform calculations
- get_current_time(): Get current time

Format your response exactly as:
Thought: [your reasoning]
Action: [tool_name(arguments)]
Observation: [will be provided by system]
... (repeat as needed)
Final Answer: [complete answer to user]
```

**2. Example Traces:**

Create 3 complete ReAct traces:

**Example 1: Simple Lookup**
```
User: What's the capital of France?

Thought: This is a factual question I should know
Action: None needed
Final Answer: The capital of France is Paris.
```

**Example 2: Calculation**
```
User: What's 15% of $1,250?

Thought: I need to calculate this precisely
Action: calculator(1250 * 0.15)
Observation: 187.5

Thought: I have the answer
Final Answer: 15% of $1,250 is $187.50
```

**Example 3: Multi-step**
```
User: How many days until Christmas?

Thought: I need current date first
Action: get_current_time()
Observation: 2026-03-01

Thought: Christmas is Dec 25, need to calculate days
Action: calculator(days_between("2026-03-01", "2026-12-25"))
Observation: 299

Thought: I have the answer
Final Answer: There are 299 days until Christmas.
```

**3. Error Cases:**

Design handling for:
- Tool doesn't exist
- Tool returns error
- Infinite loop (too many steps)
- Invalid action format
- No final answer provided

**What to figure out:**
- How to enforce format compliance
- Maximum steps before timeout
- When to force final answer
- How to handle ambiguous queries
- Whether to allow tool combinations

**Success criteria:**
✅ Complete ReAct prompt template  
✅ 3 diverse example traces  
✅ Error handling strategy  
✅ Format validation rules  
✅ Understand reasoning → action → observation flow

---

## DAY 2 (TUESDAY): Tool/Function Calling Basics

**Time:** 1.5 hours

---

### SESSION 1: Function Calling Mechanics (45 min)

**Video: "Function Calling in LLMs"** - OpenAI DevDay  
- URL: https://www.youtube.com/watch?v=3FPOobnePPo
- Duration: 6:12
- What you'll learn: How function calling works

**Reading:**
📖 **OpenAI Function Calling Guide**  
- URL: https://platform.openai.com/docs/guides/function-calling
- Duration: 20 min read
- Focus: Introduction, Parallel function calling, Best practices

**What you need to understand:**

**How Function Calling Works:**

1. **Define Tools:**
```json
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {"type": "string"},
      "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
    },
    "required": ["location"]
  }
}
```

2. **LLM Chooses Tool:**
```json
{
  "role": "assistant",
  "tool_calls": [{
    "function": {
      "name": "get_weather",
      "arguments": "{\"location\": \"London\", \"units\": \"celsius\"}"
    }
  }]
}
```

3. **Execute Function:**
```python
# Your code executes the actual function
result = get_weather(location="London", units="celsius")
# Returns: {"temperature": 18, "conditions": "sunny"}
```

4. **Return Result to LLM:**
```json
{
  "role": "tool",
  "content": "{\"temperature\": 18, \"conditions\": \"sunny\"}"
}
```

5. **LLM Generates Final Response:**
```
"It's currently 18°C and sunny in London."
```

**Key Concepts:**
- LLM doesn't execute functions (you do!)
- LLM only generates function calls
- You parse, execute, return results
- Structured outputs prevent errors

---

### SESSION 2: Tool Definition Design (45 min)

**Hands-On Exercise: Tool Schema Design**

**Requirements:**
Create `TOOL_DEFINITIONS.md` with 5 tool schemas:

**1. Search Tool:**
```json
{
  "name": "search_web",
  "description": "Search the internet for current information",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query"
      },
      "num_results": {
        "type": "integer",
        "description": "Number of results to return",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

**2. Calculator Tool:**
```json
{
  "name": "calculate",
  "description": "Perform mathematical calculations. ALWAYS use this for arithmetic instead of calculating yourself.",
  "parameters": {
    "type": "object",
    "properties": {
      "expression": {
        "type": "string",
        "description": "Mathematical expression to evaluate (e.g., '10 + 15', '1250 * 0.15')"
      }
    },
    "required": ["expression"]
  }
}
```

**3. Database Query Tool:**
Design schema for tool that:
- Queries papers database
- Accepts: category, date range, limit
- Returns: list of papers matching criteria

**4. Document Retrieval Tool:**
Design schema for tool that:
- Retrieves document by ID
- Accepts: paper_id
- Returns: full paper content

**5. Time Tool:**
Design schema for tool that:
- Gets current time/date
- Accepts: timezone (optional)
- Returns: ISO 8601 timestamp

**What to figure out:**
- How detailed should descriptions be?
- When to use enums vs strings?
- How to handle optional parameters?
- How to prevent LLM from bypassing tools (e.g., doing math itself)?
- How to validate parameter types?

**Success criteria:**
✅ 5 complete tool schemas  
✅ Clear, specific descriptions  
✅ Proper parameter types  
✅ Required vs optional fields marked  
✅ Understand how LLM uses descriptions

---

## DAY 3 (WEDNESDAY): LangChain Fundamentals

**Time:** 1.5 hours

---

### SESSION 1: LangChain Architecture (45 min)

**Video: "LangChain Explained"** - Sam Witteveen  
- URL: https://www.youtube.com/watch?v=_v_fgW2SkkQ
- Duration: 14:16
- What you'll learn: LangChain components, agents, chains

**Reading:**
📖 **LangChain Documentation - Introduction**  
- URL: https://python.langchain.com/docs/get_started/introduction
- Duration: 15 min read

**Reading:**
📖 **LangChain Agents Concepts**  
- URL: https://python.langchain.com/docs/modules/agents/
- Duration: 15 min read
- Focus: Agent types, Agent executors

**What you need to understand:**

**LangChain Components:**

**1. LLMs:**
- Chat models (OpenAI, Anthropic)
- Completion models
- Model I/O abstraction

**2. Prompts:**
- PromptTemplates
- ChatPromptTemplates
- Few-shot examples
- Output parsers

**3. Chains:**
- LLMChain (basic)
- Sequential chains
- Router chains
- Custom chains

**4. Agents:**
- ReAct agents
- Conversational agents
- OpenAI Functions agents
- Custom agents

**5. Tools:**
- Pre-built tools (search, math, etc.)
- Custom tools
- Tool calling interface

**6. Memory:**
- ConversationBufferMemory
- ConversationSummaryMemory
- VectorStoreMemory
- Custom memory

**Agent Execution Flow:**
```
User Input
    ↓
Agent (decides next action)
    ↓
Tool Execution
    ↓
Observation
    ↓
Agent (decides if done or continue)
    ↓
Final Answer
```

---

### SESSION 2: Agent Types Comparison (45 min)

**Hands-On Exercise: Agent Types Analysis**

**Requirements:**
Create `AGENT_TYPES_COMPARISON.md`:

**1. ReAct Agent:**

**When to use:**
- Need visible reasoning steps
- Debugging important
- Educational/transparent systems

**Strengths:**
- Explicit reasoning
- Easy to debug
- Understandable by humans

**Weaknesses:**
- More tokens/slower
- Can get stuck in reasoning loops
- Requires good prompt engineering

**Example use case:**
Research assistant explaining findings step-by-step

**2. OpenAI Functions Agent:**

**When to use:**
- Using OpenAI models
- Need structured outputs
- Parallel tool calling needed

**Strengths:**
- Native function calling
- Parallel execution
- Structured output
- Less prompt engineering

**Weaknesses:**
- OpenAI-specific
- Less transparent reasoning
- Costs more (function calling overhead)

**Example use case:**
Data analysis agent calling multiple APIs simultaneously

**3. Conversational Agent:**

**When to use:**
- Multi-turn conversations
- Context from previous messages matters
- Chat applications

**Strengths:**
- Maintains conversation history
- Natural dialogue flow
- Can reference previous context

**Weaknesses:**
- Token usage grows with conversation
- May get confused with long conversations
- Need memory management

**Example use case:**
Customer service chatbot

**4. Self-Ask Agent:**

**When to use:**
- Complex multi-step reasoning
- Need to break down problems
- Research-style queries

**Strengths:**
- Good at decomposition
- Systematic approach
- Handles complex questions

**Weaknesses:**
- Can be slow (many LLM calls)
- May over-decompose simple questions
- Requires search tool

**Example use case:**
Answering complex analytical questions

**What to figure out:**
- Which agent type for your fraud detection system?
- When to use which agent?
- How to combine agent types?
- Cost/performance trade-offs?

**Success criteria:**
✅ Compared 4+ agent types  
✅ Identified strengths/weaknesses  
✅ Mapped use cases to agent types  
✅ Understand trade-offs  
✅ Can justify agent selection

---

## DAY 4 (THURSDAY): LangGraph State Machines

**Time:** 1.5 hours

---

### SESSION 1: LangGraph Fundamentals (45 min)

**Video: "LangGraph Tutorial"** - LangChain  
- URL: https://www.youtube.com/watch?v=9BPCV5TYPmg
- Duration: 12:27
- What you'll learn: State graphs, nodes, edges

**Reading:**
📖 **LangGraph Documentation**  
- URL: https://langchain-ai.github.io/langgraph/
- Duration: 20 min read
- Focus: Quick start, Core concepts

**What you need to understand:**

**Why LangGraph?**
- Agents need complex control flow
- Not just sequential steps
- Conditional branching
- Loops and retries
- State management

**LangGraph Concepts:**

**1. State:**
```python
class AgentState(TypedDict):
    messages: List[Message]
    current_step: str
    tool_results: Dict
    retry_count: int
```

**2. Nodes:**
- Functions that process state
- Can be LLM calls, tool executions, logic
- Return updated state

**3. Edges:**
- Connect nodes
- Can be conditional
- Define flow control

**4. Graph:**
```
START → Analyze Query → [Decision]
                            ↓
                    Need Tool? → Execute Tool → Process Result
                            ↓
                    Have Answer? → Format Response → END
```

**Example Workflow:**
```python
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("analyze", analyze_query)
graph.add_node("execute_tool", execute_tool)
graph.add_node("format", format_response)

# Add edges
graph.add_edge(START, "analyze")
graph.add_conditional_edges(
    "analyze",
    should_use_tool,  # Function that returns "tool" or "format"
    {
        "tool": "execute_tool",
        "format": "format"
    }
)
graph.add_edge("execute_tool", "analyze")  # Loop back
graph.add_edge("format", END)
```

---

### SESSION 2: State Machine Design (45 min)

**Hands-On Exercise: Agent State Machine**

**Requirements:**
Create `AGENT_STATE_MACHINE.md`:

**Design state machine for fraud detection agent:**

**1. State Definition:**
```python
class FraudAgentState(TypedDict):
    # What state do you need to track?
    # - User query
    # - Transaction data
    # - Analysis steps taken
    # - Tool results
    # - Confidence score
    # - Final decision
```

**2. Nodes (Functions):**

**Node: parse_query**
- Input: User query
- Process: Extract transaction ID, question type
- Output: Structured query info

**Node: fetch_transaction**
- Input: Transaction ID
- Process: Query database
- Output: Transaction details

**Node: analyze_risk**
- Input: Transaction data
- Process: LLM analyzes patterns
- Output: Risk factors identified

**Node: calculate_score**
- Input: Risk factors
- Process: Use calculator tool
- Output: Risk score (0-100)

**Node: make_decision**
- Input: Risk score
- Process: Apply thresholds
- Output: APPROVE/REVIEW/REJECT

**Node: format_response**
- Input: Decision + reasoning
- Process: Format for user
- Output: Final response

**3. Edges (Control Flow):**

Map out all transitions:
- START → parse_query
- parse_query → fetch_transaction
- fetch_transaction → analyze_risk
- analyze_risk → calculate_score (conditional: if complex math needed)
- analyze_risk → make_decision (conditional: if simple logic)
- calculate_score → make_decision
- make_decision → format_response
- format_response → END

**4. Conditional Logic:**

**Condition: needs_calculation**
```python
def needs_calculation(state):
    # When do you need calculator tool?
    # - Multiple risk factors to weight
    # - Probability calculations
    # - Threshold comparisons
    return "calculate" if complex_math else "decide"
```

**Condition: needs_retry**
```python
def needs_retry(state):
    # When to retry analysis?
    # - Low confidence
    # - Missing data
    # - Tool error
    return "retry" if should_retry else "proceed"
```

**5. Error Handling:**

Design error paths:
- Database query fails → retry or use cached data?
- LLM returns invalid format → re-prompt or use default?
- Calculator error → manual review?
- Max retries exceeded → escalate to human?

**What to figure out:**
- What state to track at each step?
- When to loop vs proceed?
- How many retries before giving up?
- When to escalate to human?
- How to maintain audit trail in state?

**Success criteria:**
✅ Complete state definition  
✅ All nodes defined with inputs/outputs  
✅ Control flow mapped  
✅ Conditional logic specified  
✅ Error handling designed  
✅ Can explain why this structure

---

## DAY 5 (FRIDAY): Agent Evaluation & Debugging

**Time:** 1 hour

---

### SESSION 1: Agent Evaluation Metrics (30 min)

**Reading:**
📖 **Agent Evaluation Guide**  
- URL: https://python.langchain.com/docs/guides/productionization/evaluation/
- Duration: 15 min read

**Hands-On Exercise: Evaluation Framework**

**Requirements:**
Create `AGENT_EVALUATION.md`:

**1. Success Metrics:**

**Task Completion:**
- Did agent complete the task?
- Correct final answer?
- All required steps taken?

**Efficiency:**
- Number of tool calls
- Total tokens used
- Time to completion
- Unnecessary steps?

**Quality:**
- Reasoning clarity
- Error handling
- Edge case handling
- Response format compliance

**2. Test Cases:**

Design 10 test cases:

**Easy (3 cases):**
1. Simple lookup: "What's transaction TX001 status?"
   - Expected: 1 tool call, direct answer
2. Basic calculation: "What's total amount for user U123?"
   - Expected: 1 database query, 1 calculation, answer
3. Status check: "Is transaction TX002 fraudulent?"
   - Expected: 1 lookup, clear yes/no

**Medium (4 cases):**
4. Multi-step: "Compare spending patterns for user U123 last month vs this month"
5. Conditional: "Flag all transactions over $1000 from new users"
6. Aggregation: "What's average transaction amount by category?"
7. Temporal: "Show high-risk transactions in last 7 days"

**Hard (3 cases):**
8. Complex reasoning: "Identify unusual patterns in user U123's behavior"
9. Ambiguous: "Is this transaction suspicious?" (without specifying which)
10. Error case: "Analyze transaction TX999" (doesn't exist)

**3. Evaluation Criteria:**

For each test case, define:
- Expected final answer
- Expected number of tool calls
- Expected reasoning steps
- Acceptable alternatives
- Failure conditions

**What to figure out:**
- How to measure "quality" objectively?
- When is efficiency vs accuracy more important?
- How to handle ambiguous queries in evaluation?
- What's acceptable error rate?

**Success criteria:**
✅ 3 success metrics defined  
✅ 10 test cases created  
✅ Evaluation criteria for each  
✅ Mix of difficulty levels  
✅ Understand what "good" looks like

---

### SESSION 2: Debugging Techniques (30 min)

**Reading:**
📖 **LangSmith Tracing**  
- URL: https://docs.smith.langchain.com/
- Duration: 15 min read
- Focus: Tracing, Debugging

**Hands-On Exercise: Debug Checklist**

**Requirements:**
Create `AGENT_DEBUGGING.md`:

**1. Common Issues:**

**Issue: Infinite Loops**
- Symptom: Agent doesn't reach final answer
- Causes: Poor stopping conditions, circular logic
- Debug: Check step count, trace tool calls
- Fix: Add max iterations, improve conditions

**Issue: Wrong Tool Selection**
- Symptom: Agent uses calculator when should search
- Causes: Unclear tool descriptions, poor prompting
- Debug: Review tool descriptions, test prompt
- Fix: Improve descriptions, add examples

**Issue: Invalid Tool Arguments**
- Symptom: Tool execution fails
- Causes: LLM generates wrong format
- Debug: Log LLM output, check schema
- Fix: Better schema description, validation

**Issue: No Final Answer**
- Symptom: Agent stops without responding
- Causes: Missing final answer prompt
- Debug: Check agent configuration
- Fix: Enforce final answer step

**Issue: Hallucinated Tools**
- Symptom: Agent tries to use non-existent tool
- Causes: LLM making up tools
- Debug: Review available tools list
- Fix: Explicitly list available tools in prompt

**2. Debugging Workflow:**

**Step 1: Reproduce**
- Run with same inputs
- Enable verbose logging
- Capture all intermediate steps

**Step 2: Trace**
- Log each tool call
- Log each LLM decision
- Log state changes

**Step 3: Identify**
- Where did it go wrong?
- Which step failed?
- What was the state?

**Step 4: Fix**
- Adjust prompt
- Fix tool schema
- Add validation
- Improve error handling

**Step 5: Test**
- Re-run original case
- Run related test cases
- Verify fix doesn't break others

**3. Logging Strategy:**

What to log:
- User input
- Each reasoning step
- Each tool call (name, args)
- Each tool result
- State transitions
- Final answer
- Errors and exceptions

**What to figure out:**
- How much logging is too much?
- How to make logs searchable?
- When to use LangSmith vs custom logging?
- How to log without exposing sensitive data?

**Success criteria:**
✅ 5+ common issues documented  
✅ Debug workflow defined  
✅ Logging strategy planned  
✅ Understand how to trace agent execution  
✅ Know how to fix common problems

---

## DAY 6 (SATURDAY): Build First Agent System

**Time:** 2.5 hours

---

### SESSION 1: Simple ReAct Agent (90 min)

**Requirements:**
Build basic ReAct agent with 2 tools.

**Tools to Implement:**

**Tool 1: Search Tool (Simulated)**
- Input: query string
- Output: Mock search results (hardcoded for testing)
- Don't actually call external API yet

**Tool 2: Calculator**
- Input: mathematical expression
- Output: Calculation result
- Use Python eval (safe subset) or math library

**Agent Requirements:**

**1. ReAct Prompt:**
Create prompt that:
- Explains ReAct pattern
- Lists available tools
- Shows format examples
- Enforces format compliance

**2. Parse LLM Output:**
Build parser that:
- Extracts "Thought" sections
- Extracts "Action" and arguments
- Detects "Final Answer"
- Handles malformed responses

**3. Execute Tools:**
Build executor that:
- Matches action name to tool
- Calls tool with arguments
- Returns observation
- Handles tool errors

**4. Agent Loop:**
Build loop that:
- Sends prompt to LLM
- Parses response
- Executes action (if any)
- Adds observation to history
- Repeats until final answer
- Enforces max iterations (10)

**5. Test Cases:**

Test with these queries:
1. "What is 15% of 1250?"
2. "Search for the capital of France"
3. "Calculate 100 + 50, then search for that number"
4. "What's 10 * 5?" (should use calculator, not answer directly)
5. "Search for Python programming" (no calculation needed)

**What to figure out:**
- How to parse LLM output reliably?
- How to handle when LLM doesn't follow format?
- When to stop the loop?
- How to prevent infinite loops?
- How to chain multiple tool calls?

**Success criteria:**
✅ Agent runs successfully  
✅ Both tools working  
✅ Can handle 3+ step reasoning  
✅ All 5 test cases pass  
✅ Logs all reasoning steps  
✅ Handles errors gracefully

---

### SESSION 2: Add Memory & Polish (60 min)

**Requirements:**

**1. Add Conversation Memory:**
Enable agent to:
- Remember previous queries in session
- Reference past results
- Maintain context across queries

Example conversation:
```
User: What's 10 + 5?
Agent: [uses calculator] The answer is 15.

User: Multiply that by 2
Agent: [remembers 15, calculates 15 * 2] The answer is 30.

User: What was my first question?
Agent: [from memory] Your first question was "What's 10 + 5?"
```

**2. Improve Error Handling:**

Handle these scenarios:
- LLM returns gibberish
- Tool execution fails
- Invalid tool name
- Missing tool arguments
- Maximum iterations exceeded
- Empty final answer

For each, define:
- How to detect
- What to do (retry, fallback, error message)
- How to log

**3. Add Tracing:**

Implement trace that shows:
```
=== Agent Trace ===
Step 1:
  Thought: I need to calculate 15% of 1250
  Action: calculator(1250 * 0.15)
  Observation: 187.5

Step 2:
  Thought: I have the answer
  Final Answer: 15% of $1,250 is $187.50

=== Summary ===
Total steps: 2
Tool calls: 1
Success: Yes
```

**4. Create Demo Script:**

Build script that:
- Starts agent
- Runs 5 example queries
- Shows trace for each
- Demonstrates memory
- Shows error handling

**What to figure out:**
- How to maintain conversation context?
- How long to keep memory?
- When to clear memory?
- How to display traces clearly?
- How to make demo impressive?

**Success criteria:**
✅ Conversation memory working  
✅ Can reference past queries  
✅ All error cases handled  
✅ Trace output clear and useful  
✅ Demo script polished  
✅ Ready to show working agent

---

## DAY 7 (SUNDAY): LangChain Agent Integration

**Time:** 2 hours

---

### SESSION 1: Rebuild with LangChain (60 min)

**Requirements:**
Rebuild Saturday's agent using LangChain framework.

**1. Install LangChain:**
```bash
pip install langchain langchain-openai
```

**2. Convert Tools:**
Convert your tools to LangChain format:
- Use `@tool` decorator
- Define proper schemas
- Add descriptions

**3. Create Agent:**
Use LangChain's agent:
- Choose agent type (ReAct recommended)
- Configure with your tools
- Set memory
- Configure verbose mode

**4. Test Compatibility:**
Run same 5 test cases from Day 6.
Verify:
- All tests pass
- Behavior is similar
- Traces are visible
- Memory works

**What to figure out:**
- How LangChain agent differs from custom?
- What does LangChain handle automatically?
- What trade-offs exist?
- When to use custom vs LangChain?
- How to debug LangChain agents?

**Success criteria:**
✅ LangChain agent working  
✅ Tools converted successfully  
✅ All test cases pass  
✅ Understand LangChain abstractions  
✅ Can compare custom vs framework approach

---

### SESSION 2: Agent Comparison & Documentation (60 min)

**Requirements:**

**1. Performance Comparison:**

Create `AGENT_COMPARISON.md`:

Compare custom agent vs LangChain:

**Metrics:**
- Lines of code
- Development time
- Flexibility
- Debugging ease
- Performance (speed, tokens)
- Maintainability

**Custom Agent:**
- Pros: ?
- Cons: ?
- When to use: ?

**LangChain Agent:**
- Pros: ?
- Cons: ?
- When to use: ?

**2. Week 15 Documentation:**

Create `WEEK15_SUMMARY.md`:

**What You Built:**
- ReAct agent from scratch
- Calculator + search tools
- Conversation memory
- LangChain integration

**What You Learned:**
- ReAct pattern mechanics
- Tool calling workflow
- Agent evaluation
- Debugging techniques
- LangChain framework

**Key Insights:**
- What was harder than expected?
- What surprised you?
- What would you do differently?
- What's still unclear?

**Next Steps:**
- Week 16 preview
- What to improve
- Questions to explore

**3. Portfolio Preparation:**

Prepare to showcase:
- Working agent demo
- Trace examples
- Code walkthrough
- Architecture diagram

**What to figure out:**
- Which approach is better for your use case?
- How to explain agent behavior in interview?
- What metrics matter most?
- How to demonstrate agent intelligence?

**Success criteria:**
✅ Detailed comparison completed  
✅ Week summary documented  
✅ Portfolio materials prepared  
✅ Can explain agent architecture  
✅ Ready for Week 16 (advanced tools)

---

## 📚 ADDITIONAL RESOURCES

**ReAct:**
- Original Paper: https://arxiv.org/abs/2210.03629
- Blog Post: https://blog.research.google/2022/11/react-synergizing-reasoning-and-acting.html

**LangChain:**
- Documentation: https://python.langchain.com/docs/get_started/introduction
- Agents Guide: https://python.langchain.com/docs/modules/agents/
- GitHub: https://github.com/langchain-ai/langchain

**LangGraph:**
- Documentation: https://langchain-ai.github.io/langgraph/
- Tutorials: https://github.com/langchain-ai/langgraph/tree/main/examples

**Function Calling:**
- OpenAI Guide: https://platform.openai.com/docs/guides/function-calling
- Anthropic Tool Use: https://docs.anthropic.com/claude/docs/tool-use

**Agent Patterns:**
- Agent Design Patterns: https://eugeneyan.com/writing/llm-patterns/
- AI Agents Overview: https://lilianweng.github.io/posts/2023-06-23-agent/

---

## ✅ WEEK 15 DELIVERABLES

**Documentation:**
- [ ] REACT_PATTERN.md - ReAct prompt template and examples
- [ ] TOOL_DEFINITIONS.md - 5 tool schemas
- [ ] AGENT_TYPES_COMPARISON.md - Agent types analysis
- [ ] AGENT_STATE_MACHINE.md - State machine design
- [ ] AGENT_EVALUATION.md - Test cases and metrics
- [ ] AGENT_DEBUGGING.md - Debug checklist
- [ ] AGENT_COMPARISON.md - Custom vs LangChain comparison
- [ ] WEEK15_SUMMARY.md - Week summary and insights

**Working Code:**
- [ ] Custom ReAct agent with 2 tools
- [ ] Conversation memory implementation
- [ ] Error handling system
- [ ] Trace logging
- [ ] LangChain agent implementation
- [ ] Demo script

**Understanding:**
- [ ] Can explain ReAct pattern
- [ ] Can explain function calling mechanics
- [ ] Can design tool schemas
- [ ] Can choose appropriate agent type
- [ ] Can debug agent issues
- [ ] Can evaluate agent performance

---

## 🎯 SUCCESS CRITERIA

**By end of Week 15, you should be able to:**

**Conceptual:**
- Explain how ReAct pattern works
- Explain function calling flow
- Describe different agent types
- Understand state machines for agents
- Know how to evaluate agents

**Practical:**
- Build ReAct agent from scratch
- Define tool schemas properly
- Implement tool execution
- Add conversation memory
- Debug agent issues
- Use LangChain agents

**Portfolio Impact:**
This week adds:
- ✅ Working agent system
- ✅ Understanding of agent architectures
- ✅ Tool calling implementation
- ✅ Framework knowledge (LangChain)
- ✅ Foundation for Week 16 (advanced tools)

---

**Total Learning Time:** 11-12 hours  
**Implementation Readiness:** Basic agent patterns mastered  
**Next Week:** Advanced tool use + Calculator tool (Fintech critical!)

---

**Document Generated:** December 26, 2025  
**For:** Week 15 - Agent Foundations  
**Part of:** Phase 2 Cohort (Weeks 15-21)