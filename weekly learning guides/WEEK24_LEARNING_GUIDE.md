# WEEK 24 LEARNING GUIDE: Circuit Breakers + Resilience Engineering

**Timeline:** April 27 - May 3, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Circuit breakers, graceful degradation, chaos engineering, SLA monitoring

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Circuit breaker pattern implementation
- Offline fallback system (rule-based fraud detection)
- Graceful degradation tiers
- Chaos engineering experiments
- SLA monitoring and alerting

**What You'll Learn:**
- Resilience engineering principles
- Circuit breaker states and transitions
- Fallback strategies for ML systems
- Chaos engineering practices
- SLA definition and monitoring
- Failure recovery patterns

**Fintech Application - CRITICAL:**

**The Banking Reality:**
```
Banking SLAs are Non-Negotiable:
- 99.9% uptime = 8.76 hours downtime/year MAX
- Transaction processing CANNOT stop
- "Sorry, ML is down" = Unacceptable to regulators
- Fraud detection must continue (even degraded)

Real Outages That Have Happened:
1. OpenAI API down for 6 hours (2023)
2. AWS us-east-1 outage (2021) - 11 hours
3. Database connection pool exhausted
4. Network partition between services
5. Memory leak crashes container

What Banks Do:
- Multi-layer fallbacks (ML → Rules → Manual)
- Circuit breakers (stop hammering failing service)
- Graceful degradation (reduce features, not fail)
- Chaos testing (break things intentionally)
```

**The Problem Without Resilience:**
```
Scenario: OpenAI API goes down

Without Circuit Breaker:
1. Every fraud check calls OpenAI
2. Each request times out after 30 seconds
3. 100 requests/sec × 30s = 3,000 hanging requests
4. Thread pool exhausted
5. Entire service crashes
6. ALL transactions blocked (not just fraud checks)
7. Bank loses $50,000/minute in blocked payments
8. Regulatory violation (must process payments)

With Circuit Breaker + Fallback:
1. First 5 failures detected
2. Circuit opens immediately
3. Stop calling OpenAI (save resources)
4. Switch to rule-based fraud detection
5. Fraud detection continues (90% accuracy vs 95%, but working)
6. Transactions processed normally
7. Circuit auto-retries OpenAI every 60 seconds
8. When OpenAI back, circuit closes, resume ML
```

**Week 24 Achieves:**
1. Detect failures fast (5 failures in 10 seconds)
2. Stop hammering failed service (circuit opens)
3. Fallback to rules (offline mode)
4. Monitor recovery (auto-retry)
5. Return to normal (circuit closes)
6. Test with chaos (simulate failures)

---

## DAY 1 (MONDAY): Circuit Breaker Fundamentals

**Time:** 1.5 hours

### SESSION 1: Resilience Patterns (45 min)

**Learning Resources:**

**Video:**
- "Circuit Breaker Pattern" - Fireship
- URL: https://www.youtube.com/watch?v=ADHcBxEXvFA
- Duration: 5:43
- Focus: Core concept, states, transitions

**Reading:**
- "Circuit Breaker Pattern" - Martin Fowler
- URL: https://martinfowler.com/bliki/CircuitBreaker.html
- Duration: 10 min
- Focus: Classic pattern explanation

**Additional Reading:**
- "Release It! Design Patterns" - Michael Nygard (excerpts)
- Chapter on circuit breakers and bulkheads
- Duration: 20 min
- Focus: Production resilience patterns

**What You Need to Understand:**

**The Three States:**

**1. CLOSED (Normal Operation):**
```
Everything working normally
- Requests pass through to service
- Failures counted
- If failures exceed threshold → OPEN
```

**2. OPEN (Failure Detected):**
```
Service is failing
- Requests DO NOT pass through
- Return fallback response immediately
- Save resources (no wasted calls)
- After timeout period → HALF_OPEN
```

**3. HALF_OPEN (Testing Recovery):**
```
Testing if service recovered
- Allow limited requests through (e.g., 3)
- If successful → CLOSED (resume normal)
- If failed → OPEN (still broken)
```

**State Transitions:**
```
CLOSED → OPEN:
- Condition: 5 failures in 10 seconds
- Action: Stop all requests, return fallback

OPEN → HALF_OPEN:
- Condition: 60 seconds elapsed
- Action: Allow 3 test requests

HALF_OPEN → CLOSED:
- Condition: 3 test requests succeed
- Action: Resume normal operation

HALF_OPEN → OPEN:
- Condition: 1 test request fails
- Action: Back to open, reset timeout
```

**Why This Matters:**

**Resource Protection:**
- Prevent thread pool exhaustion
- Reduce wasted network calls
- Free resources for healthy services

**Fast Failure:**
- Fail in milliseconds (not 30 second timeouts)
- Better user experience
- Prevent cascade failures

**Automatic Recovery:**
- Self-healing system
- No manual intervention needed
- Tests recovery automatically

### SESSION 2: Tenacity Library (45 min)

**Learning Resources:**

**Reading:**
- "Tenacity Documentation"
- URL: https://tenacity.readthedocs.io/
- Duration: 20 min
- Focus: Retry decorators, wait strategies, stop conditions

**What You Need to Understand:**

**Tenacity Features:**

**1. Retry Decorators:**
- Automatic retry on exception
- Configurable retry conditions
- Wait strategies between retries
- Stop conditions (max attempts, timeout)

**2. Wait Strategies:**
- Fixed wait: 5 seconds between retries
- Exponential backoff: 5s, 10s, 20s, 40s...
- Random jitter: Prevent thundering herd

**3. Stop Conditions:**
- Max attempts: Stop after N tries
- Time limit: Stop after T seconds
- Exception-based: Stop on specific errors

