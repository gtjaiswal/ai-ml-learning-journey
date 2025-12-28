# WEEK 16 LEARNING GUIDE: Advanced Tool Use + Calculator Tool

**Timeline:** March 2-8, 2026
**Total Time:** ~11-12 hours
**Focus:** Custom tool development, calculator tool (fintech critical), API integration

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Custom tool development framework
- **Calculator tool (FINTECH CRITICAL)**
- Stock price API tool
- Multi-tool agent system
- Tool error handling and retries

**What You'll Learn:**
- Custom tool creation patterns
- Tool validation and error handling
- API integration as tools
- Why calculator tool is critical for fintech
- Tool composition and chaining

**Time Allocation:**
- Mon-Fri: 1-1.5 hours/day (7-7.5h total)
- Weekend: 4-4.5 hours (2-2.5h Sat, 2h Sun)
- Total: 11-12 hours

---

## DAY 1 (MONDAY): Custom Tool Development

**Time:** 1.5 hours

---

### SESSION 1: Tool Design Patterns (45 min)

**Video: "Building Custom LangChain Tools"** - Sam Witteveen
- URL: https://www.youtube.com/watch?v=SBZ1ESpz08Q
- Duration: 17:43
- What you'll learn: Tool decorator, custom tools, best practices

**Reading:**
📖 **LangChain Custom Tools Documentation**
- URL: https://python.langchain.com/docs/modules/tools/custom_tools
- Duration: 20 min read

**What you need to understand:**

**Tool Requirements:**

1. **Function signature**
2. **Clear description** (LLM uses this!)
3. **Type hints** (for validation)
4. **Error handling**
5. **Return format** (string, dict, etc.)

**Good Tool Example:**
```python
@tool
def calculate_roi(investment: float, returns: float) -> str:
    """
    Calculate Return on Investment (ROI) percentage.

    Args:
        investment: Initial investment amount in dollars
        returns: Total returns received in dollars

    Returns:
        ROI percentage as a formatted string

    Example:
        calculate_roi(1000, 1200) returns "ROI: 20.00%"
    """
    try:
        roi = ((returns - investment) / investment) * 100
        return f"ROI: {roi:.2f}%"
    except ZeroDivisionError:
        return "Error: Investment cannot be zero"
    except Exception as e:
        return f"Error calculating ROI: {str(e)}"
```

**What makes it good:**
- Clear description explaining what it does
- Type hints for validation
- Example in docstring
- Error handling
- Formatted output
- Edge case handling (zero investment)

---

### SESSION 2: Tool Development Framework (45 min)

**Hands-On Exercise: Tool Template**

**Requirements:**
Create `TOOL_DEVELOPMENT_GUIDE.md`:

**1. Tool Template:**
```python
@tool
def tool_name(param1: type1, param2: type2) -> str:
    """
    [One sentence: What does this tool do?]

    [Detailed description: When should LLM use this tool?]

    Args:
        param1: [Clear description of parameter 1]
        param2: [Clear description of parameter 2]

    Returns:
        [What format does output have?]

    Example:
        tool_name(value1, value2) returns "[example output]"

    Errors:
        - [What can go wrong?]
        - [How are errors returned?]
    """
    try:
        # Validation
        if invalid_input:
            return "Error: [specific error message]"

        # Core logic
        result = process(param1, param2)

        # Format output
        return formatted_result

    except SpecificException as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
```

**2. Tool Design Checklist:**

For every tool, ensure:
- [ ] Clear, specific description (LLM understands purpose)
- [ ] All parameters have type hints
- [ ] All parameters documented with examples
- [ ] Return type specified
- [ ] Example usage in docstring
- [ ] Input validation
- [ ] Error handling (specific errors)
- [ ] Formatted output (consistent structure)
- [ ] Edge cases handled
- [ ] No side effects (idempotent if possible)

**3. Common Pitfalls:**

**Pitfall 1: Vague Description**
- Bad: "Calculates something"
- Good: "Calculates ROI percentage given investment and returns"

