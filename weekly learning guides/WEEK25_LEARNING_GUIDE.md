# WEEK 25 LEARNING GUIDE: Production Monitoring Stack

**Timeline:** May 4-10, 2026  
**Total Time:** ~11-12 hours  
**Focus:** LangSmith tracing, Prometheus metrics, Grafana dashboards, CloudWatch integration, alerting

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- LangSmith integration (LLM observability)
- Prometheus metrics (application monitoring)
- Grafana dashboards (6 comprehensive dashboards)
- CloudWatch integration (AWS native monitoring)
- Multi-tier alerting system
- Cost tracking dashboard
- Performance analysis system

**What You'll Learn:**
- LLM observability with LangSmith
- Metrics collection with Prometheus
- Dashboard creation with Grafana
- CloudWatch Logs and Metrics
- Alert configuration and routing
- Cost optimization through monitoring
- Performance debugging techniques

**Fintech Application - CRITICAL:**

**The Banking Monitoring Reality:**
```
Why Banks Need Extreme Observability:

Regulatory Requirements:
- SOX compliance: 90-day audit trail required
- Basel III: Complete transaction history
- GDPR: Track all data access
- PCI-DSS: Log all card data operations

Financial Impact:
- 1 minute downtime = $50,000 lost transactions
- Fraud detection failure = $500K/day average fraud losses
- Slow responses = Customer churn (0.5s delay = 20% drop)
- Cost overruns = Budget violations, CFO unhappy

Operational Reality:
- 3 AM incidents require fast diagnosis
- "Why did this fraud check cost $0.50?" (should be $0.04)
- "Which LLM prompt is slowest?"
- "Is the degradation worth the cost savings?"
```

**The Problem Without Comprehensive Monitoring:**
```
Scenario: Fraud detection accuracy drops from 95% to 88%

Without Monitoring:
- Notice: 2 weeks later when fraud losses spike
- Root cause: Unknown (changed prompt? Model? Data?)
- Cost: $150K in undetected fraud
- Debug time: 3 days of investigation
- Result: Customer lost confidence

With Comprehensive Monitoring:
- Notice: 10 minutes (alert: accuracy < 90%)
- Root cause: Dashboard shows prompt change at 14:23
- Cost: $800 in fraud (10 minutes only)
- Debug time: 5 minutes (trace shows exact issue)
- Result: Rollback prompt, issue resolved
```

**Week 25 Achieves:**
1. **LangSmith:** Every LLM call traced (prompt, response, cost, latency)
2. **Prometheus:** 15+ custom metrics (requests, errors, latency)
3. **Grafana:** 6 dashboards (health, performance, business, cost)
4. **CloudWatch:** Container metrics, logs, insights queries
5. **Alerts:** 3-tier (info → warning → critical)
6. **Cost tracking:** Per-query cost visibility
7. **Performance analysis:** Identify bottlenecks

---

## DAY 1 (MONDAY): LangSmith Setup & Tracing

**Time:** 1.5 hours

### SESSION 1: LLM Observability Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "LangSmith Introduction" - LangChain
- URL: https://www.youtube.com/watch?v=hwfJBIvGMZk
- Duration: 12:00
- Focus: Why LLM observability matters

**Reading:**
- "LangSmith Documentation"
- URL: https://docs.smith.langchain.com/
- Duration: 20 min
- Focus: Tracing, monitoring, evaluation

**What You Need to Understand:**

**Why LLM Observability is Different:**
```
Traditional API Monitoring:
- Request/response
- Latency, errors
- Status codes
- Simple metrics

LLM API Monitoring (More Complex):
- Full prompt text (what did we ask?)
- Full response (what did it say?)
- Token counts (how much did it cost?)
- Model version (which GPT-4?)
- Temperature/parameters (what settings?)
- Chain of calls (RAG = multiple LLM calls)
- Prompt engineering (which prompt version?)
- Cost per query (varies by length)
```

**What LangSmith Provides:**

**1. Tracing:**
- Every LLM call captured
- Full prompt and response stored
- Token counts tracked
- Latency measured
- Nested traces (RAG chains)

**2. Cost Tracking:**
- Per-query cost
- Daily/monthly totals
- Cost breakdown by model
- Identify expensive queries

**3. Prompt Versioning:**
- Track prompt changes
- A/B test prompts
- Rollback to previous versions

**4. Debugging:**
- See exact prompt that caused error
- Replay failed queries
- Inspect intermediate steps

**5. Evaluation:**
- Test prompt changes
- Compare model outputs
- Quality metrics

**Banking Use Cases:**

**Use Case 1: Cost Accountability**
```
Question: "Why is our OpenAI bill $15,000 this month?"

Without LangSmith:
- No idea which queries expensive
- Can't identify wasteful prompts
- Just see total bill

With LangSmith:
- Dashboard shows: 80% cost from single query type
- Trace reveals: Fraud checks sending entire 5-page policy document in prompt
- Fix: Reduce context to relevant section only
- Result: Cost drops to $4,000/month (73% savings)
```

**Use Case 2: Audit Trail**
```
Regulator: "Show us the AI decision for loan rejection #12345"

Without LangSmith:
- No record of exact prompt
- No record of LLM response
- Can't reproduce decision
- Compliance violation

With LangSmith:
- Search by transaction ID
- See exact prompt sent
- See exact GPT-4 response
- See timestamp, user, model version
- Full audit trail for 90 days
```

**Use Case 3: Performance Debugging**
```
Issue: "Fraud detection suddenly slow (5s → 15s)"

Without LangSmith:
- Don't know which step slow
- Is it OpenAI? Database? Embedding?
- Trial and error debugging

With LangSmith:
- Trace shows latency breakdown:
  - Embedding: 0.5s
  - OpenSearch: 1s
  - GPT-4: 13s (PROBLEM!)
  - Database: 0.5s
- Drill into GPT-4 trace
- Prompt is 8,000 tokens (too long!)
- Fix: Reduce context
- Result: Back to 5s
```

### SESSION 2: Implement LangSmith Tracing (Requirements)

**Requirements:**

Integrate LangSmith into fraud detection system:

**Component 1: LangSmith Account Setup**
- Requirements: Create and configure LangSmith account
- Steps:
  1. Sign up at smith.langchain.com
  2. Create project: "fraud-detection-prod"
  3. Generate API key
  4. Store in AWS Secrets Manager
- Environment variables:
  - LANGCHAIN_TRACING_V2=true
  - LANGCHAIN_API_KEY={from secrets manager}
  - LANGCHAIN_PROJECT=fraud-detection-prod
- What to figure out: Project naming convention
- Document: Setup instructions

**Component 2: Trace All LLM Calls**
- Requirements: Automatic tracing of every OpenAI call
- Trace captures:
  - Full prompt text
  - Full response text
  - Model used (gpt-4, gpt-3.5-turbo)
  - Temperature/parameters
  - Token counts (prompt + completion)
  - Latency (time to first token, total time)
  - Cost (calculated from tokens × pricing)
  - Timestamp
  - User/request context
- Implementation: Use @traceable decorator
- What to figure out: Which metadata to include in traces
- Document: Tracing implementation requirements

**Component 3: Custom Metadata**
- Requirements: Add business context to traces
- Metadata to include:
  - transaction_id (link to transaction)
  - customer_id (who is this for)
  - fraud_check_type (initial, review, appeal)
  - tier (full service, degraded, fallback)
  - is_fallback (boolean - was rule-based used?)
  - environment (prod, staging, dev)