**4. Callbacks:**
- Before retry: Log attempt
- After retry: Record metrics
- On exception: Custom handling

**Circuit Breaker with Tenacity:**
- Not built-in to tenacity
- Need external circuit breaker library
- Or implement manually
- Tenacity handles retries, not circuit breaking

**Alternative Libraries:**
- pybreaker: Pure circuit breaker
- circuitbreaker: Simpler decorator
- resilience4j: Java equivalent (for reference)

### SESSION 3: Design Circuit Breaker (Requirements)

**Requirements:**

Design circuit breaker for OpenAI API calls:

**Component 1: Circuit Breaker State Manager**
- Requirements: Track state and failures
- States: CLOSED, OPEN, HALF_OPEN
- Failure threshold: 5 failures in 10-second window
- Open timeout: 60 seconds
- Half-open test requests: 3
- What to figure out: How to track failures in time window (sliding window? fixed window?)
- Document: State machine diagram

**Component 2: Failure Detection**
- Requirements: Define what counts as failure
- Failures:
  - Timeout (> 30 seconds)
  - HTTP 5xx errors
  - Connection errors
  - Rate limit errors (429)
- Not failures:
  - HTTP 4xx (except 429)
  - Validation errors
- What to figure out: Should degraded responses (high latency) count as failures?
- Document: Failure criteria

**Component 3: Fallback Strategy**
- Requirements: What to do when circuit OPEN
- Option 1: Return cached response (if available)
- Option 2: Return rule-based fraud detection
- Option 3: Return error with retry-after header
- Recommended: Option 2 (rule-based fallback)
- What to figure out: How to communicate degraded mode to client
- Document: Fallback behavior

**Component 4: Metrics and Logging**
- Requirements: Track circuit breaker health
- Metrics needed:
  - Current state (CLOSED/OPEN/HALF_OPEN)
  - Failure count (last 10 seconds)
  - Success rate
  - Time in OPEN state
  - Circuit trips per hour
- Logs:
  - State transitions (CLOSED → OPEN)
  - Each failure
  - Recovery attempts
- What to figure out: How to alert when circuit opens
- Document: Observability requirements

**Component 5: Configuration**
- Requirements: Make thresholds configurable
- Configurable parameters:
  - Failure threshold (default: 5)
  - Time window (default: 10 seconds)
  - Open timeout (default: 60 seconds)
  - Half-open test count (default: 3)
- Storage: Environment variables or config file
- What to figure out: Appropriate values for your system
- Document: Configuration spec

**Component 6: Testing Requirements**
- Requirements: How to test circuit breaker
- Test scenarios:
  - 5 consecutive failures → circuit opens
  - Circuit stays open for 60 seconds
  - After 60s, allows 3 test requests
  - 3 successes → circuit closes
  - 1 failure in half-open → back to open
  - Fallback response returned when open
- What to figure out: How to simulate failures in tests
- Document: Test strategy

**Success Criteria:**
- Circuit breaker state machine designed
- Failure detection criteria defined
- Fallback strategy documented
- Metrics and logging specified
- Configuration parameters identified
- Test scenarios documented

---

## DAY 2 (TUESDAY): Offline Fallback System

**Time:** 1.5 hours

### SESSION 1: Rule-Based Fraud Detection (45 min)

**Learning Resources:**

**Reading:**
- "Rule-Based vs ML Systems"
- URL: Search for "rule-based fraud detection vs machine learning"
- Duration: 15 min
- Focus: When rules work, when ML needed

**What You Need to Understand:**

**Rule-Based Fraud Detection:**
```
How It Works:
- IF amount > $5,000 AND merchant = "electronics" → HIGH RISK
- IF location != customer_country AND amount > $1,000 → SUSPICIOUS
- IF velocity > 5 transactions in 10 minutes → BLOCK

Advantages:
- Deterministic (same input = same output)
- Fast (<1ms)
- No external dependencies
- Explainable (shows which rule triggered)
- Works offline

Disadvantages:
- Lower accuracy (85% vs 95% with ML)
- Misses subtle patterns
- Requires manual rule updates
- Brittle (fraudsters learn rules)

When to Use:
- ML service unavailable (fallback)
- Low-risk transactions (save ML costs)
- Compliance requirements (explainability)
- Cold start (no ML model yet)
```

**Banking Rule Categories:**

**1. Amount-Based Rules:**
- Transaction amount vs customer average
- Daily/weekly spending limits
- Unusual high-value transactions

**2. Location-Based Rules:**
- Geographic distance from last transaction
- High-risk countries
- Impossible travel (NYC → London in 1 hour)

**3. Merchant-Based Rules:**
- High-risk merchant categories
- First-time merchant
- Merchant reputation score

**4. Velocity-Based Rules:**
- Transactions per minute/hour/day
- Consecutive declined transactions
- Multiple cards from same IP

**5. Time-Based Rules:**
- Unusual transaction times (3 AM)
- Frequency patterns
- Weekend vs weekday behavior

### SESSION 2: Build Rule Engine (Requirements)

**Requirements:**

Build rule-based fraud detection system:

**Component 1: Rule Categories**
- Requirements: Implement 5 rule categories
- Categories:
  1. Amount rules (5 rules)
  2. Location rules (4 rules)
  3. Merchant rules (3 rules)
  4. Velocity rules (4 rules)
  5. Time rules (3 rules)
- Total: 19 rules minimum
- What to figure out: Which rules most effective
- Document: Rule catalog

**Rule 1: High Amount**
- Requirements: Detect unusually high transactions
- Logic: amount > customer_average_transaction × 5
- Risk score: +30 points
- Example: Customer averages $50, transaction is $300 → SUSPICIOUS
- What to figure out: Appropriate multiplier (3x? 5x? 10x?)
- Document: High amount rule