**Pitfall 2: Missing Validation**
- Bad: Assumes inputs are valid
- Good: Checks for None, zero, negative values

**Pitfall 3: Unclear Errors**
- Bad: "Error occurred"
- Good: "Error: Investment amount must be greater than zero"

**Pitfall 4: Inconsistent Format**
- Bad: Sometimes returns number, sometimes string
- Good: Always returns formatted string

**Pitfall 5: Side Effects**
- Bad: Modifies database
- Good: Read-only operation

**What to figure out:**
- How detailed should descriptions be?
- When to raise exceptions vs return error strings?
- How to balance validation vs simplicity?
- What format for different output types?

**Success criteria:**
✅ Complete tool template created
✅ Design checklist documented
✅ Common pitfalls identified
✅ Understand what makes a good tool
✅ Ready to build custom tools

---

## DAY 2 (TUESDAY): Calculator Tool - Fintech Critical

**Time:** 1.5 hours

---

### SESSION 1: Why Calculator Tool Matters (45 min)

**The Problem: LLMs Can't Do Math**

**Video: "Why AI Models Are Bad at Math"**
- URL: https://www.youtube.com/watch?v=3KX3PCKYmY4
- Duration: 6:22
- What you'll learn: Why LLMs hallucinate numbers

**Reading:**
📖 **LLM Math Limitations**
- URL: https://www.alignmentforum.org/posts/BgoKdAzogxmgkuuAt/language-models-seem-to-be-much-better-at-math-than-i-thought
- Duration: 15 min read

**Understanding the Issue:**

**Test:**
Ask GPT-4: "What's 789 × 456?"

**Common responses:**
- 359,784 (WRONG - actual: 359,784)
- "Approximately 360,000" (vague)
- Sometimes correct by luck

**Why this is unacceptable in fintech:**

**Scenario 1: Fraud Scoring**
```
LLM: "Risk score is 10 + 10 = 21"  ← WRONG
Correct: 20

Impact: False positive/negative in fraud detection
Cost: Lost legitimate transaction OR missed fraud
```

**Scenario 2: Transaction Amount**
```
LLM: "Total is $1,234.56 + $789.12 = $2,024.68"  ← WRONG
Correct: $2,023.68

Impact: Incorrect accounting
Cost: Reconciliation issues, customer complaints
```

**Scenario 3: Interest Calculation**
```
LLM: "Interest on $100,000 at 5% = $5,500"  ← WRONG
Correct: $5,000

Impact: Regulatory violation
Cost: Fines, audits, reputational damage
```

**The Solution: ALWAYS Use Calculator Tool**

Never allow LLM to do arithmetic probabilistically.

---

### SESSION 2: Calculator Tool Implementation (45 min)

**Hands-On Exercise: Build Calculator Tool**

**Requirements:**
Create comprehensive calculator tool.

**1. Basic Calculator:**
```python
@tool
def calculate(expression: str) -> str:
    """
    Perform mathematical calculations. ALWAYS use this tool for ANY arithmetic.
    NEVER calculate numbers yourself - you will get it wrong.

    This tool is CRITICAL for fintech applications where accuracy is mandatory.

    Supported operations:
    - Basic: +, -, *, /
    - Parentheses: ()
    - Exponents: **
    - Modulo: %

    Args:
        expression: Mathematical expression as string (e.g., "10 + 15", "1250 * 0.15")

    Returns:
        Result as formatted string with original expression

    Examples:
        calculate("10 + 15") returns "10 + 15 = 25"
        calculate("1250 * 0.15") returns "1250 * 0.15 = 187.5"
        calculate("(100 + 50) * 2") returns "(100 + 50) * 2 = 300"

    Errors:
        - Division by zero returns error message
        - Invalid expression returns error message
        - Security: Only math operations allowed (no exec/eval of arbitrary code)
    """
    # What to implement:
    # - Parse expression safely
    # - Evaluate using safe math parser (NOT eval!)
    # - Format result
    # - Handle errors
```

**What to figure out:**

