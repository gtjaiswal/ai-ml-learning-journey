# WEEK 17 LEARNING GUIDE: Multi-Agent Systems

**Timeline:** March 9-15, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Multi-agent orchestration, supervisor/worker patterns, LangGraph workflows

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Supervisor-worker agent system
- Parallel agent execution
- Agent communication protocols
- Multi-agent fraud detection system
- Agent coordination workflows

**What You'll Learn:**
- When to use multiple agents vs single agent
- Supervisor/worker pattern
- Agent communication patterns
- Task delegation strategies
- Conflict resolution between agents
- LangGraph for multi-agent orchestration

**Time Allocation:**
- Mon-Fri: 1-1.5 hours/day (7-7.5h total)
- Weekend: 4-4.5 hours (2-2.5h Sat, 2h Sun)
- Total: 11-12 hours

---

## DAY 1 (MONDAY): Multi-Agent Fundamentals

**Time:** 1.5 hours

---

### SESSION 1: Why Multiple Agents? (45 min)

**Video: "Multi-Agent Systems Explained"** - Deeplearning.AI  
- URL: https://www.youtube.com/watch?v=e8Y8EZU81h0
- Duration: 8:42
- What you'll learn: Multi-agent benefits, use cases

**Video: "AutoGen Multi-Agent Framework"** - Microsoft  
- URL: https://www.youtube.com/watch?v=RLwyXRVvlNk
- Duration: 15:30
- What you'll learn: Multi-agent architecture patterns

**Reading:**
📖 **Multi-Agent AI Systems**  
- URL: https://arxiv.org/abs/2308.10848
- Duration: 20 min read
- Focus: Abstract, Introduction, Section 2 (Architecture)

**What you need to understand:**

**Single Agent Limitations:**

**Problem 1: Complexity**
```
Single agent trying to:
- Analyze transaction
- Check fraud patterns
- Query multiple databases
- Calculate risk scores
- Generate report

Result: Overwhelmed, context limit exceeded, poor performance
```

**Problem 2: Specialization**
```
Single agent must be expert in:
- SQL queries
- Statistical analysis
- Regulatory compliance
- Customer communication
- Financial calculations

Result: Jack of all trades, master of none
```

**Problem 3: Parallel Processing**
```
Single agent processes sequentially:
Step 1 → Wait → Step 2 → Wait → Step 3 → Wait

Result: Slow, inefficient
```

**Multi-Agent Solution:**

**Agent 1: Data Retriever**
- Specializes in database queries
- Optimized prompts for data extraction
- Parallel queries to multiple sources

**Agent 2: Analyst**
- Specializes in fraud pattern detection
- Statistical analysis
- Risk scoring

**Agent 3: Compliance Checker**
- Knows all regulations
- Checks against rules
- Flags violations

**Agent 4: Report Generator**
- Customer-facing communication
- Clear explanations
- Professional formatting

**Agent 5: Supervisor**
- Coordinates other agents
- Delegates tasks
- Combines results
- Makes final decision

**Benefits:**
- ✅ Specialization → Better quality
- ✅ Parallelization → Faster
- ✅ Modularity → Easier to maintain
- ✅ Scalability → Add agents as needed
- ✅ Clarity → Each agent has clear role

**When NOT to Use Multi-Agent:**
- Simple, single-step tasks
- Low complexity queries
- Limited tools needed
- Fast response critical (coordination overhead)

---

### SESSION 2: Multi-Agent Patterns (45 min)

**Hands-On Exercise: Pattern Analysis**

**Requirements:**
Create `MULTI_AGENT_PATTERNS.md`:

**Pattern 1: Supervisor-Worker**

**Structure:**
```
Supervisor Agent
    ↓
Delegates to →  Worker 1 | Worker 2 | Worker 3
                   ↓          ↓          ↓
                Results → Supervisor → Final Decision
```

**Use Case:**
Complex analysis requiring different expertise

**Example:**
```
User: "Analyze transaction TX123 for fraud"

Supervisor:
  - Delegates to Data Agent → Get transaction details
  - Delegates to Pattern Agent → Check fraud patterns
  - Delegates to Risk Agent → Calculate risk score
  - Combines results → Makes decision
```

**Strengths:**
- Clear coordination
- Centralized decision-making
- Easy to add workers
- Supervisor handles conflicts

**Weaknesses:**
- Single point of failure (supervisor)
- Sequential if supervisor waits for all
- Supervisor can become bottleneck

**When to use:**
- Clear hierarchy needed
- Central decision authority required
- Workers independent

**Pattern 2: Peer-to-Peer**

**Structure:**
```
Agent 1 ↔ Agent 2 ↔ Agent 3
   ↕         ↕         ↕
  All agents communicate directly
```

**Use Case:**
Collaborative problem-solving, debate

**Example:**
```
Optimistic Agent: "Transaction looks legitimate"
Pessimistic Agent: "I see 3 red flags"
Neutral Agent: "Let's weigh evidence systematically"

→ Debate → Consensus → Decision
```

**Strengths:**
- No single point of failure
- Diverse perspectives
- Collaborative refinement

**Weaknesses:**
- Can deadlock (no consensus)
- Complex coordination
- Harder to debug

**When to use:**
- Multiple valid approaches
- Want diverse viewpoints
- No clear authority

**Pattern 3: Pipeline**