**Rule 2: Geographic Anomaly**
- Requirements: Detect unusual locations
- Logic: transaction_country != customer_home_country
- Risk score: +25 points
- Enhanced: Calculate distance from last transaction
- What to figure out: How to handle traveling customers
- Document: Location rule

**Rule 3: High-Risk Merchant**
- Requirements: Flag risky merchant categories
- High-risk categories:
  - Electronics (often stolen cards)
  - Wire transfers
  - Gambling
  - Cryptocurrency
  - Adult entertainment
- Risk score: +20 points per category
- What to figure out: Complete list of high-risk categories
- Document: Merchant rules

**Rule 4: Velocity Check**
- Requirements: Detect rapid transactions
- Logic: Count transactions in last 10 minutes
- Thresholds:
  - > 3 transactions → +15 points
  - > 5 transactions → +30 points (block)
- What to figure out: Appropriate time windows
- Document: Velocity rules

**Rule 5: Unusual Time**
- Requirements: Detect odd transaction times
- Logic: transaction_hour between 1 AM and 5 AM
- Risk score: +10 points
- Enhanced: Compare to customer's typical hours
- What to figure out: Timezone handling
- Document: Time-based rules

**Component 2: Risk Scoring System**
- Requirements: Combine rule scores
- Scoring:
  - Each rule contributes points (0-30)
  - Sum all triggered rules
  - Final score: 0-100
- Thresholds:
  - 0-30: LOW RISK (approve)
  - 31-60: MEDIUM RISK (review)
  - 61-100: HIGH RISK (block)
- What to figure out: Calibrate thresholds with historical data
- Document: Scoring algorithm

**Component 3: Rule Triggering Logic**
- Requirements: Evaluate all rules, return triggered ones
- Process:
  1. Run all 19 rules
  2. Collect triggered rules
  3. Sum risk scores
  4. Determine final risk level
  5. Return: risk_score, triggered_rules[], recommendation
- What to figure out: Run rules in parallel or sequential?
- Document: Evaluation logic

**Component 4: Response Format**
- Requirements: Match ML service response format
- Response structure:
  - is_fraud: boolean
  - risk_score: 0-100
  - risk_factors: list of triggered rules
  - recommendation: "APPROVE" | "BLOCK" | "REVIEW"
  - mode: "FALLBACK" (indicate rule-based)
- What to figure out: How to communicate fallback mode to client
- Document: Response schema

**Component 5: Rule Configuration**
- Requirements: Make rules configurable
- Configuration file: rules.yaml
- Per-rule settings:
  - enabled: true/false
  - weight: risk score contribution
  - threshold: trigger condition
- What to figure out: Hot-reload rules without restart?
- Document: Configuration format

**Component 6: Performance Requirements**
- Requirements: Fast execution
- Target: Complete evaluation in < 5ms
- Optimization:
  - Short-circuit evaluation (stop early if score > 100)
  - Cache customer data
  - Precompute velocity counters
- What to figure out: Measure actual performance
- Document: Performance benchmarks

**Success Criteria:**
- 19+ rules implemented
- Risk scoring algorithm working
- Response format matches ML service
- Configuration externalized
- Evaluation time < 5ms
- Can replace ML service transparently

---

## DAY 3 (WEDNESDAY): Graceful Degradation

**Time:** 1.5 hours

### SESSION 1: Degradation Strategies (45 min)

**Learning Resources:**

**Reading:**
- "Graceful Degradation vs Progressive Enhancement"
- URL: https://www.w3.org/wiki/Graceful_degradation_versus_progressive_enhancement
- Duration: 10 min
- Focus: Core concepts (from web, applies to backend)

**Additional Reading:**
- "Building Resilient Systems" - AWS Well-Architected
- URL: https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.reliability.en.html
- Duration: 20 min
- Focus: Reliability patterns

**What You Need to Understand:**

**Graceful Degradation Concept:**
```
Hard Failure (Bad):
Service down → Return 500 error → User sees "System unavailable"

Graceful Degradation (Good):
Service down → Reduce features → User gets partial service

Example - Fraud Detection:
Level 1: ML fraud detection (95% accuracy)
  ↓ (if OpenAI down)
Level 2: Rule-based detection (85% accuracy)
  ↓ (if database down)
Level 3: Basic checks only (70% accuracy)
  ↓ (if everything down)
Level 4: Allow all transactions (0% detection, but payments work)
```

**Banking Application:**
```
Tier 1: Full Service (All systems operational)
- ML fraud detection (GPT-4)
- RAG for policy lookup
- Real-time risk scoring
- Customer behavior analysis

Tier 2: Degraded Service (ML unavailable)
- Rule-based fraud detection
- Cached policy responses
- Static risk scores
- Basic behavior checks

Tier 3: Minimal Service (Database read-only)
- Basic fraud rules only
- No history lookup
- All transactions flagged for review
- Manual approval required

Tier 4: Emergency Mode (Database down)
- Allow transactions < $100
- Block transactions > $100
- Log all for batch processing
- Manual reconciliation later

Tier 5: Maintenance Mode (Planned outage)
- Return maintenance message
- Queue transactions for later
- Provide expected recovery time
```

### SESSION 2: Implement Degradation Tiers (Requirements)

**Requirements:**

Implement 5 degradation tiers:

**Component 1: Health Check System**
- Requirements: Check health of all dependencies
- Dependencies to check:
  - OpenAI API (POST /v1/chat/completions)
  - PostgreSQL database (SELECT 1)
  - Redis cache (PING)
  - OpenSearch (GET /_cluster/health)
- Health states:
  - HEALTHY: Response time < 100ms, success
  - DEGRADED: Response time 100-1000ms, or occasional failures
  - UNHEALTHY: Timeouts or consistent failures
