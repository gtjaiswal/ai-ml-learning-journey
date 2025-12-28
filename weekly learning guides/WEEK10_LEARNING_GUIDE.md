# WEEK 10 LEARNING GUIDE: Production Features & System Hardening

**Pre-learning for Steps 21-24 (Production Improvements)**

**Time Investment:** 4-5 hours over the weekend before Week 10

---

## LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **Redis & Caching** - Caching strategies and Redis fundamentals
2. **Structured Logging** - JSON logging and observability patterns
3. **Rate Limiting** - Protecting APIs from abuse
4. **Error Handling** - Production-grade exception management
5. **System Observability** - Monitoring and debugging production systems

**Goal:** Transform your RAG system from prototype to production-ready

---

## WHAT YOU ALREADY KNOW (from Weeks 3-9)

[CHECK] **Weeks 3-5 (MOAI Weeks 1-2):**
- Docker, PostgreSQL, FastAPI fundamentals
- Airflow orchestration
- PDF parsing and data ingestion

[CHECK] **Weeks 7-9 (MOAI Weeks 3-5):**
- OpenSearch and BM25 search
- RAG system architecture
- Semantic search with embeddings
- Hybrid search strategies
- LLM integration with Ollama
- Gradio web interface

**You now have:**
- Working search system
- Automated data pipeline
- RAG capabilities with LLM
- Functional web interface
- End-to-end RAG system

**Week 10 Focus:**
Making your system **production-ready**:
- Performance optimization with caching
- Observability through structured logging
- Security with rate limiting
- Reliability through error handling

---

## LEARNING SCHEDULE

### **Saturday/Sunday Before Week Starts (4-5 hours)**

**Recommended pre-learning:**
- Redis fundamentals (1 hour)
- Caching patterns (1 hour)
- Structured logging (1 hour)
- Rate limiting algorithms (1 hour)
- Error handling patterns (1 hour)

### **During Week (as needed)**

**Monday-Tuesday:**
- Redis commands reference (30 min)
- Cache invalidation strategies (30 min)

**Wednesday-Thursday:**
- Logging configuration (30 min)
- Rate limiting tuning (30 min)

**Friday:**
- Production deployment checklist (1 hour)

---

## CORE LEARNING MODULES

### **MODULE 1: Redis & Caching Fundamentals** [TIME] 75 minutes

#### **1.1 What is Redis?** (25 min)

**Video:**
[VIDEO] **"Redis in 100 Seconds"** - Fireship  
URL: https://www.youtube.com/watch?v=G1rOthIU-uo  
Watch: Full video (2 min)

[VIDEO] **"Redis Crash Course"** - Traversy Media  
URL: https://www.youtube.com/watch?v=jgpVdJB2sKQ  
Watch: First 20 minutes (basics and use cases)

**What is Redis:**
- In-memory data store
- Key-value database
- Extremely fast (microsecond latency)
- Supports complex data structures
- Built-in persistence options

**Why Redis for caching:**
```
Without caching:
User query -> OpenSearch -> Embedding API -> LLM -> 15 seconds

With caching:
User query (same as before) -> Redis -> 50ms (300x faster!)
```

**Redis vs Other Caching:**

```
Redis                    Memcached              In-Memory Dict
-----                    ---------              --------------
[CHECK] Persistent       [X] Not persistent     [X] Lost on restart
[CHECK] Data structures  [X] Only strings       [CHECK] Any Python object
[CHECK] Atomic ops       [CHECK] Atomic ops     [X] Not thread-safe
[CHECK] Built-in expire  [CHECK] Built-in       [X] Manual cleanup
[CHECK] Clustering       [CHECK] Clustering     [X] Single process
```

**For production:** Redis is industry standard

**Reading:**
[BOOK] **"Introduction to Redis"** - Redis Docs  
URL: https://redis.io/docs/about/  
Read: Introduction and data types (10 min)

#### **1.2 Redis Data Structures** (25 min)