**Structure:**
```
Input → Agent 1 → Agent 2 → Agent 3 → Output
        (Clean)   (Analyze)  (Report)
```

**Use Case:**
Sequential processing stages

**Example:**
```
Raw Transaction →
  Agent 1 (Cleaner): Remove PII, normalize →
  Agent 2 (Analyzer): Detect patterns, score risk →
  Agent 3 (Reporter): Format for compliance →
Final Report
```

**Strengths:**
- Simple, linear flow
- Each agent improves output
- Easy to understand
- Easy to debug

**Weaknesses:**
- Slowest (no parallelization)
- Failure in one stage blocks all
- Can't handle branching logic

**When to use:**
- Clear sequential steps
- Each step builds on previous
- Order matters

**Pattern 4: Hierarchical**

**Structure:**
```
        CEO Agent
           ↓
    Manager Agents
           ↓
    Worker Agents
```

**Use Case:**
Complex organizations, escalation

**Example:**
```
Worker Agents: Handle routine transactions
Manager Agents: Handle escalations, unusual cases
CEO Agent: Handle critical decisions, conflicts

Transaction → Worker (can handle?) 
              → Yes: Process
              → No: Escalate to Manager
                    → Manager (can handle?)
                    → Yes: Process
                    → No: Escalate to CEO
```

**Strengths:**
- Scales well
- Clear escalation path
- Efficient (most handled at lowest level)

**Weaknesses:**
- Complex to implement
- Communication overhead
- Can be slow for escalations

**When to use:**
- Large systems
- Clear authority levels
- Most cases simple, few complex

**What to figure out:**
- Which pattern for fraud detection?
- Can patterns combine?
- How to choose pattern for problem?
- What are trade-offs?

**Success criteria:**
✅ 4 patterns documented  
✅ Strengths/weaknesses identified  
✅ Use cases mapped  
✅ Understand pattern selection  
✅ Can design for specific problem

---

## DAY 2 (TUESDAY): Supervisor-Worker Implementation

**Time:** 1.5 hours

---

### SESSION 1: Supervisor Agent Design (45 min)

**Reading:**
📖 **LangGraph Multi-Agent Documentation**  
- URL: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/
- Duration: 25 min read

**What you need to understand:**

**Supervisor Responsibilities:**

**1. Task Decomposition:**
Break complex query into subtasks
```
Query: "Is this transaction fraudulent and what's the risk?"

Subtasks:
1. Fetch transaction data
2. Check against fraud patterns
3. Calculate risk score
4. Determine fraud status
```

**2. Worker Selection:**
Match subtask to appropriate worker
```
Subtask 1 → Data Agent (best at queries)
Subtask 2 → Pattern Agent (fraud expertise)
Subtask 3 → Calculator Agent (math)
Subtask 4 → Decision Agent (final call)
```

**3. Execution Coordination:**
Decide sequence: parallel or sequential?
```
Parallel:
  Subtask 1 ─┐
  Subtask 2 ─┼→ All at once → Combine
  Subtask 3 ─┘

Sequential:
  Subtask 1 → Result → Subtask 2 → Result → ...
```

**4. Result Aggregation:**
Combine worker outputs into coherent answer
```
Data Agent: Transaction details
Pattern Agent: 3 red flags found
Calculator: Risk score 87/100
Decision Agent: HIGH RISK - REJECT

Supervisor: "Transaction rejected. Risk score 87/100. 
             Red flags: unusual location, high amount, new merchant."
```

**5. Conflict Resolution:**
What if workers disagree?
```
Agent A: "Legitimate"
Agent B: "Fraudulent"

Supervisor strategies:
- Majority vote
- Trust most specialized agent
- Request clarification
- Escalate to human
```

---

### SESSION 2: Worker Agent Design (45 min)

**Hands-On Exercise: Worker Agent Specs**

**Requirements:**
Create `WORKER_AGENTS_SPEC.md`:

**Worker 1: Data Retrieval Agent**

**Specialization:** Database queries, data fetching

**Tools:**
- database_query
- get_transaction
- get_customer_history

**Prompt Template:**
```
You are a Data Retrieval Specialist.

Your ONLY job is to fetch data from databases.
Do NOT analyze, do NOT make decisions.
Just retrieve the exact data requested.

When given a task:
1. Identify what data is needed
2. Choose appropriate tool
3. Fetch the data
4. Return raw data clearly formatted

If data doesn't exist, say so clearly.
```

**Input Format:**
- Specific data request
- Transaction ID or customer ID
- Date ranges if needed

**Output Format:**
```json
{
  "status": "success",
  "data": {...},
  "source": "database_name",
  "timestamp": "2026-03-09T10:30:00Z"
}
```

**Success Criteria:**
- Returns data exactly as stored
- No interpretation or analysis
- Clear error messages
- Fast response

**Worker 2: Pattern Analysis Agent**

**Specialization:** Fraud pattern detection

**Tools:**
- pattern_matcher
- anomaly_detector
- historical_comparison

**Prompt Template:**
```
You are a Fraud Pattern Analyst.

Your job is to identify suspicious patterns in transaction data.

Known fraud patterns:
- High amount + new merchant
- Foreign country + odd hours
- Multiple transactions in short time
- Velocity anomalies

When given transaction data:
1. Check each pattern
2. Note severity (low/medium/high)
3. List specific red flags
4. DO NOT make final fraud decision (that's supervisor's job)

Be thorough but concise.
```