- Purpose: Filter and analyze traces by business dimension
- What to figure out: What metadata is most useful
- Document: Metadata schema

**Component 4: Cost Tracking**
- Requirements: Track cost per query
- Calculation:
  - Prompt tokens × $0.01/1K (GPT-4 input)
  - Completion tokens × $0.03/1K (GPT-4 output)
  - Total cost per query
- Aggregations needed:
  - Cost per hour/day/month
  - Cost by fraud_check_type
  - Cost by customer (identify expensive customers)
  - Cost by tier (full vs degraded)
- Target: < $0.04 per fraud check average
- What to figure out: How to alert on high-cost queries
- Document: Cost tracking requirements

**Component 5: Trace Search and Filtering**
- Requirements: Ability to find specific traces
- Search criteria:
  - By transaction_id
  - By customer_id
  - By date range
  - By cost (> $0.10)
  - By latency (> 10s)
  - By error status
  - By tier (degraded only)
- Use cases:
  - Debug specific transaction
  - Find all expensive queries
  - Audit trail for regulator
- What to figure out: Retention period (90 days for compliance?)
- Document: Search requirements

**Component 6: Prompt Version Tracking**
- Requirements: Track when prompts change
- Versioning scheme:
  - fraud_detection_v1
  - fraud_detection_v2
  - fraud_detection_v3
- What to track:
  - Prompt text (full template)
  - When changed
  - Who changed it
  - Why changed (release notes)
  - Performance impact
- Purpose: Rollback if new prompt performs worse
- What to figure out: How to version prompts programmatically
- Document: Versioning strategy

**Component 7: Performance Dashboards**
- Requirements: LangSmith dashboard for monitoring
- Dashboards to create in LangSmith:
  1. Cost tracking (daily spend, top expensive queries)
  2. Latency monitoring (P50, P95, P99)
  3. Error tracking (failed calls, error types)
  4. Token usage (average tokens per call)
  5. Model usage (GPT-4 vs GPT-3.5 distribution)
- What to figure out: Alert thresholds
- Document: Dashboard requirements

**Success Criteria:**
- LangSmith account configured
- All LLM calls traced automatically
- Custom metadata included
- Cost tracking working
- Traces searchable
- Prompt versioning enabled
- Dashboards created in LangSmith
- 90-day audit trail verified

---

## DAY 2 (TUESDAY): Prometheus Metrics

**Time:** 1.5 hours

### SESSION 1: Prometheus Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "Prometheus Monitoring Explained" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=h4Sl21AKiDg
- Duration: 17:00
- Focus: Architecture, scraping, metrics types

**Reading:**
- "Prometheus Documentation - Introduction"
- URL: https://prometheus.io/docs/introduction/overview/
- Duration: 15 min
- Focus: Data model, metric types

**Additional Reading:**
- "Prometheus Best Practices"
- URL: https://prometheus.io/docs/practices/naming/
- Duration: 15 min
- Focus: Metric naming, labels

**What You Need to Understand:**

**Prometheus Architecture:**
```
┌─────────────────────────────────────────┐
│  Your Application (FastAPI)            │
│  - Exposes /metrics endpoint            │
│  - Returns metrics in Prometheus format│
└─────────────┬───────────────────────────┘
              │
              │ HTTP GET /metrics every 15s
              │
              v
┌─────────────────────────────────────────┐
│  Prometheus Server                      │
│  - Scrapes /metrics                     │
│  - Stores time-series data              │
│  - Evaluates alert rules                │
└─────────────┬───────────────────────────┘
              │
              │ Query with PromQL
              │
              v
┌─────────────────────────────────────────┐
│  Grafana (Visualization)                │
│  - Queries Prometheus                   │
│  - Displays dashboards                  │
└─────────────────────────────────────────┘
```

**Metric Types:**

**1. Counter (only goes up):**
- Total requests served
- Total errors
- Total fraud detected
- Example: `fraud_detections_total{result="suspicious"}`

**2. Gauge (goes up and down):**
- Current CPU usage
- Active connections
- Queue depth
- Example: `circuit_breaker_state{service="openai", state="open"}`

**3. Histogram (distribution):**
- Request latency buckets
- Response size distribution
- Example: `fraud_check_duration_seconds{le="0.5"}`

**4. Summary (like histogram but calculated):**
- Quantiles (P50, P95, P99)
- Less flexible than histogram

**Metric Naming Convention:**
```
Format: {namespace}_{name}_{unit}

Examples:
- fraud_detection_requests_total (counter)
- fraud_detection_duration_seconds (histogram)
- openai_api_calls_total (counter)
- circuit_breaker_state (gauge)
- database_connection_pool_active (gauge)
```

**Labels (Dimensions):**
```
Metric with labels:
fraud_detection_requests_total{
  method="POST",
  endpoint="/api/v1/predict",
  status="200",
  tier="full"
}

Allows queries like:
- Total requests: sum(fraud_detection_requests_total)
- Only errors: sum(fraud_detection_requests_total{status=~"5.."})
- By tier: sum by (tier) (fraud_detection_requests_total)
```

### SESSION 2: Implement Prometheus Metrics (Requirements)

**Requirements:**

Add comprehensive metrics to fraud detection service:

**Component 1: Prometheus Client Setup**
- Requirements: Expose /metrics endpoint
- Library: prometheus-client (Python)
- Endpoint: GET /metrics
- Format: Prometheus text format
- Update frequency: Real-time (updated on each request)
- What to figure out: Metric registry configuration
- Document: Client setup requirements

**Component 2: HTTP Request Metrics**
- Requirements: Track all HTTP requests
- Metrics needed:

**Metric 1: Request Counter**
- Name: `http_requests_total`
- Type: Counter
- Labels: method, endpoint, status_code, tier
- Purpose: Count all requests
- Example: `http_requests_total{method="POST", endpoint="/predict", status_code="200", tier="full"} 15432`

**Metric 2: Request Duration**
- Name: `http_request_duration_seconds`
- Type: Histogram
- Buckets: 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10
- Labels: method, endpoint, tier
- Purpose: Track latency distribution
- What to figure out: Appropriate bucket boundaries

**Metric 3: Request Size**
- Name: `http_request_size_bytes`
- Type: Histogram
- Labels: method, endpoint
- Purpose: Track request payload size

**Metric 4: Response Size**
- Name: `http_response_size_bytes`
- Type: Histogram
- Labels: endpoint, status_code
- Purpose: Track response payload size

- What to figure out: How to instrument FastAPI middleware
- Document: HTTP metrics requirements

**Component 3: Business Metrics**
- Requirements: Track fraud detection specific metrics

**Metric 5: Fraud Detections**
- Name: `fraud_detections_total`
- Type: Counter
- Labels: result (suspicious, legitimate, review), tier (full, degraded)
- Purpose: Count fraud detection outcomes

**Metric 6: Risk Score Distribution**
- Name: `fraud_risk_score`
- Type: Histogram
- Buckets: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
- Labels: tier
- Purpose: Track risk score distribution

**Metric 7: False Positive Rate**
- Name: `fraud_false_positives_total`
- Type: Counter
- Labels: tier
- Purpose: Track incorrectly flagged transactions (requires feedback)

**Metric 8: Transaction Amount**
- Name: `transaction_amount_dollars`
- Type: Histogram
- Buckets: 1, 10, 50, 100, 500, 1000, 5000, 10000
- Purpose: Track transaction amounts processed