**Security:**
- How to prevent code injection?
- How to allow only math operations?
- Is Python's `eval()` safe? (NO!)
- What library to use instead? (ast, numexpr, py_expression_eval)

**Precision:**
- Float precision issues (0.1 + 0.2 = 0.30000000000000004)
- How to round for financial calculations?
- When to use Decimal type?

**Validation:**
- What expressions are valid?
- How to reject dangerous inputs?
- How to give helpful error messages?

**2. Financial Calculator:**
```python
@tool
def calculate_percentage(value: float, percentage: float) -> str:
    """
    Calculate percentage of a value. Use for discount, tax, commission calculations.

    Args:
        value: The base value
        percentage: Percentage to calculate (e.g., 15 for 15%)

    Returns:
        Both the percentage amount and percentage of value

    Example:
        calculate_percentage(1250, 15) returns "15% of $1,250.00 = $187.50"
    """
```
```python
@tool
def calculate_compound_interest(principal: float, rate: float, years: int) -> str:
    """
    Calculate compound interest. Use for investment returns, loan calculations.

    Args:
        principal: Initial amount in dollars
        rate: Annual interest rate (e.g., 5 for 5%)
        years: Number of years

    Returns:
        Final amount and interest earned

    Example:
        calculate_compound_interest(10000, 5, 10) returns
        "Principal: $10,000.00, Rate: 5%, Years: 10
         Final Amount: $16,288.95, Interest Earned: $6,288.95"
    """
```

**3. Prompt Engineering:**

**System Prompt Addition:**
```
CRITICAL: You are FORBIDDEN from performing arithmetic calculations yourself.
For ANY mathematical operation, you MUST use the calculate() tool.

Examples of MANDATORY tool use:
- "10 + 5" → Use calculate("10 + 5")
- "What's 15% of $1,250?" → Use calculate_percentage(1250, 15)
- Adding numbers → Use calculate()
- Multiplying → Use calculate()
- ANY arithmetic → Use calculate()

NEVER say "The answer is X" without using the calculator tool first.
This is a FINANCIAL system where accuracy is legally required.
```

**What to figure out:**
- How to force LLM to always use calculator?
- How to handle when LLM ignores instruction?
- How to detect if LLM did math without tool?
- How to validate calculation results?

**Success criteria:**
✅ Basic calculator tool working
✅ Safe evaluation (no code injection)
✅ Financial calculator functions
✅ Clear error messages
✅ System prompt enforces tool use
✅ Tested with 10+ expressions

---

## DAY 3 (WEDNESDAY): API Integration Tools

**Time:** 1.5 hours

---

### SESSION 1: API Tools Pattern (45 min)

**Video: "Building API Tools for Agents"**
- URL: https://www.youtube.com/watch?v=ziu_1F4rIYo
- Duration: 11:37
- What you'll learn: Wrapping APIs as tools

**What you need to understand:**

**API Tool Pattern:**
```python
@tool
def api_tool_name(param: str) -> str:
    """Tool description for LLM"""

    try:
        # 1. Validate inputs
        # 2. Make API request
        # 3. Parse response
        # 4. Format for LLM
        # 5. Return result
    except APIException:
        # Handle API errors
    except NetworkException:
        # Handle network errors
```

**Key Considerations:**

**1. Rate Limiting:**
- API has limits (e.g., 100 requests/hour)
- How to track usage?
- How to handle limit reached?
- Caching strategy?

**2. Authentication:**
- API keys management
- Don't expose keys in error messages
- How to handle expired keys?

**3. Error Handling:**
- API down → return error, not crash
- Invalid response → parse defensively
- Timeout → configurable timeout
- Retry logic → exponential backoff

**4. Response Formatting:**
- API returns JSON → convert to readable text
- Large responses → summarize, don't dump all
- Null/missing fields → handle gracefully

---

### SESSION 2: Stock Price Tool (45 min)

**Hands-On Exercise: Build Stock Price Tool**

**Requirements:**
Create stock price lookup tool.