**Input Format:**
- Transaction data (from Data Agent)
- Customer historical data

**Output Format:**
```json
{
  "patterns_found": ["high_amount_new_merchant", "unusual_time"],
  "red_flags": [
    {"flag": "Amount $5000 vs avg $150", "severity": "high"},
    {"flag": "Transaction at 3 AM", "severity": "medium"}
  ],
  "pattern_count": 2,
  "recommendation": "SUSPICIOUS"
}
```

**Success Criteria:**
- Identifies relevant patterns
- Explains why pattern matters
- No final decision (stays in lane)

**Worker 3: Risk Scoring Agent**

**Specialization:** Quantitative risk calculation

**Tools:**
- calculate
- statistical_analysis
- risk_model

**Prompt Template:**
```
You are a Risk Scoring Specialist.

Calculate numerical risk scores based on provided factors.

Risk factors and weights:
- Amount anomaly: 30%
- Location anomaly: 25%
- Time anomaly: 15%
- Merchant anomaly: 20%
- Velocity anomaly: 10%

ALWAYS use calculator tool for arithmetic.

When given factors:
1. Calculate weighted score for each
2. Sum total risk score (0-100)
3. Categorize: Low (0-30), Medium (31-70), High (71-100)
4. Show calculation steps
```

**Input Format:**
- Red flags from Pattern Agent
- Severity ratings

**Output Format:**
```json
{
  "calculations": {
    "amount_score": "30 * 0.8 = 24",
    "location_score": "25 * 1.0 = 25",
    ...
  },
  "total_score": 87,
  "category": "HIGH",
  "confidence": 0.92
}
```

**Success Criteria:**
- All math done with calculator tool
- Shows work
- Consistent scoring
- No subjective judgment

**Worker 4: Decision Agent**

**Specialization:** Final fraud determination

**Tools:**
- None (uses provided analysis)

**Prompt Template:**
```
You are a Fraud Decision Specialist.

Make final APPROVE/REVIEW/REJECT decision based on:
- Risk score
- Pattern analysis
- Company policy

Decision rules:
- Risk < 30: APPROVE
- Risk 30-70: REVIEW (human needed)
- Risk > 70: REJECT

When deciding:
1. Apply decision rules
2. Explain reasoning
3. Cite specific evidence
4. Recommend next steps
```

**Input Format:**
- Risk score
- Pattern analysis
- Transaction data

**Output Format:**
```json
{
  "decision": "REJECT",
  "reasoning": "Risk score 87/100 (HIGH). Multiple red flags: unusual location, high amount, new merchant.",
  "next_steps": "Block transaction, notify customer, flag account for review"
}
```

**Success Criteria:**
- Follows decision rules consistently
- Clear reasoning
- Actionable recommendations

**What to figure out:**
- How much overlap should workers have?
- How to prevent workers overstepping?
- What if worker can't complete task?
- How to validate worker outputs?

**Success criteria:**
✅ 4 worker agents specified  
✅ Each has clear specialization  
✅ Tools assigned appropriately  
✅ Prompts enforce boundaries  
✅ Output formats standardized

---

## DAY 3 (WEDNESDAY): Agent Communication

**Time:** 1.5 hours

---

### SESSION 1: Communication Protocols (45 min)

**Video: "Agent Communication in Multi-Agent Systems"**  
- URL: https://www.youtube.com/watch?v=8pMR3hQ_TOU
- Duration: 12:15
- What you'll learn: Message passing, coordination

**What you need to understand:**

**Communication Methods:**

**Method 1: Shared State**
```python
class SharedState(TypedDict):
    transaction_data: Dict
    pattern_analysis: Dict
    risk_score: int
    decision: str
    messages: List[Message]

# Each agent reads and writes to shared state
```

**Pros:**
- Simple
- All agents see everything
- Easy to debug

**Cons:**
- Race conditions (concurrent writes)
- Unclear ownership
- Hard to track who changed what

**Method 2: Message Passing**
```python
# Agent A sends message to Agent B
message = {
    "from": "supervisor",
    "to": "data_agent",
    "task": "fetch_transaction",
    "params": {"transaction_id": "TX123"}
}

# Agent B processes, sends response
response = {
    "from": "data_agent",
    "to": "supervisor",
    "result": {...},
    "status": "success"
}
```

**Pros:**
- Clear sender/receiver
- Async communication
- Traceable

**Cons:**
- More complex
- Need message queue
- Can lose messages

**Method 3: Function Calls**
```python
# Supervisor calls worker directly
result = data_agent.fetch_transaction("TX123")
```

**Pros:**
- Synchronous, simple
- Clear call stack
- Easy error handling

**Cons:**
- Blocking
- Tight coupling
- Hard to parallelize

**LangGraph Approach:**

Uses **shared state** with **structured updates**:
```python
# Each agent returns state update
def data_agent(state: State) -> State:
    # Read from state
    transaction_id = state["transaction_id"]
    
    # Do work
    data = fetch_transaction(transaction_id)
    
    # Return state update
    return {
        "transaction_data": data,
        "messages": state["messages"] + [
            {"agent": "data_agent", "status": "complete"}
        ]
    }
```

**Benefits:**
- Clear state transitions
- Immutable updates (functional)
- Easy to trace
- Works with LangGraph routing