- What to figure out: Which business metrics most valuable
- Document: Business metrics requirements

**Component 4: LLM Metrics**
- Requirements: Track OpenAI API usage

**Metric 9: LLM Calls**
- Name: `llm_api_calls_total`
- Type: Counter
- Labels: model (gpt-4, gpt-3.5-turbo), status (success, error), tier
- Purpose: Count LLM API calls

**Metric 10: LLM Latency**
- Name: `llm_api_duration_seconds`
- Type: Histogram
- Buckets: 0.5, 1, 2, 5, 10, 15, 20, 30
- Labels: model, tier
- Purpose: Track LLM response times

**Metric 11: Token Usage**
- Name: `llm_tokens_total`
- Type: Counter
- Labels: model, type (prompt, completion)
- Purpose: Track token consumption

**Metric 12: LLM Cost**
- Name: `llm_cost_dollars_total`
- Type: Counter
- Labels: model
- Purpose: Track cumulative LLM costs

- What to figure out: How to calculate cost per request
- Document: LLM metrics requirements

**Component 5: System Metrics**
- Requirements: Track service health

**Metric 13: Circuit Breaker State**
- Name: `circuit_breaker_state`
- Type: Gauge
- Values: 0 (closed), 1 (open), 2 (half_open)
- Labels: service (openai, database, redis)
- Purpose: Track circuit breaker states

**Metric 14: Degradation Tier**
- Name: `service_tier`
- Type: Gauge
- Values: 1-5 (tier number)
- Purpose: Track current service tier

**Metric 15: Database Connections**
- Name: `database_connections_active`
- Type: Gauge
- Purpose: Track active database connections

**Metric 16: Cache Hit Rate**
- Name: `cache_hits_total` and `cache_misses_total`
- Type: Counter
- Labels: cache_type (redis, local)
- Purpose: Track cache effectiveness

- What to figure out: Additional system metrics needed
- Document: System metrics requirements

**Component 6: Prometheus Middleware**
- Requirements: Automatic metric collection
- Implementation: FastAPI middleware
- Functionality:
  - Intercept all requests
  - Record start time
  - Execute request
  - Record end time, status, size
  - Update metrics
  - Continue request
- What to figure out: Performance impact of metrics collection
- Document: Middleware requirements

**Component 7: Custom Metrics**
- Requirements: Application-specific metrics
- Examples:
  - Time spent in rule evaluation
  - Number of rules triggered
  - Fallback activation count
  - Model routing decisions (GPT-4 vs GPT-3.5)
- What to figure out: Which custom metrics add value
- Document: Custom metrics catalog

**Success Criteria:**
- /metrics endpoint exposed
- 15+ metrics defined
- HTTP request metrics working
- Business metrics tracked
- LLM metrics captured
- System metrics monitored
- Middleware implemented
- Metrics accessible to Prometheus

---

## DAY 3 (WEDNESDAY): Grafana Dashboards

**Time:** 1.5 hours

### SESSION 1: Grafana Fundamentals (30 min)

**Learning Resources:**

**Video:**
- "Grafana Crash Course" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=QD2k6xZNmGQ
- Duration: 22:00
- Focus: Datasources, dashboards, panels

**Reading:**
- "Grafana Documentation - Getting Started"
- URL: https://grafana.com/docs/grafana/latest/getting-started/
- Duration: 10 min
- Focus: Dashboard basics

**What You Need to Understand:**

**Grafana Concepts:**

**1. Data Source:**
- Where data comes from
- Your setup: Prometheus, CloudWatch
- Configure once, use in many dashboards

**2. Dashboard:**
- Collection of panels
- Your setup: 6 dashboards
- Can have variables (filters)

**3. Panel:**
- Single visualization
- Types: Graph, gauge, table, heatmap, stat
- Queries Prometheus with PromQL

**4. PromQL (Prometheus Query Language):**
```
Examples:
- Rate: rate(http_requests_total[5m])
- Sum: sum(http_requests_total)
- By label: sum by (endpoint) (http_requests_total)
- Percentage: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])
```

**5. Variables:**
- Filter dashboards
- Example: $environment (prod, staging)
- Dropdown at top of dashboard

### SESSION 2: Build 6 Dashboards (Requirements)

**Requirements:**

Create comprehensive monitoring dashboards:

**Dashboard 1: Service Health Overview**
- Requirements: High-level service status
- Time range: Last 1 hour (default)
- Refresh: 30 seconds

**Row 1: Current Status (4 panels)**
- Panel 1: Uptime Percentage (Stat panel)
  - Query: Calculate uptime from health checks
  - Display: 99.95%
  - Color: Green > 99.9%, Yellow > 99%, Red < 99%

- Panel 2: Active Tasks (Gauge panel)
  - Query: ECS task count
  - Display: 4 / 10 (current / max)
  - Thresholds: Green < 70%, Yellow < 90%, Red >= 90%

- Panel 3: Current Tier (Stat panel)
  - Query: service_tier gauge
  - Display: "Tier 1 - Full Service"
  - Color: Green = Tier 1, Yellow = Tier 2-3, Red = Tier 4-5

- Panel 4: Circuit Breaker Status (Stat panel)
  - Query: circuit_breaker_state
  - Display: "CLOSED" (all healthy)
  - Color: Green = CLOSED, Red = OPEN, Yellow = HALF_OPEN

**Row 2: Traffic & Performance (3 panels)**
- Panel 5: Request Rate (Graph panel)
  - Query: rate(http_requests_total[5m])
  - Display: Line graph, requests/second
  - Time series for last hour

- Panel 6: Error Rate (Graph panel)
  - Query: rate(http_requests_total{status=~"5.."}[5m])
  - Display: Line graph, errors/second
  - Threshold line at 1% of traffic

- Panel 7: P95 Latency (Graph panel)
  - Query: histogram_quantile(0.95, http_request_duration_seconds)
  - Display: Line graph, seconds
  - Threshold line at 2 seconds (SLA)

**Row 3: Resources (3 panels)**
- Panel 8: CPU Usage (Graph panel)
  - Query: From CloudWatch, ECS container CPU
  - Display: Line graph per task

- Panel 9: Memory Usage (Graph panel)
  - Query: From CloudWatch, ECS container memory
  - Display: Line graph per task

- Panel 10: Database Connections (Graph panel)
  - Query: database_connections_active
  - Display: Line graph
  - Threshold: Connection pool limit

- What to figure out: Optimal panel layout
- Document: Service Health dashboard requirements

**Dashboard 2: Application Metrics**
- Requirements: Detailed application performance
- Time range: Last 6 hours (default)

**Row 1: Request Analytics (4 panels)**
- Panel 1: Requests by Endpoint (Bar gauge)
  - Query: sum by (endpoint) (http_requests_total)
  - Display: Horizontal bars

- Panel 2: Status Code Distribution (Pie chart)
  - Query: sum by (status_code) (http_requests_total)
  - Display: Pie chart (200, 400, 404, 500, etc.)

- Panel 3: Latency Heatmap (Heatmap panel)
  - Query: http_request_duration_seconds
  - Display: Heatmap showing latency distribution over time

- Panel 4: Request Size (Graph panel)
  - Query: histogram_quantile(0.95, http_request_size_bytes)
  - Display: P95 request size over time

**Row 2: Business Metrics (3 panels)**
- Panel 5: Fraud Detections (Graph panel)
  - Query: rate(fraud_detections_total[5m]) by result
  - Display: Stacked area chart (suspicious, legitimate, review)

