# WEEK 25 LEARNING GUIDE: Production Monitoring Stack

**Timeline:** May 4-10, 2026  
**Total Time:** ~11-12 hours  
**Focus:** LangSmith tracing, Prometheus metrics, Grafana dashboards, CloudWatch integration, alerts, cost tracking

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- LangSmith integration for LLM tracing
- Prometheus metrics collection
- Grafana dashboards (5 dashboards)
- CloudWatch integration for AWS services
- Alert rules and notifications
- Cost tracking per query
- Performance monitoring system

**What You'll Learn:**
- LLM observability with LangSmith
- Metrics collection with Prometheus
- Dashboard creation with Grafana
- CloudWatch Logs and Metrics
- Alert configuration (PagerDuty/Slack)
- Cost attribution and tracking
- Performance optimization via monitoring

**Fintech Application - CRITICAL:**

**The Business Problem:**
```
Production ML System Opacity:
- ML models are black boxes
- Can't debug why fraud detection failed
- Don't know which LLM calls are expensive
- Can't prove compliance to auditors
- No visibility into model performance degradation

Real-World Scenario:
CFO: "Why did our OpenAI bill jump from $5K to $15K this month?"
You: "Uh... not sure. Let me check the code?"
CFO: "That's not acceptable. I need cost per query, per customer, per use case."

Compliance Officer: "Prove to me that the fraud detection system flagged this high-risk transaction."
You: "Well, I don't have the logs from 3 months ago..."
Compliance: "That's a regulatory violation. We need 90-day audit trail."

Engineering Manager: "P95 latency went from 2s to 8s. What changed?"
You: "Could be the embeddings? Or the LLM? Or the database? Not sure..."
Manager: "We need to know exactly where the latency is. Debug this."
```

**The Solution - Comprehensive Monitoring:**
```
Observability Stack:
┌─────────────────────────────────────────────────┐
│  LangSmith (LLM Tracing)                        │
│  - Every LLM call logged                        │
│  - Input/output captured                        │
│  - Cost per query tracked                       │
│  - Latency by model                             │
└─────────────────────────────────────────────────┘
           │
           v
┌─────────────────────────────────────────────────┐
│  Prometheus (Metrics)                           │
│  - Request count, latency, errors               │
│  - Custom business metrics                      │
│  - Resource utilization                         │
└─────────────────────────────────────────────────┘
           │
           v
┌─────────────────────────────────────────────────┐
│  Grafana (Visualization)                        │
│  - Real-time dashboards                         │
│  - Alerts and notifications                     │
│  - Historical trend analysis                    │
└─────────────────────────────────────────────────┘
           │
           v
┌─────────────────────────────────────────────────┐
│  CloudWatch (AWS Integration)                   │
│  - ECS container metrics                        │
│  - RDS database metrics                         │
│  - Cost Explorer integration                    │
└─────────────────────────────────────────────────┘

Capabilities Achieved:
✓ CFO Question: "Cost per query" → LangSmith shows $0.03/fraud-check
✓ Compliance: "90-day audit trail" → All LLM calls logged to S3
✓ Engineering: "Where's the latency?" → Grafana shows embeddings = 6s
✓ SLA Monitoring: "Are we meeting 99.9%?" → Prometheus calculates uptime
✓ Cost Optimization: "What's most expensive?" → LangSmith: GPT-4 fraud checks
```

**Why This Matters:**
- **Cost Control:** Prevent runaway OpenAI bills (critical at scale)
- **Compliance:** 90-day audit trail for SOX/Basel III
- **Performance:** Debug latency issues (can't fix what you can't measure)
- **SLA Monitoring:** Track uptime and prove compliance
- **Optimization:** Identify expensive operations (optimize intelligently)
- **Troubleshooting:** Root cause analysis when issues occur

**Week 25 Achieves:**
1. LangSmith traces every LLM call (cost + performance)
2. Prometheus collects all metrics (business + technical)
3. Grafana visualizes everything (real-time dashboards)
4. CloudWatch integrates AWS services (infrastructure)
5. Alerts notify on-call (proactive issue detection)

---

## DAY 1 (MONDAY): LangSmith Setup & Tracing

**Time:** 1.5 hours

### SESSION 1: LangSmith Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "LangSmith Overview" - LangChain
- URL: https://www.youtube.com/watch?v=ypBzkbvQvro
- Duration: 12:30
- Focus: LangSmith features, tracing, monitoring

**Reading:**
- "LangSmith Documentation" - LangChain
- URL: https://docs.smith.langchain.com/
- Duration: 25 min
- Focus: Setup, tracing, projects, datasets

**What You Need to Understand:**

**What is LangSmith?**
- Observability platform for LLM applications
- Traces every LLM call (input, output, latency, cost)
- Debugging tool (see exactly what LLM received/returned)
- Dataset management (collect production data for evaluation)
- Cost tracking (aggregate costs by project/user/endpoint)

**Key Features:**

**1. Tracing:**
```
Single Fraud Detection Request:
┌─────────────────────────────────────────┐
│  Trace: fraud_detection_123             │
│  Duration: 2.3s                         │
│  Cost: $0.04                            │
├─────────────────────────────────────────┤
│  Span 1: Retrieve customer history     │
│    Input: customer_id: 12345            │
│    Output: 120 transactions             │
│    Duration: 0.3s                       │
├─────────────────────────────────────────┤
│  Span 2: Embed transaction description  │
│    Input: "ELECTRONICS STORE $5000"     │
│    Model: text-embedding-3-small        │
│    Output: [0.023, -0.45, ...]          │
│    Duration: 0.2s | Cost: $0.0001      │
├─────────────────────────────────────────┤
│  Span 3: Vector search (similar fraud) │
│    Input: embedding vector              │
│    Output: 5 similar past frauds        │
│    Duration: 0.1s                       │
├─────────────────────────────────────────┤
│  Span 4: GPT-4 fraud analysis          │
│    Input: Transaction + history + similar│
│    Prompt tokens: 1,200                 │
│    Completion tokens: 300               │
│    Model: gpt-4-turbo                   │
│    Output: {"fraud": true, "score": 92} │
│    Duration: 1.5s | Cost: $0.039        │
└─────────────────────────────────────────┘
Total Cost: $0.0001 + $0.039 = $0.0391
```