---

### SESSION 2: Coordination Strategies (45 min)

**Hands-On Exercise: Coordination Design**

**Requirements:**
Create `AGENT_COORDINATION.md`:

**Strategy 1: Sequential Coordination**

**Flow:**
```
Supervisor → Worker 1 → Wait for result →
             Worker 2 (uses result from 1) → Wait →
             Worker 3 (uses result from 2) → Wait →
             Combine → Done
```

**Use When:**
- Each step depends on previous
- Order critical
- Can't parallelize

**Example:**
```
1. Data Agent: Fetch transaction
2. Pattern Agent: Analyze (needs transaction data)
3. Risk Agent: Score (needs pattern analysis)
4. Decision Agent: Decide (needs risk score)
```

**Coordination Logic:**
```python
def sequential_coordination(state):
    # Step 1
    state = data_agent(state)
    if state["data_status"] != "success":
        return error_handler(state)
    
    # Step 2
    state = pattern_agent(state)
    if state["pattern_status"] != "success":
        return error_handler(state)
    
    # Step 3
    state = risk_agent(state)
    # etc.
```

**Strategy 2: Parallel Coordination**

**Flow:**
```
Supervisor → Worker 1 ┐
          → Worker 2 ├→ All execute simultaneously
          → Worker 3 ┘
                ↓
          Wait for all → Combine → Done
```

**Use When:**
- Workers independent
- No dependencies between workers
- Speed critical

**Example:**
```
Parallel:
- Data Agent: Fetch transaction
- History Agent: Fetch customer history
- Merchant Agent: Fetch merchant info

All run at same time → Combine results
```

**Coordination Logic:**
```python
def parallel_coordination(state):
    # Launch all workers
    results = await asyncio.gather(
        data_agent(state),
        history_agent(state),
        merchant_agent(state)
    )
    
    # Combine results
    state["combined_data"] = merge_results(results)
    return state
```

**Strategy 3: Conditional Coordination**

**Flow:**
```
Supervisor → Worker 1 → Decision point
                          ↓              ↓
                    Condition A    Condition B
                          ↓              ↓
                      Worker 2       Worker 3
```

**Use When:**
- Logic branches
- Different paths for different cases
- Want to avoid unnecessary work

**Example:**
```
Data Agent fetches transaction →
  If amount > $1000:
    → Complex Analysis Agent (deep check)
  Else:
    → Simple Analysis Agent (quick check)
```

**Coordination Logic:**
```python
def conditional_coordination(state):
    state = data_agent(state)
    
    # Decision point
    if state["transaction_amount"] > 1000:
        state = complex_analysis_agent(state)
    else:
        state = simple_analysis_agent(state)
    
    return state
```

**Strategy 4: Iterative Coordination**

**Flow:**
```
Supervisor → Worker 1 → Check quality
                ↓
          Good enough? → No → Refine → Worker 1 (again)
                ↓
              Yes → Done
```

**Use When:**
- Quality threshold needed
- Refinement possible
- Want best answer, not fast answer

**Example:**
```
Analysis Agent analyzes transaction →
  Confidence > 90%? 
    → Yes: Done
    → No: Gather more data, analyze again
```

**Coordination Logic:**
```python
def iterative_coordination(state, max_iterations=3):
    for i in range(max_iterations):
        state = analysis_agent(state)
        
        if state["confidence"] > 0.9:
            break
        
        # Refine
        state = gather_more_data(state)
    
    return state
```

**What to figure out:**
- Which strategy for fraud detection?
- Can strategies combine?
- How to handle failures in parallel?
- When to use which strategy?

**Success criteria:**
✅ 4 coordination strategies documented  
✅ Use cases identified  
✅ Coordination logic outlined  
✅ Understand trade-offs  
✅ Can choose appropriate strategy

---

## DAY 4 (THURSDAY): LangGraph Multi-Agent

**Time:** 1.5 hours

---

### SESSION 1: LangGraph State Graphs (45 min)

**Reading:**
📖 **LangGraph Multi-Agent Tutorial**  
- URL: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/
- Duration: 30 min read + code review

**What you need to understand:**

**LangGraph for Multi-Agent:**

**State Definition:**
```python
class AgentState(TypedDict):
    messages: Annotated[List[Message], add_messages]
    next_agent: str
    transaction_data: Optional[Dict]
    pattern_analysis: Optional[Dict]
    risk_score: Optional[int]
    final_decision: Optional[str]
```

**Agent Nodes:**
```python
# Each worker is a node
def data_agent_node(state: AgentState) -> AgentState:
    # Call data agent
    result = data_agent.invoke(state)
    return {
        "transaction_data": result,
        "next_agent": "pattern_agent"
    }

def pattern_agent_node(state: AgentState) -> AgentState:
    # Call pattern agent
    result = pattern_agent.invoke(state)
    return {
        "pattern_analysis": result,
        "next_agent": "risk_agent"
    }
```

**Supervisor Node:**
```python
def supervisor_node(state: AgentState) -> AgentState:
    # Decide which agent to call next
    if not state.get("transaction_data"):
        return {"next_agent": "data_agent"}
    elif not state.get("pattern_analysis"):
        return {"next_agent": "pattern_agent"}
    # ... etc
```