- What to figure out: How often to check health (every 10 seconds?)
- Document: Health check spec

**Component 2: Tier Selection Logic**
- Requirements: Automatically select appropriate tier
- Decision tree:
  - All healthy → Tier 1 (Full)
  - ML unhealthy → Tier 2 (Degraded)
  - DB degraded → Tier 3 (Minimal)
  - DB unhealthy → Tier 4 (Emergency)
  - Planned maintenance → Tier 5 (Maintenance)
- What to figure out: Should tier selection be automatic or manual override?
- Document: Tier selection algorithm

**Tier 1: Full Service**
- Requirements: All features enabled
- Features:
  - GPT-4 fraud detection
  - RAG policy lookup
  - Real-time embeddings
  - Customer behavior analysis
  - Full transaction history
- Response time: < 2 seconds (P95)
- Accuracy: 95%
- What to figure out: Performance baseline
- Document: Full service SLA

**Tier 2: Degraded Service (ML Offline)**
- Requirements: Rule-based fallback
- Features enabled:
  - Rule-based fraud detection (19 rules)
  - Database queries (transaction history)
  - Redis cache (embeddings)
  - Basic risk scoring
- Features disabled:
  - GPT-4 calls
  - RAG responses
  - Real-time embeddings
- Response time: < 500ms (P95)
- Accuracy: 85%
- Indicator: Response includes "mode": "DEGRADED"
- What to figure out: How to communicate degradation to users
- Document: Degraded mode spec

**Tier 3: Minimal Service (Database Read-Only)**
- Requirements: Minimal fraud checks
- Features enabled:
  - Basic amount checks (> $5,000 = high risk)
  - Cached customer data (if available)
  - Simple rule subset (5 critical rules only)
- Features disabled:
  - Database writes
  - Transaction history lookup
  - Velocity checks (need DB)
- Response time: < 200ms (P95)
- Accuracy: 70%
- Behavior: Flag all transactions > $1,000 for manual review
- What to figure out: Which 5 rules are most critical
- Document: Minimal mode spec

**Tier 4: Emergency Mode (Database Offline)**
- Requirements: Allow critical transactions only
- Logic:
  - Amount < $100 → APPROVE (low risk)
  - Amount >= $100 → BLOCK (require manual approval)
- Features disabled:
  - All database queries
  - All ML/rules
  - History lookup
- Behavior:
  - Log all transactions to file
  - Queue for batch processing when DB recovers
  - Return "EMERGENCY_MODE" in response
- What to figure out: How to persist transactions without database
- Document: Emergency mode spec

**Tier 5: Maintenance Mode**
- Requirements: Planned maintenance
- Response: HTTP 503 Service Unavailable
- Headers:
  - Retry-After: 3600 (1 hour)
  - X-Maintenance-Mode: true
- Body:
  - Message: "Scheduled maintenance in progress"
  - Expected recovery: ISO timestamp
  - Contact: Support email
- What to figure out: How to schedule maintenance windows
- Document: Maintenance mode spec

**Component 3: Tier Transition Logic**
- Requirements: Smooth transitions between tiers
- Rules:
  - Degrade immediately when unhealthy detected
  - Recover gradually (wait 5 minutes of healthy before upgrading)
  - No flip-flopping (hysteresis - different thresholds for up/down)
- Alerts:
  - Slack: "Degraded to Tier 2 - ML offline"
  - PagerDuty: "Emergency - Tier 4 activated"
- What to figure out: Recovery wait times per tier
- Document: Transition logic

**Component 4: Client Communication**
- Requirements: Inform clients of degraded mode
- Methods:
  - Response header: X-Service-Tier: DEGRADED
  - Response body: "mode": "DEGRADED"
  - Status code: Still 200 (success), not 503
  - Documentation: API docs explain tier meanings
- What to figure out: Should clients retry differently in degraded mode?
- Document: Client communication spec

**Component 5: Monitoring Degradation**
- Requirements: Track tier changes and duration
- Metrics:
  - Current tier (gauge)
  - Time in each tier (counter)
  - Tier transitions per day (counter)
  - Requests served per tier (counter)
- Dashboards:
  - Service Tier Timeline (visualize tier changes)
  - Requests by Tier (pie chart)
  - Degradation Impact (accuracy drop)
- What to figure out: SLA impact of degradation
- Document: Degradation monitoring

**Success Criteria:**
- 5 tiers implemented
- Health check system working
- Automatic tier selection
- Smooth transitions
- Client notifications
- Monitoring dashboards
- Can handle all failure scenarios gracefully

---

## DAY 4 (THURSDAY): Chaos Engineering

**Time:** 1.5 hours

### SESSION 1: Chaos Engineering Principles (45 min)

**Learning Resources:**

**Video:**
- "Chaos Engineering Explained" - AWS re:Invent
- URL: https://www.youtube.com/watch?v=FrfkP1MX4hM
- Duration: 25:00
- Focus: Principles, Netflix Chaos Monkey

**Reading:**
- "Principles of Chaos Engineering"
- URL: https://principlesofchaos.org/
- Duration: 15 min
- Focus: Core principles, steady state

**What You Need to Understand:**

**Chaos Engineering Definition:**
```
Breaking things intentionally to build confidence

NOT:
- Random destructive testing
- Production incidents
- Hope and pray

IS:
- Controlled experiments
- Hypothesis-driven
- Measured impact
- Learning from failures
```

**The Principles:**

**1. Define Steady State:**
- Measurable output indicating normal behavior
- Examples:
  - Request success rate > 99%
  - Latency P95 < 2 seconds
  - Fraud detection accuracy > 90%

**2. Hypothesize Steady State Continues:**
- "I believe the system will maintain 99% success rate even if OpenAI is unavailable"
- Test this hypothesis