**1. Strings (Most Common for Caching):**
```
Key: "search_results:transformers_ml"
Value: '{"papers": [...], "count": 5}'

Operations:
SET key value          # Store
GET key               # Retrieve
SETEX key 3600 value  # Store with expiration (1 hour)
DEL key               # Delete
```

**2. Hashes (Structured Data):**
```
Key: "paper:2304.12345"
Fields:
  title: "Attention Is All You Need"
  authors: "Vaswani et al."
  year: "2017"

Operations:
HSET key field value  # Set field
HGET key field        # Get field
HGETALL key          # Get all fields
```

**3. Lists (Ordered Collections):**
```
Key: "recent_queries"
Values: ["transformers", "BERT", "GPT", ...]

Operations:
LPUSH key value      # Add to beginning
RPUSH key value      # Add to end
LRANGE key 0 9       # Get first 10
```

**4. Sets (Unique Collections):**
```
Key: "user:123:categories"
Members: {"cs.AI", "cs.LG", "cs.CL"}

Operations:
SADD key member      # Add member
SMEMBERS key         # Get all members
SISMEMBER key member # Check existence
```

**For RAG caching:** Strings with JSON are sufficient

**Reading:**
[BOOK] **"Redis Data Types"** - Redis Docs  
URL: https://redis.io/docs/data-types/  
Read: Strings section (10 min)

#### **1.3 Caching Strategies** (25 min)

**Cache-Aside (Lazy Loading):**
```
Flow:
1. Check cache for key
2. If found (cache hit) -> return cached value
3. If not found (cache miss):
   - Query database
   - Store in cache
   - Return value

Pros: Only cache what's used
Cons: First request slow (cache miss)
```

**Write-Through:**
```
Flow:
1. Write to cache
2. Write to database
3. Return success

Pros: Cache always up-to-date
Cons: Slower writes
```

**Write-Behind (Write-Back):**
```
Flow:
1. Write to cache
2. Return success immediately
3. Asynchronously write to database

Pros: Fast writes
Cons: Risk of data loss
```

**For RAG:** Cache-aside is best (read-heavy workload)

**TTL (Time-To-Live):**
```
Search results: 1 hour (3600 seconds)
- Queries don't change frequently
- Balance freshness vs performance

Embeddings: 7 days (604800 seconds)
- Expensive to regenerate
- Content rarely changes

LLM responses: 15 minutes (900 seconds)
- Balance between speed and freshness
- Queries might evolve
```

**Cache Invalidation:**

When to invalidate:
1. New papers added -> Clear search caches
2. Paper deleted -> Clear that paper's caches
3. Embeddings regenerated -> Clear embedding caches

**Reading:**
[BOOK] **"Caching Strategies"** - AWS  
URL: https://aws.amazon.com/caching/best-practices/  
Read: Cache-aside pattern (10 min)

---

### **MODULE 2: Structured Logging** [TIME] 60 minutes

#### **2.1 Why Structured Logging?** (20 min)

**Traditional Logging (Unstructured):**
```
2025-12-28 10:30:45 User asked question about transformers
2025-12-28 10:30:46 Search returned 5 results
2025-12-28 10:30:47 LLM generated answer in 15.2 seconds
```

**Problems:**
- Hard to parse programmatically
- Can't aggregate metrics easily
- Difficult to filter and search
- No context correlation

**Structured Logging (JSON):**
```json
{
  "timestamp": "2025-12-28T10:30:45Z",
  "level": "INFO",
  "event": "search_query",
  "user_id": "user_123",
  "query": "transformers",
  "results_count": 5,
  "duration_ms": 245,
  "trace_id": "abc-123-def"
}
```

**Benefits:**
- [CHECK] Machine-readable (JSON)
- [CHECK] Easy to search and filter
- [CHECK] Aggregate metrics (avg duration, count by event)
- [CHECK] Correlate across requests (trace_id)
- [CHECK] Integrate with monitoring tools

**Video:**
[VIDEO] **"Structured Logging Best Practices"**  
URL: https://www.youtube.com/results?search_query=structured+logging+best+practices  
Watch: Any comprehensive overview (15 min)