**Graph Construction:**
```python
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("data_agent", data_agent_node)
workflow.add_node("pattern_agent", pattern_agent_node)
workflow.add_node("risk_agent", risk_agent_node)

# Add edges
workflow.add_edge(START, "supervisor")

workflow.add_conditional_edges(
    "supervisor",
    lambda state: state["next_agent"],
    {
        "data_agent": "data_agent",
        "pattern_agent": "pattern_agent",
        "risk_agent": "risk_agent",
        "FINISH": END
    }
)

# After each worker, go back to supervisor
workflow.add_edge("data_agent", "supervisor")
workflow.add_edge("pattern_agent", "supervisor")
workflow.add_edge("risk_agent", "supervisor")
```

**Execution:**
```python
app = workflow.compile()

result = app.invoke({
    "messages": [{"role": "user", "content": "Analyze TX123"}],
    "next_agent": "supervisor"
})
```

---

### SESSION 2: Multi-Agent Graph Design (45 min)

**Hands-On Exercise: Fraud Detection Graph**

**Requirements:**
Create `FRAUD_DETECTION_GRAPH.md`:

**1. State Definition:**

Define comprehensive state:
```python
class FraudDetectionState(TypedDict):
    # What state do you need to track?
    # - Original query
    # - Transaction ID
    # - Data from each agent
    # - Current step
    # - Errors if any
    # - Final decision
```

**2. Agent Nodes:**

Define each agent node:

**Supervisor Node:**
- Reads current state
- Decides next agent
- Returns next_agent or FINISH

**Data Agent Node:**
- Fetches transaction data
- Updates state with data
- Returns to supervisor

**Pattern Agent Node:**
- Analyzes patterns
- Updates state with analysis
- Returns to supervisor

**Risk Agent Node:**
- Calculates risk score
- Updates state with score
- Returns to supervisor

**Decision Agent Node:**
- Makes final decision
- Updates state with decision
- Returns FINISH

**3. Graph Structure:**

**Visual Diagram:**
```
START
  ↓
Supervisor ←──────┐
  ↓               │
  ├→ Data Agent ──┘
  ├→ Pattern Agent ┘
  ├→ Risk Agent ───┘
  ├→ Decision Agent
  ↓
END
```

**Conditional Routing:**
```python
def route_to_next_agent(state):
    # What logic determines next agent?
    # - If no data: data_agent
    # - If data but no patterns: pattern_agent
    # - If patterns but no score: risk_agent
    # - If score: decision_agent
    # - If decision: FINISH
```

**4. Error Handling:**

How to handle:
- Agent fails to respond
- Agent returns invalid data
- Agent gets stuck
- Maximum iterations exceeded
- Conflict between agents

**5. Optimization:**

Consider:
- Can any agents run in parallel?
- Can some steps be skipped?
- How to cache results?
- How to minimize LLM calls?

**What to figure out:**
- What state is essential vs nice-to-have?
- How to route efficiently?
- How to detect completion?
- How to handle errors gracefully?
- How to optimize performance?

**Success criteria:**
✅ Complete state definition  
✅ All agent nodes defined  
✅ Graph structure visualized  
✅ Routing logic specified  
✅ Error handling planned  
✅ Ready to implement

---

## DAY 5 (FRIDAY): Agent Conflict Resolution

**Time:** 1 hour

---

### SESSION 1: Conflict Scenarios (30 min)

**Reading:**
📖 **Multi-Agent Conflict Resolution**  
- URL: https://arxiv.org/abs/2307.02485
- Duration: 15 min read (Introduction + Section 3)

**Hands-On Exercise: Conflict Catalog**

**Requirements:**
Create `AGENT_CONFLICTS.md`:

**Conflict 1: Disagreement on Risk**

**Scenario:**
```
Pattern Agent: "HIGH RISK - 5 red flags"
Risk Agent: "MEDIUM RISK - score 55/100"

Conflict: Severity mismatch
```

**Resolution Options:**

**Option A: Trust Specialist**
- Risk Agent is quantitative specialist
- Use its numerical score as truth
- Decision: MEDIUM RISK

**Option B: Conservative Approach**
- In fraud detection, err on side of caution
- Use higher risk assessment
- Decision: HIGH RISK

**Option C: Supervisor Arbitration**
- Supervisor examines evidence
- Makes independent assessment
- Decision: Based on full context

**Option D: Human Escalation**
- Conflicts go to human reviewer
- Decision: MANUAL REVIEW

**Recommendation for Fintech:**
- Use Option B (conservative) + log conflict for review

**Conflict 2: Missing Data**

**Scenario:**
```
Data Agent: "Customer history unavailable"
Pattern Agent: "Cannot analyze without history"

Conflict: Cannot proceed
```

**Resolution Options:**

**Option A: Fail Gracefully**
- Return error to user
- Explain what's missing

**Option B: Proceed with Limited Data**
- Pattern Agent uses available data only
- Lower confidence score

**Option C: Use Defaults**
- Assume average customer profile
- Flag assumption in output

**Option D: Retry**
- Retry data fetch
- If still fails, escalate

**Recommendation for Fintech:**
- Retry once, then fail gracefully (Option D → A)

**Conflict 3: Contradictory Evidence**

**Scenario:**
```
Agent A: "Location suspicious (foreign country)"
Agent B: "Location legitimate (customer is traveling)"

Conflict: Same fact, opposite interpretations
```

**Resolution Options:**