- Panel 6: Risk Score Distribution (Heatmap panel)
  - Query: fraud_risk_score
  - Display: Heatmap of risk scores over time

- Panel 7: Fraud Detection Rate (Stat panel)
  - Query: sum(fraud_detections_total{result="suspicious"}) / sum(fraud_detections_total)
  - Display: 5.2% (percentage of transactions flagged)

**Row 3: LLM Metrics (3 panels)**
- Panel 8: LLM Call Rate (Graph panel)
  - Query: rate(llm_api_calls_total[5m]) by model
  - Display: Line graph (GPT-4 vs GPT-3.5)

- Panel 9: LLM Latency by Model (Graph panel)
  - Query: histogram_quantile(0.95, llm_api_duration_seconds) by model
  - Display: Compare GPT-4 vs GPT-3.5 latency

- Panel 10: Token Usage (Graph panel)
  - Query: rate(llm_tokens_total[5m]) by type
  - Display: Stacked area (prompt tokens, completion tokens)

- What to figure out: Most valuable application metrics
- Document: Application Metrics dashboard requirements

**Dashboard 3: Business KPIs**
- Requirements: Executive-level metrics
- Time range: Last 7 days (default)

**Row 1: Key Metrics (4 panels)**
- Panel 1: Total Transactions (Stat panel)
  - Query: sum(http_requests_total{endpoint="/predict"})
  - Display: 1.2M (last 7 days)

- Panel 2: Fraud Detection Accuracy (Gauge panel)
  - Query: Requires ground truth data
  - Display: 94.5% (if available)
  - Thresholds: Green > 90%, Yellow > 85%, Red < 85%

- Panel 3: Average Response Time (Stat panel)
  - Query: avg(rate(http_request_duration_seconds[7d]))
  - Display: 1.85s

- Panel 4: Service Availability (Stat panel)
  - Query: Uptime calculation over 7 days
  - Display: 99.95%

**Row 2: Fraud Analytics (3 panels)**
- Panel 5: Fraud Trend (Graph panel)
  - Query: sum(fraud_detections_total{result="suspicious"}) over time
  - Display: Daily fraud detections

- Panel 6: False Positive Trend (Graph panel)
  - Query: rate(fraud_false_positives_total[1d])
  - Display: False positives per day

- Panel 7: Transaction Amount Analysis (Table panel)
  - Query: Group transactions by amount bucket
  - Display: Table with count per bucket

**Row 3: Operational Metrics (3 panels)**
- Panel 8: Tier Distribution (Pie chart)
  - Query: Time spent in each tier over 7 days
  - Display: Pie chart (Tier 1: 98%, Tier 2: 2%)

- Panel 9: Circuit Breaker Trips (Stat panel)
  - Query: Count of circuit breaker opens
  - Display: 3 trips (last 7 days)

- Panel 10: Recovery Time (Stat panel)
  - Query: Average time in OPEN state
  - Display: 3.5 minutes average

- What to figure out: Which KPIs executives care about
- Document: Business KPIs dashboard requirements

**Dashboard 4: Cost Tracking**
- Requirements: Monitor AWS and LLM costs
- Time range: Last 30 days (default)

**Row 1: Total Costs (3 panels)**
- Panel 1: Total Monthly Cost (Stat panel)
  - Query: Sum of all cost sources
  - Display: $1,247 (current month to date)

- Panel 2: Cost Trend (Graph panel)
  - Query: Daily cost over 30 days
  - Display: Stacked area (Fargate, LLM, Data Transfer, Other)

- Panel 3: Cost per Transaction (Stat panel)
  - Query: Total cost / Total transactions
  - Display: $0.038 per transaction

**Row 2: LLM Costs (4 panels)**
- Panel 4: LLM Cost Breakdown (Pie chart)
  - Query: sum by (model) (llm_cost_dollars_total)
  - Display: GPT-4 vs GPT-3.5 vs fallback

- Panel 5: Hourly LLM Cost (Graph panel)
  - Query: rate(llm_cost_dollars_total[1h])
  - Display: Cost per hour trend

- Panel 6: Cost per Model (Table panel)
  - Query: List models with total cost, calls, avg cost per call
  - Display: Table sorted by total cost

- Panel 7: Expensive Queries (Table panel)
  - Query: From LangSmith, queries > $0.10
  - Display: Top 10 expensive queries

**Row 3: Infrastructure Costs (3 panels)**
- Panel 8: Fargate Cost (Graph panel)
  - Query: From CloudWatch Cost Explorer
  - Display: Daily Fargate cost

- Panel 9: Data Transfer Cost (Graph panel)
  - Query: From CloudWatch
  - Display: Data egress costs

- Panel 10: Storage Cost (Stat panel)
  - Query: S3 + RDS + OpenSearch storage costs
  - Display: Monthly storage cost

**Row 4: Cost Optimization (2 panels)**
- Panel 11: Savings from Model Routing (Stat panel)
  - Query: Calculate savings from using GPT-3.5 vs GPT-4
  - Display: $487 saved this month (estimated)

- Panel 12: Budget Status (Gauge panel)
  - Query: Current month cost / Monthly budget
  - Display: 62% of budget used (day 18 of month)
  - Thresholds: Green < 75%, Yellow < 90%, Red >= 90%

- What to figure out: How to pull cost data from AWS
- Document: Cost Tracking dashboard requirements

**Dashboard 5: SLA Monitoring**
- Requirements: Track against defined SLAs
- Time range: Last 24 hours (default)

**Row 1: SLA Summary (4 panels)**
- Panel 1: Availability SLA (Gauge panel)
  - Target: 99.9%
  - Current: 99.95%
  - Status: ✅ Meeting SLA

- Panel 2: Latency SLA (Gauge panel)
  - Target: P95 < 2 seconds
  - Current: P95 1.85 seconds
  - Status: ✅ Meeting SLA

- Panel 3: Error Rate SLA (Gauge panel)
  - Target: < 1%
  - Current: 0.12%
  - Status: ✅ Meeting SLA

- Panel 4: Data Freshness SLA (Gauge panel)
  - Target: < 5 minutes
  - Current: 2.3 minutes
  - Status: ✅ Meeting SLA

**Row 2: SLA Trends (4 panels)**
- Panel 5-8: Graph panels for each SLA showing trend over 24 hours
  - Display threshold line for target
  - Highlight violations in red

**Row 3: Error Budget (2 panels)**
- Panel 9: Error Budget Remaining (Gauge panel)
  - Query: Calculate based on 99.9% SLA
  - Display: 55% budget remaining

- Panel 10: Error Budget Burn Rate (Graph panel)
  - Query: Rate of error budget consumption
  - Display: Projected budget depletion date

- What to figure out: How to calculate error budgets
- Document: SLA Monitoring dashboard requirements

**Dashboard 6: Performance Analysis**
- Requirements: Deep performance debugging
- Time range: Last 1 hour (default)

**Row 1: Latency Breakdown (3 panels)**
- Panel 1: Total Request Latency (Graph panel)
  - Query: P50, P95, P99 latency
  - Display: 3 lines

- Panel 2: Latency by Component (Stacked graph panel)
  - Query: Time spent in each component
  - Display: Database, LLM, Processing, Network
  - Purpose: Identify bottlenecks

- Panel 3: Slowest Endpoints (Table panel)
  - Query: P99 latency per endpoint
  - Display: Table sorted by slowest