**3. Introduce Real-World Chaos:**
- Simulates actual failures that can happen
- Examples:
  - Service crashes
  - Network delays
  - Database slow queries
  - Disk full
  - High CPU

**4. Disprove Hypothesis:**
- Try to break the system
- If steady state maintained → System is resilient
- If steady state violated → Found a weakness

**Chaos Experiments for Fraud Detection:**

**Experiment 1: OpenAI Unavailable**
- Hypothesis: System falls back to rules, maintains > 85% accuracy
- Chaos: Block outbound calls to api.openai.com
- Measure: Success rate, latency, accuracy
- Expected: Circuit opens, rules activate, no errors

**Experiment 2: Database Latency**
- Hypothesis: System handles slow DB queries gracefully
- Chaos: Add 5-second delay to database queries
- Measure: Request timeouts, error rate
- Expected: Timeouts handled, fallback triggered

**Experiment 3: Memory Exhaustion**
- Hypothesis: Container restarts without losing transactions
- Chaos: Allocate memory until OOM kill
- Measure: Request loss, recovery time
- Expected: ECS restarts container, no data loss

**Experiment 4: Network Partition**
- Hypothesis: Service degrades gracefully when isolated
- Chaos: Drop 50% of network packets
- Measure: Error rate, retry behavior
- Expected: Retries succeed, circuit breakers prevent overload

**Experiment 5: Cascading Failure**
- Hypothesis: Failure doesn't cascade to healthy services
- Chaos: Make fraud service very slow (10s latency)
- Measure: Impact on Java backend, transaction processing
- Expected: Java times out cleanly, transactions continue

### SESSION 2: Design Chaos Experiments (Requirements)

**Requirements:**

Design 5 chaos experiments:

**Experiment 1: OpenAI API Failure**
- Requirements: Test circuit breaker and fallback
- Hypothesis: "When OpenAI unavailable, circuit opens within 10 seconds and fallback maintains > 85% fraud detection accuracy"
- Chaos injection: Block DNS resolution for api.openai.com
- Duration: 5 minutes
- Measurements:
  - Time to circuit open
  - Fallback activation time
  - Fraud detection accuracy (compare with historical)
  - Request success rate (should be 100%)
  - Response latency (should be faster with fallback)
- Success criteria:
  - Circuit opens within 10 seconds
  - Fallback accuracy > 85%
  - Zero 5xx errors
  - Latency < 500ms during fallback
- What to figure out: How to inject DNS failure
- Document: Experiment #1 plan

**Experiment 2: Database Connection Pool Exhaustion**
- Requirements: Test connection handling
- Hypothesis: "When database connections exhausted, service queues requests and doesn't crash"
- Chaos injection: Set max connections to 5, send 100 concurrent requests
- Duration: 2 minutes
- Measurements:
  - Connection pool wait time
  - Request queue depth
  - Timeout errors
  - Container crashes
- Success criteria:
  - No container crashes
  - Requests queue gracefully
  - Clear error messages for timeouts
- What to figure out: How to limit connection pool
- Document: Experiment #2 plan

**Experiment 3: ECS Task Sudden Termination**
- Requirements: Test graceful shutdown
- Hypothesis: "When ECS task killed, in-flight requests complete successfully"
- Chaos injection: Send SIGTERM to container
- Duration: 30 seconds grace period
- Measurements:
  - In-flight requests at termination
  - Requests completed successfully
  - Requests lost/failed
  - Time to shutdown
- Success criteria:
  - All in-flight requests complete
  - Shutdown within 30 seconds
  - ALB removes from rotation immediately
- What to figure out: Graceful shutdown implementation
- Document: Experiment #3 plan

**Experiment 4: Network Partition Between Services**
- Requirements: Test Java-Python integration resilience
- Hypothesis: "When network between Java and Python fails, Java falls back to cached results or rule-based detection"
- Chaos injection: Drop 100% of packets between Java and Python services
- Duration: 3 minutes
- Measurements:
  - Java service error rate
  - Java fallback activation
  - End-user transaction success rate
  - Recovery time when network restored
- Success criteria:
  - Java detects failure within 5 seconds
  - Activates fallback
  - Transactions continue processing
  - Auto-recovers when network restored
- What to figure out: Java service fallback implementation
- Document: Experiment #4 plan

**Experiment 5: Resource Exhaustion (CPU)**
- Requirements: Test auto-scaling response
- Hypothesis: "When CPU saturated, ECS auto-scales and maintains P95 latency < 5 seconds"
- Chaos injection: Run CPU-intensive task consuming 90% CPU
- Duration: 10 minutes
- Measurements:
  - CPU utilization
  - Request latency (P95, P99)
  - Auto-scaling triggers
  - Number of tasks scaled
  - Time to scale
- Success criteria:
  - Auto-scaling triggers within 3 minutes
  - Tasks scale from 2 → 4+
  - P95 latency stays < 5 seconds
  - No request failures
- What to figure out: Auto-scaling configuration tuning
- Document: Experiment #5 plan