**Choose API:**
Options (pick one):
- Alpha Vantage (free tier: 5 requests/min)
- Yahoo Finance (via yfinance library)
- Financial Modeling Prep (free tier available)

**Tool Implementation:**
```python
@tool
def get_stock_price(symbol: str) -> str:
    """
    Get current stock price and basic information for a stock symbol.
    Use this when user asks about stock prices, market data, or company trading info.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL", "GOOGL", "MSFT")

    Returns:
        Current price, change, and percentage change formatted as text

    Example:
        get_stock_price("AAPL") returns:
        "Apple Inc (AAPL):
         Current Price: $178.45
         Change: +$2.35 (+1.33%)
         Last Updated: 2026-03-03 16:00:00 ET"

    Errors:
        - Invalid symbol: "Error: Symbol 'XYZ' not found"
        - API error: "Error: Unable to fetch stock data. Please try again."
        - Rate limit: "Error: API rate limit reached. Please wait."
    """

    # What to implement:
    # 1. Validate symbol format
    # 2. Call API with error handling
    # 3. Parse JSON response
    # 4. Format nicely for LLM
    # 5. Handle all error cases
```

**What to figure out:**

**API Integration:**
- How to get API key?
- How to make request?
- What endpoint to call?
- How to parse response?

**Caching:**
- Stock prices change constantly
- Cache for how long? (1 minute? 5 minutes?)
- How to implement cache?
- When to invalidate?

**Formatting:**
- How to format currency?
- How to format percentages?
- How to indicate positive vs negative change?
- What information is essential vs nice-to-have?

**Error Handling:**
- Invalid symbol (typo)
- Market closed (return last price? error?)
- API down
- Rate limit exceeded
- Network timeout

**Validation:**
- Is "AAPL" valid? Yes
- Is "aapl" valid? (Should uppercase it)
- Is "NOTREAL" valid? No
- Is "" valid? No

**Success criteria:**
✅ Stock price tool working
✅ API integrated correctly
✅ Caching implemented
✅ All errors handled
✅ Response well-formatted
✅ Tested with 5+ symbols

---

## DAY 4 (THURSDAY): Tool Error Handling & Retries

**Time:** 1.5 hours

---

### SESSION 1: Retry Strategies (45 min)

**Reading:**
📖 **Tenacity Documentation**
- URL: https://tenacity.readthedocs.io/
- Duration: 20 min read
- Focus: Retry decorators, wait strategies

**What you need to understand:**

**Why Retry?**
- Network glitches
- API temporary unavailable
- Rate limit recovery
- Transient errors

**Retry Strategies:**

**1. Simple Retry:**
```python
max_retries = 3
for attempt in range(max_retries):
    try:
        return api_call()
    except TemporaryError:
        if attempt == max_retries - 1:
            raise
        time.sleep(1)
```

**2. Exponential Backoff:**
```python
wait_time = 2 ** attempt  # 1s, 2s, 4s, 8s...
time.sleep(wait_time)
```

**Why exponential?**
- Gives service time to recover
- Reduces load on failing service
- Industry best practice

**3. Retry with Jitter:**
```python
wait_time = (2 ** attempt) + random.uniform(0, 1)
```

**Why jitter?**
- Prevents thundering herd
- Multiple clients don't retry simultaneously

