# WEEK 24 LEARNING GUIDE: Circuit Breakers + Resilience Engineering

**Timeline:** April 27 - May 3, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Circuit breaker pattern, resilience engineering, graceful degradation, chaos engineering, SLA monitoring

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Circuit breaker implementation (tenacity library)
- Offline fallback system (rule-based when AI unavailable)
- Graceful degradation strategies
- Chaos engineering tests
- SLA monitoring dashboard
- Resilience testing framework

**What You'll Learn:**
- Circuit breaker pattern fundamentals
- Resilience engineering principles
- Graceful degradation design
- Chaos engineering practices
- Retry strategies (exponential backoff)
- Bulkhead pattern
- Timeout handling
- SLA definition and monitoring

**Fintech Application - CRITICAL:**

**The Business Problem:**
```
Banking SLA Requirements:
- 99.9% uptime (8.76 hours downtime/year max)
- If fraud detection fails → transactions blocked = customer anger + lost revenue
- If OpenAI API down → system cannot go completely offline

Real-World Scenarios:
1. OpenAI API outage (happened March 2023, lasted 3 hours)
   - Your fraud detection: OFFLINE
   - Customer transactions: BLOCKED
   - Business impact: $50K revenue/hour lost

2. Database connection pool exhausted
   - New requests: FAIL
   - Customer experience: "Service unavailable"
   - Reputation damage: Trending on Twitter

3. Slow dependency (embedding model taking 30s instead of 2s)
   - All requests: TIMEOUT
   - System: OVERLOADED
   - Cascading failure: Entire platform down

Banking Regulatory Requirements (SOX, Basel III):
- Must have offline fallback for critical systems
- Cannot deny all transactions if ML unavailable
- Must log all failures for audit
- Must have disaster recovery plan
```

**The Solution - Resilience Engineering:**
```
Circuit Breaker Pattern:
┌─────────────────────────────────────────┐
│  Transaction Request                    │
└─────────┬───────────────────────────────┘
          │
          v
┌─────────────────────────────────────────┐
│  Circuit Breaker (monitors failures)    │
│                                         │
│  State: CLOSED (normal operation)       │
│  ├─ Try ML service                      │
│  ├─ If 5 failures in 10 requests        │
│  └─ OPEN circuit → Use fallback         │
│                                         │
│  State: OPEN (service degraded)         │
│  ├─ Don't call ML service               │
│  ├─ Use rule-based system               │
│  └─ After 60s → Try again (HALF-OPEN)   │
│                                         │
│  State: HALF-OPEN (testing recovery)    │
│  ├─ Try 1 request to ML service         │
│  ├─ If success → CLOSE circuit          │
│  └─ If fail → OPEN circuit again        │
└─────────────────────────────────────────┘
          │
          ├─────────┬──────────┐
          v         v          v
    ML Service  Rule-Based  Manual Review
    (Primary)   (Fallback)  (High-value)
```

**Why This Matters:**
- **SLA Compliance:** Meet 99.9% uptime requirement
- **Revenue Protection:** Keep accepting transactions during outages
- **Customer Experience:** Graceful degradation, not hard failures
- **Regulatory:** Offline fallback = compliance requirement
- **Risk Management:** Prevent cascading failures
- **Audit Trail:** Log all degraded-mode decisions

**Week 24 Achieves:**
1. Implement circuit breakers (prevent cascade failures)
2. Build rule-based fallback (work offline)
3. Test with chaos engineering (simulate failures)
4. Monitor SLAs (track uptime/latency)
5. Document degraded modes (audit compliance)

---

## DAY 1 (MONDAY): Circuit Breaker Fundamentals

**Time:** 1.5 hours

### SESSION 1: Circuit Breaker Pattern (45 min)

**Learning Resources:**

**Video:**
- "Circuit Breaker Pattern Explained" - ByteByteGo
- URL: https://www.youtube.com/watch?v=ADHcBxEXvFA
- Duration: 8:12
- Focus: Circuit breaker states, failure detection

**Reading:**
- "Circuit Breaker Pattern" - Microsoft Azure Architecture
- URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
- Duration: 20 min
- Focus: Pattern details, implementation strategies

**What You Need to Understand:**

**The Problem - Cascading Failures:**
```
Without Circuit Breaker:
User Request → API → ML Service (DOWN)
                ├─ Timeout after 30s
                ├─ Retry 3 times
                └─ Total wait: 90 seconds
                
Result:
- User waits 90s for error
- API threads blocked (thread pool exhausted)
- Other requests queued (cascading failure)
- Entire system becomes unresponsive
```

**The Solution - Circuit Breaker:**
```
With Circuit Breaker:
User Request → API → Circuit Breaker
                     ├─ Detects ML service DOWN
                     ├─ OPEN circuit immediately
                     └─ Use fallback (rule-based)
                     
Result:
- User gets response in 100ms (fast failure)
- No waiting for timeout
- API threads available for other requests
- System remains responsive
```

**Three States Explained:**

**1. CLOSED (Normal Operation)**
- Circuit: Closed (electricity flows = requests go through)
- Behavior: All requests go to ML service
- Monitoring: Track failure rate
- Transition: If failure_rate > threshold → OPEN
- Example: 5 failures in last 10 requests (50%) → OPEN

**2. OPEN (Service Degraded)**
- Circuit: Open (electricity blocked = requests blocked)
- Behavior: No requests to ML service (fail fast)
- Action: Use fallback system immediately
- Duration: Wait timeout period (e.g., 60 seconds)
- Transition: After timeout → HALF-OPEN

**3. HALF-OPEN (Testing Recovery)**
- Circuit: Half-open (testing if safe to close)
- Behavior: Allow 1 test request to ML service
- Success: ML service working → CLOSE circuit
- Failure: ML service still down → OPEN circuit again
- Purpose: Automatic recovery when service restored

**Key Parameters:**