**Row 2: Database Performance (3 panels)**
- Panel 4: Query Duration (Graph panel)
  - Query: Database query latency histogram
  - Display: P95 query time

- Panel 5: Connection Pool (Graph panel)
  - Query: Active vs idle connections
  - Display: Stacked area

- Panel 6: Slow Queries (Table panel)
  - Query: From CloudWatch RDS logs
  - Display: Queries > 1 second

**Row 3: LLM Performance (3 panels)**
- Panel 7: Time to First Token (Graph panel)
  - Query: LLM streaming latency
  - Display: Time until first token received

- Panel 8: Token Generation Speed (Graph panel)
  - Query: Tokens per second
  - Display: Throughput over time

- Panel 9: LLM Error Analysis (Table panel)
  - Query: LLM errors by type
  - Display: Count per error type

**Row 4: Optimization Opportunities (3 panels)**
- Panel 10: Cache Effectiveness (Stat panel)
  - Query: cache_hits / (cache_hits + cache_misses)
  - Display: 87% hit rate

- Panel 11: Largest Requests (Table panel)
  - Query: P99 request size
  - Display: Endpoints with largest payloads

- Panel 12: Savings Identified (Stat panel)
  - Query: Calculate potential savings from optimizations
  - Display: $124/day savings opportunity

- What to figure out: Most impactful performance metrics
- Document: Performance Analysis dashboard requirements

**Component: Dashboard Variables**
- Requirements: Make dashboards filterable
- Variables to add:
  - $environment (prod, staging, dev)
  - $tier (1, 2, 3, 4, 5)
  - $endpoint (list of endpoints)
  - $model (gpt-4, gpt-3.5-turbo)
- Purpose: Filter all panels with dropdown
- What to figure out: How to configure Grafana variables
- Document: Variable configuration

**Success Criteria:**
- 6 dashboards created
- Each dashboard has 8-12 panels
- All panels query Prometheus/CloudWatch successfully
- Dashboards auto-refresh
- Variables working
- Color coding applied (green/yellow/red)
- Thresholds set appropriately
- Can drill down from summary to detail

---

## DAY 4 (THURSDAY): CloudWatch Integration

**Time:** 1 hour

### SESSION 1: CloudWatch Logs & Metrics (30 min)

**Learning Resources:**

**Reading:**
- "CloudWatch Concepts"
- URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
- Duration: 15 min
- Focus: Logs, metrics, namespaces

**What You Need to Understand:**

**CloudWatch Components:**

**1. CloudWatch Logs:**
- Application logs from containers
- Searchable with Logs Insights
- Retention configurable

**2. CloudWatch Metrics:**
- Time-series data
- Custom metrics from application
- Container metrics from ECS

**3. CloudWatch Alarms:**
- Trigger on metric thresholds
- Notify SNS, PagerDuty, etc.

**4. CloudWatch Dashboards:**
- Alternative to Grafana
- Native AWS dashboards

**Why Both Prometheus and CloudWatch:**
```
Prometheus:
- Application metrics (custom)
- Fast, local scraping
- Better for real-time debugging
- Free (self-hosted)

CloudWatch:
- Infrastructure metrics (ECS, RDS)
- Native AWS integration
- Persistent storage
- Alerting included
- Costs money

Best Practice: Use both
- Prometheus for app metrics, Grafana for visualization
- CloudWatch for infrastructure, logs, long-term storage
- Export Prometheus to CloudWatch for disaster recovery
```

### SESSION 2: CloudWatch Integration (Requirements)

**Requirements:**

Integrate application with CloudWatch:

**Component 1: CloudWatch Logs**
- Requirements: Send structured logs to CloudWatch
- Log groups:
  - /ecs/fraud-detection/application
  - /ecs/fraud-detection/access
- Log format: JSON
- Fields to log:
  - timestamp (ISO 8601)
  - level (INFO, WARNING, ERROR)
  - message
  - request_id (correlation)
  - transaction_id
  - latency_ms
  - status_code
  - tier
  - is_fallback
- What to figure out: Log retention (30 days? 90 days for compliance?)
- Document: Logging configuration

**Component 2: Custom Metrics to CloudWatch**
- Requirements: Publish application metrics to CloudWatch
- Library: boto3 CloudWatch client
- Namespace: FraudDetection
- Metrics to publish:
  - FraudDetectionsPerMinute
  - AverageResponseTime
  - ErrorRate
  - ModelCost (dollars per hour)
  - CircuitBreakerState
  - CurrentTier
- Publishing frequency: Every 60 seconds (batched)
- What to figure out: CloudWatch costs (custom metrics pricing)
- Document: Metric publishing requirements

**Component 3: Container Insights**
- Requirements: Enable ECS Container Insights
- Provides:
  - CPU utilization per task
  - Memory utilization per task
  - Network I/O
  - Disk I/O
- Automatic dashboards in CloudWatch
- What to figure out: Additional cost of Container Insights
- Document: Container Insights setup

**Component 4: CloudWatch Logs Insights Queries**
- Requirements: Pre-built queries for troubleshooting
- Queries to create:

**Query 1: Error Logs (Last Hour)**
```
fields @timestamp, level, message, transaction_id
| filter level = "ERROR"
| sort @timestamp desc
| limit 100
```

**Query 2: Slowest Requests (P99)**
```
fields @timestamp, endpoint, latency_ms, transaction_id
| stats max(latency_ms) as p99_latency by endpoint
| sort p99_latency desc
```

**Query 3: Fraud Detections per Hour**
```
fields @timestamp, result
| filter result in ["suspicious", "legitimate"]
| stats count() by result, bin(@timestamp, 1h)
```

**Query 4: Failed Health Checks**
```
fields @timestamp, message
| filter endpoint = "/health" and status_code != 200
| sort @timestamp desc
```

**Query 5: 5xx Errors by Endpoint**
```
fields @timestamp, endpoint, status_code, message
| filter status_code >= 500
| stats count() by endpoint, status_code
| sort count desc
```

- What to figure out: Most useful queries for on-call engineers
- Document: Saved queries

**Component 5: CloudWatch Dashboard**
- Requirements: Native CloudWatch dashboard
- Widgets:
  - ECS task count (line graph)
  - CPU utilization (stacked area)
  - Memory utilization (stacked area)
  - Log errors (number widget)
  - Custom metrics (line graphs)
- Purpose: Backup if Grafana down
- What to figure out: Which widgets most critical
- Document: CloudWatch dashboard requirements

**Success Criteria:**
- Logs flowing to CloudWatch
- JSON format validated
- Custom metrics published
- Container Insights enabled
- Logs Insights queries saved
- CloudWatch dashboard created
- Can query logs effectively

---

## DAY 5 (FRIDAY): Alert Configuration

**Time:** 1.5 hours

### SESSION: Multi-Tier Alerting (Requirements)

**Requirements:**

Configure comprehensive alerting system:

**Component 1: Alert Severity Levels**
- Requirements: Three-tier alerting
- Levels:

**Level 1: INFO (Dashboard Only)**
- Definition: Informational events
- Examples:
  - Service tier changed to Tier 2 (degraded)
  - Circuit breaker opened (expected behavior)
  - Cache hit rate below 80%
- Action: Display on dashboard, no notification
- Purpose: Awareness, not urgent

**Level 2: WARNING (Slack)**
- Definition: Requires attention soon
- Examples:
  - Error rate > 0.5% (approaching SLA)
  - Latency P95 > 1.5s (approaching SLA)
  - Cost > 110% of daily budget
  - Circuit breaker open for > 5 minutes