#### **2.2 Log Levels and Events** (20 min)

**Standard Log Levels:**

**DEBUG:** Detailed diagnostic information
```json
{
  "level": "DEBUG",
  "event": "cache_lookup",
  "key": "search:transformers",
  "hit": true
}
```

**INFO:** General informational messages
```json
{
  "level": "INFO",
  "event": "search_completed",
  "query": "transformers",
  "results": 5,
  "duration_ms": 245
}
```

**WARNING:** Something unexpected but recoverable
```json
{
  "level": "WARNING",
  "event": "slow_query",
  "query": "transformers",
  "duration_ms": 2500,
  "threshold_ms": 1000
}
```

**ERROR:** Error occurred, needs attention
```json
{
  "level": "ERROR",
  "event": "llm_generation_failed",
  "error": "timeout",
  "query": "transformers",
  "attempts": 3
}
```

**CRITICAL:** System-level failure
```json
{
  "level": "CRITICAL",
  "event": "database_connection_lost",
  "database": "postgresql",
  "retry_count": 5
}
```

**Event Types for RAG:**
- search_query
- cache_hit / cache_miss
- embedding_generated
- llm_request / llm_response
- error_occurred
- slow_query

**Reading:**
[BOOK] **"Python Logging Best Practices"**  
URL: https://docs.python.org/3/howto/logging.html  
Read: Basic and Advanced tutorials (15 min)

#### **2.3 Logging in Production** (20 min)

**What to Log:**

**DO log:**
- Request parameters (query, top_k, model)
- Response metadata (duration, results_count)
- Performance metrics (latency, cache hit rate)
- Errors and exceptions
- Resource usage (memory, CPU trends)
- Business metrics (searches per day, popular queries)

**DON'T log:**
- Sensitive data (API keys, passwords)
- Full LLM responses (too verbose, use summary)
- Personal user information (unless required and encrypted)
- Binary data (embeddings, PDF content)

**Log Aggregation:**

For production, send logs to:
- CloudWatch (AWS)
- Datadog
- Elasticsearch + Kibana (ELK stack)
- Grafana Loki

**For learning:** File-based logging is sufficient

**Log Rotation:**
```
logs/
  app.log           # Current
  app.log.1         # Yesterday
  app.log.2         # 2 days ago
  ...
  app.log.7         # 7 days ago (then deleted)
```

**Reading:**
[BOOK] **"Structured Logging in Python"** - structlog  
URL: https://www.structlog.org/en/stable/  
Read: Why and Getting Started (10 min)

---

### **MODULE 3: Rate Limiting** [TIME] 60 minutes

#### **3.1 Why Rate Limiting?** (20 min)

**The Problem:**

Without rate limiting:
```
Malicious user:
for i in range(10000):
    requests.post("/api/v1/ask", json={"query": "test"})

Result:
- Your API server crashes
- Costs spike (LLM API calls)
- Legitimate users affected
```

**The Solution:** Rate limiting

```
Limit: 10 requests per minute per user

Request 1-10: [CHECK] Allowed
Request 11: [X] Denied (429 Too Many Requests)
After 60 seconds: Reset, allow 10 more
```

**Benefits:**
- [CHECK] Prevent abuse
- [CHECK] Control costs (LLM calls expensive)
- [CHECK] Fair resource allocation
- [CHECK] Protect infrastructure
- [CHECK] Improve reliability

**Video:**
[VIDEO] **"Rate Limiting Explained"**  
URL: https://www.youtube.com/results?search_query=rate+limiting+explained  
Watch: Any clear explanation (10 min)

#### **3.2 Rate Limiting Algorithms** (25 min)

**1. Fixed Window:**
```
Minute 1 (00:00-00:59): 10 requests allowed
Minute 2 (01:00-01:59): 10 requests allowed

Problem: Burst at window boundary
- Request 10 at 00:59
- Request 11 at 01:00
- 20 requests in 2 seconds!
```

**2. Sliding Window:**
```
Track: Last 60 seconds continuously

At 01:30, count requests from 00:30-01:30
At 01:35, count requests from 00:35-01:35

Better: No boundary burst
```