**2. Projects:**
- Organize traces by environment (dev, staging, prod)
- Separate by use case (fraud-detection, rag-qa, embeddings)
- Your projects: fraud-detection-prod, fraud-detection-staging

**3. Datasets:**
- Collect real production examples
- Build test sets from production traffic
- Version control for datasets
- Use for evaluation (Week 20 agent evaluation)

**4. Cost Tracking:**
- Automatic cost calculation per trace
- Aggregate by time period
- Group by user, endpoint, or model
- Export to CSV for finance team

**Why LangSmith for Fintech:**
```
Use Case 1: Cost Attribution
Question: "Which customers cost us the most in ML?"
LangSmith: 
- Customer A: 1000 fraud checks/day × $0.04 = $40/day = $1,200/month
- Customer B: 100 fraud checks/day × $0.04 = $4/day = $120/month
Action: Charge customer A more, or optimize their queries

Use Case 2: Compliance Audit Trail
Question: "Prove you flagged this transaction as fraud on March 15"
LangSmith:
- Trace ID: fraud_detection_456789
- Timestamp: 2026-03-15 14:32:11 UTC
- Input: Transaction amount $50,000, Nigeria
- Output: {"fraud": true, "confidence": 95%, "flags": ["high amount", "high-risk country"]}
- Model: gpt-4-turbo, Cost: $0.04
Action: Show auditor complete trace = compliance ✓

Use Case 3: Performance Debugging
Question: "Why is P95 latency 8 seconds instead of 2 seconds?"
LangSmith:
- Span analysis shows: Embeddings = 6s (problem!), GPT-4 = 1.5s (normal), Database = 0.3s (normal)
Action: Switch to faster embedding model or cache embeddings
```

### SESSION 2: LangSmith Integration (45 min)

**Requirements:**

Integrate LangSmith into fraud detection system:

**Component 1: LangSmith Setup**
- Requirements: Create account, get API key, create projects
- Projects: fraud-detection-prod, fraud-detection-staging, fraud-detection-dev
- What to figure out: Project naming conventions
- Document: LangSmith configuration

**Component 2: Instrument LLM Calls**
- Requirements: Wrap all OpenAI calls with LangSmith tracing
- Method: Use LangSmith decorators or context managers
- Capture: Input prompt, Output response, Model used, Token counts, Latency, Cost
- What to figure out: How to add custom metadata (customer_id, transaction_id)
- Document: Instrumentation patterns

**Example Integration:**
```python
from langsmith import Client, traceable
from openai import AsyncOpenAI
import os

# Initialize clients
langsmith_client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
openai_client = AsyncOpenAI()

@traceable(
    name="fraud_detection",
    project="fraud-detection-prod",
    metadata_fn=lambda inputs: {
        "customer_id": inputs.get("customer_id"),
        "transaction_id": inputs.get("transaction_id"),
        "amount": inputs.get("amount")
    }
)
async def analyze_fraud_with_gpt4(transaction, customer_profile):
    # Build prompt
    prompt = f"""
    Analyze this transaction for fraud:
    Amount: ${transaction.amount}
    Merchant: {transaction.merchant}
    Location: {transaction.location}
    Customer avg: ${customer_profile.avg_amount}
    
    Provide fraud assessment.
    """
    
    # Call GPT-4 (automatically traced by LangSmith)
    response = await openai_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a fraud detection expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    
    # LangSmith automatically captures:
    # - Input: prompt
    # - Output: response
    # - Model: gpt-4-turbo
    # - Tokens: prompt_tokens + completion_tokens
    # - Cost: calculated from tokens and model pricing
    # - Latency: time from request to response
    
    return response.choices[0].message.content

# Usage
result = await analyze_fraud_with_gpt4(
    transaction=transaction,
    customer_profile=customer_profile
)
```

**Component 3: Custom Spans**
- Requirements: Add spans for non-LLM operations
- Examples: Database queries, Vector searches, Rule-based logic
- Purpose: See complete request flow, not just LLM calls
- What to figure out: Appropriate span granularity
- Document: Span hierarchy

**Example Custom Spans:**
```python
from langsmith import trace

@trace(name="retrieve_customer_history")
async def get_customer_transactions(customer_id):
    async with db.session() as session:
        result = await session.execute(
            select(Transaction)
            .where(Transaction.customer_id == customer_id)
            .order_by(Transaction.timestamp.desc())
            .limit(100)
        )
        return result.scalars().all()

@trace(name="vector_similarity_search")
async def find_similar_fraud(embedding):
    results = await opensearch_client.search(
        index="fraud-patterns",
        body={
            "query": {
                "knn": {
                    "embedding": {
                        "vector": embedding,
                        "k": 5
                    }
                }
            }
        }
    )
    return results['hits']['hits']

@traceable(name="complete_fraud_analysis", project="fraud-detection-prod")
async def complete_fraud_analysis(transaction_id):
    # This creates a parent trace
    transaction = await get_transaction(transaction_id)  # Span 1
    customer = await get_customer(transaction.customer_id)  # Span 2
    history = await get_customer_transactions(customer.id)  # Span 3 (traced)
    
    # Embed transaction
    embedding = await embed_transaction(transaction)  # Span 4
    
    # Find similar fraud
    similar = await find_similar_fraud(embedding)  # Span 5 (traced)
    
    # GPT-4 analysis
    analysis = await analyze_fraud_with_gpt4(transaction, customer)  # Span 6 (traced)
    
    return analysis
```

**Component 4: Cost Tracking**
- Requirements: Enable cost tracking in LangSmith
- Configuration: Provide OpenAI pricing, Set project budget ($1000/month)
- Alerts: Alert if daily cost > $50, Alert if project exceeds budget
- What to figure out: Who gets cost alerts (engineering + finance)
- Document: Cost monitoring setup

**Component 5: Datasets from Production**
- Requirements: Collect production traces for testing
- Method: Export traces to dataset (100 real fraud examples)
- Purpose: Build golden dataset for evaluation (Week 20)
- What to figure out: How often to refresh dataset
- Document: Dataset management