- Action: Slack message to #fraud-detection-alerts
- Response time: Within 1 hour
- Purpose: Fix before becomes critical

**Level 3: CRITICAL (PagerDuty)**
- Definition: Immediate action required
- Examples:
  - Availability < 99% (SLA violated)
  - Error rate > 1% (SLA violated)
  - All tasks down (service unavailable)
  - Multiple circuit breakers open
  - Cost > 150% of daily budget
- Action: Page on-call engineer
- Response time: Within 15 minutes
- Purpose: Service restoration

- What to figure out: Escalation policy
- Document: Severity levels

**Component 2: Prometheus Alert Rules**
- Requirements: Define alert rules in Prometheus

**Alert Rule Format:**
```yaml
groups:
- name: fraud_detection_alerts
  interval: 30s
  rules:
  - alert: <AlertName>
    expr: <PromQL query>
    for: <duration>
    labels:
      severity: <warning|critical>
    annotations:
      summary: <short description>
      description: <detailed description>
```

**Critical Alerts:**

**Alert 1: High Error Rate**
- Query: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.01`
- Duration: 5 minutes
- Severity: critical
- Summary: "Error rate exceeds 1% SLA"
- Description: "Error rate is {{ $value | humanizePercentage }} over last 5 minutes"

**Alert 2: Service Down**
- Query: `up{job="fraud-detection"} == 0`
- Duration: 1 minute
- Severity: critical
- Summary: "Fraud detection service is down"
- Description: "All tasks unreachable"

**Alert 3: High Latency**
- Query: `histogram_quantile(0.95, http_request_duration_seconds) > 2`
- Duration: 10 minutes
- Severity: critical
- Summary: "P95 latency exceeds 2s SLA"
- Description: "P95 latency is {{ $value }}s"

**Alert 4: Circuit Breaker Stuck Open**
- Query: `circuit_breaker_state{service="openai"} == 1`
- Duration: 10 minutes
- Severity: critical
- Summary: "OpenAI circuit breaker stuck open"
- Description: "Service degraded for > 10 minutes"

**Warning Alerts:**

**Alert 5: Elevated Error Rate**
- Query: `rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.005`
- Duration: 10 minutes
- Severity: warning
- Summary: "Error rate approaching SLA limit"
- Description: "Error rate is {{ $value | humanizePercentage }}"

**Alert 6: Elevated Latency**
- Query: `histogram_quantile(0.95, http_request_duration_seconds) > 1.5`
- Duration: 15 minutes
- Severity: warning
- Summary: "P95 latency elevated"
- Description: "P95 latency is {{ $value }}s"

**Alert 7: High Cost**
- Query: `rate(llm_cost_dollars_total[1h]) > 0.5`
- Duration: 30 minutes
- Severity: warning
- Summary: "LLM costs elevated"
- Description: "Cost rate is ${{ $value }}/hour"

**Alert 8: Low Cache Hit Rate**
- Query: `sum(rate(cache_hits_total[5m])) / (sum(rate(cache_hits_total[5m])) + sum(rate(cache_misses_total[5m]))) < 0.7`
- Duration: 20 minutes
- Severity: warning
- Summary: "Cache hit rate below 70%"
- Description: "Hit rate is {{ $value | humanizePercentage }}"

- What to figure out: Appropriate thresholds and durations
- Document: Alert rules

**Component 3: Alert Routing**
- Requirements: Send alerts to correct destination
- Routing logic:

**Alertmanager Configuration:**
```yaml
route:
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'slack-warnings'
  routes:
  - match:
      severity: critical
    receiver: 'pagerduty-critical'
  - match:
      severity: warning
    receiver: 'slack-warnings'
```

**Receivers:**
- slack-warnings: Webhook to Slack channel
- pagerduty-critical: PagerDuty integration key
- email-daily: Daily digest for INFO level

- What to figure out: Integration configurations
- Document: Routing rules

**Component 4: Alert Templates**
- Requirements: Clear, actionable alert messages
- Template for Slack:
```
🔴 CRITICAL: <alert name>
Service: Fraud Detection
Status: {{ status }}
Severity: {{ severity }}
Value: {{ value }}
Description: {{ description }}
Runbook: <link to runbook>
Dashboard: <link to Grafana dashboard>
```

- Template for PagerDuty:
```
Summary: <alert name>
Severity: critical
Details:
  - Service: Fraud Detection
  - Metric: {{ metric }}
  - Current Value: {{ value }}
  - Threshold: {{ threshold }}
  - Duration: {{ for }}