**3. Token Bucket (Best for APIs):**
```
Bucket: Holds 10 tokens
Refill: 1 token per 6 seconds (10 per minute)

Request arrives:
- If token available: Remove token, allow request
- If bucket empty: Deny request (429)

Allows: Bursts up to bucket size
Smooths: Over time, averages to refill rate
```

**4. Leaky Bucket:**
```
Bucket: Queue of requests
Leak: Process N requests per second

Incoming faster than leak: Queue fills
Queue full: Deny new requests

Smooths: Perfectly constant output rate
```

**For RAG:** Token bucket is best (allows bursts, easy to implement)

**Reading:**
[BOOK] **"Rate Limiting Strategies"** - Kong  
URL: https://konghq.com/blog/how-to-design-a-scalable-rate-limiting-algorithm  
Read: Token bucket section (10 min)

#### **3.3 Rate Limiting in Practice** (15 min)

**Per-User Limits:**
```
Free tier: 10 requests/minute
Premium: 100 requests/minute
Enterprise: 1000 requests/minute
```

**Per-Endpoint Limits:**
```
/api/v1/search: 60 requests/minute (cheap)
/api/v1/ask: 10 requests/minute (expensive, uses LLM)
/api/v1/stream: 5 requests/minute (very expensive)
```

**Response Headers:**
```
X-RateLimit-Limit: 10           # Total allowed
X-RateLimit-Remaining: 7         # Remaining this window
X-RateLimit-Reset: 1672531200    # Unix timestamp when reset
Retry-After: 45                  # Seconds until retry allowed
```

**Error Response:**
```json
{
  "error": "rate_limit_exceeded",
  "message": "Rate limit of 10 requests per minute exceeded",
  "retry_after": 45
}
```

**Storage:** Use Redis
- Fast
- Atomic operations
- Built-in expiration
- Distributed (multiple servers can share state)

**Reading:**
[BOOK] **"Rate Limiting with Redis"**  
URL: https://redis.io/glossary/rate-limiting/  
Read: Implementation patterns (10 min)

---

### **MODULE 4: Error Handling & Custom Exceptions** [TIME] 60 minutes

#### **4.1 Exception Hierarchy** (20 min)

**Python Exception Hierarchy:**
```
BaseException
  ├─ SystemExit
  ├─ KeyboardInterrupt
  └─ Exception
      ├─ ValueError
      ├─ TypeError
      ├─ HTTPException (FastAPI)
      └─ Your Custom Exceptions
```

**Why Custom Exceptions:**

Bad:
```python
# ANTI-PATTERN - DON'T DO THIS

raise Exception("Paper not found")
raise Exception("LLM timeout")
raise Exception("Rate limit exceeded")

# All look the same, hard to handle differently
```

Good:
```python
# REQUIREMENTS ONLY

# Custom exception hierarchy needed:
# - RAGException (base)
#   - SearchException
#     - PaperNotFoundException
#     - SearchTimeoutException
#   - LLMException
#     - LLMTimeoutException
#     - LLMUnavailableException
#   - RateLimitException

# Each exception type can be caught and handled appropriately
```

**Benefits:**
- Specific error handling
- Clear error semantics
- Better logging
- Client-friendly error messages

**Video:**
[VIDEO] **"Python Custom Exceptions"**  
URL: https://www.youtube.com/results?search_query=python+custom+exceptions  
Watch: Any tutorial (15 min)

#### **4.2 Error Handling Patterns** (20 min)

**Pattern 1: Try-Except-Else-Finally**
```python
# REQUIREMENTS ONLY

# Structure needed:
# try:
#     Attempt operation
# except SpecificException:
#     Handle specific error
# except AnotherException:
#     Handle another error
# else:
#     Runs if no exception
# finally:
#     Always runs (cleanup)
```

**Pattern 2: Context Managers**
```python
# REQUIREMENTS ONLY

# For resource cleanup:
# - Database connections
# - File handles
# - Redis connections

# Context manager ensures cleanup even if error occurs
```