**Success Criteria:**
- LangSmith account created
- All LLM calls instrumented
- Custom spans added for key operations
- Cost tracking enabled
- Can view traces in LangSmith dashboard
- Production dataset collecting

---

## DAY 2 (TUESDAY): Prometheus Metrics

**Time:** 1.5 hours

### SESSION 1: Prometheus Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "Prometheus Monitoring Explained" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=h4Sl21AKiDg
- Duration: 16:52
- Focus: Prometheus architecture, metrics types

**Reading:**
- "Prometheus Documentation - Introduction"
- URL: https://prometheus.io/docs/introduction/overview/
- Duration: 20 min
- Focus: Metrics types, PromQL basics

**What You Need to Understand:**

**Prometheus Architecture:**
```
┌──────────────────────────────────────┐
│  Your Application (FastAPI)         │
│  - Exposes /metrics endpoint         │
│  - Returns metrics in Prometheus fmt│
└───────────┬──────────────────────────┘
            │
            v (scrapes every 15s)
┌──────────────────────────────────────┐
│  Prometheus Server                   │
│  - Pulls metrics from targets        │
│  - Stores time-series data           │
│  - Evaluates alert rules             │
└───────────┬──────────────────────────┘
            │
            v
┌──────────────────────────────────────┐
│  Grafana                             │
│  - Queries Prometheus                │
│  - Visualizes metrics                │
└──────────────────────────────────────┘
```

**Metric Types:**

**1. Counter (always increases):**
- Use for: Total requests, Total errors, Total fraud detected
- Example: `fraud_detections_total = 1,245`
- Operations: Can only increment
- Query: Rate of change: `rate(fraud_detections_total[5m])`

**2. Gauge (can go up or down):**
- Use for: Current values (CPU, memory, queue length)
- Example: `active_requests = 37`
- Operations: Inc, dec, set
- Query: Current value: `active_requests`

**3. Histogram (distribution of values):**
- Use for: Latency, Request size
- Example: `api_latency_seconds` buckets: [0.1, 0.5, 1, 2, 5]
- Operations: Observe value
- Query: P95 latency: `histogram_quantile(0.95, api_latency_seconds_bucket)`

**4. Summary (similar to histogram):**
- Use for: Latency percentiles (pre-calculated)
- Example: `api_latency_summary{quantile="0.95"} = 1.8s`
- Operations: Observe value
- Query: Direct percentile: `api_latency_summary{quantile="0.95"}`

**For Your Application:**
- Counters: fraud_detections_total, requests_total, errors_total
- Gauges: active_requests, circuit_breaker_state, degraded_mode
- Histograms: request_duration_seconds, ml_latency_seconds

### SESSION 2: Instrument Application (45 min)

**Requirements:**

Add Prometheus metrics to FastAPI application:

**Component 1: Prometheus Client Library**
- Requirements: Install and configure prometheus_client
- Endpoint: /metrics (Prometheus scrapes this)
- Format: Prometheus exposition format
- What to figure out: How to expose metrics from FastAPI
- Document: Prometheus setup

**Example Setup:**
```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Response
import time

app = FastAPI()

# Define metrics
fraud_detections_total = Counter(
    'fraud_detections_total',
    'Total number of fraud detections',
    ['status']  # Labels: detected, not_detected
)

request_duration_seconds = Histogram(
    'request_duration_seconds',
    'Request duration in seconds',
    ['endpoint', 'method']
)

active_requests = Gauge(
    'active_requests',
    'Number of requests currently being processed'
)

ml_latency_seconds = Histogram(
    'ml_latency_seconds',
    'ML service latency in seconds',
    ['model']
)

circuit_breaker_state = Gauge(
    'circuit_breaker_state',
    'Circuit breaker state (0=closed, 1=open)',
    ['service']
)

@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
```

**Component 2: Request Instrumentation**
- Requirements: Track all API requests
- Metrics: requests_total (counter), request_duration_seconds (histogram), errors_total (counter)
- Labels: endpoint, method, status_code
- What to figure out: How to use FastAPI middleware
- Document: Request metrics

**Example Middleware:**
```python
from starlette.middleware.base import BaseHTTPMiddleware
import time

class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Increment active requests
        active_requests.inc()
        
        # Track start time
        start_time = time.time()
        
        try:
            # Process request
            response = await call_next(request)
            
            # Record metrics
            duration = time.time() - start_time
            request_duration_seconds.labels(
                endpoint=request.url.path,
                method=request.method
            ).observe(duration)
            
            # Increment request counter
            requests_total.labels(
                endpoint=request.url.path,
                method=request.method,
                status_code=response.status_code
            ).inc()
            
            return response
            
        except Exception as e:
            # Record error
            errors_total.labels(
                endpoint=request.url.path,
                exception=type(e).__name__
            ).inc()
            raise
            
        finally:
            # Decrement active requests
            active_requests.dec()

# Add middleware
app.add_middleware(PrometheusMiddleware)
```

**Component 3: Business Metrics**
- Requirements: Track fraud detection specific metrics
- Metrics: fraud_detections_total, risk_score_distribution, ml_service_failures_total, fallback_usage_total
- What to figure out: When to increment each metric
- Document: Business metrics

**Example Business Metrics:**
```python
risk_score_distribution = Histogram(
    'risk_score_distribution',
    'Distribution of risk scores',
    buckets=[0, 20, 40, 60, 80, 100]
)

ml_service_failures_total = Counter(
    'ml_service_failures_total',
    'Total ML service failures',
    ['reason']  # timeout, error, rate_limit
)

fallback_usage_total = Counter(
    'fallback_usage_total',
    'Total times fallback (rule-based) was used'
)

@app.post("/analyze-fraud")
async def analyze_fraud(transaction: Transaction):
    try:
        # Try ML service
        result = await ml_service.predict(transaction)
        
        # Record metrics
        fraud_detections_total.labels(
            status='detected' if result.is_fraud else 'not_detected'
        ).inc()
        
        risk_score_distribution.observe(result.risk_score)
        
        ml_latency_seconds.labels(model='gpt-4-turbo').observe(result.latency)
        
        return result
        
    except MLServiceTimeout:
        ml_service_failures_total.labels(reason='timeout').inc()
        fallback_usage_total.inc()
        
        # Use fallback
        result = rule_based_detection(transaction)
        return result
```