**Failure Threshold:**
- Metric: Failure rate (failures / total requests)
- Example: 50% failures in 10-request window
- Too low (10%): Opens too easily (false positives)
- Too high (90%): Doesn't protect (opens too late)
- **Fintech Recommendation:** 30-50% threshold

**Timeout Period:**
- Duration: How long circuit stays OPEN
- Example: 60 seconds
- Too short (5s): Hammers failing service
- Too long (10m): Slow to recover
- **Fintech Recommendation:** 30-60 seconds

**Request Volume Threshold:**
- Minimum: Need X requests before calculating failure rate
- Example: At least 10 requests
- Why: Prevents opening on 1 random failure
- **Fintech Recommendation:** 10-20 requests

### SESSION 2: Tenacity Library (Python) (45 min)

**Learning Resources:**

**Reading:**
- "Tenacity Documentation" - GitHub
- URL: https://tenacity.readthedocs.io/
- Duration: 25 min
- Focus: Retry strategies, circuit breaker implementation

**What You Need to Understand:**

**Tenacity Features:**
- Retry with exponential backoff
- Circuit breaker pattern
- Timeout handling
- Retry on specific exceptions
- Stop after max attempts
- Wait strategies (fixed, random, exponential)

**Basic Circuit Breaker with Tenacity:**
```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    CircuitBreaker
)
import httpx
import time

# Circuit breaker configuration
circuit_breaker = CircuitBreaker(
    failure_threshold=5,      # Open after 5 failures
    recovery_timeout=60,      # Try to close after 60s
    expected_exception=httpx.HTTPError
)

# Retry with circuit breaker
@retry(
    stop=stop_after_attempt(3),           # Max 3 retries
    wait=wait_exponential(multiplier=1, min=2, max=10),  # 2s, 4s, 8s
    retry=retry_if_exception_type(httpx.HTTPError),
    retry_error_callback=circuit_breaker  # Use circuit breaker
)
async def call_ml_service(transaction):
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.post(
            "https://ml-service/predict",
            json=transaction.dict()
        )
        response.raise_for_status()
        return response.json()
```

**Exponential Backoff Explained:**
```
Attempt 1: Immediate (0s wait)
Attempt 2: Wait 2s (2^1 seconds)
Attempt 3: Wait 4s (2^2 seconds)
Attempt 4: Wait 8s (2^3 seconds)

Why?
- Give failing service time to recover
- Prevent hammering with rapid retries
- Distributed across time (reduce load spike)
```

**Circuit Breaker State Tracking:**
```python
from tenacity import CircuitBreaker

class MLServiceCircuitBreaker:
    def __init__(self):
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=60,
            expected_exception=Exception
        )
        self.fallback_count = 0
        self.total_requests = 0
    
    async def call_with_circuit_breaker(self, func, *args, **kwargs):
        self.total_requests += 1
        
        try:
            # Check circuit state
            if self.circuit_breaker.opened:
                print(f"Circuit OPEN - using fallback")
                self.fallback_count += 1
                return await self.fallback_fraud_detection(*args, **kwargs)
            
            # Circuit CLOSED - try ML service
            result = await func(*args, **kwargs)
            self.circuit_breaker.success()  # Record success
            return result
            
        except Exception as e:
            self.circuit_breaker.failure()  # Record failure
            
            if self.circuit_breaker.opened:
                # Circuit just opened - use fallback
                print(f"Circuit OPENED after failure: {e}")
                self.fallback_count += 1
                return await self.fallback_fraud_detection(*args, **kwargs)
            else:
                # Circuit still closed - propagate error
                raise
    
    async def fallback_fraud_detection(self, transaction):
        # Rule-based fraud detection (implemented Day 2)
        return rule_based_fraud_check(transaction)
    
    def get_stats(self):
        return {
            "total_requests": self.total_requests,
            "fallback_count": self.fallback_count,
            "fallback_rate": self.fallback_count / self.total_requests if self.total_requests > 0 else 0,
            "circuit_state": "OPEN" if self.circuit_breaker.opened else "CLOSED"
        }
```

**Success Criteria:**
- Understand 3 circuit breaker states
- Know when to use circuit breakers
- Understand exponential backoff strategy
- Can configure tenacity library
- Can track circuit breaker state

---

## DAY 2 (TUESDAY): Offline Fallback System

**Time:** 1.5 hours

### SESSION 1: Rule-Based Fraud Detection (45 min)

**Requirements:**

Build deterministic fraud detection (no ML):

**Component 1: Rule Engine**
- Requirements: Pure Python rules (no AI)
- Why: Works when OpenAI API down
- Rules: Amount-based, Location-based, Time-based, Velocity-based, Merchant-based
- What to figure out: Which rules most effective
- Document: Rule definitions

**Rule Categories:**

**1. Amount-Based Rules:**
```python
def check_amount_rules(transaction, customer_profile):
    red_flags = []
    
    # Rule 1: Amount > 10x customer average
    if transaction.amount > customer_profile.avg_amount * 10:
        red_flags.append(f"Amount {transaction.amount} exceeds 10x average {customer_profile.avg_amount}")
    
    # Rule 2: Amount > $5,000 (high-risk threshold)
    if transaction.amount > 5000:
        red_flags.append(f"High amount: ${transaction.amount}")
    
    # Rule 3: Round number (fraud pattern)
    if transaction.amount % 100 == 0 and transaction.amount >= 500:
        red_flags.append(f"Suspicious round amount: ${transaction.amount}")
    
    return red_flags
```

**2. Location-Based Rules:**
```python
def check_location_rules(transaction, customer_profile):
    red_flags = []
    
    # Rule 1: Foreign country (customer normally domestic)
    if transaction.country != customer_profile.home_country:
        red_flags.append(f"Foreign transaction: {transaction.country}")
    
    # Rule 2: High-risk countries (Nigeria, Russia, etc.)
    HIGH_RISK_COUNTRIES = ['NG', 'RU', 'CN', 'PK']
    if transaction.country_code in HIGH_RISK_COUNTRIES:
        red_flags.append(f"High-risk country: {transaction.country}")
    
    # Rule 3: Geographic impossibility (two transactions 1000 miles apart in 1 hour)
    last_location = customer_profile.last_transaction_location
    if calculate_distance(transaction.location, last_location) > 1000:
        time_diff = transaction.timestamp - customer_profile.last_transaction_time
        if time_diff < timedelta(hours=1):
            red_flags.append(f"Geographic impossibility: {transaction.location} from {last_location} in {time_diff}")
    
    return red_flags
```