**Pattern 3: Retry with Backoff**
```python
# REQUIREMENTS ONLY

# For transient failures:
# - Network errors
# - Service temporarily unavailable
# - Rate limits

# Retry strategy:
# 1. First retry: Wait 1 second
# 2. Second retry: Wait 2 seconds
# 3. Third retry: Wait 4 seconds
# 4. Give up, raise exception

# Exponential backoff prevents overwhelming service
```

**Pattern 4: Circuit Breaker**
```python
# REQUIREMENTS ONLY

# For cascading failures:
# If service fails repeatedly:
# 1. Open circuit (stop calling service)
# 2. Wait timeout period
# 3. Try again (half-open)
# 4. If success, close circuit
# 5. If failure, open again

# Prevents wasting resources on failing service
```

**Reading:**
[BOOK] **"Exception Handling Best Practices"** - Real Python  
URL: https://realpython.com/python-exceptions/  
Read: Custom exceptions section (10 min)

#### **4.3 HTTP Status Codes** (20 min)

**Success Codes:**
- **200 OK:** Request succeeded
- **201 Created:** Resource created successfully
- **204 No Content:** Success, no data to return

**Client Error Codes (4xx):**
- **400 Bad Request:** Invalid input (validation failed)
- **401 Unauthorized:** Missing or invalid authentication
- **403 Forbidden:** Authenticated but not authorized
- **404 Not Found:** Resource doesn't exist
- **422 Unprocessable Entity:** Validation error (Pydantic)
- **429 Too Many Requests:** Rate limit exceeded

**Server Error Codes (5xx):**
- **500 Internal Server Error:** Unexpected server error
- **502 Bad Gateway:** Upstream service error
- **503 Service Unavailable:** Service temporarily down
- **504 Gateway Timeout:** Upstream timeout

**For RAG Endpoints:**

```
/api/v1/ask endpoint status codes:

200: Answer generated successfully
400: Invalid query (empty, too long)
422: Pydantic validation failed
429: Rate limit exceeded
500: Unexpected error
503: LLM service unavailable
504: LLM timeout
```

**Error Response Format:**
```json
{
  "error": {
    "code": "llm_timeout",
    "message": "LLM service timed out after 30 seconds",
    "details": {
      "query": "What are transformers?",
      "timeout_seconds": 30
    }
  }
}
```

**Reading:**
[BOOK] **"HTTP Status Codes"** - MDN  
URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status  
Read: 4xx and 5xx sections (10 min)

---

### **MODULE 5: System Observability** [TIME] 45 minutes

#### **5.1 Metrics to Track** (15 min)

**Performance Metrics:**
- Request latency (p50, p95, p99)
- Throughput (requests per second)
- Error rate (% of failed requests)
- Cache hit rate (% of requests served from cache)

**Resource Metrics:**
- CPU usage (%)
- Memory usage (MB)
- Disk I/O (ops/sec)
- Network I/O (MB/sec)

**Business Metrics:**
- Searches per day
- Popular queries (top 10)
- Average papers per search
- LLM usage (tokens per day)

**Cost Metrics:**
- LLM API costs ($ per day)
- Infrastructure costs
- Cache savings ($ saved)

#### **5.2 Monitoring Tools** (15 min)

**For Learning (Simple):**
- File-based logging
- Grafana + Prometheus (self-hosted)
- Docker stats

**For Production:**
- CloudWatch (AWS)
- Datadog (all-in-one)
- New Relic
- Grafana Cloud

**Key Dashboards Needed:**
1. System Health (CPU, memory, errors)
2. API Performance (latency, throughput)
3. Cache Performance (hit rate, savings)
4. Business Metrics (searches, costs)

#### **5.3 Alerting** (15 min)

**Alert Conditions:**
- Error rate >5% for 5 minutes
- p95 latency >5 seconds
- Cache hit rate <50%
- LLM availability <95%
- Disk usage >80%

**Alert Channels:**
- Email
- Slack
- PagerDuty (critical)
- SMS (critical only)