**Component 4: Circuit Breaker Metrics**
- Requirements: Track circuit breaker state
- Metric: circuit_breaker_state (gauge: 0=closed, 1=open, 0.5=half-open)
- Update: Whenever circuit state changes
- What to figure out: How to integrate with tenacity circuit breaker
- Document: Circuit breaker metrics

**Component 5: Cost Metrics**
- Requirements: Track OpenAI API costs
- Metric: openai_cost_total (counter), openai_tokens_total (counter)
- Calculation: Tokens × model price
- What to figure out: How to get token counts from OpenAI response
- Document: Cost tracking

**Success Criteria:**
- Prometheus client library integrated
- /metrics endpoint exposed
- Request metrics collected (duration, count, errors)
- Business metrics tracked (fraud detections, risk scores)
- Circuit breaker state exposed
- Cost metrics calculated

---

## DAY 3 (WEDNESDAY): Grafana Dashboards

**Time:** 1.5 hours

### SESSION 1: Grafana Setup (45 min)

**Learning Resources:**

**Video:**
- "Grafana Tutorial for Beginners" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=p_FtR6hT5Mk
- Duration: 20:18
- Focus: Grafana setup, dashboards, panels

**Reading:**
- "Grafana Documentation - Getting Started"
- URL: https://grafana.com/docs/grafana/latest/getting-started/
- Duration: 15 min
- Focus: Data sources, dashboards, variables

**What You Need to Understand:**

**Grafana Components:**

**1. Data Sources:**
- Prometheus (metrics)
- CloudWatch (AWS metrics)
- PostgreSQL (business data)
- Your setup: Add all three

**2. Dashboards:**
- Collection of panels
- Organized by theme
- Your dashboards: Service Health, Application Metrics, Cost Tracking, Business KPIs, SLA Monitoring

**3. Panels:**
- Graph (time series)
- Gauge (single value)
- Stat (number)
- Table (data table)
- Heatmap (distribution)

**4. Variables:**
- Dashboard-level filters
- Example: $environment (prod, staging, dev)
- Dynamic queries based on variable

### SESSION 2: Create 5 Dashboards (45 min)

**Requirements:**

Build comprehensive monitoring dashboards:

**Dashboard 1: Service Health**
- Requirements: High-level service status
- Panels: Uptime percentage (gauge, target: 99.9%), Active requests (graph, 5-minute window), Error rate (graph, % of requests), Circuit breaker state (gauge: 0=closed, 1=open), ECS task count (stat, running tasks)
- Purpose: At-a-glance health check
- What to figure out: Appropriate time ranges for each panel
- Document: Service health dashboard

**PromQL Queries for Service Health:**
```
# Uptime percentage (last 24 hours)
(sum(rate(requests_total{status_code!~"5.."}[24h])) / sum(rate(requests_total[24h]))) * 100

# Active requests (current)
active_requests

# Error rate (5-minute window)
(sum(rate(requests_total{status_code=~"5.."}[5m])) / sum(rate(requests_total[5m]))) * 100

# Circuit breaker state
circuit_breaker_state{service="ml-service"}

# ECS task count (from CloudWatch)
aws_ecs_service_running_count{service="fraud-detection"}
```

**Dashboard 2: Application Metrics**
- Requirements: Application performance details
- Panels: Request duration P50/P95/P99 (graph, multi-line), Requests per second (graph), Error rate by endpoint (graph, stacked), ML service latency (graph, by model), Fallback usage rate (graph, % using rules vs ML)
- Purpose: Performance troubleshooting
- What to figure out: How to display multiple percentiles on same graph
- Document: Application metrics dashboard

**Dashboard 3: Business KPIs**
- Requirements: Fraud detection specific metrics
- Panels: Fraud detections per hour (graph), Risk score distribution (heatmap), Fraud rate (% of transactions flagged), Average risk score (stat), Top risk categories (table)
- Purpose: Business stakeholder view
- What to figure out: How to query PostgreSQL for top categories
- Document: Business KPIs dashboard

**Dashboard 4: Cost Tracking**
- Requirements: OpenAI API cost monitoring
- Panels: Total cost today (stat, $ amount), Cost per hour (graph), Cost by model (pie chart), Cost per customer (table, top 10), Projected monthly cost (stat, extrapolated)
- Purpose: Finance team visibility
- What to figure out: How to calculate projected cost from current trend
- Document: Cost dashboard

**Dashboard 5: SLA Monitoring**
- Requirements: Track SLA compliance
- Panels: Availability % (gauge, 99.9% target line), P95 latency (graph, 2s target line), Error rate (graph, 1% target line), Time in degraded mode (stat, minutes), SLA compliance status (table, per metric)
- Purpose: SLA reporting and compliance
- What to figure out: How to calculate SLA compliance over different periods
- Document: SLA dashboard

**Success Criteria:**
- Grafana installed and running
- 3 data sources connected (Prometheus, CloudWatch, PostgreSQL)
- All 5 dashboards created
- All panels displaying data correctly
- Dashboards accessible via URL

---

## DAY 4 (THURSDAY): CloudWatch Integration

**Time:** 1.5 hours

### SESSION 1: CloudWatch Basics (45 min)

**Learning Resources:**

**Reading:**
- "Amazon CloudWatch Documentation"
- URL: https://docs.aws.amazon.com/cloudwatch/
- Duration: 20 min
- Focus: Metrics, Logs, Alarms

**What You Need to Understand:**

**CloudWatch Components:**

**1. CloudWatch Metrics:**
- AWS services auto-publish metrics
- ECS: CPUUtilization, MemoryUtilization
- RDS: DatabaseConnections, ReadLatency
- ALB: TargetResponseTime, HealthyHostCount

**2. CloudWatch Logs:**
- Application logs from containers
- ECS logs to /ecs/fraud-detection
- Retention: 30 days
- Query with CloudWatch Logs Insights

**3. CloudWatch Alarms:**
- Trigger on metric thresholds
- Actions: SNS notification, Auto-scaling, Lambda

**4. CloudWatch Container Insights:**
- Enhanced ECS metrics
- Per-task CPU/memory
- Network I/O