Runbook: <link>
```

- What to figure out: Most helpful alert information
- Document: Alert templates

**Component 5: Alert Deduplication**
- Requirements: Prevent alert spam
- Strategies:
  - Group by: alertname, severity (alerts for same issue grouped)
  - Group wait: 30s (wait for similar alerts)
  - Group interval: 5m (send grouped alerts together)
  - Repeat interval: 4h (don't repeat same alert for 4 hours)
- Purpose: Reduce noise, prevent fatigue
- What to figure out: Appropriate intervals
- Document: Deduplication strategy

**Component 6: Alert Silencing**
- Requirements: Temporarily mute alerts
- Use cases:
  - Planned maintenance (silence all alerts)
  - Known issue being worked (silence specific alert)
  - False positive (silence until fixed)
- Silencing rules:
  - By label (service=fraud-detection)
  - By alert name
  - By time window
- What to figure out: Silence approval process
- Document: Silencing procedures

**Component 7: Alert Testing**
- Requirements: Validate alerting works
- Tests:
  - Trigger high error rate → PagerDuty page received
  - Trigger high latency → Slack message received
  - Verify templates render correctly
  - Verify runbook links work
  - Test alert grouping
  - Test deduplication
- What to figure out: How to trigger test alerts
- Document: Testing procedures

**Success Criteria:**
- 8+ alert rules defined
- Critical alerts page on-call
- Warning alerts sent to Slack
- Templates clear and actionable
- Deduplication working
- Silencing configured
- All alerts tested
- Runbooks linked from alerts

---

## DAY 6 (SATURDAY): Performance Dashboard

**Time:** 2.5 hours

### SESSION: Build Performance Dashboard (Requirements)

**Requirements:**

Create comprehensive performance analysis dashboard:

**Component 1: Latency Deep Dive**
- Requirements: Detailed latency breakdown
- Visualizations needed:

**Panel 1: Request Latency Percentiles**
- Metrics: P50, P75, P90, P95, P99
- Time range: Last 6 hours
- Display: Multi-line graph
- Purpose: Identify tail latency issues

**Panel 2: Latency Heatmap**
- Metric: Request duration distribution over time
- Display: Heatmap (time on X, latency buckets on Y, color = count)
- Purpose: Spot latency spikes

**Panel 3: Component Latency Breakdown**
- Metrics: Time spent in each component
  - Request parsing: <5ms
  - Database query: 10-50ms
  - LLM API call: 1000-2000ms
  - Rule evaluation (fallback): <5ms
  - Response serialization: <5ms
- Display: Stacked bar chart
- Purpose: Identify bottleneck (usually LLM)

**Panel 4: Latency by Endpoint**
- Metrics: P95 latency per endpoint
- Display: Bar chart, sorted by slowest
- Purpose: Find slow endpoints

- What to figure out: How to measure component-level latency
- Document: Latency panels

**Component 2: Cost Analysis**
- Requirements: Identify cost optimization opportunities

**Panel 5: Cost per Transaction Trend**
- Metric: Total cost / Total transactions (daily)
- Display: Line graph over 30 days
- Target line: $0.04 per transaction
- Purpose: Track cost efficiency

**Panel 6: Model Cost Comparison**
- Metrics: Cost per call for GPT-4 vs GPT-3.5
- Display: Bar chart
- Calculation: Total cost / Total calls per model
- Purpose: Justify model routing

**Panel 7: Most Expensive Queries**
- Metric: From LangSmith, top 10 queries by cost
- Display: Table with query ID, cost, tokens, timestamp
- Purpose: Find outliers to optimize

**Panel 8: Savings from Optimizations**
- Metrics: Calculate savings from:
  - Model routing (GPT-3.5 vs GPT-4)
  - Caching (cache hits × avg cost)
  - Fallback (rule-based vs LLM)
- Display: Pie chart showing savings breakdown
- Purpose: Demonstrate ROI of optimizations

- What to figure out: How to calculate potential savings
- Document: Cost analysis panels

**Component 3: LLM Performance**
- Requirements: Optimize LLM usage

**Panel 9: Token Efficiency**
- Metrics: Tokens per query (prompt + completion)
- Display: Histogram
- Insights: Identify prompts with excessive tokens
- Purpose: Optimize prompt length

**Panel 10: Model Selection Effectiveness**
- Metrics: % of queries routed to each model
- Display: Pie chart (GPT-4: 20%, GPT-3.5: 80%)
- Purpose: Validate routing strategy

**Panel 11: LLM Error Rate by Model**
- Metrics: Errors per model
- Display: Table
- Purpose: Identify problematic models

**Panel 12: Time to First Token**
- Metric: Latency until LLM starts streaming
- Display: Line graph (P95)
- Purpose: Track LLM responsiveness

- What to figure out: Optimal token usage per query type
- Document: LLM performance panels

**Component 4: Database Performance**
- Requirements: Monitor database bottlenecks

**Panel 13: Query Execution Time**
- Metric: Database query duration (P95)
- Display: Line graph
- Threshold: 100ms
- Purpose: Detect slow queries

**Panel 14: Connection Pool Usage**
- Metrics: Active, idle, total connections
- Display: Stacked area chart
- Threshold: Max pool size
- Purpose: Detect connection leaks

**Panel 15: Top Slow Queries**
- Metric: From CloudWatch RDS logs
- Display: Table of queries > 500ms
- Purpose: Identify queries to optimize

**Panel 16: Database CPU Utilization**
- Metric: From CloudWatch RDS
- Display: Line graph
- Purpose: Detect database overload

- What to figure out: How to correlate app queries with RDS metrics
- Document: Database panels

**Component 5: Cache Performance**
- Requirements: Evaluate cache effectiveness

**Panel 17: Cache Hit Rate**
- Metric: cache_hits / (cache_hits + cache_misses)
- Display: Gauge (target: > 80%)
- Purpose: Track cache effectiveness

**Panel 18: Cache Latency**
- Metrics: Redis GET latency (P95)
- Display: Line graph
- Expected: < 5ms
- Purpose: Detect Redis performance issues

**Panel 19: Cache Size**
- Metric: Redis memory usage
- Display: Line graph
- Purpose: Plan cache capacity

**Panel 20: Cache Eviction Rate**
- Metric: Rate of cache evictions
- Display: Line graph
- Purpose: Determine if cache too small

- What to figure out: Optimal cache configuration
- Document: Cache performance panels

**Component 6: Business Impact Analysis**
- Requirements: Connect performance to business outcomes

**Panel 21: Revenue Impact of Latency**
- Calculation: Estimate revenue lost due to slow responses
- Assumption: 100ms delay = 1% conversion drop
- Display: Stat panel showing daily revenue impact
- Purpose: Justify performance investments

**Panel 22: Fraud Detection Effectiveness vs Cost**
- Metrics: Detection rate vs cost per detection
- Display: Scatter plot (X = cost, Y = detection rate)
- Purpose: Optimize cost-effectiveness

**Panel 23: Tier Impact Analysis**
- Metrics: Compare metrics by tier
  - Tier 1: Accuracy 95%, Cost $0.045
  - Tier 2: Accuracy 85%, Cost $0.002
- Display: Table
- Purpose: Understand degradation trade-offs

**Panel 24: Optimization Opportunities**
- Calculation: List top 5 optimization opportunities
- Examples:
  - Reduce prompt length in fraud checks: $200/day savings
  - Increase cache TTL: $50/day savings
  - Route more queries to GPT-3.5: $300/day savings
- Display: Table ranked by impact
- Purpose: Prioritize optimizations

- What to figure out: How to calculate business impact
- Document: Business impact panels

**Component 7: Real-Time Monitoring**
- Requirements: Live performance tracking

**Panel 25: Real-Time Request Rate**
- Metric: Requests per second (refreshing every 1s)
- Display: Number panel with sparkline
- Purpose: Monitor live traffic

**Panel 26: Live Latency**
- Metric: P95 latency (last 1 minute)
- Display: Number panel with color coding
- Purpose: Immediate performance visibility

**Panel 27: Active Circuit Breakers**
- Metric: Count of open circuit breakers
- Display: Stat panel (0 = green, 1+ = red)
- Purpose: Quick health check

**Panel 28: Current Tier**
- Metric: service_tier gauge
- Display: Stat panel with tier name
- Purpose: Know degradation state

- What to figure out: Optimal refresh rate (1s? 5s?)
- Document: Real-time panels

**Success Criteria:**
- Performance dashboard created
- 28 panels configured
- All metrics flowing
- Latency breakdown visible
- Cost analysis complete
- Optimization opportunities identified
- Real-time monitoring working
- Dashboard actionable for engineers

---

## DAY 7 (SUNDAY): Week Summary

**Time:** 2 hours

### SESSION: Documentation & Week Summary (Requirements)

**Requirements:**

Create comprehensive monitoring documentation:

**Document 1: Monitoring Runbook**
- Requirements: Operations guide for monitoring stack
- Sections:
  1. Monitoring architecture overview
  2. What each tool does (LangSmith, Prometheus, Grafana, CloudWatch)
  3. How to access dashboards
  4. How to read metrics
  5. Common troubleshooting scenarios
  6. How to create custom metrics
  7. How to modify dashboards
  8. Alert investigation procedures
- Audience: On-call engineers, new team members
- What to figure out: Most common support questions
- Document: MONITORING_RUNBOOK.md

**Document 2: Dashboard Guide**
- Requirements: Explain each dashboard's purpose
- For each of 6 dashboards:
  - Purpose: What questions does it answer?
  - When to use: What scenarios?
  - Key panels: Most important visualizations
  - Interpretation: How to read it
  - Action items: What to do based on data
- Examples:
  - Service Health → Use for health checks, key panels are uptime/tier/circuit breakers
  - Cost Tracking → Use for budget reviews, key panel is daily cost trend
- What to figure out: Dashboard usage patterns
- Document: DASHBOARD_GUIDE.md

**Document 3: Metrics Catalog**
- Requirements: Document all metrics
- For each metric:
  - Name: fraud_detections_total
  - Type: Counter
  - Labels: result, tier
  - Purpose: Track fraud detection outcomes
  - Queries: Example PromQL queries
  - Alerts: Which alerts use this metric
- Total: 15+ metrics documented
- What to figure out: Complete metric inventory
- Document: METRICS_CATALOG.md

**Document 4: Alert Response Procedures**
- Requirements: What to do when alert fires
- For each alert:
  - Alert name
  - Severity
  - What it means
  - Immediate actions
  - Investigation steps
  - Resolution procedures
  - Escalation path
- Example:
  - "High Error Rate" → Check error logs, identify cause, rollback if recent deploy, escalate if unresolved in 30 min
- What to figure out: Detailed response procedures
- Document: ALERT_RESPONSE_GUIDE.md

**Document 5: Week 25 Summary**
- Requirements: Comprehensive week summary
- Sections:

**What You Built:**
- LangSmith tracing (100% LLM call visibility)
- Prometheus metrics (15+ custom metrics)
- Grafana dashboards (6 comprehensive dashboards)
- CloudWatch integration (logs + metrics + insights)
- Multi-tier alerting (INFO → WARNING → CRITICAL)
- Cost tracking ($0.038/transaction visibility)
- Performance analysis (latency breakdown, optimization opportunities)

**Fintech Impact - CRITICAL:**
- **Regulatory Compliance:** 90-day audit trail (SOX, Basel III, GDPR)
- **Cost Control:** $7.2K/month savings identified (73% reduction)
- **Performance Debugging:** Reduced MTTR from 3 days → 5 minutes
- **Fraud Detection:** Track accuracy degradation in real-time
- **SLA Monitoring:** Prove 99.9% uptime to auditors

**Technical Achievements:**
- Observability: 100% LLM calls traced with full context
- Metrics: 15+ Prometheus metrics + CloudWatch integration
- Dashboards: 6 Grafana dashboards with 70+ panels
- Alerting: 8+ alert rules with multi-tier routing
- Cost Tracking: Per-query cost visibility
- Performance: Latency breakdown by component
- Optimization: Identified $7.2K/month savings

**Cost Savings Identified:**
- Prompt optimization: $200/day (reduce token usage)
- Model routing: $300/day (GPT-3.5 vs GPT-4)
- Cache improvements: $50/day (increase hit rate)
- Total potential: $550/day = $16.5K/month savings

**Interview Talking Points:**
- Story 1: "Implemented comprehensive observability stack with LangSmith, Prometheus, and Grafana, reducing MTTR from 3 days to 5 minutes through detailed LLM tracing and component-level latency breakdown"
- Story 2: "Built cost tracking dashboard that identified $16.5K/month optimization opportunities, achieving 73% cost reduction through prompt optimization and intelligent model routing"
- Story 3: "Designed multi-tier alerting system with PagerDuty integration, ensuring 99.9% uptime SLA through proactive monitoring and automated incident response"
- Story 4: "Created 90-day audit trail with LangSmith for regulatory compliance (SOX, Basel III), capturing every LLM decision with full prompt and response context"

- What to document: Complete achievements, fintech impact, cost analysis
- Document: WEEK25_SUMMARY.md

**Optimization Roadmap:**
- Requirements: Next steps for monitoring improvements
- Improvements identified:
  1. **Distributed Tracing:** Add Jaeger for multi-service traces (Java → Python)
  2. **Synthetic Monitoring:** Proactive testing with cron jobs
  3. **Anomaly Detection:** ML-based alerting (detect unusual patterns)
  4. **Log Analysis:** Advanced pattern detection with AI
  5. **Cost Forecasting:** Predict next month's costs
- Prioritization: Impact vs effort
- What to figure out: Which improvements provide most value
- Document: Roadmap in summary

**Success Criteria:**
- 5 documents created (runbook, guide, catalog, alerts, summary)
- Week summary comprehensive
- Fintech impact quantified ($16.5K/month savings)
- Technical achievements documented
- Interview stories prepared (STAR format)
- Optimization roadmap defined
- Ready for Week 26

---

## 📚 ADDITIONAL RESOURCES

**LangSmith:**
- Documentation: https://docs.smith.langchain.com/
- Tracing Guide: https://docs.smith.langchain.com/tracing

**Prometheus:**
- Documentation: https://prometheus.io/docs/
- Query Examples: https://prometheus.io/docs/prometheus/latest/querying/examples/
- Best Practices: https://prometheus.io/docs/practices/

**Grafana:**
- Documentation: https://grafana.com/docs/
- Dashboard Best Practices: https://grafana.com/docs/grafana/latest/best-practices/
- PromQL Guide: https://grafana.com/blog/2020/02/04/introduction-to-promql-the-prometheus-query-language/

**CloudWatch:**
- Logs Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html
- Custom Metrics: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html
- Container Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html

**Alerting:**
- Alertmanager: https://prometheus.io/docs/alerting/latest/alertmanager/
- PagerDuty Integration: https://www.pagerduty.com/docs/guides/prometheus-integration-guide/

---

## ✅ WEEK 25 DELIVERABLES

**Documentation:**
- LANGSMITH_SETUP.md - LangSmith integration requirements
- PROMETHEUS_METRICS.md - Metrics catalog
- GRAFANA_DASHBOARDS.md - Dashboard requirements (6 dashboards)
- CLOUDWATCH_INTEGRATION.md - CloudWatch setup requirements
- ALERT_CONFIGURATION.md - Alert rules and routing
- MONITORING_RUNBOOK.md - Operations guide
- DASHBOARD_GUIDE.md - Dashboard usage guide
- METRICS_CATALOG.md - Complete metric inventory
- ALERT_RESPONSE_GUIDE.md - Alert procedures
- WEEK25_SUMMARY.md - Week summary

**Requirements Specifications (No Code):**
- LangSmith tracing requirements (metadata, cost tracking)
- Prometheus metrics (15+ metrics documented)
- Grafana dashboards (6 dashboards, 70+ panels)
- CloudWatch integration (logs, metrics, queries)
- Alert rules (8+ alerts with routing)
- Performance dashboard (28 panels)

**Dashboard Designs:**
- Service Health dashboard design
- Application Metrics dashboard design
- Business KPIs dashboard design
- Cost Tracking dashboard design
- SLA Monitoring dashboard design
- Performance Analysis dashboard design

**Understanding:**
- LLM observability importance
- Prometheus metrics collection
- Grafana visualization
- CloudWatch integration
- Multi-tier alerting
- Cost optimization through monitoring
- Performance debugging techniques

---

## 🎯 SUCCESS CRITERIA

**By end of Week 25:**

**Conceptual:**
- Understand LLM observability needs
- Know Prometheus metric types
- Understand dashboard design principles
- Know alert severity levels
- Understand cost tracking methodology

**Practical:**
- LangSmith tracing requirements documented
- 15+ Prometheus metrics defined
- 6 Grafana dashboards designed (70+ panels)
- CloudWatch integration requirements specified
- 8+ alert rules configured
- Performance analysis dashboard designed
- Cost savings opportunities identified ($16.5K/month)

**Portfolio Impact:**
- ✅ Production observability demonstrated (FINTECH CRITICAL)
- ✅ Regulatory compliance (90-day audit trail for SOX/Basel III)
- ✅ Cost optimization ($16.5K/month savings identified)
- ✅ MTTR reduction (3 days → 5 minutes)
- ✅ SLA monitoring (prove 99.9% uptime)
- ✅ Performance debugging (component-level latency breakdown)

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Audit trail + cost control mandatory for banking  
**Cost Savings Identified:** $16.5K/month (73% reduction)  
**Next Week:** CI/CD Pipeline (Week 26)