**Option A: Gather More Context**
- Check flight bookings
- Check prior travel pattern
- Resolve with more data

**Option B: Probabilistic Combination**
- Weight both opinions
- Calculate combined probability
- Decision based on threshold

**Option C: Rule-Based**
- If travel confirmed → trust Agent B
- If travel not confirmed → trust Agent A

**Recommendation for Fintech:**
- Option A (more context) if available, else Option C

**What to figure out:**
- What conflicts are possible?
- Which resolution for each?
- How to detect conflicts automatically?
- When to escalate vs resolve?
- How to log for audit?

**Success criteria:**
✅ 5+ conflict scenarios identified  
✅ Resolution options documented  
✅ Recommendations made  
✅ Understand trade-offs  
✅ Audit trail considered

---

### SESSION 2: Consensus Mechanisms (30 min)

**Hands-On Exercise: Consensus Design**

**Requirements:**
Create `CONSENSUS_MECHANISMS.md`:

**Mechanism 1: Majority Vote**

**How it works:**
```
3 agents vote:
Agent A: APPROVE
Agent B: REJECT
Agent C: REJECT

Result: REJECT (2 out of 3)
```

**Use when:**
- Multiple agents with equal authority
- Clear binary decisions
- Odd number of agents

**Limitations:**
- Requires odd number
- All votes equal weight
- No specialist priority

**Mechanism 2: Weighted Vote**

**How it works:**
```
Agents with weights:
Data Agent (weight 1): APPROVE
Pattern Agent (weight 3): REJECT
Risk Agent (weight 2): REJECT

Calculation:
APPROVE: 1
REJECT: 3 + 2 = 5

Result: REJECT
```

**Use when:**
- Some agents more expert
- Want to prioritize certain factors
- Confidence scores available

**Limitations:**
- Need to define weights
- Weights might be wrong
- Complex to explain

**Mechanism 3: Threshold-Based**

**How it works:**
```
Require 2 out of 3 to agree:
Agent A: APPROVE
Agent B: APPROVE  
Agent C: REJECT

Result: APPROVE (threshold met)

But if:
Agent A: APPROVE
Agent B: REJECT
Agent C: REVIEW

Result: MANUAL_REVIEW (no threshold met)
```

**Use when:**
- Want strong consensus
- Avoid edge cases
- Multiple decision categories

**Mechanism 4: Confidence-Weighted**

**How it works:**
```
Agents with confidence:
Agent A: APPROVE (confidence 0.6)
Agent B: REJECT (confidence 0.9)
Agent C: APPROVE (confidence 0.5)

Weighted average:
APPROVE: (0.6 + 0.5) / 2 = 0.55
REJECT: 0.9 / 1 = 0.9

Result: REJECT (higher confidence)
```

**Use when:**
- Agents provide confidence scores
- Want to trust confident agents
- Probabilistic decisions acceptable

**What to figure out:**
- Which mechanism for fraud detection?
- How to combine mechanisms?
- How to handle ties?
- What if no consensus?
- How to validate mechanism choice?

**Success criteria:**
✅ 4 consensus mechanisms documented  
✅ Use cases identified  
✅ Limitations understood  
✅ Recommendation made  
✅ Can implement chosen mechanism

---

## DAY 6 (SATURDAY): Build Multi-Agent System

**Time:** 2.5 hours

---

### SESSION 1: Implement Supervisor-Worker (90 min)

**Requirements:**
Build complete supervisor-worker fraud detection system.

**System Components:**

**1. Supervisor Agent:**
- Decomposes user query
- Delegates to workers
- Combines results
- Makes final decision

**2. Worker Agents (4):**
- Data Retrieval Agent
- Pattern Analysis Agent
- Risk Scoring Agent
- Decision Agent

**3. LangGraph Workflow:**
- State management
- Conditional routing
- Error handling
- Result aggregation

**Implementation Requirements:**

**State:**
```python
class FraudDetectionState(TypedDict):
    # Define all state fields needed
    # Include transaction data, analysis results, decision
```

**Supervisor:**
```python
def supervisor_agent(state):
    # Determine which worker to call next
    # Based on current state
    # Return next_agent name or FINISH
```

**Workers:**
```python
def data_worker(state):
    # Fetch transaction data
    # Update state
    # Return to supervisor

def pattern_worker(state):
    # Analyze patterns
    # Update state
    # Return to supervisor

def risk_worker(state):
    # Calculate risk score (using calculator tool!)
    # Update state
    # Return to supervisor

def decision_worker(state):
    # Make final decision
    # Update state
    # Return FINISH
```

**Graph:**
```python
graph = StateGraph(FraudDetectionState)

# Add all nodes
# Add conditional edges from supervisor
# Add edges from workers back to supervisor
# Compile graph
```

**Test Cases:**

**Test 1: Simple Legitimate**
```
Input: "Check transaction TX001"
Expected:
  - Data worker fetches TX001
  - Pattern worker finds no red flags
  - Risk worker scores 15/100 (LOW)
  - Decision worker: APPROVE
```

**Test 2: Clear Fraud**
```
Input: "Analyze TX002"
Expected:
  - Data worker fetches TX002
  - Pattern worker finds 5 red flags
  - Risk worker scores 95/100 (HIGH)
  - Decision worker: REJECT
```