### SESSION 2: CloudWatch Configuration (45 min)

**Requirements:**

Configure comprehensive CloudWatch monitoring:

**Component 1: Container Insights**
- Requirements: Enable for ECS cluster
- Metrics: Per-task CPU%, Memory%, Network in/out, Disk I/O
- What to figure out: Impact on costs ($0.30/month per task)
- Document: Container Insights setup

**Component 2: Custom Metrics**
- Requirements: Publish application metrics to CloudWatch
- Metrics: Fraud detection rate, ML service availability, Circuit breaker state
- Method: boto3 CloudWatch client
- What to figure out: Namespace naming convention
- Document: Custom metrics

**Example Custom Metrics:**
```python
import boto3
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')

async def publish_metrics(fraud_detected: bool, risk_score: int, ml_available: bool):
    cloudwatch.put_metric_data(
        Namespace='FraudDetection/Application',
        MetricData=[
            {
                'MetricName': 'FraudDetected',
                'Value': 1 if fraud_detected else 0,
                'Unit': 'Count',
                'Timestamp': datetime.utcnow()
            },
            {
                'MetricName': 'RiskScore',
                'Value': risk_score,
                'Unit': 'None',
                'Timestamp': datetime.utcnow()
            },
            {
                'MetricName': 'MLServiceAvailable',
                'Value': 1 if ml_available else 0,
                'Unit': 'Count',
                'Timestamp': datetime.utcnow()
            }
        ]
    )
```

**Component 3: Log Groups**
- Requirements: Structured logging to CloudWatch Logs
- Log groups: /ecs/fraud-detection/application, /ecs/fraud-detection/access, /aws/ecs/fraud-detection-cluster
- Format: JSON structured logs
- What to figure out: Log retention period (30 days? 90 days for compliance?)
- Document: Log configuration

**Component 4: Logs Insights Queries**
- Requirements: Pre-built queries for troubleshooting
- Query 1: Error logs, Query 2: Slowest requests, Query 3: Fraud detections per hour, Query 4: Circuit breaker state changes
- What to figure out: Most useful queries for on-call
- Document: Saved queries

**Example Logs Insights Queries:**
```
# Error logs (last hour)
fields @timestamp, @message, level, error
| filter level = "ERROR"
| sort @timestamp desc
| limit 100

# Slowest requests (P99)
fields @timestamp, endpoint, duration
| filter duration > 2000
| sort duration desc
| limit 20

# Fraud detections per hour
fields @timestamp
| filter fraud_detected = true
| stats count() as fraud_count by bin(@timestamp, 1h)

# Circuit breaker state changes
fields @timestamp, circuit_state, reason
| filter circuit_state_changed = true
| sort @timestamp desc
```

**Component 5: CloudWatch Dashboards**
- Requirements: AWS-native dashboards (complement Grafana)
- Widgets: ECS CPU/Memory, RDS connections, ALB response time, Custom application metrics
- Purpose: AWS-centric view (Grafana for application view)
- What to figure out: When to use CloudWatch vs Grafana dashboards
- Document: CloudWatch dashboards

**Success Criteria:**
- Container Insights enabled
- Custom metrics publishing
- Log groups configured with retention
- Logs Insights queries saved
- CloudWatch dashboards created

---

## DAY 5 (FRIDAY): Alert Configuration

**Time:** 1 hour

### SESSION 1: Alert Strategy (30 min)

**Requirements:**

Define alerting strategy:

**Alert Categories:**

**Category 1: Critical (Page On-Call)**
- Alerts: Service completely down (all ECS tasks failing), Error rate > 10%, P95 latency > 10s, SLA breach (availability < 99.9%)
- Notification: PagerDuty → on-call engineer immediately
- Response time: < 15 minutes
- What to figure out: On-call rotation schedule
- Document: Critical alerts

**Category 2: Warning (Slack/Email)**
- Alerts: Error rate 1-10%, P95 latency 2-10s, Circuit breaker open > 5 minutes, Degraded mode > 10 minutes, Cost > $50/day
- Notification: Slack #alerts channel + email
- Response time: < 1 hour during business hours
- What to figure out: Slack webhook URL
- Document: Warning alerts

**Category 3: Informational (Dashboard Only)**
- Alerts: New deployment completed, Auto-scaling event, Circuit breaker state change (closed → open)
- Notification: Dashboard annotation only
- Response time: None required
- What to figure out: How to add annotations to Grafana
- Document: Informational events

### SESSION 2: Implement Alerts (30 min)

**Requirements:**

Configure alerts in Grafana and CloudWatch:

**Component 1: Grafana Alerts**
- Requirements: Alert rules in Grafana
- Rules: High error rate, High latency, Low fraud detection rate (possible circuit breaker issue)
- What to figure out: Alert evaluation frequency (every 1 min? 5 min?)
- Document: Grafana alert rules

**Example Grafana Alert:**
```yaml
# High Error Rate Alert
name: High Error Rate
condition: (sum(rate(requests_total{status_code=~"5.."}[5m])) / sum(rate(requests_total[5m]))) * 100 > 5
for: 5m  # Must be true for 5 minutes
severity: critical
annotations:
  summary: "Error rate is {{ $value }}%"
  description: "Error rate has exceeded 5% for the last 5 minutes"
notifications:
  - pagerduty
  - slack
```

**Component 2: CloudWatch Alarms**
- Requirements: Alert on AWS infrastructure metrics
- Alarms: ECS CPU > 80% for 5 minutes, RDS connections > 80% of max, ALB unhealthy target count > 0, ECS task count < 2 (high availability)
- What to figure out: SNS topic for notifications
- Document: CloudWatch alarms