**3. Time-Based Rules:**
```python
def check_time_rules(transaction, customer_profile):
    red_flags = []
    
    # Rule 1: Transaction between 2 AM - 5 AM (unusual hours)
    hour = transaction.timestamp.hour
    if 2 <= hour <= 5:
        red_flags.append(f"Unusual time: {hour}:00")
    
    # Rule 2: Weekend transaction (customer normally weekdays only)
    if transaction.timestamp.weekday() >= 5:  # Saturday=5, Sunday=6
        if customer_profile.weekend_transactions_rate < 0.1:
            red_flags.append(f"Unusual weekend transaction")
    
    return red_flags
```

**4. Velocity-Based Rules:**
```python
def check_velocity_rules(transaction, customer_profile):
    red_flags = []
    
    # Rule 1: More than 5 transactions in 10 minutes
    recent_transactions = get_transactions_last_n_minutes(customer_profile.id, 10)
    if len(recent_transactions) > 5:
        red_flags.append(f"High velocity: {len(recent_transactions)} transactions in 10 minutes")
    
    # Rule 2: Total spend in 24 hours > 5x daily average
    daily_spend = get_total_spend_last_n_hours(customer_profile.id, 24)
    if daily_spend > customer_profile.avg_daily_spend * 5:
        red_flags.append(f"High daily spend: ${daily_spend} vs avg ${customer_profile.avg_daily_spend}")
    
    return red_flags
```

**5. Merchant-Based Rules:**
```python
def check_merchant_rules(transaction):
    red_flags = []
    
    # Rule 1: Known fraud merchant (blacklist)
    BLACKLISTED_MERCHANTS = load_merchant_blacklist()
    if transaction.merchant_id in BLACKLISTED_MERCHANTS:
        red_flags.append(f"Blacklisted merchant: {transaction.merchant_name}")
    
    # Rule 2: High-risk merchant category (electronics, jewelry)
    HIGH_RISK_CATEGORIES = ['electronics', 'jewelry', 'luxury_goods']
    if transaction.merchant_category in HIGH_RISK_CATEGORIES:
        if transaction.amount > 1000:
            red_flags.append(f"High-risk category: {transaction.merchant_category}")
    
    return red_flags
```

**Component 2: Risk Scoring Algorithm**
- Requirements: Combine all rules into single risk score
- Logic: Each red flag adds points, Different weights per rule
- Scale: 0-100 risk score
- What to figure out: Optimal weights for each rule
- Document: Scoring algorithm

**Risk Score Calculation:**
```python
def calculate_rule_based_risk_score(transaction, customer_profile):
    all_red_flags = []
    
    # Collect red flags from all rule categories
    all_red_flags.extend(check_amount_rules(transaction, customer_profile))
    all_red_flags.extend(check_location_rules(transaction, customer_profile))
    all_red_flags.extend(check_time_rules(transaction, customer_profile))
    all_red_flags.extend(check_velocity_rules(transaction, customer_profile))
    all_red_flags.extend(check_merchant_rules(transaction))
    
    # Weight each red flag type
    WEIGHTS = {
        'Blacklisted merchant': 50,
        'High-risk country': 30,
        'Geographic impossibility': 40,
        'High velocity': 25,
        'Amount exceeds 10x': 20,
        'High amount': 15,
        'Foreign transaction': 10,
        'Unusual time': 5,
        'Unusual weekend': 5,
        'Suspicious round amount': 5
    }
    
    # Calculate score
    risk_score = 0
    for flag in all_red_flags:
        for key, weight in WEIGHTS.items():
            if key in flag:
                risk_score += weight
                break
    
    # Cap at 100
    risk_score = min(risk_score, 100)
    
    return {
        'risk_score': risk_score,
        'is_fraud': risk_score >= 70,  # Threshold
        'red_flags': all_red_flags,
        'decision': 'BLOCK' if risk_score >= 70 else 'APPROVE'
    }
```

### SESSION 2: Integration with Circuit Breaker (45 min)

**Requirements:**

Connect rule-based system to circuit breaker:

**Component 1: Unified Fraud Detection Interface**
- Requirements: Single function that tries ML, falls back to rules
- API: `analyze_fraud(transaction)` → returns same schema regardless of method
- What to figure out: How to track which method was used
- Document: Integration pattern

**Unified Interface:**
```python
from enum import Enum

class DetectionMethod(Enum):
    ML_PRIMARY = "ml_primary"
    RULE_BASED_FALLBACK = "rule_based_fallback"
    MANUAL_REVIEW = "manual_review"

class FraudDetectionService:
    def __init__(self):
        self.circuit_breaker = MLServiceCircuitBreaker()
        self.ml_client = OpenAIClient()
        self.rule_engine = RuleBasedEngine()
        
    async def analyze_fraud(self, transaction, customer_profile):
        try:
            # Try ML service (with circuit breaker)
            if not self.circuit_breaker.circuit_breaker.opened:
                result = await self.ml_client.predict(transaction, customer_profile)
                return {
                    **result,
                    'detection_method': DetectionMethod.ML_PRIMARY,
                    'degraded_mode': False
                }
        except Exception as e:
            logger.warning(f"ML service failed: {e}")
            # Circuit breaker will handle opening
        
        # Fallback to rule-based
        logger.info("Using rule-based fallback")
        result = self.rule_engine.calculate_risk_score(transaction, customer_profile)
        return {
            **result,
            'detection_method': DetectionMethod.RULE_BASED_FALLBACK,
            'degraded_mode': True
        }
```