**Test 3: Edge Case**
```
Input: "Review TX003"
Expected:
  - Data worker fetches TX003
  - Pattern worker finds 2 red flags
  - Risk worker scores 55/100 (MEDIUM)
  - Decision worker: MANUAL_REVIEW
```

**Test 4: Missing Data**
```
Input: "Check TX999" (doesn't exist)
Expected:
  - Data worker: transaction not found
  - Supervisor: error handling
  - Return: clear error message
```

**Test 5: Complex Query**
```
Input: "Is TX004 fraud and what's the risk percentage?"
Expected:
  - Full analysis
  - Both decision and risk score in answer
  - Clear explanation
```

**What to figure out:**
- How to structure state effectively?
- How supervisor knows when done?
- How to handle worker errors?
- How to optimize routing?
- How to make output clear?

**Success criteria:**
✅ All 4 workers implemented  
✅ Supervisor routing working  
✅ LangGraph graph compiled  
✅ All 5 test cases pass  
✅ Errors handled gracefully  
✅ Clear audit trail in logs

---

### SESSION 2: Add Parallel Execution (60 min)

**Requirements:**
Optimize system with parallel agent execution.

**Identify Parallelization Opportunities:**

**Currently Sequential:**
```
Data Agent → Pattern Agent → Risk Agent → Decision
   2s           3s             2s            1s
Total: 8 seconds
```

**Can Parallelize:**
```
                  ┌→ Pattern Agent (3s) ┐
Data Agent (2s) → ├→ Risk Agent (2s)    ├→ Decision (1s)
                  └→ History Agent (2s)  ┘

Total: 2s + 3s (max parallel) + 1s = 6 seconds
Savings: 2 seconds (25%)
```

**Implementation:**

**Identify Independent Workers:**
```python
# These can run in parallel (both need only transaction data):
- Pattern Agent
- Risk Agent  
- Customer History Agent (if added)
```

**Modify Graph:**
```python
# After data agent, fork to multiple workers
workflow.add_conditional_edges(
    "supervisor",
    route_function,
    {
        "parallel_analysis": ["pattern_agent", "risk_agent"],
        "decision": "decision_agent"
    }
)

# All parallel workers go back to supervisor
workflow.add_edge("pattern_agent", "supervisor")
workflow.add_edge("risk_agent", "supervisor")
```

**Synchronization:**
```python
def supervisor_after_parallel(state):
    # Check if all parallel workers done
    if state.get("pattern_analysis") and state.get("risk_score"):
        return "decision_agent"
    else:
        return "wait"  # Not all done yet
```

**Test Performance:**
- Measure time for sequential
- Measure time for parallel
- Calculate improvement
- Verify results identical

**What to figure out:**
- Which workers can parallelize?
- How to synchronize results?
- How to handle if one fails?
- Does parallel actually help? (overhead vs savings)

**Success criteria:**
✅ Parallel execution implemented  
✅ Synchronization working  
✅ Performance measured  
✅ Results still correct  
✅ Error handling maintained

---

## DAY 7 (SUNDAY): Testing & Documentation

**Time:** 2 hours

---

### SESSION 1: Comprehensive Testing (60 min)

**Requirements:**
Create thorough test suite for multi-agent system.

**Test Categories:**

**Category 1: Functional Tests (10 tests)**

**Test basic functionality:**
1. Simple approve case
2. Simple reject case
3. Manual review case
4. Edge case (borderline risk)
5. High-value transaction
6. International transaction
7. New customer
8. Repeat offender
9. Legitimate but unusual
10. Complex multi-factor case

**For each test:**
```markdown
## Test: [Name]

**Input:** [Query/Transaction]

**Expected Agent Flow:**
1. Supervisor → Data Agent
2. Data Agent → Supervisor
3. Supervisor → Pattern Agent
4. ... etc

**Expected Output:**
{
  "decision": "...",
  "risk_score": X,
  "reasoning": "...",
  "agents_used": [...]
}

**Pass Criteria:**
- Correct decision
- Correct risk score (±5)
- Clear reasoning
- All agents used appropriately
```

**Category 2: Error Tests (5 tests)**

**Test error handling:**
1. Transaction doesn't exist
2. Database unavailable
3. Worker agent timeout
4. Invalid input format
5. Conflicting agent results

**For each test:**
- How system detects error
- How error is handled
- What user sees
- System doesn't crash

**Category 3: Performance Tests (3 tests)**

**Test performance:**
1. Single transaction (baseline)
2. 10 transactions in batch
3. Parallel vs sequential timing

**Measurements:**
- Average response time
- P95 response time
- Memory usage
- LLM calls per transaction
- Cost per transaction

**Category 4: Integration Tests (2 tests)**

**Test full system:**
1. End-to-end realistic scenario
2. Multi-turn conversation with follow-ups

**Execute All Tests:**
- Run full test suite
- Record results
- Document failures
- Fix issues
- Re-run until all pass

**What to figure out:**
- Are tests comprehensive?
- What edge cases missing?
- How to automate testing?
- What's acceptable performance?

**Success criteria:**
✅ 20 tests created  
✅ All tests pass  
✅ Performance measured  
✅ Errors handled correctly  
✅ System robust

---

### SESSION 2: Documentation & Week Summary (60 min)

**Requirements:**

**1. System Documentation:**

Create `MULTI_AGENT_SYSTEM_DOCS.md`:

**Architecture Section:**
- System diagram
- Agent responsibilities
- Communication flow
- State management