**Component 3: PagerDuty Integration**
- Requirements: Route critical alerts to PagerDuty
- Setup: Create PagerDuty service, Get integration key, Configure in Grafana
- What to figure out: Escalation policy (if on-call doesn't respond)
- Document: PagerDuty setup

**Component 4: Slack Integration**
- Requirements: Send warnings to Slack
- Setup: Create Slack app, Get webhook URL, Configure in Grafana
- Format: Rich message with graph snapshot
- What to figure out: Which channel (#alerts vs #fraud-detection)
- Document: Slack integration

**Component 5: Alert Fatigue Prevention**
- Requirements: Avoid too many alerts
- Strategies: Group related alerts, Use appropriate thresholds, Require sustained condition (not spikes), Auto-resolve when condition clears
- What to figure out: How many alerts per day is acceptable? (Target: < 5/day)
- Document: Alert tuning

**Success Criteria:**
- 5+ alert rules configured in Grafana
- 5+ CloudWatch alarms created
- PagerDuty integration working (test alert sent)
- Slack integration working (test message sent)
- Alert fatigue prevention strategies implemented

---

## DAY 6 (SATURDAY): Performance Dashboard

**Time:** 2.5 hours

### SESSION 1: Build Performance Dashboard (90 min)

**Requirements:**

Create detailed performance analysis dashboard:

**Panel 1: Latency Breakdown**
- Requirements: Show where time is spent
- Visualization: Stacked area chart
- Metrics: Database query time, Embedding generation time, Vector search time, GPT-4 inference time, Total request time
- Purpose: Identify bottlenecks
- What to figure out: How to measure each component
- Document: Latency breakdown

**Panel 2: Throughput**
- Requirements: Requests per second over time
- Visualization: Line graph
- Metrics: Total requests/s, Successful requests/s, Failed requests/s
- Annotations: Deployment markers
- What to figure out: What throughput is sustainable?
- Document: Throughput monitoring

**Panel 3: Error Analysis**
- Requirements: Understand error patterns
- Visualization: Table
- Columns: Error type, Count, % of total, Last occurrence, Example message
- Purpose: Prioritize error fixes
- What to figure out: How to extract error types from logs
- Document: Error analysis

**Panel 4: Resource Utilization**
- Requirements: Track resource usage
- Visualization: Multi-line graph
- Metrics: ECS task CPU%, ECS task Memory%, Database CPU%, Database connections
- Purpose: Right-size infrastructure
- What to figure out: What utilization is healthy (70%? 80%?)
- Document: Resource monitoring

**Panel 5: Queue Depths**
- Requirements: Detect backpressure
- Visualization: Gauge
- Metrics: Active requests (current), Pending requests (queue), Database connection pool (available)
- Alerts: Queue depth > 50
- What to figure out: How to implement request queue
- Document: Queue monitoring

**Panel 6: Cache Hit Rate**
- Requirements: Measure caching effectiveness
- Visualization: Stat + graph
- Metrics: Cache hits / (cache hits + misses), Saved time (hits × avg query time), Cost saved (hits × avg query cost)
- Purpose: Justify caching investment
- What to figure out: What hit rate is good (> 80%?)
- Document: Cache monitoring

### SESSION 2: Optimization Insights (60 min)

**Requirements:**

Use dashboard to find optimization opportunities:

**Analysis 1: Latency Hotspots**
- Requirements: Identify slowest components
- Method: Sort latency breakdown by duration
- Findings: [Run analysis and document results]
- Example: If embeddings = 70% of time → Cache embeddings OR Use faster model OR Batch embed requests
- What to figure out: Cost-benefit of each optimization
- Document: Latency optimizations

**Analysis 2: Error Patterns**
- Requirements: Find most common errors
- Method: Group errors by type, count occurrences
- Findings: [Run analysis and document results]
- Example: If "OpenAI rate limit" = 40% of errors → Request higher rate limit OR Implement retry with backoff OR Add caching
- What to figure out: Root cause for each error type
- Document: Error reduction plan

**Analysis 3: Resource Right-Sizing**
- Requirements: Optimize ECS task resources
- Current: 0.5 vCPU, 1 GB memory
- Actual usage: 30% CPU, 60% memory
- Recommendation: Reduce to 0.25 vCPU, 0.5 GB memory (save 50%)
- What to figure out: Test smaller tasks in staging first
- Document: Resource optimization

**Analysis 4: Cost Optimization**
- Requirements: Reduce OpenAI costs
- Current cost breakdown: GPT-4 fraud analysis: $0.04/request (80% of cost), Embeddings: $0.0001/request (1% of cost), Total: $0.04/request × 10K/day = $400/day = $12K/month
- Optimizations: Cache repeat transactions (10% cache hit rate = $1.2K/month saved), Use GPT-3.5 for low-risk transactions (50% switch = $6K/month saved), Batch embeddings (negligible savings)
- What to figure out: Which optimizations to implement first
- Document: Cost optimization plan

**Success Criteria:**
- Performance dashboard complete (6 panels)
- All 4 optimization analyses documented
- Specific recommendations for improvements
- Cost-benefit calculated for each optimization

---

## DAY 7 (SUNDAY): Week Summary & Documentation

**Time:** 2 hours

### SESSION 1: Monitoring Runbook (60 min)

**Requirements:**

Create operational monitoring runbook:

 **Runbook Section 1: Dashboard Guide**
- Requirements: Explain each dashboard and when to use it
- Service Health: First check when on-call alert fires
- Application Metrics: Performance debugging (latency spikes)
- Business KPIs: Daily standup review, executive reporting
- Cost Tracking: Weekly finance review, budget monitoring
- SLA Monitoring: Monthly compliance reporting, audit preparation
- What to figure out: Who is responsible for each dashboard
- Document: Dashboard usage guide

**Runbook Section 2: Alert Response Procedures**
- Requirements: Step-by-step response for each alert
- Critical Alert: Service Down → Check ECS console (tasks running?), Check CloudWatch logs (errors?), Check AWS Health Dashboard (regional outage?), Rollback last deployment if recent, Escalate to engineering manager if > 30 min
- Warning Alert: High Latency → Check Grafana latency breakdown panel, Identify slow component (DB? ML? embeddings?), Scale up if resource-constrained, Engage on-call if > 1 hour
- Cost Alert: Daily Budget Exceeded → Check LangSmith cost dashboard (which customer?), Review recent changes (new feature? traffic spike?), Implement temporary rate limiting if necessary, Review with engineering manager next day
- What to figure out: Escalation paths for each alert
- Document: Alert response procedures

**Runbook Section 3: Common Investigations**
- Requirements: How to investigate frequent issues
- Investigation 1: "Why is latency high?" → Check Grafana latency breakdown (which component?), Check CloudWatch ECS metrics (CPU/memory high?), Check LangSmith traces (specific model slow?), Check database metrics (connection pool exhausted?)
- Investigation 2: "Why are costs high?" → Check LangSmith cost dashboard (group by customer), Check cost per query trend (increased?), Identify expensive models (GPT-4 vs GPT-3.5), Review recent feature changes (new LLM calls?)
- Investigation 3: "Why is error rate elevated?" → Check CloudWatch Logs Insights (error types), Check Grafana error breakdown (which endpoint?), Check circuit breaker state (ML service down?), Check recent deployments (new bug introduced?)
- What to figure out: Most common investigations to document
- Document: Investigation procedures

**Runbook Section 4: Prometheus Query Reference**
- Requirements: Useful PromQL queries for troubleshooting
- Query 1: Current error rate: `(sum(rate(requests_total{status_code=~"5.."}[5m])) / sum(rate(requests_total[5m]))) * 100`
- Query 2: P95 latency by endpoint: `histogram_quantile(0.95, sum(rate(request_duration_seconds_bucket[5m])) by (endpoint, le))`
- Query 3: Fraud detection rate: `rate(fraud_detections_total{status="detected"}[1h])`
- Query 4: Circuit breaker state: `circuit_breaker_state{service="ml-service"}`
- Query 5: Fallback usage rate: `(rate(fallback_usage_total[5m]) / rate(requests_total[5m])) * 100`
- What to figure out: Which queries most useful for on-call
- Document: PromQL reference

**Runbook Section 5: Capacity Planning**
- Requirements: Use metrics to plan scaling
- Current capacity: 2 ECS tasks, 100 req/s sustained, 200 req/s peak (brief)
- Scaling indicators: CPU > 70% sustained, Active requests > 50, P95 latency > 3s
- Scaling actions: Add 1 task when CPU > 70% for 5 min, Add 2 tasks when CPU > 85% for 3 min, Max 10 tasks (cost limit)
- Cost calculation: 1 task = $18/month, Scale to 4 tasks = $72/month (baseline at 2 tasks = $36/month)
- What to figure out: When to scale up vs optimize code
- Document: Capacity planning guide

### SESSION 2: Week Summary (60 min)

**Requirements:**

Create WEEK25_SUMMARY.md:

**Section 1: What You Built**
- LangSmith integration (traces every LLM call)
- Prometheus metrics (15+ custom metrics)
- Grafana dashboards (5 dashboards, 30+ panels)
- CloudWatch integration (Container Insights, custom metrics, logs)
- Alert system (10+ alerts, PagerDuty + Slack)
- Performance dashboard (latency breakdown, optimization insights)
- Monitoring runbook (alert response, investigations, PromQL queries)
- Document: Complete build inventory

**Section 2: Fintech Impact - CRITICAL**
- Cost Control: Track OpenAI costs per query/customer/model (prevent runaway bills)
- Compliance: 90-day audit trail via LangSmith + CloudWatch Logs (SOX/Basel III)
- Performance: Latency breakdown identifies bottlenecks (optimize systematically)
- SLA Monitoring: Track 99.9% uptime commitment (prove compliance)
- Troubleshooting: Root cause analysis via traces (debug production issues)
- Optimization: Data-driven decisions (cost vs performance trade-offs)
- Document: Regulatory value

**Section 3: Monitoring Capabilities**
- LLM Observability: Every OpenAI call traced (input, output, cost, latency)
- Application Metrics: Requests, errors, latency, fraud detections (Prometheus)
- Infrastructure Metrics: ECS CPU/memory, RDS connections, ALB health (CloudWatch)
- Business KPIs: Fraud rate, risk scores, cost per customer (dashboards)
- Alerting: Critical → PagerDuty, Warning → Slack, Info → Dashboard (multi-tier)
- Cost Attribution: $0.04/fraud-check, $12K/month total, Customer A = $1,200/month (LangSmith)
- Document: Monitoring coverage

**Section 4: Optimization Opportunities Identified**
- Opportunity 1: Cache embeddings (10% hit rate = $1.2K/month saved)
- Opportunity 2: Use GPT-3.5 for low-risk (50% switch = $6K/month saved)
- Opportunity 3: Right-size ECS tasks (0.5 → 0.25 vCPU = 50% infrastructure cost saved)
- Opportunity 4: Batch database queries (reduce latency by 30%)
- Total potential savings: $7.2K/month + 30% faster
- Document: Optimization roadmap

**Section 5: Interview Talking Points**
- Story 1: "Implemented comprehensive monitoring stack with LangSmith, Prometheus, and Grafana, providing complete observability from LLM calls to infrastructure"
- Story 2: "Configured cost tracking per customer using LangSmith, enabling finance team to identify Customer A costing $1,200/month and implement usage-based pricing"
- Story 3: "Built latency breakdown dashboard identifying embeddings as 70% of request time, leading to caching strategy that reduced latency by 40%"
- Story 4: "Established 90-day audit trail via LangSmith and CloudWatch Logs, ensuring SOX compliance for ML-based fraud detection system"
- Story 5: "Configured multi-tier alerting (PagerDuty for critical, Slack for warnings) with alert fatigue prevention, reducing false positives by 80%"
- Document: STAR format stories

**Section 6: Production Readiness**
- Observability: Complete visibility into LLM, application, infrastructure layers
- Cost Tracking: Real-time per-query costs, projected monthly spend
- Performance: Latency breakdown, bottleneck identification
- SLA Monitoring: 99.9% uptime tracked and reported
- Alerting: Multi-tier alerts with appropriate escalation
- Compliance: 90-day audit trail for regulatory requirements
- Runbook: Documented procedures for common incidents
- Document: Production checklist

**Section 7: Metrics Collected**
- LangSmith: 8 metrics (cost, latency, tokens, model, etc.)
- Prometheus: 15+ metrics (requests, errors, fraud detections, circuit breaker, etc.)
- CloudWatch: 10+ metrics (ECS CPU/memory, RDS connections, ALB health, etc.)
- Business: 5 metrics (fraud rate, risk score distribution, cost per customer, etc.)
- Total: 40+ metrics tracked continuously
- Document: Metrics inventory

**Section 8: Dashboards Created**
- Dashboard 1: Service Health (5 panels) - At-a-glance system status
- Dashboard 2: Application Metrics (6 panels) - Performance troubleshooting
- Dashboard 3: Business KPIs (5 panels) - Stakeholder reporting
- Dashboard 4: Cost Tracking (5 panels) - Finance visibility
- Dashboard 5: SLA Monitoring (5 panels) - Compliance tracking
- Dashboard 6: Performance Analysis (6 panels) - Optimization insights
- Total: 6 dashboards, 32 panels
- Document: Dashboard catalog

**Success Criteria:**
- Monitoring runbook complete (5 sections)
- Week summary comprehensive
- Fintech impact articulated
- Optimization opportunities quantified
- Interview stories ready
- Production readiness documented

---

## 📚 ADDITIONAL RESOURCES

**LangSmith:**
- LangSmith Documentation: https://docs.smith.langchain.com/
- LangSmith Tracing Guide: https://docs.smith.langchain.com/tracing
- LangSmith Datasets: https://docs.smith.langchain.com/evaluation/datasets

**Prometheus:**
- Prometheus Documentation: https://prometheus.io/docs/
- PromQL Tutorial: https://prometheus.io/docs/prometheus/latest/querying/basics/
- Prometheus Best Practices: https://prometheus.io/docs/practices/naming/

**Grafana:**
- Grafana Documentation: https://grafana.com/docs/grafana/latest/
- Dashboard Best Practices: https://grafana.com/docs/grafana/latest/best-practices/
- Alerting Guide: https://grafana.com/docs/grafana/latest/alerting/

**CloudWatch:**
- CloudWatch Documentation: https://docs.aws.amazon.com/cloudwatch/
- Container Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html
- Logs Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html

**Monitoring Best Practices:**
- Google SRE Book - Monitoring: https://sre.google/sre-book/monitoring-distributed-systems/
- The Four Golden Signals: https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals
- RED Method: https://www.weave.works/blog/the-red-method-key-metrics-for-microservices-architecture/

---

## ✅ WEEK 25 DELIVERABLES

**Documentation:**
- LANGSMITH_SETUP.md - LangSmith integration guide
- PROMETHEUS_METRICS.md - Metrics catalog and PromQL queries
- GRAFANA_DASHBOARDS.md - Dashboard documentation
- CLOUDWATCH_INTEGRATION.md - AWS monitoring setup
- ALERT_CONFIGURATION.md - Alert rules and notification setup
- MONITORING_RUNBOOK.md - Operational procedures
- WEEK25_SUMMARY.md - Week summary

**Implementation Files (Requirements):**
- langsmith_config.py - LangSmith tracing setup (requirements documented)
- prometheus_metrics.py - Metrics definitions (requirements documented)
- grafana_dashboards.json - Dashboard configurations (requirements documented)
- cloudwatch_publisher.py - Custom metrics publisher (requirements documented)
- alert_rules.yaml - Grafana alert definitions (requirements documented)

**Dashboards:**
- Service Health Dashboard (5 panels)
- Application Metrics Dashboard (6 panels)
- Business KPIs Dashboard (5 panels)
- Cost Tracking Dashboard (5 panels)
- SLA Monitoring Dashboard (5 panels)
- Performance Analysis Dashboard (6 panels)

**Queries:**
- 20+ PromQL queries for Grafana panels
- 10+ CloudWatch Logs Insights queries
- 5+ PostgreSQL queries for business metrics

**Alerts:**
- 5+ critical alerts (PagerDuty)
- 5+ warning alerts (Slack)
- 5+ CloudWatch alarms (SNS)

**Understanding:**
- LLM observability with LangSmith
- Metrics collection and querying (Prometheus/PromQL)
- Dashboard design and visualization
- Alert strategy and configuration
- Cost tracking and attribution
- Compliance audit trails
- Performance analysis and optimization

---

## 🎯 SUCCESS CRITERIA

**By end of Week 25:**

**Conceptual:**
- Understand observability vs monitoring
- Know the four golden signals (latency, traffic, errors, saturation)
- Understand metric types (counter, gauge, histogram, summary)
- Know when to alert (critical vs warning)
- Understand cost attribution strategies
- Know compliance audit trail requirements

**Practical:**
- Integrate LangSmith for LLM tracing
- Collect metrics with Prometheus
- Build dashboards in Grafana
- Publish custom CloudWatch metrics
- Configure multi-tier alerting
- Track costs per query/customer
- Create operational runbooks
- Identify optimization opportunities

**Portfolio Impact:**
- ✅ Complete observability stack (FINTECH CRITICAL)
- ✅ Cost tracking and attribution (CFO-ready)
- ✅ 90-day audit trail (SOX compliance)
- ✅ SLA monitoring (99.9% uptime tracking)
- ✅ Performance optimization (data-driven decisions)
- ✅ Alert system (proactive issue detection)
- ✅ Production-grade monitoring (enterprise-ready)

---

## 💡 FINTECH IMPACT SUMMARY

**Cost Control:**
- Track $0.04/fraud-check, $12K/month total
- Identify Customer A = $1,200/month (implement usage-based pricing)
- Prevent runaway OpenAI bills (budget alerts at $50/day)

**Compliance:**
- 90-day audit trail (SOX/Basel III requirement)
- Prove fraud detection flagged high-risk transaction
- Complete LLM call history (input, output, decision)

**Performance:**
- Latency breakdown identifies embeddings = 70% of time
- Optimize based on data (not guesswork)
- Reduce P95 latency from 8s → 3s (targeted optimization)

**SLA Monitoring:**
- Track 99.9% uptime commitment
- Prove compliance to stakeholders
- Alert before SLA breach (proactive)

**Troubleshooting:**
- Root cause analysis via traces
- Debug production issues efficiently
- Reduce MTTR (mean time to recovery)

**Optimization:**
- Data-driven decisions ($7.2K/month savings identified)
- Cost vs performance trade-offs quantified
- Prioritize improvements by impact

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Cost control + compliance + performance  
**Next Week:** CI/CD Pipeline (Week 26)

**Status:** WEEKS 24-25 COMPLETE ✓