**Component 2: Degraded Mode Monitoring**
- Requirements: Track when running in degraded mode
- Metrics: Fallback usage rate, Time in degraded mode, Accuracy comparison (ML vs rules)
- Alerts: Alert if degraded mode > 5 minutes
- What to figure out: When to alert operations team
- Document: Degraded mode monitoring

**Component 3: Audit Logging**
- Requirements: Log all degraded-mode decisions
- Fields: transaction_id, detection_method, degraded_mode=true, risk_score, decision, timestamp
- Purpose: Regulatory compliance (prove system worked during ML outage)
- What to figure out: Log retention period (90 days for SOX?)
- Document: Audit trail

**Component 4: Performance Comparison**
- Requirements: Compare ML vs rule-based accuracy
- Test: Run both methods on same transactions when ML available
- Metrics: ML accuracy: 94%, Rule-based accuracy: 78%, Trade-off: 16% accuracy drop but system stays online
- What to figure out: Acceptable accuracy degradation
- Document: Performance comparison

**Success Criteria:**
- Rule-based system implemented (5 categories)
- Risk scoring algorithm working
- Integrated with circuit breaker
- Degraded mode tracked
- Audit logging complete

---

## DAY 3 (WEDNESDAY): Graceful Degradation Strategies

**Time:** 1.5 hours

### SESSION 1: Degradation Patterns (45 min)

**Learning Resources:**

**Reading:**
- "Building Resilient Services" - AWS Architecture Blog
- URL: https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/
- Duration: 25 min
- Focus: Graceful degradation patterns

**What You Need to Understand:**

**Degradation Levels:**

**Level 1: Full Functionality (100% Features)**
- ML fraud detection with GPT-4
- Real-time embeddings
- Citation extraction
- Full RAG pipeline
- Uptime: 99.9% target