**Usage Section:**
- How to run system
- Example queries
- Expected outputs
- Configuration options

**Agent Reference:**
For each agent:
- Purpose
- Tools used
- Input format
- Output format
- Prompt template

**Performance Section:**
- Benchmark results
- Optimization notes
- Resource requirements
- Cost analysis

**Troubleshooting Section:**
- Common issues
- Debug steps
- Log interpretation
- Contact points

**2. Week 17 Summary:**

Create `WEEK17_SUMMARY.md`:

**What You Built:**
- Supervisor-worker system
- 4 specialized agents
- LangGraph orchestration
- Parallel execution
- Comprehensive tests

**Key Learnings:**

**Technical:**
- Multi-agent patterns
- Supervisor-worker architecture
- LangGraph state management
- Agent communication
- Conflict resolution
- Performance optimization

**Fintech-Specific:**
- When to use multiple agents
- How to enforce calculator usage across agents
- Audit trail importance
- Conservative decision-making
- Error handling in financial systems

**Challenges & Solutions:**
- Challenge: Agent coordination complexity
  - Solution: LangGraph state management
- Challenge: Ensuring calculator usage
  - Solution: Strict agent prompts + validation
- Challenge: Performance overhead
  - Solution: Parallel execution where possible

**3. Portfolio Preparation:**

**Demo Script:**
Show:
1. Simple case (fast path)
2. Complex case (all agents used)
3. Error case (graceful handling)
4. Parallel execution (performance)

**Interview Talking Points:**
- "I built a multi-agent fraud detection system with specialized agents..."
- "The supervisor coordinates 4 workers, each expert in their domain..."
- "I optimized with parallel execution, reducing latency 25%..."
- "All agents use calculator tool to ensure mathematical accuracy..."
- "The system handles errors gracefully and provides clear audit trails..."

**Architecture Diagram:**
Create visual showing:
- Supervisor agent (coordinator)
- 4 worker agents (specialists)
- LangGraph workflow
- Parallel execution paths
- Error handling flow

**What to figure out:**
- What's most impressive to showcase?
- How to explain complexity simply?
- What metrics to highlight?
- What questions might interviewers ask?

**Success criteria:**
✅ Complete system documentation  
✅ Week summary comprehensive  
✅ Demo script polished  
✅ Interview stories ready  
✅ Architecture diagram clear  
✅ Ready to present system

---

## 📚 ADDITIONAL RESOURCES

**Multi-Agent Systems:**
- AutoGen: https://github.com/microsoft/autogen
- CrewAI: https://github.com/joaomdmoura/crewai
- LangGraph Multi-Agent: https://langchain-ai.github.io/langgraph/tutorials/multi_agent/

**Academic Papers:**
- Multi-Agent RL: https://arxiv.org/abs/2108.13295
- Agent Communication: https://arxiv.org/abs/2307.02485
- Cooperative AI: https://arxiv.org/abs/2012.08630

**LangGraph:**
- Documentation: https://langchain-ai.github.io/langgraph/
- Tutorials: https://github.com/langchain-ai/langgraph/tree/main/examples

---

## ✅ WEEK 17 DELIVERABLES

**Documentation:**
- [ ] MULTI_AGENT_PATTERNS.md - Pattern analysis
- [ ] WORKER_AGENTS_SPEC.md - Worker specifications
- [ ] AGENT_COORDINATION.md - Coordination strategies
- [ ] FRAUD_DETECTION_GRAPH.md - Graph design
- [ ] AGENT_CONFLICTS.md - Conflict resolution
- [ ] CONSENSUS_MECHANISMS.md - Consensus approaches
- [ ] MULTI_AGENT_SYSTEM_DOCS.md - System documentation
- [ ] WEEK17_SUMMARY.md - Week summary

**Working System:**
- [ ] Supervisor agent
- [ ] 4 worker agents
- [ ] LangGraph workflow
- [ ] Parallel execution
- [ ] 20-test suite passing

**Understanding:**
- [ ] Multi-agent patterns mastered
- [ ] Supervisor-worker architecture
- [ ] Agent communication protocols
- [ ] Conflict resolution strategies
- [ ] LangGraph orchestration
- [ ] Performance optimization

---

## 🎯 SUCCESS CRITERIA

**By end of Week 17, you should be able to:**

**Conceptual:**
- Explain when to use multi-agent vs single agent
- Describe supervisor-worker pattern
- Understand agent communication methods
- Know conflict resolution strategies
- Understand coordination patterns

**Practical:**
- Design multi-agent systems
- Implement supervisor-worker architecture
- Use LangGraph for orchestration
- Handle agent conflicts
- Optimize with parallel execution
- Test multi-agent systems thoroughly

**Portfolio Impact:**
This week adds:
- ✅ Multi-agent fraud detection system
- ✅ Advanced orchestration with LangGraph
- ✅ Parallel execution optimization
- ✅ Production-grade error handling
- ✅ Comprehensive testing
- ✅ Strong system design demonstration

---

**Total Learning Time:** 11-12 hours  
**System Complexity:** High - demonstrates advanced AI engineering  
**Next Week:** Multimodal agents + Table extraction (Financial data)

---

**Document Generated:** December 27, 2025  
**For:** Week 17 - Multi-Agent Systems  
**Part of:** Phase 2 Cohort (Weeks 15-21)