**For learning:** Simple email alerts sufficient

---

## HANDS-ON EXERCISES

### **Exercise 1: Cache Key Design**

**Task:** Design cache keys for these scenarios:

1. Search results for query "transformers"
2. Embedding for text chunk "Our approach uses..."
3. LLM response for question "What is BERT?"

**Requirements:**
- Keys must be unique
- Keys must be descriptive
- Keys must support invalidation

**Expected format:**
```
search:[query_hash]:[top_k]:[use_hybrid]
embedding:[text_hash]:[model]:[task]
llm:[query_hash]:[model]:[temperature]
```

---

### **Exercise 2: Log Event Design**

**Task:** Design JSON log event for successful search

**Requirements:**
- Include all relevant fields
- Use appropriate log level
- Add correlation ID for tracing
- Include performance metrics

**Expected structure:**
```json
{
  "timestamp": "...",
  "level": "INFO",
  "event": "search_completed",
  "trace_id": "...",
  "query": "...",
  "results_count": 5,
  "duration_ms": 245,
  "cache_hit": false
}
```

---

### **Exercise 3: Rate Limit Calculation**

**Task:** Token bucket with 10 tokens, refill 1 per 6 seconds

**Scenario:**
- t=0s: 5 requests arrive
- t=10s: 8 requests arrive
- t=20s: 4 requests arrive

**Questions:**
1. How many requests allowed at each time?
2. How many tokens in bucket at t=0, t=10, t=20?
3. Which requests are denied?

**Calculation:**
```
t=0s: Start with 10 tokens
  5 requests -> Use 5 tokens
  Remaining: 5 tokens
  Allowed: All 5 requests

t=10s: 10 seconds passed
  Refilled: 10/6 = 1.67 tokens (round down to 1)
  Bucket: 5 + 1 = 6 tokens
  8 requests -> Use 6 tokens, deny 2
  Remaining: 0 tokens
  Allowed: 6/8 requests

t=20s: 10 seconds passed
  Refilled: 1 token
  Bucket: 0 + 1 = 1 token
  4 requests -> Use 1 token, deny 3
  Remaining: 0 tokens
  Allowed: 1/4 requests
```

---

## RESEARCH QUESTIONS

### **Conceptual Questions:**

1. **Why cache?**
   - What problem does caching solve?
   - What are the tradeoffs?

2. **When NOT to cache?**
   - What data shouldn't be cached?
   - When does caching hurt performance?

3. **What is structured logging?**
   - How is it different from print statements?
   - What makes it "structured"?

4. **Why rate limit?**
   - What attacks does it prevent?
   - What are the tradeoffs?

5. **What is a token bucket?**
   - How does it allow bursts?
   - Why better than fixed window?

6. **What makes a good exception hierarchy?**
   - How specific should exceptions be?
   - When to create custom exceptions?

### **Practical Questions:**

1. **How do you choose TTL?**
   - What factors matter?
   - How to tune over time?

2. **How do you invalidate cache?**
   - When to clear cache?
   - How to avoid stale data?

3. **What should you log?**
   - What's too much logging?
   - What's too little?

4. **How do you set rate limits?**
   - How to balance protection vs usability?
   - How to handle legitimate bursts?

5. **How do you handle errors gracefully?**
   - Which errors to retry?
   - Which to fail fast?

6. **How do you debug production issues?**
   - What logs to check first?
   - How to correlate events?

---

## KEY TAKEAWAYS

**Remember these 10 things:**

1. **Redis = In-memory cache**
   - Microsecond latency
   - 100-300x faster than database
   - Industry standard for caching

2. **Cache-aside = Lazy loading**
   - Check cache first
   - Query database on miss
   - Store in cache for next time

3. **TTL = Time-To-Live**
   - How long to keep cached data
   - Balance freshness vs performance
   - Search: 1 hour, Embeddings: 7 days

4. **Structured logging = JSON logs**
   - Machine-readable
   - Easy to search and aggregate
   - Essential for production