**What to retry:**
- ✅ Network errors
- ✅ 5xx server errors
- ✅ Rate limit (429)
- ✅ Timeouts
- ❌ 4xx client errors (bad request - won't fix with retry)
- ❌ Authentication errors
- ❌ Invalid input

---

### SESSION 2: Tool Error Framework (45 min)

**Hands-On Exercise: Error Handling System**

**Requirements:**
Create `TOOL_ERROR_HANDLING.md`:

**1. Error Categories:**

**Category 1: User Input Errors**
- Invalid parameters
- Missing required fields
- Out of range values

**Action:**
- Don't retry
- Return clear error message
- Suggest correction

**Example:**
```
Input: calculate("abc + def")
Return: "Error: Invalid expression 'abc + def'.
         Please use numbers and math operators (+, -, *, /).
         Example: calculate('10 + 5')"
```

**Category 2: Transient Errors**
- Network timeout
- API temporarily down
- Rate limit

**Action:**
- Retry with backoff
- Max 3 attempts
- Return error if all fail

**Example:**
```
Attempt 1: Network timeout → Wait 2s
Attempt 2: Network timeout → Wait 4s
Attempt 3: Network timeout → Return error
```

**Category 3: Configuration Errors**
- Missing API key
- Invalid credentials
- Wrong endpoint

**Action:**
- Don't retry
- Log for debugging
- Return generic error to user

**Example:**
```
Error: Stock price service unavailable.
       (Internal: API key not configured)
```

**Category 4: Unexpected Errors**
- Unknown exceptions
- Parsing failures

**Action:**
- Log full stack trace
- Don't retry
- Return safe error message

**2. Error Response Format:**

**Standard Error Response:**
```json
{
    "success": false,
    "error": {
        "type": "ValidationError",
        "message": "Symbol 'XYZ' not found",
        "suggestion": "Please check the stock symbol and try again",
        "retryable": false
    }
}
```

**For LLM (string format):**
```
"Error: Symbol 'XYZ' not found. Please check the stock symbol and try again."
```

**3. Retry Configuration:**
```python
retry_config = {
    "max_attempts": 3,
    "initial_wait": 2,  # seconds
    "max_wait": 30,     # seconds
    "exponential_base": 2,
    "jitter": True,
    "retry_on": [
        NetworkError,
        TimeoutError,
        RateLimitError
    ],
    "dont_retry_on": [
        ValidationError,
        AuthenticationError
    ]
}
```

**What to figure out:**
- How many retries is reasonable?
- How long to wait between retries?
- What errors should never retry?
- How to communicate errors to LLM?
- How to log for debugging?

**Success criteria:**
✅ Error categories defined
✅ Retry strategy per category
✅ Error response format standardized
✅ Retry configuration documented
✅ Understand when to retry vs fail

---

## DAY 5 (FRIDAY): Tool Composition

**Time:** 1 hour

---

### SESSION 1: Multi-Tool Workflows (30 min)

**Reading:**
📖 **Tool Chaining Patterns**
- URL: https://python.langchain.com/docs/modules/agents/agent_types/
- Duration: 15 min read

**Hands-On Exercise: Tool Chain Design**

**Requirements:**
Create `TOOL_CHAINS.md`:

**Scenario 1: Investment Analysis**

**User:** "Should I invest in Apple stock right now?"

**Tool Chain:**
1. `get_stock_price("AAPL")` → Current price, change
2. `calculate_percentage(price, change_percent)` → Verify math
3. `search("Apple recent news")` → Context
4. Final answer based on all data

**Scenario 2: Portfolio Value**

**User:** "What's my portfolio worth if I have 100 AAPL and 50 GOOGL shares?"

**Tool Chain:**
1. `get_stock_price("AAPL")` → $178.45
2. `calculate("100 * 178.45")` → $17,845
3. `get_stock_price("GOOGL")` → $142.30
4. `calculate("50 * 142.30")` → $7,115
5. `calculate("17845 + 7115")` → Total: $24,960

**Scenario 3: ROI Calculation**

**User:** "I bought 50 shares of MSFT at $300 each. What's my ROI at current price?"

**Tool Chain:**
1. `calculate("50 * 300")` → Investment: $15,000
2. `get_stock_price("MSFT")` → Current: $380
3. `calculate("50 * 380")` → Current value: $19,000
4. `calculate_roi(15000, 19000)` → ROI: 26.67%

**What to figure out:**
- How to ensure LLM uses tools in right order?
- How to pass results between tools?
- What if intermediate tool fails?
- How to validate final answer?

**Success criteria:**
✅ 3+ tool chain scenarios designed
✅ Tool order logical
✅ Error handling considered
✅ Can explain why order matters

---

### SESSION 2: Tool Validation (30 min)

**Hands-On Exercise: Validation Framework**

**Requirements:**
Create `TOOL_VALIDATION.md`:

**1. Pre-Execution Validation:**

**Validate before calling tool:**
```python
def validate_calculate_input(expression: str) -> tuple[bool, str]:
    """
    Validate calculator input before execution.

    Returns:
        (is_valid, error_message)
    """
    # Check 1: Not empty
    # Check 2: Only allowed characters
    # Check 3: Balanced parentheses
    # Check 4: No dangerous patterns
    # Check 5: Reasonable length
```

**What to check:**
- Type correct?
- Required fields present?
- Values in valid range?
- Format correct?
- No injection attempts?

**2. Post-Execution Validation:**

**Validate tool response:**
```python
def validate_tool_response(response: str) -> tuple[bool, str]:
    """
    Validate tool response before returning to LLM.

    Returns:
        (is_valid, error_message)
    """
    # Check 1: Response not empty
    # Check 2: Expected format
    # Check 3: No error indicators
    # Check 4: Reasonable length
    # Check 5: No sensitive data exposed
```

**3. Agent-Level Validation:**

**Validate agent decisions:**
- Did agent choose appropriate tool?
- Are tool arguments reasonable?
- Is sequence logical?
- Does final answer use tool results?
- Did agent verify calculations?

**Example Check:**
```
User: "What's 10 + 5?"

✗ Bad: Agent says "The answer is 15" (didn't use tool)
✓ Good: Agent calls calculate("10 + 5"), returns "10 + 5 = 15"
```

**What to figure out:**
- What validations are essential vs paranoid?
- When to validate vs trust?
- How to handle validation failures?
- Performance impact of validation?

**Success criteria:**
✅ Pre-execution validation defined
✅ Post-execution validation defined
✅ Agent-level validation defined
✅ Calculator usage enforced
✅ Understand validation trade-offs

---

## DAY 6 (SATURDAY): Multi-Tool Agent System

**Time:** 2.5 hours

---

### SESSION 1: Build Multi-Tool Agent (90 min)

**Requirements:**
Build agent with 4 tools working together.

**Tools to Include:**

1. **Calculator** (from Day 2)
2. **Stock Price** (from Day 3)
3. **Search** (simulated or real)
4. **Database Query** (simulated - query fraud transactions)

**Agent Capabilities:**

The agent should handle:
1. Pure calculation queries
2. Stock price lookups
3. Investment calculations
4. Multi-step analysis
5. Fraud investigation queries

**Test Scenarios:**

**Test 1: Basic Calculation**
```
User: "What's 15% of $1,250?"
Expected: Uses calculate_percentage(1250, 15)
Answer: "15% of $1,250.00 is $187.50"
```

**Test 2: Stock Lookup**
```
User: "What's Apple's stock price?"
Expected: Uses get_stock_price("AAPL")
Answer: Current price with change
```

**Test 3: Investment Value**
```
User: "I have 100 shares of MSFT at $380 each. What's it worth?"
Expected:
  1. calculate("100 * 380")
  2. Returns "$38,000.00"
```

**Test 4: ROI Calculation**
```
User: "Bought GOOGL at $120, now $142. 50 shares. What's my ROI?"
Expected:
  1. calculate("50 * 120") → $6,000 invested
  2. calculate("50 * 142") → $7,100 current value
  3. calculate_roi(6000, 7100) → ROI: 18.33%
```

**Test 5: Complex Query**
```
User: "Compare my investment: 100 AAPL shares vs 150 GOOGL shares. Which is worth more?"
Expected:
  1. get_stock_price("AAPL")
  2. calculate("100 * [AAPL price]")
  3. get_stock_price("GOOGL")
  4. calculate("150 * [GOOGL price]")
  5. Compare and answer
```

**Test 6: Fraud Query**
```
User: "Show high-risk transactions over $5000 this week"
Expected:
  1. database_query(amount>5000, risk=high, date=this_week)
  2. Format results
```

**What to figure out:**
- How to handle complex multi-step queries?
- How to ensure calculator always used for math?
- How to handle tool execution order?
- What if tool fails mid-chain?
- How to format final answer?

**Success criteria:**
✅ All 4 tools integrated
✅ All 6 test scenarios pass
✅ Calculator enforced for all math
✅ Multi-step queries work
✅ Errors handled gracefully
✅ Clear audit trail of tool calls

---

### SESSION 2: Agent Polish & Testing (60 min)

**Requirements:**

**1. Comprehensive Testing:**

Create test suite with 15 queries:
- 5 simple (single tool)
- 5 medium (2-3 tools)
- 5 complex (4+ tools, branching logic)

Document for each:
- Query
- Expected tools called
- Expected answer format
- Pass/fail criteria

**2. Error Scenario Testing:**

Test these failure modes:
- Calculator with invalid expression
- Stock symbol doesn't exist
- API timeout
- Database unavailable
- LLM tries to do math without tool

For each, verify:
- Error message is clear
- Agent doesn't crash
- User gets helpful response

**3. Performance Testing:**

Measure:
- Average response time
- Tool calls per query
- Token usage
- Success rate

**4. Demo Preparation:**

Create demo script showing:
- Basic calculation
- Stock lookup
- Investment analysis
- Error handling
- Complex multi-step query

**What to figure out:**
- What's acceptable performance?
- When to optimize vs accept?
- How to present to stakeholders?
- What metrics matter most?

**Success criteria:**
✅ 15-test suite passes
✅ All error scenarios handled
✅ Performance measured
✅ Demo script polished
✅ Ready to showcase

---

## DAY 7 (SUNDAY): Documentation & Week Summary

**Time:** 2 hours

---

### SESSION 1: Tool Library Documentation (60 min)

**Requirements:**
Create comprehensive tool library documentation.

**1. TOOL_LIBRARY.md:**

Document all tools:

**For Each Tool:**
```markdown
## Tool Name: calculate

**Purpose:** Perform mathematical calculations with guaranteed accuracy

**Why It Exists:** LLMs cannot do arithmetic reliably. In fintech,
                  mathematical accuracy is legally required.

**When to Use:**
- Any arithmetic operation
- Percentage calculations
- Financial formulas
- Comparing numbers

**When NOT to Use:**
- No mathematical operation needed

**Parameters:**
- expression (string): Math expression like "10 + 5"

**Returns:**
- Formatted string: "10 + 5 = 15"

**Examples:**
1. calculate("100 + 50") → "100 + 50 = 150"
2. calculate("1250 * 0.15") → "1250 * 0.15 = 187.5"

**Error Handling:**
- Division by zero → Error message
- Invalid syntax → Error message
- Security: Only math allowed

**Testing:**
- ✅ Basic arithmetic
- ✅ Parentheses
- ✅ Decimals
- ✅ Error cases

**Maintenance:**
- Review quarterly
- Update for new requirements
```

**2. FINTECH_CALCULATOR_IMPORTANCE.md:**

Document why calculator tool is critical:

**The Problem:**
- LLMs are probabilistic
- Math requires deterministic answers
- Example failures with costs

**The Solution:**
- Dedicated calculator tool
- Force LLM to always use it
- Validate all calculations

**Impact:**
- Zero math errors
- Regulatory compliance
- Customer trust
- Audit trail

**Interview Story:**
Write 2-3 paragraphs explaining:
- Why you added calculator tool
- How you enforce its use
- Impact on accuracy
- How this differentiates you

---

### SESSION 2: Week 16 Summary (60 min)

**Requirements:**
Create `WEEK16_SUMMARY.md`:

**1. What You Built:**
- Custom tool development framework
- Calculator tool (fintech critical)
- Stock price tool
- Tool error handling system
- Multi-tool agent
- Validation framework

**2. Key Learnings:**

**Technical:**
- Tool design patterns
- API integration
- Error handling strategies
- Retry logic
- Validation approaches

**Fintech-Specific:**
- Why LLMs can't do math
- Calculator tool criticality
- Deterministic vs probabilistic
- Regulatory requirements
- Audit trails

**3. Challenges & Solutions:**

For each challenge:
- What was hard?
- How did you solve it?
- What would you do differently?

**4. Portfolio Preparation:**

**Demo Script:**
- Show calculator enforcement
- Show multi-step reasoning
- Show error handling
- Show stock integration

**Interview Talking Points:**
- "I implemented a calculator tool because LLMs hallucinate math..."
- "In fintech, we can't accept probabilistic answers for arithmetic..."
- "I enforced tool use through system prompts and validation..."

**5. Next Week Preview:**

Week 17 focus:
- Multi-agent systems
- Agent orchestration
- LangGraph workflows
- Supervisor/worker patterns

**What to figure out:**
- What's your strongest example?
- What surprised you most?
- What needs more practice?
- What questions remain?

**Success criteria:**
✅ All tools documented
✅ Calculator importance explained
✅ Week summary comprehensive
✅ Portfolio materials ready
✅ Interview stories prepared
✅ Understand fintech impact

---

## 📚 ADDITIONAL RESOURCES

**Tool Development:**
- LangChain Tools: https://python.langchain.com/docs/modules/tools/
- Custom Tools Guide: https://python.langchain.com/docs/modules/tools/custom_tools

**Math in LLMs:**
- Why LLMs Struggle with Math: https://arxiv.org/abs/2308.07922
- Tool-Augmented LLMs: https://arxiv.org/abs/2302.04761

**Error Handling:**
- Tenacity Library: https://tenacity.readthedocs.io/
- Python Retrying: https://github.com/jd/tenacity

**API Integration:**
- Alpha Vantage: https://www.alphavantage.co/
- yfinance: https://pypi.org/project/yfinance/
- Requests Documentation: https://requests.readthedocs.io/

---

## ✅ WEEK 16 DELIVERABLES

**Documentation:**
- [ ] TOOL_DEVELOPMENT_GUIDE.md - Tool template and checklist
- [ ] TOOL_ERROR_HANDLING.md - Error handling framework
- [ ] TOOL_CHAINS.md - Multi-tool workflow scenarios
- [ ] TOOL_VALIDATION.md - Validation framework
- [ ] TOOL_LIBRARY.md - Complete tool documentation
- [ ] FINTECH_CALCULATOR_IMPORTANCE.md - Why calculator matters
- [ ] WEEK16_SUMMARY.md - Week summary and insights

**Working Tools:**
- [ ] Calculator tool (basic + financial)
- [ ] Stock price tool
- [ ] Search tool
- [ ] Database query tool (simulated)

**Working Agent:**
- [ ] Multi-tool agent system
- [ ] 15-test suite passing
- [ ] Error handling comprehensive
- [ ] Demo script ready

**Understanding:**
- [ ] Why calculator tool is critical for fintech
- [ ] How to design effective tools
- [ ] How to handle tool errors
- [ ] How to validate tool usage
- [ ] How to chain tools

---

## 🎯 SUCCESS CRITERIA

**By end of Week 16, you should be able to:**

**Conceptual:**
- Explain why LLMs can't do math reliably
- Explain calculator tool importance for fintech
- Describe tool design patterns
- Understand retry strategies
- Know validation approaches

**Practical:**
- Build custom tools with proper schemas
- Integrate APIs as tools
- Implement error handling and retries
- Validate tool inputs and outputs
- Force LLM to use calculator
- Chain multiple tools

**Portfolio Impact:**
This week adds:
- ✅ Calculator tool (FINTECH CRITICAL)
- ✅ Understanding of LLM limitations
- ✅ Production-grade error handling
- ✅ API integration skills
- ✅ Multi-tool agent system
- ✅ Strong interview story

---

**Total Learning Time:** 11-12 hours
**Fintech Impact:** CRITICAL - Calculator tool prevents math errors
**Next Week:** Multi-agent systems + LangGraph workflows

---

**Document Generated:** December 26, 2025
**For:** Week 16 - Advanced Tool Use + Calculator Tool
**Part of:** Phase 2 Cohort (Weeks 15-21)