**Component: Chaos Testing Framework**
- Requirements: Reusable chaos injection framework
- Features needed:
  - Experiment scheduler (run daily/weekly)
  - Chaos injection methods (network, CPU, memory, service failure)
  - Metrics collection (before, during, after)
  - Automated rollback (if experiment causes actual outage)
  - Blast radius control (affect only 1 task, not all)
  - Safety checks (don't run in production during peak hours)
- What to figure out: Use chaos tool (Chaos Mesh, Gremlin) or build custom
- Document: Framework requirements

**Component: Experiment Execution**
- Requirements: How to run experiments safely
- Process:
  1. Review hypothesis with team
  2. Set monitoring alerts
  3. Start experiment in test environment
  4. Monitor steady state metrics
  5. Inject chaos
  6. Observe impact
  7. Restore normal state
  8. Analyze results
  9. Document learnings
  10. Fix weaknesses found
- Safety: Never run in production without thorough testing in staging
- What to figure out: Experiment review process
- Document: Execution procedure

**Component: Results Documentation**
- Requirements: Document experiment outcomes
- Documentation needed:
  - Hypothesis (what we believed)
  - Actual results (what happened)
  - Metrics collected
  - Weaknesses discovered
  - Fixes implemented
  - Re-test results
- Format: Experiment report template
- What to figure out: Knowledge sharing process
- Document: Report template

**Success Criteria:**
- 5 experiments designed
- Hypotheses clearly stated
- Chaos injection methods defined
- Measurements specified
- Success criteria set
- Safety procedures documented
- Framework requirements defined

---

## DAY 5 (FRIDAY): SLA Monitoring

**Time:** 1 hour

### SESSION 1: Define SLAs (30 min)

**Learning Resources:**

**Reading:**
- "SLI, SLO, SLA - Google SRE Book"
- URL: https://sre.google/sre-book/service-level-objectives/
- Duration: 20 min
- Focus: Defining good SLOs

**What You Need to Understand:**

**SLI vs SLO vs SLA:**

**SLI (Service Level Indicator):**
- Metric that measures service quality
- Examples:
  - Request success rate
  - Latency
  - Throughput

**SLO (Service Level Objective):**
- Target value for SLI
- Internal goal
- Examples:
  - Success rate > 99.9%
  - P95 latency < 2 seconds

**SLA (Service Level Agreement):**
- Contract with customers
- Promise with consequences
- Examples:
  - 99.9% uptime or money back
  - < 2s latency or penalty

**Banking SLA Requirements:**
```
Regulatory Requirements:
- Payment systems must have 99.9%+ uptime
- Transaction processing cannot stop
- Fraud detection must be available 24/7
- Audit trail must be complete

Typical Banking SLAs:
- Uptime: 99.95% (4.38 hours/year downtime)
- Latency: P95 < 2 seconds
- Error rate: < 0.1%
- Data freshness: < 5 minutes
```

### SESSION 2: Implement SLA Monitoring (Requirements)

**Requirements:**

Define and monitor 4 critical SLAs:

**SLA 1: Availability**
- Requirements: Track uptime
- Target: 99.9% uptime (8.76 hours/year downtime)
- Measurement: Successful health check responses / Total health checks
- Health check: GET /health every 30 seconds
- Success: HTTP 200 response within 5 seconds
- Tracking window: Rolling 30-day window
- What to figure out: How to track uptime accurately (third-party monitoring?)
- Document: Availability SLA

**SLA 2: Latency**
- Requirements: Track response times
- Target: P95 latency < 2 seconds
- Measurement: Time from request received to response sent
- Endpoints to track:
  - POST /api/v1/predict (fraud detection)
  - GET /api/v1/health
- Tracking: Histogram metric, calculate P50, P95, P99
- Reporting: Daily latency report
- What to figure out: Latency breakdown by component (Java, Python, DB, OpenAI)
- Document: Latency SLA

**SLA 3: Error Rate**
- Requirements: Track failures
- Target: < 1% error rate
- Measurement: (4xx + 5xx responses) / Total requests
- Exclusions: Intentional 400 errors (validation failures)
- Tracking: Per endpoint error rate
- Alert: > 1% errors for 5 minutes → Page on-call
- What to figure out: Which error codes count as SLA violations
- Document: Error rate SLA

**SLA 4: Data Freshness**
- Requirements: Fraud model uses recent data
- Target: Customer data refreshed within 5 minutes
- Measurement: Current time - Last data sync timestamp
- Data sources:
  - Customer profile (name, address, limits)
  - Transaction history (last 90 days)
  - Behavior patterns (spending habits)
- Alert: Sync delay > 5 minutes → Warning
- What to figure out: How to measure data freshness
- Document: Data freshness SLA

**Component: SLA Dashboard**
- Requirements: Real-time SLA monitoring
- Widgets needed:
  - Current uptime % (30-day rolling)
  - Latency percentiles (P50, P95, P99) - last hour
  - Error rate (last 24 hours)
  - Data freshness (current delay)
  - SLA compliance trend (last 90 days)
- Color coding:
  - Green: Meeting SLA
  - Yellow: Within 5% of SLA
  - Red: Violating SLA
- What to figure out: Dashboard refresh rate
- Document: Dashboard specification

**Component: SLA Alerts**
- Requirements: Alert when SLA violated
- Alert levels:
  - WARNING: Within 5% of SLA threshold
  - CRITICAL: SLA violated
  - EMERGENCY: Multiple SLAs violated
- Destinations:
  - Slack: All alerts
  - PagerDuty: CRITICAL and EMERGENCY only
  - Email: Daily summary
- What to figure out: Alert fatigue prevention
- Document: Alerting rules

**Component: SLA Reporting**
- Requirements: Regular SLA reports
- Reports needed:
  - Daily: SLA compliance summary
  - Weekly: Trend analysis
  - Monthly: Executive summary with incidents
  - Quarterly: SLA review for adjustments
- Metrics to include:
  - Actual vs target SLA
  - Number of violations
  - Duration of violations
  - Root causes
  - Remediation actions
- What to figure out: Report distribution list
- Document: Reporting requirements

**Component: Error Budget**
- Requirements: Calculate remaining error budget
- Concept: If SLA is 99.9%, you have 0.1% "allowed failures"
- Calculation:
  - Total requests in 30 days: 100,000,000
  - Error budget: 100,000 (0.1%)
  - Errors so far: 45,000
  - Remaining budget: 55,000 (55%)
- Use: Decide when to deploy (don't deploy if budget low)
- What to figure out: Error budget policy (freeze deploys at what threshold?)
- Document: Error budget spec

**Success Criteria:**
- 4 SLAs defined clearly
- Measurement methods specified
- Targets set appropriately
- Dashboard designed
- Alerts configured
- Reporting automated
- Error budget tracked

---

## DAY 6 (SATURDAY): Testing & Validation

**Time:** 2.5 hours

### SESSION: Comprehensive Resilience Testing (Requirements)

**Requirements:**

Test all resilience mechanisms:

**Test Suite 1: Circuit Breaker Tests**
- Requirements: Validate circuit breaker behavior
- Test scenarios:
  1. 5 failures → Circuit opens
  2. Circuit stays open for 60 seconds
  3. After 60s, allows 3 test requests
  4. 3 successes → Circuit closes
  5. 1 failure in half-open → Back to open
  6. Fallback response returned when open
  7. Metrics accurately track state
  8. Alerts sent on state change
  9. Configuration changes take effect
  10. Concurrent requests handled correctly
- What to figure out: How to inject failures reliably in tests
- Document: Circuit breaker test suite

**Test Suite 2: Fallback System Tests**
- Requirements: Validate rule-based fallback
- Test scenarios:
  1. Fallback matches ML response format
  2. 19 rules evaluate correctly
  3. Risk score calculated accurately
  4. High-risk transactions blocked
  5. Low-risk transactions approved
  6. Edge cases handled (missing data)
  7. Performance < 5ms
  8. Fallback indication in response
  9. Logging captures all rule triggers
  10. Configuration updates work
- What to figure out: Test data for all 19 rules
- Document: Fallback test suite

**Test Suite 3: Degradation Tests**
- Requirements: Validate all 5 tiers
- Test scenarios:
  1. Tier 1: Full service works
  2. Tier 2: ML offline, rules activate
  3. Tier 3: DB read-only, minimal rules work
  4. Tier 4: DB offline, emergency mode activates
  5. Tier 5: Maintenance mode returns 503
  6. Transitions happen automatically
  7. Recovery waits appropriate time
  8. No flip-flopping between tiers
  9. Alerts sent on tier changes
  10. Client notifications work
- What to figure out: How to simulate each failure type
- Document: Degradation test suite

**Test Suite 4: Chaos Experiment Validation**
- Requirements: Run all 5 experiments in test environment
- Experiments to validate:
  1. OpenAI failure experiment
  2. Database pool exhaustion
  3. ECS task termination
  4. Network partition
  5. CPU saturation
- For each:
  - Run in test environment
  - Validate hypothesis
  - Measure metrics
  - Document results
  - Identify weaknesses
  - Fix issues found
  - Re-test
- What to figure out: Experiment automation
- Document: Chaos validation results

**Test Suite 5: SLA Monitoring Validation**
- Requirements: Verify SLA tracking accuracy
- Test scenarios:
  1. Uptime calculated correctly
  2. Latency percentiles accurate
  3. Error rate tracking works
  4. Data freshness measured
  5. Dashboard updates in real-time
  6. Alerts trigger at thresholds
  7. Reports generated correctly
  8. Error budget calculated
  9. SLA violations logged
  10. Historical data retained
- What to figure out: How to verify accuracy
- Document: Monitoring validation

**Load Testing Requirements:**
- Requirements: Test under realistic load during failures
- Scenarios:
  1. Normal load: 100 TPS, ML working
  2. High load: 500 TPS, ML working
  3. Normal load: 100 TPS, ML failing (circuit open)
  4. High load: 500 TPS, ML failing
  5. Spike: 0 → 1000 TPS suddenly, ML working
  6. Spike during failure: 0 → 1000 TPS, ML failing
- Measurements:
  - Latency under each scenario
  - Error rate
  - Circuit breaker behavior
  - Fallback performance
  - Auto-scaling response
- Tools: k6, Locust, or Artillery
- What to figure out: Realistic load patterns
- Document: Load test requirements

**Integration Testing Requirements:**
- Requirements: End-to-end testing with all components
- Test flow:
  1. Java sends request to Python
  2. Python calls OpenAI (mocked)
  3. OpenAI fails after 3 requests
  4. Circuit opens
  5. Python switches to fallback
  6. Java receives response (mode: DEGRADED)
  7. Java handles degraded response
  8. OpenAI recovers
  9. Circuit closes
  10. Resume normal operation
- What to figure out: Test environment setup
- Document: Integration test scenarios

**Success Criteria:**
- All test suites passing
- 50+ test scenarios covered
- Load testing completed
- Performance benchmarks established
- Chaos experiments validated
- SLA monitoring verified
- Integration testing complete
- Zero critical bugs found

---

## DAY 7 (SUNDAY): Week Summary

**Time:** 2 hours

### SESSION: Documentation & Runbooks (Requirements)

**Requirements:**

Create comprehensive resilience documentation:

**Document 1: Circuit Breaker Runbook**
- Requirements: Operations guide for circuit breakers
- Sections:
  1. What is circuit breaker
  2. Current configuration
  3. How to check circuit state
  4. What to do when circuit opens
  5. How to manually trip circuit
  6. How to manually reset circuit
  7. How to adjust thresholds
  8. Troubleshooting common issues
  9. Metrics and alerts
- Audience: On-call engineers
- What to figure out: Common troubleshooting scenarios
- Document: CIRCUIT_BREAKER_RUNBOOK.md

**Document 2: Degradation Playbook**
- Requirements: Guide for handling degradation
- Sections:
  1. Understanding the 5 tiers
  2. How tier selection works
  3. Monitoring current tier
  4. Manual tier override (emergency)
  5. Impact of each tier (accuracy, features)
  6. Customer communication templates
  7. Escalation procedures
  8. Recovery checklist
- Audience: On-call + managers
- What to figure out: Escalation paths
- Document: DEGRADATION_PLAYBOOK.md

**Document 3: Chaos Engineering Guide**
- Requirements: How to run chaos experiments safely
- Sections:
  1. Chaos engineering principles
  2. Experiment design template
  3. Safety procedures
  4. Approved experiments
  5. How to run an experiment
  6. Results documentation
  7. Post-experiment review
  8. Continuous improvement
- Audience: SRE team
- What to figure out: Experiment approval process
- Document: CHAOS_ENGINEERING_GUIDE.md

**Document 4: SLA Incident Response**
- Requirements: What to do when SLA violated
- Sections:
  1. SLA definitions and targets
  2. How to check SLA status
  3. Incident severity levels
  4. Response procedures per severity
  5. Communication templates
  6. Postmortem template
  7. SLA violation tracking
  8. Customer notifications
- Audience: On-call + customer support
- What to figure out: Customer notification thresholds
- Document: SLA_INCIDENT_RESPONSE.md

**Document 5: Week 24 Summary**
- Requirements: Comprehensive week summary
- Sections needed:
  - What You Built (circuit breakers, fallback, degradation, chaos, SLAs)
  - Fintech Impact (banking SLA requirements, regulatory compliance)
  - Technical Achievements (metrics, test coverage)
  - Resilience Metrics (MTTR, MTBF, recovery time)
  - Interview Talking Points (STAR format stories)
  - Next Steps (Week 25 preview)
- What to document:
  - 5 resilience mechanisms implemented
  - 50+ test scenarios
  - 5 chaos experiments
  - 4 SLAs defined and monitored
- Document: WEEK24_SUMMARY.md

**Optimization Roadmap:**
- Requirements: Future resilience improvements
- Improvements to consider:
  1. Multi-region failover (disaster recovery)
  2. Advanced chaos automation (GameDays)
  3. Predictive failure detection (ML for anomalies)
  4. Self-healing systems (auto-remediation)
  5. Chaos as a service (inject chaos in production safely)
- Prioritization: Impact vs effort matrix
- What to figure out: Which improvements provide most value
- Document: Roadmap in summary

**Success Criteria:**
- 4 runbooks/playbooks created
- Week summary comprehensive
- Fintech impact articulated
- Technical achievements quantified
- Interview stories prepared
- Optimization roadmap defined

---

## 📚 ADDITIONAL RESOURCES

**Circuit Breakers:**
- Martin Fowler Article: https://martinfowler.com/bliki/CircuitBreaker.html
- Tenacity Documentation: https://tenacity.readthedocs.io/
- pybreaker Library: https://pypi.org/project/pybreaker/

**Chaos Engineering:**
- Principles of Chaos: https://principlesofchaos.org/
- Chaos Mesh: https://chaos-mesh.org/
- AWS Fault Injection Simulator: https://aws.amazon.com/fis/

**SLAs:**
- Google SRE Book - SLOs: https://sre.google/sre-book/service-level-objectives/
- Error Budgets: https://sre.google/workbook/error-budget-policy/
- SLA Best Practices: https://aws.amazon.com/architecture/well-architected/

**Resilience Patterns:**
- Release It! - Michael Nygard (book)
- AWS Well-Architected - Reliability Pillar: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/

---

## ✅ WEEK 24 DELIVERABLES

**Documentation:**
- CIRCUIT_BREAKER_SPEC.md - Circuit breaker requirements
- FALLBACK_SYSTEM.md - Rule-based fraud detection requirements
- DEGRADATION_TIERS.md - 5-tier degradation requirements
- CHAOS_EXPERIMENTS.md - 5 experiment designs
- SLA_MONITORING.md - 4 SLA specifications
- CIRCUIT_BREAKER_RUNBOOK.md - Operations guide
- DEGRADATION_PLAYBOOK.md - Degradation handling guide
- CHAOS_ENGINEERING_GUIDE.md - Experiment procedures
- SLA_INCIDENT_RESPONSE.md - Incident handling guide
- WEEK24_SUMMARY.md - Week summary

**Requirements Specifications (No Code):**
- Circuit breaker state machine requirements
- Rule-based fraud detection (19 rules)
- Degradation tier logic (5 tiers)
- Chaos experiment procedures (5 experiments)
- SLA monitoring system (4 SLAs)
- Test suite requirements (50+ scenarios)

**Test Documentation:**
- Circuit breaker test requirements
- Fallback system test requirements
- Degradation test requirements
- Chaos validation requirements
- Load testing requirements
- Integration testing requirements

**Understanding:**
- Circuit breaker pattern
- Resilience engineering principles
- Graceful degradation strategies
- Chaos engineering methodology
- SLA definition and monitoring
- Failure recovery patterns

---

## 🎯 SUCCESS CRITERIA

**By end of Week 24:**

**Conceptual:**
- Understand circuit breaker states
- Know when to use fallbacks
- Understand graceful degradation
- Know chaos engineering principles
- Understand SLA vs SLO vs SLI

**Practical:**
- Design circuit breaker (requirements documented)
- Build rule-based fallback (19 rules documented)
- Implement 5 degradation tiers (requirements specified)
- Design 5 chaos experiments (procedures documented)
- Define 4 SLAs (monitoring requirements specified)

**Portfolio Impact:**
- ✅ Production resilience demonstrated (FINTECH CRITICAL)
- ✅ Banking SLA compliance (99.9% uptime requirement)
- ✅ Regulatory compliance (graceful degradation, not failures)
- ✅ Chaos engineering competency (rare skill)
- ✅ SLA monitoring expertise (operations maturity)

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Banking SLA compliance mandatory  
**Next Week:** Production Monitoring Stack (Week 25)