5. **Log levels matter**
   - DEBUG: Development
   - INFO: Normal operations
   - WARNING: Unexpected but handled
   - ERROR: Needs attention

6. **Rate limiting = Protection**
   - Prevent abuse
   - Control costs
   - Fair resource allocation

7. **Token bucket = Best algorithm**
   - Allows bursts
   - Smooth average rate
   - Easy to implement with Redis

8. **Custom exceptions = Clarity**
   - Specific error handling
   - Better debugging
   - Client-friendly messages

9. **HTTP status codes communicate intent**
   - 200: Success
   - 400: Client error
   - 500: Server error
   - 429: Rate limited

10. **Observability = Production requirement**
    - Log everything important
    - Track key metrics
    - Alert on anomalies

**If you understand these 10:** Production-ready! [CHECK]

---

## ADDITIONAL RESOURCES (Optional Deep Dives)

### **Redis:**
- Redis University: https://university.redis.com/
- Redis Commands Cheat Sheet: https://redis.io/commands/
- Redis Persistence: https://redis.io/docs/management/persistence/

### **Caching:**
- "Caching Best Practices" - AWS: https://aws.amazon.com/caching/
- Cache Invalidation Patterns: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/cache-invalidation.html

### **Logging:**
- Python Logging Cookbook: https://docs.python.org/3/howto/logging-cookbook.html
- structlog Documentation: https://www.structlog.org/
- ELK Stack Tutorial: https://www.elastic.co/guide/

### **Rate Limiting:**
- NGINX Rate Limiting: https://www.nginx.com/blog/rate-limiting-nginx/
- Redis Rate Limiting: https://redis.io/glossary/rate-limiting/
- Token Bucket Algorithm: https://en.wikipedia.org/wiki/Token_bucket

### **Observability:**
- Observability Engineering (book)
- Prometheus Getting Started: https://prometheus.io/docs/introduction/
- Grafana Tutorials: https://grafana.com/tutorials/

---

## AFTER LEARNING

### **You're ready to build Steps 21-24 when you can:**

**Knowledge Check:**
- [ ] Explain how Redis caching works
- [ ] Understand cache-aside pattern
- [ ] Choose appropriate TTL values
- [ ] Design structured log events
- [ ] Understand token bucket algorithm
- [ ] Create custom exception hierarchy
- [ ] Map errors to HTTP status codes
- [ ] Know what metrics to track

**Practical Check:**
- [ ] Can design cache keys
- [ ] Can invalidate cache appropriately
- [ ] Can structure JSON logs
- [ ] Can implement rate limiting concept
- [ ] Can handle errors gracefully
- [ ] Can debug with logs
- [ ] Can set up monitoring

**Then proceed to:**
- **STEP21_COMPLETE.md** - Redis caching layer
- **STEP22_COMPLETE.md** - Structured logging
- **STEP23_COMPLETE.md** - Rate limiting
- **STEP24_COMPLETE.md** - Error handling

---

## WEEK 10 SUCCESS METRICS

**By end of this week, you'll have:**
- [TARGET] Redis caching 150-400x speedup on repeated queries
- [TARGET] Structured JSON logging for all operations
- [TARGET] Token bucket rate limiting (10 req/min on /ask)
- [TARGET] Custom exception hierarchy
- [TARGET] Proper HTTP status codes
- [TARGET] Production-ready error handling
- [TARGET] Observable system with key metrics

**Performance Targets:**
- Cache hit rate: >60% after warm-up
- Cached query response: <100ms
- Log volume: <100MB per day
- Error rate: <1% of requests
- Rate limit accuracy: 100% enforcement

**Quality Targets:**
- All errors have appropriate status codes
- All operations logged with context
- Cache invalidation working correctly
- Rate limits protect system without UX impact

---

**Time estimate:** 4-5 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Total week time:** ~16-18 hours (learning + implementation)

---

**Document Generated:** December 28, 2025  
**For:** Career Transition Week 10 (MOAI Week 6)  
**Status:** Production Features - Ready for Steps 21-24  
**Format:** Clean ASCII - No Character Corruption