**Level 2: Degraded Performance (80% Features)**
- ML fraud detection with GPT-3.5 (faster, cheaper)
- Cached embeddings (use yesterday's vectors)
- No citations (just answers)
- Simplified RAG
- Trigger: High latency (P95 > 5s)

**Level 3: Essential Only (50% Features)**
- Rule-based fraud detection
- Keyword search only (no ML)
- Canned responses for FAQs
- No RAG (static content)
- Trigger: ML service down

**Level 4: Read-Only (20% Features)**
- View past transactions only
- No new fraud analysis
- Display cached data
- Trigger: Database connection issues

**Level 5: Maintenance Mode (0% Features)**
- "System temporarily unavailable"
- Show estimated recovery time
- Trigger: Complete system failure

**Fintech Application:**
```
Banking Use Case - Transaction Processing:

Level 1 (Normal):
- ML fraud detection (94% accuracy)
- Process all transactions
- Real-time risk scoring

Level 2 (Performance Degraded):
- Switch to GPT-3.5 (92% accuracy, 2x faster)
- Still process all transactions
- Slightly lower accuracy acceptable

Level 3 (ML Unavailable):
- Rule-based fraud detection (78% accuracy)
- Process most transactions
- Flag edge cases for manual review
- Better than blocking all transactions

Level 4 (Database Issues):
- In-memory cache for recent transactions
- Block new high-risk transactions
- Allow known-safe transactions (< $50, regular merchant)

Level 5 (Complete Failure):
- "Service temporarily unavailable, please try again in 5 minutes"
- Emergency contact number for urgent transactions
```

### SESSION 2: Implement Degradation Tiers (45 min)

**Requirements:**

Build multi-tier degradation system:

**Component 1: Feature Flags**
- Requirements: Enable/disable features dynamically
- Tool: Simple Python dict or use LaunchDarkly
- Flags: use_ml_fraud_detection, use_embeddings, use_rag, use_citations
- What to figure out: How to toggle flags without redeployment
- Document: Feature flag management

**Component 2: Automatic Tier Detection**
- Requirements: Auto-detect which tier to use
- Checks: ML service health (circuit breaker state), Database latency, API response time
- Logic: If ML down → Tier 3, If latency high → Tier 2, Else → Tier 1
- What to figure out: Health check implementation
- Document: Tier selection logic

**Component 3: Tier-Specific Behavior**
- Requirements: Different code paths per tier
- Implementation: Strategy pattern (different strategies per tier)
- What to figure out: How to switch strategies dynamically
- Document: Strategy pattern implementation

**Example Implementation:**
```python
from enum import Enum

class DegradationTier(Enum):
    FULL = 1
    DEGRADED_PERFORMANCE = 2
    ESSENTIAL_ONLY = 3
    READ_ONLY = 4
    MAINTENANCE = 5

class ResilienceManager:
    def __init__(self):
        self.current_tier = DegradationTier.FULL
        self.circuit_breaker = MLServiceCircuitBreaker()
        
    def detect_tier(self):
        # Check ML service
        if self.circuit_breaker.circuit_breaker.opened:
            return DegradationTier.ESSENTIAL_ONLY
        
        # Check database latency
        db_latency = get_db_latency()
        if db_latency > 5.0:  # 5 seconds
            return DegradationTier.READ_ONLY
        
        # Check API latency
        api_latency = get_api_p95_latency()
        if api_latency > 5.0:
            return DegradationTier.DEGRADED_PERFORMANCE
        
        # All healthy
        return DegradationTier.FULL
    
    async def analyze_fraud(self, transaction, customer_profile):
        tier = self.detect_tier()
        
        if tier == DegradationTier.FULL:
            # Use GPT-4 ML fraud detection
            return await self.ml_fraud_detection_gpt4(transaction)
        
        elif tier == DegradationTier.DEGRADED_PERFORMANCE:
            # Use GPT-3.5 (faster, cheaper)
            return await self.ml_fraud_detection_gpt35(transaction)
        
        elif tier == DegradationTier.ESSENTIAL_ONLY:
            # Use rule-based fallback
            return self.rule_based_fraud_detection(transaction)
        
        elif tier == DegradationTier.READ_ONLY:
            # Use cached risk score if available
            cached = get_cached_risk_score(transaction.id)
            if cached:
                return cached
            else:
                return {'error': 'Unable to analyze new transactions'}
        
        else:  # MAINTENANCE
            return {'error': 'System under maintenance'}
```

**Success Criteria:**
- 5 degradation tiers defined
- Automatic tier detection implemented
- Tier-specific behavior working
- Feature flags integrated

---

## DAY 4 (THURSDAY): Chaos Engineering

**Time:** 1.5 hours

### SESSION 1: Chaos Engineering Principles (45 min)

**Learning Resources:**

**Video:**
- "Chaos Engineering Explained" - Netflix
- URL: https://www.youtube.com/watch?v=IbCH08GiMMw
- Duration: 16:20
- Focus: Chaos engineering principles, Netflix examples

**Reading:**
- "Principles of Chaos Engineering" - Chaos Monkey
- URL: https://principlesofchaos.org/
- Duration: 15 min
- Focus: Chaos engineering methodology

**What You Need to Understand:**

**Chaos Engineering Definition:**
- Intentionally inject failures into production systems
- Discover weaknesses before they cause real outages
- Build confidence in system resilience

**Why Chaos Engineering in Fintech:**
```
Scenario: OpenAI API outage on Black Friday
- Without chaos testing: Entire fraud detection fails, Transactions blocked, $500K revenue lost, Customer complaints flood support
- With chaos testing: Already tested this scenario, Circuit breaker works, Rule-based fallback activated, Transactions continue processing, Minimal customer impact
```

**Chaos Experiments:**

**Experiment 1: Dependency Failure**
- Hypothesis: "If OpenAI API fails, system will use rule-based fallback"
- Method: Block outbound requests to api.openai.com
- Expected: Circuit opens after 5 failures, Rule-based system takes over, Transactions continue processing
- Actual: [Run experiment to find out]

**Experiment 2: Database Latency**
- Hypothesis: "If database queries take > 5s, system will use cached data"
- Method: Add artificial delay to all database queries
- Expected: System detects latency, Switches to read-only tier, Uses cached risk scores
- Actual: [Run experiment to find out]

**Experiment 3: Partial Failure**
- Hypothesis: "If 50% of ECS tasks fail, load balancer routes to healthy tasks"
- Method: Stop 1 of 2 ECS tasks
- Expected: Load balancer detects unhealthy task, Routes 100% traffic to healthy task, Auto-scaling launches replacement task
- Actual: [Run experiment to find out]

**Experiment 4: Network Partition**
- Hypothesis: "If ML service can't reach database, it fails gracefully"
- Method: Block network between ML service and database
- Expected: ML service returns error immediately (not hang), API falls back to rule-based, Audit log records network failure
- Actual: [Run experiment to find out]

**Experiment 5: Cascading Failure**
- Hypothesis: "If circuit breaker disabled, one slow service crashes entire system"
- Method: Disable circuit breaker, Make ML service take 60s per request
- Expected: Without circuit breaker, all threads blocked waiting for ML, System becomes unresponsive, Proves circuit breaker is necessary
- Actual: [Demonstrate value of circuit breaker]

### SESSION 2: Run Chaos Experiments (45 min)

**Requirements:**

Execute chaos experiments in staging environment:

**Component 1: Experiment Framework**
- Requirements: Structure for running experiments
- Tool: Python scripts or AWS Fault Injection Simulator
- What to figure out: How to safely inject failures
- Document: Experiment methodology

**Component 2: OpenAI API Failure Test**
- Requirements: Simulate OpenAI API outage
- Method: Use network proxy to block api.openai.com
- Observe: Circuit breaker opens, Fallback activates, Response time < 200ms (fast failure)
- What to figure out: How long to run test (5 min? 30 min?)
- Document: Experiment results

**Component 3: Database Latency Test**
- Requirements: Inject 10-second delay in database queries
- Method: Modify database connection to add sleep()
- Observe: API response time increases, Degradation tier changes, System still responsive
- What to figure out: What's acceptable max latency?
- Document: Latency tolerance

**Component 4: ECS Task Failure Test**
- Requirements: Kill ECS tasks randomly
- Method: AWS FIS action: Stop random ECS tasks
- Observe: Load balancer routes around failures, Auto-scaling replaces tasks, No user-facing errors
- What to figure out: How fast does auto-scaling react?
- Document: High availability validation

**Component 5: Metrics During Chaos**
- Requirements: Monitor metrics during experiments
- Metrics: Error rate, Latency (P95, P99), Circuit breaker state, Fallback usage rate
- What to figure out: What's "normal" during failure?
- Document: Chaos metrics baseline

**Experiment Execution Script:**
```python
import asyncio
import time
from typing import Dict

class ChaosExperiment:
    def __init__(self, name: str):
        self.name = name
        self.results = []
    
    async def inject_fault(self):
        """Override in subclass"""
        pass
    
    async def remove_fault(self):
        """Override in subclass"""
        pass
    
    async def run_experiment(self, duration_seconds: int):
        print(f"Starting experiment: {self.name}")
        
        # Baseline metrics
        baseline = await self.collect_metrics()
        print(f"Baseline: {baseline}")
        
        # Inject fault
        await self.inject_fault()
        print(f"Fault injected")
        
        # Monitor during fault
        start = time.time()
        while time.time() - start < duration_seconds:
            metrics = await self.collect_metrics()
            self.results.append(metrics)
            await asyncio.sleep(10)  # Every 10 seconds
        
        # Remove fault
        await self.remove_fault()
        print(f"Fault removed")
        
        # Recovery metrics
        recovery = await self.collect_metrics()
        print(f"Recovery: {recovery}")
        
        # Analyze results
        self.analyze_results()
    
    async def collect_metrics(self) -> Dict:
        return {
            'timestamp': time.time(),
            'error_rate': get_error_rate(),
            'latency_p95': get_latency_p95(),
            'circuit_state': get_circuit_state(),
            'fallback_usage': get_fallback_usage()
        }
    
    def analyze_results(self):
        print(f"\n--- {self.name} Results ---")
        print(f"Total samples: {len(self.results)}")
        
        # Calculate averages
        avg_error_rate = sum(r['error_rate'] for r in self.results) / len(self.results)
        avg_latency = sum(r['latency_p95'] for r in self.results) / len(self.results)
        avg_fallback = sum(r['fallback_usage'] for r in self.results) / len(self.results)
        
        print(f"Avg error rate during fault: {avg_error_rate:.2%}")
        print(f"Avg P95 latency during fault: {avg_latency:.2f}s")
        print(f"Avg fallback usage: {avg_fallback:.2%}")
        
        # Determine if experiment passed
        passed = (
            avg_error_rate < 0.05 and  # < 5% errors
            avg_latency < 5.0 and       # < 5s latency
            avg_fallback > 0.80         # > 80% fallback usage
        )
        
        print(f"Experiment PASSED: {passed}")

class OpenAIFailureExperiment(ChaosExperiment):
    async def inject_fault(self):
        # Block OpenAI API
        os.system("iptables -A OUTPUT -d api.openai.com -j DROP")
    
    async def remove_fault(self):
        # Unblock OpenAI API
        os.system("iptables -D OUTPUT -d api.openai.com -j DROP")

# Run experiment
experiment = OpenAIFailureExperiment("OpenAI API Failure")
await experiment.run_experiment(duration_seconds=300)  # 5 minutes
```

**Success Criteria:**
- All 5 chaos experiments defined
- At least 2 experiments executed
- Results documented
- Weaknesses identified
- Improvements planned

---

## DAY 5 (FRIDAY): SLA Monitoring

**Time:** 1 hour

### SESSION 1: Define SLAs (30 min)

**Requirements:**

Define Service Level Agreements:

**SLA 1: Availability**
- Metric: Uptime percentage
- Target: 99.9% (8.76 hours downtime/year)
- Measurement: Successful health checks / total health checks
- What to figure out: What counts as "down"? (health check fails)
- Document: Availability SLA

**SLA 2: Latency**
- Metric: P95 response time
- Target: < 2 seconds (95th percentile)
- Measurement: CloudWatch metrics from API Gateway/ALB
- What to figure out: Include circuit breaker fast-failures?
- Document: Latency SLA

**SLA 3: Error Rate**
- Metric: Failed requests / total requests
- Target: < 1% errors
- Measurement: HTTP 5xx responses / all responses
- What to figure out: Are 4xx errors included? (No, client errors)
- Document: Error rate SLA

**SLA 4: Data Freshness**
- Metric: Time since last successful ML prediction
- Target: < 5 minutes
- Measurement: Timestamp of last successful ML call
- What to figure out: Alert if running rule-based for > 5 min
- Document: Degraded mode SLA

### SESSION 2: SLA Dashboard (30 min)

**Requirements:**

Create SLA monitoring dashboard:

**Component 1: CloudWatch Dashboard**
- Requirements: Real-time SLA metrics
- Widgets: Availability gauge (99.9% target line), Latency graph (P50, P95, P99), Error rate graph (1% target line), Degraded mode indicator (red when degraded)
- What to figure out: Refresh frequency (1 minute real-time)
- Document: Dashboard configuration

**Component 2: SLA Compliance Tracking**
- Requirements: Calculate SLA compliance over time periods
- Periods: Last 24 hours, Last 7 days, Last 30 days, Month-to-date
- Formula: (Successful minutes / Total minutes) × 100
- What to figure out: How to handle maintenance windows
- Document: Compliance calculation

**Component 3: SLA Breach Alerts**
- Requirements: Alert when SLA violated
- Trigger: Availability < 99.9% for 1 hour, Latency > 2s (P95) for 5 minutes, Error rate > 1% for 5 minutes, Degraded mode > 10 minutes
- Action: SNS → PagerDuty → On-call engineer
- What to figure out: Who gets paged? (on-call rotation)
- Document: Alert configuration

**Component 4: SLA Report**
- Requirements: Monthly SLA compliance report
- Contents: Availability: 99.92% (target: 99.9%) ✓, Latency P95: 1.8s (target: <2s) ✓, Error rate: 0.7% (target: <1%) ✓, Incidents: 2 (downtime: 45 min total)
- Audience: Engineering management, Customers (if external SLA)
- What to figure out: Report format (PDF? Dashboard?)
- Document: Report template

**Success Criteria:**
- SLAs defined clearly (4 metrics)
- CloudWatch dashboard created
- Compliance tracking implemented
- SLA breach alerts configured
- Monthly report template ready

---

## DAY 6 (SATURDAY): Testing & Validation

**Time:** 2.5 hours

### SESSION 1: Resilience Test Suite (90 min)

**Requirements:**

Build comprehensive resilience test suite:

**Test Category 1: Circuit Breaker Tests**
- Test 1.1: Circuit opens after threshold failures
- Test 1.2: Circuit stays open for timeout period
- Test 1.3: Circuit half-opens and tests recovery
- Test 1.4: Circuit closes on successful recovery
- Test 1.5: Fallback used when circuit open
- What to figure out: How to simulate failures in tests
- Document: Circuit breaker test cases

**Test Category 2: Fallback Tests**
- Test 2.1: Rule-based system returns valid fraud score
- Test 2.2: Rule-based accuracy >= 75% (benchmark)
- Test 2.3: Fallback completes in < 100ms
- Test 2.4: Audit log records degraded-mode usage
- What to figure out: How to measure rule-based accuracy
- Document: Fallback validation

**Test Category 3: Degradation Tests**
- Test 3.1: System detects tier automatically
- Test 3.2: Tier 2 uses GPT-3.5 (not GPT-4)
- Test 3.3: Tier 3 uses rules (not ML)
- Test 3.4: Tier transitions smoothly (no errors)
- What to figure out: How to mock health checks
- Document: Degradation testing

**Test Category 4: Recovery Tests**
- Test 4.1: System recovers when ML service restored
- Test 4.2: Circuit closes after successful test
- Test 4.3: Returns to Tier 1 (full functionality)
- Test 4.4: No manual intervention required
- What to figure out: How to simulate recovery
- Document: Recovery validation

**Test Category 5: Chaos Tests (Automated)**
- Test 5.1: OpenAI API failure → rule-based fallback
- Test 5.2: Database latency → cached data
- Test 5.3: ECS task failure → load balancer reroutes
- Test 5.4: Network partition → graceful error
- What to figure out: How to run chaos tests in CI/CD
- Document: Automated chaos testing

**Example Test:**
```python
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_circuit_breaker_opens_after_threshold_failures():
    # Setup
    fraud_service = FraudDetectionService()
    transaction = create_test_transaction()
    
    # Simulate 5 ML service failures
    with patch('ml_client.predict', side_effect=Exception("OpenAI API error")):
        for i in range(5):
            result = await fraud_service.analyze_fraud(transaction, customer_profile)
    
    # Assert circuit opened
    assert fraud_service.circuit_breaker.circuit_breaker.opened == True
    
    # Assert fallback was used
    assert result['detection_method'] == DetectionMethod.RULE_BASED_FALLBACK
    
    # Assert degraded mode flagged
    assert result['degraded_mode'] == True

@pytest.mark.asyncio
async def test_rule_based_fallback_accuracy():
    # Setup
    rule_engine = RuleBasedEngine()
    test_cases = load_test_cases_with_ground_truth()  # 100 transactions
    
    # Run rule-based on all test cases
    correct = 0
    for transaction, expected_fraud in test_cases:
        result = rule_engine.calculate_risk_score(transaction, customer_profile)
        if result['is_fraud'] == expected_fraud:
            correct += 1
    
    # Assert accuracy >= 75%
    accuracy = correct / len(test_cases)
    assert accuracy >= 0.75, f"Rule-based accuracy {accuracy:.2%} below 75% threshold"
```

### SESSION 2: Load Testing During Failures (60 min)

**Requirements:**

Test system performance under failure conditions:

**Load Test 1: Normal Load Baseline**
- Requirements: Establish baseline metrics
- Tool: Locust or k6
- Load: 100 requests/second for 5 minutes
- Measure: Latency (P50, P95, P99), Error rate, Throughput
- What to figure out: Normal system capacity
- Document: Baseline performance

**Load Test 2: Load During ML Outage**
- Requirements: Test with circuit breaker open
- Setup: Block OpenAI API, Generate same load (100 req/s)
- Measure: Latency (should be faster due to rule-based), Error rate (should be low), Fallback usage (should be 100%)
- What to figure out: Can system handle load in degraded mode?
- Document: Degraded mode performance

**Load Test 3: Load During Recovery**
- Requirements: Test circuit half-open behavior
- Setup: Restore OpenAI API during load test
- Observe: Circuit tests recovery, Some requests use ML, some use rules, Gradual return to normal
- What to figure out: How long to recover fully?
- Document: Recovery performance

**Load Test 4: Stress Test (Find Breaking Point)**
- Requirements: Increase load until system fails
- Load: Start 100 req/s, increase 50 req/s every minute
- Observe: At what load does error rate exceed 1%?, What fails first (database, ML, API)?, How does circuit breaker help?
- What to figure out: System capacity limits
- Document: Capacity planning

**Success Criteria:**
- All 20+ tests written and passing
- Load testing completed (4 scenarios)
- Performance validated in degraded mode
- System capacity limits identified
- Test automation configured

---

## DAY 7 (SUNDAY): Week Summary & Documentation

**Time:** 2 hours

### SESSION 1: Runbook Creation (60 min)

**Requirements:**

Create operational runbooks:

**Runbook 1: ML Service Outage**
- Scenario: OpenAI API is down
- Detection: Circuit breaker opens, CloudWatch alarm "ML Service Unavailable"
- Impact: System running in degraded mode (rule-based)
- Response: 1. Verify OpenAI status page, 2. Check circuit breaker state, 3. Verify fallback working, 4. Alert engineering if > 30 minutes, 5. Monitor SLA compliance
- Recovery: Circuit auto-recovers when OpenAI restored
- Document: ML outage runbook

**Runbook 2: High Latency**
- Scenario: P95 latency > 5 seconds
- Detection: CloudWatch alarm "High Latency"
- Impact: Poor customer experience
- Response: 1. Check degradation tier (should auto-switch to Tier 2), 2. Investigate slow dependency (database? ML? embeddings?), 3. Check auto-scaling (scale out more tasks), 4. Consider circuit breaker threshold adjustment
- Recovery: Latency returns to normal as system scales or switches tiers
- Document: Latency runbook

**Runbook 3: SLA Breach**
- Scenario: Availability drops below 99.9%
- Detection: CloudWatch alarm "SLA Breach"
- Impact: Not meeting uptime commitment
- Response: 1. Identify cause of downtime, 2. Implement fix or mitigation, 3. Document incident in log, 4. Calculate downtime impact on monthly SLA, 5. Notify stakeholders if customer-facing SLA
- Recovery: Restore service, document lesson learned
- Document: SLA breach runbook

**Runbook 4: Complete System Failure**
- Scenario: All ECS tasks failing, can't auto-recover
- Detection: PagerDuty alert "Critical System Failure"
- Impact: Service completely unavailable
- Response: 1. Check AWS Health Dashboard (regional outage?), 2. Review recent deployments (rollback?), 3. Check CloudWatch Logs for errors, 4. Manually scale to 0 and back to 2 tasks (force restart), 5. If continues, activate disaster recovery (cross-region)
- Recovery: System restarts, verify health checks pass
- Document: Disaster recovery runbook

### SESSION 2: Week Summary (60 min)

**Requirements:**

Create WEEK24_SUMMARY.md:

**Section 1: What You Built**
- Circuit breaker with tenacity library
- Rule-based fraud detection fallback (5 categories)
- 5-tier graceful degradation system
- Chaos engineering experiments (5 scenarios)
- SLA monitoring dashboard
- Resilience test suite (20+ tests)
- Operational runbooks (4 scenarios)
- Document: Complete build inventory

**Section 2: Fintech Impact - CRITICAL**
- Banking SLA Requirements: 99.9% uptime mandatory
- Regulatory Compliance: Offline fallback required (SOX, Basel III)
- Revenue Protection: Keep processing transactions during ML outages
- Customer Experience: Graceful degradation, not hard failures
- Audit Trail: Log all degraded-mode decisions for compliance
- Document: Regulatory value

**Section 3: Resilience Achievements**
- Circuit Breaker: Opens after 5 failures, prevents cascade
- Fallback System: Rule-based 78% accuracy (vs 94% ML)
- Graceful Degradation: 5 tiers from full to maintenance
- Chaos Tested: All 5 failure scenarios validated
- SLA Monitoring: 99.9% availability tracked
- Fast Failure: <100ms response in degraded mode (not 30s timeout)
- Document: Resilience metrics

**Section 4: Chaos Engineering Insights**
- Experiment 1: OpenAI API outage → circuit breaker works ✓
- Experiment 2: Database latency → tier switches automatically ✓
- Experiment 3: ECS task failure → load balancer routes around ✓
- Experiment 4: Network partition → graceful error handling ✓
- Experiment 5: Without circuit breaker → entire system hangs ✗
- Document: Chaos learnings

**Section 5: Interview Talking Points**
- Story 1: "Implemented circuit breaker pattern, preventing cascading failures during OpenAI API outages"
- Story 2: "Built rule-based fallback system achieving 78% fraud detection accuracy when ML unavailable, ensuring 99.9% uptime SLA"
- Story 3: "Designed 5-tier graceful degradation strategy, enabling system to continue operating during partial failures"
- Story 4: "Conducted chaos engineering experiments, validating system resilience under 5 failure scenarios"
- Document: STAR format stories

**Section 6: Production Readiness**
- Resilience: Survives dependency failures without cascading
- Monitoring: SLA compliance tracked and reported
- Testing: 20+ automated resilience tests
- Documentation: Runbooks for 4 incident scenarios
- Compliance: Audit trail for degraded-mode decisions
- Document: Production checklist

**Success Criteria:**
- 4 runbooks complete
- Week summary comprehensive
- Fintech impact articulated
- Interview stories ready
- Production readiness documented

---

## 📚 ADDITIONAL RESOURCES

**Circuit Breakers:**
- Martin Fowler on Circuit Breaker: https://martinfowler.com/bliki/CircuitBreaker.html
- Tenacity Documentation: https://tenacity.readthedocs.io/
- Hystrix (Netflix): https://github.com/Netflix/Hystrix/wiki

**Resilience Engineering:**
- AWS Builders Library: https://aws.amazon.com/builders-library/
- Google SRE Book: https://sre.google/books/
- Release It! (book) by Michael Nygard

**Chaos Engineering:**
- Chaos Monkey: https://netflix.github.io/chaosmonkey/
- Principles of Chaos: https://principlesofchaos.org/
- AWS Fault Injection Simulator: https://aws.amazon.com/fis/

**SLA/SLO:**
- Google SRE - SLIs, SLOs, SLAs: https://sre.google/sre-book/service-level-objectives/
- Implementing SLOs: https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-slis-slas-and-slos

---

## ✅ WEEK 24 DELIVERABLES

**Documentation:**
- CIRCUIT_BREAKER_GUIDE.md - Circuit breaker implementation
- FALLBACK_SYSTEM.md - Rule-based fraud detection
- GRACEFUL_DEGRADATION.md - 5-tier degradation strategy
- CHAOS_EXPERIMENTS.md - Chaos engineering results
- SLA_MONITORING.md - SLA definition and tracking
- RUNBOOKS.md - Operational runbooks (4 scenarios)
- WEEK24_SUMMARY.md - Week summary

**Implementation Files (Requirements):**
- circuit_breaker.py - Tenacity-based circuit breaker (requirements documented)
- rule_based_fraud.py - Fallback fraud detection (requirements documented)
- degradation_manager.py - Tier detection and switching (requirements documented)
- chaos_experiments.py - Automated chaos tests (requirements documented)
- sla_monitoring.py - SLA calculation and reporting (requirements documented)

**Test Suites:**
- test_circuit_breaker.py - Circuit breaker tests (5 tests)
- test_fallback.py - Fallback accuracy tests (4 tests)
- test_degradation.py - Tier switching tests (4 tests)
- test_chaos.py - Automated chaos tests (5 tests)
- test_recovery.py - Recovery tests (4 tests)

**Dashboards:**
- CloudWatch SLA dashboard (4 widgets)
- Degraded mode monitoring
- Circuit breaker state visualization

**Understanding:**
- Circuit breaker pattern and implementation
- Graceful degradation strategies
- Chaos engineering methodology
- SLA definition and monitoring
- Rule-based fallback systems
- Resilience testing approaches

---

## 🎯 SUCCESS CRITERIA

**By end of Week 24:**

**Conceptual:**
- Understand circuit breaker pattern deeply
- Know when/why to use graceful degradation
- Understand chaos engineering value
- Can define meaningful SLAs
- Know resilience vs availability

**Practical:**
- Implement circuit breakers with tenacity
- Build rule-based fallback systems
- Design multi-tier degradation
- Run chaos engineering experiments
- Monitor and report SLA compliance
- Write operational runbooks
- Test resilience automatically

**Portfolio Impact:**
- ✅ Production resilience expertise (FINTECH CRITICAL)
- ✅ 99.9% uptime capability demonstrated
- ✅ Chaos engineering experience
- ✅ SLA management competency
- ✅ Regulatory compliance (offline fallback)
- ✅ Operational readiness (runbooks)
- ✅ Enterprise-grade reliability

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - 99.9% uptime SLA + regulatory compliance  
**Next Week:** Production Monitoring Stack (Week 25)