# WEEK 23 LEARNING GUIDE: ECS Deployment + Java Integration

**Timeline:** April 20-26, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Docker optimization, AWS ECS deployment, Java-Python integration, blue-green deployment, monitoring

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Optimized Docker images (multi-stage builds)
- ECS Fargate deployment
- Java Spring Boot integration
- Blue-green deployment pipeline
- CloudWatch monitoring dashboards

**What You'll Learn:**
- Docker multi-stage build optimization
- AWS ECS/Fargate architecture
- Container orchestration concepts
- Java-Python REST integration
- Blue-green deployment strategy
- CloudWatch Logs and metrics
- System design for high-scale ML

**Fintech Application - CRITICAL:**

**The Business Problem:**
```
Legacy Banking Reality:
- Core Banking = Java/J2EE (20+ years old code)
- Payment Rails = Java Spring Boot
- Transaction Processing = Java
- Account Management = Java

ML Reality:
- scikit-learn = Python only
- PyTorch = Python only
- HuggingFace = Python only
- LangChain = Python only

The Dilemma:
- Can't rewrite Core Banking in Python (impossible - millions of lines, decades of business logic)
- Can't do ML in Java (weak ecosystem, no modern libraries)
- Must integrate Java backend with Python ML service

Banking Use Case:
Transaction comes in → Java Core Banking (validates, checks balance)
                    ↓
                  Fraud Check Needed
                    ↓
Java calls Python ML service via REST API
                    ↓
Python returns: {"fraud": true, "risk_score": 92, "reason": "unusual_location"}
                    ↓
Java decides: Block transaction or Allow with monitoring
```

**Why This Matters:**
- **90% of banks run Java Core Banking** (COBOL/Java legacy systems)
- **Python ML services must integrate with Java backends**
- **Developers who bridge legacy + modern = highly valuable**
- **Bilingual Java + Python = rare combination in ML market**

**The Solution - Hybrid Architecture:**
```
┌─────────────────────────────────────────┐
│  Java Spring Boot (Core Banking)       │
│  Port: 8080                             │
│  - Transaction validation               │
│  - Balance checks                       │
│  - Payment processing                   │
└─────────────┬───────────────────────────┘
              │
              │ REST API call
              │ POST /api/v1/predict
              │ {"transaction_id": "123", ...}
              │
              v
┌─────────────────────────────────────────┐
│  Python FastAPI (ML Service)            │
│  Port: 8000                             │
│  - Fraud detection (GPT-4)              │
│  - Risk scoring                         │
│  - RAG for policy lookup                │
└─────────────────────────────────────────┘

Deployed on:
- Java: Separate ECS service (or EC2)
- Python: ECS Fargate (this week's focus)
- Communication: Internal VPC network
```

**Week 23 Achieves:**
1. Containerize Python ML service (FastAPI)
2. Deploy to AWS ECS Fargate (production-grade)
3. Integrate with Java Spring Boot (REST API)
4. Blue-green deployment (zero downtime)
5. CloudWatch monitoring (observability)

---

## DAY 1 (MONDAY): Docker Multi-Stage Builds

**Time:** 1.5 hours

### SESSION 1: Docker Optimization Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "Docker Multi-Stage Builds Explained" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=zpkqNPwEzac
- Duration: 10:24
- Focus: Why multi-stage, size reduction, security

**Reading:**
- "Docker Multi-Stage Builds" - Docker Documentation
- URL: https://docs.docker.com/build/building/multi-stage/
- Duration: 20 min
- Focus: Best practices, examples

**What You Need to Understand:**

**The Problem - Fat Docker Images:**
```
Single-Stage Build Problems:
1. Size: 1.2 GB image (includes build tools, dev dependencies, tests)
2. Security: Includes gcc, make, pip (attack surface)
3. Slow: Takes 5 minutes to pull/push
4. Cost: More storage, more bandwidth

What's in a fat image:
- Python 3.11 (400 MB)
- Build tools: gcc, make, g++ (200 MB)
- Dev dependencies: pytest, black, mypy (100 MB)
- All pip cache (300 MB)
- Source code (50 MB)
- Compiled packages (150 MB)
Total: 1.2 GB
```

**The Solution - Multi-Stage Builds:**
```
Two-Stage Approach:

Stage 1: Builder (temporary)
- Full Python with build tools
- Install all dependencies
- Compile packages
- Run tests
- This stage is DISCARDED

Stage 2: Runtime (final image)
- Slim Python (no build tools)
- Copy only compiled packages from Stage 1
- Copy only application code
- No pip cache, no tests, no build tools
- Result: 400 MB (67% reduction)
```

**Key Concepts:**

**Base Image Selection:**
- python:3.11 = 1GB (full Debian, all tools)
- python:3.11-slim = 400 MB (minimal Debian)
- python:3.11-alpine = 150 MB (Alpine Linux, smaller but compatibility issues)
- **Recommendation:** python:3.11-slim (good balance)

**Layer Caching:**
- Each Dockerfile instruction = new layer
- Layers are cached if unchanged
- Order matters: least-changing first, most-changing last
- Best practice: Copy requirements.txt first, then code

**Security Best Practices:**
- Run as non-root user (create app user)
- Don't include secrets in image
- Minimize installed packages
- Use specific version tags (not :latest)

### SESSION 2: Build Optimized Dockerfile (45 min)

**Requirements:**

Create production-optimized Dockerfile for FastAPI ML service:

**Component 1: Multi-Stage Structure**
- Requirements: Two stages (builder + runtime)
- Stage 1 name: builder
- Stage 2: Final image (unnamed)
- What to figure out: What to copy from builder to runtime
- Document: Stage responsibilities

**Component 2: Builder Stage**
- Requirements: Install all dependencies, compile packages
- Base image: python:3.11 (full, includes build tools)
- Actions needed:
  - Set working directory /app
  - Copy requirements.txt
  - Install dependencies with pip
  - Copy source code
  - (Optional) Run tests
- What to figure out: Which pip flags to use (--no-cache-dir?)
- Document: Builder stage purpose

**Component 3: Runtime Stage**
- Requirements: Minimal production image
- Base image: python:3.11-slim
- Actions needed:
  - Create non-root user "appuser"
  - Set working directory /app
  - Copy installed packages from builder stage
  - Copy application code
  - Switch to appuser
  - Expose port 8000
  - Set health check
- What to figure out: Where are packages installed in builder? (/usr/local/lib/python3.11/site-packages)
- Document: Runtime stage requirements

**Component 4: Layer Optimization**
- Requirements: Minimize layers, maximize caching
- Order: Base image → System packages → Requirements → Code
- Why: requirements.txt changes less than code
- Cache benefit: Code change doesn't rebuild dependencies
- What to figure out: Optimal instruction order
- Document: Layer caching strategy

**Component 5: Environment Configuration**
- Requirements: Externalize all configuration
- No hardcoded: Database URLs, API keys, Environment (prod/dev)
- Method: Environment variables
- What to figure out: Which variables needed (DATABASE_URL, OPENAI_API_KEY, etc.)
- Document: Required environment variables

**Component 6: Health Check**
- Requirements: Container health monitoring
- Endpoint: GET /health
- Interval: Every 30 seconds
- Timeout: 5 seconds
- Retries: 3 failures = unhealthy
- What to figure out: What health check should verify (API responsive? Database connected?)
- Document: Health check implementation

**Component 7: Security Hardening**
- Requirements: Minimize attack surface
- Create appuser: UID 1000, non-root
- File permissions: appuser owns /app directory
- No secrets in image: Use environment variables or AWS Secrets Manager
- What to figure out: How to create user in Dockerfile
- Document: Security measures

**Success Criteria:**
- Two-stage Dockerfile created
- Image size < 500 MB (target: ~400 MB)
- Builds in < 2 minutes (with cache)
- Runs as non-root user
- Health check configured
- No secrets in image

---

## DAY 2 (TUESDAY): AWS ECS Fundamentals

**Time:** 1.5 hours

### SESSION 1: ECS Architecture (45 min)

**Learning Resources:**

**Video:**
- "AWS ECS Tutorial for Beginners" - Stephane Maarek
- URL: https://www.youtube.com/watch?v=esISkPlnxL0
- Duration: 18:46
- Focus: ECS concepts, Fargate vs EC2

**Reading:**
- "Amazon ECS Documentation - What is ECS"
- URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- Duration: 20 min
- Focus: Core concepts, architecture

**What You Need to Understand:**

**ECS Core Concepts:**

**1. Cluster:**
- Logical grouping of tasks/services
- Can span multiple Availability Zones
- Your cluster: fraud-detection-cluster

**2. Task Definition:**
- Blueprint for your application
- Like a Dockerfile but for ECS
- Specifies: Container image, CPU/memory, Environment variables, IAM roles
- Versioned: task-definition:1, task-definition:2

**3. Task:**
- Running instance of task definition
- Ephemeral (can be stopped/started)
- Gets private IP address
- Multiple containers can run in one task

**4. Service:**
- Manages tasks (ensures N tasks always running)
- Integrates with load balancer
- Auto-scaling capability
- Handles task failures (restarts automatically)

**5. Fargate vs EC2:**

**Fargate (Serverless):**
- AWS manages servers
- You specify CPU/memory
- Pay per task (by CPU/memory/duration)
- Easier, less operational overhead
- **Your choice:** Fargate

**EC2 Launch Type:**
- You manage EC2 instances
- More control
- Potentially cheaper at scale
- More operational overhead

**ECS Architecture for Fraud Detection:**
```
┌─────────────────────────────────────────┐
│  Application Load Balancer (ALB)       │
│  Port: 443 (HTTPS)                      │
└─────────────┬───────────────────────────┘
              │
              │ Routes to healthy targets
              │
┌─────────────┴───────────────────────────┐
│  ECS Service: fraud-detection           │
│  Desired count: 2 tasks                 │
│  Min: 2, Max: 10                        │
└─────────────┬───────────────────────────┘
              │
              ├──────────────┬──────────────┐
              │              │              │
         Task 1          Task 2         Task 3
         (AZ-1)          (AZ-2)         (AZ-3)
         
Each task:
- Container: fraud-detection:latest
- CPU: 0.5 vCPU
- Memory: 1 GB
- Port: 8000
```

**Networking:**
- VPC: fraud-detection-vpc
- Subnets: 3 public subnets (one per AZ)
- Security Group: Allow 8000 from ALB only
- Tasks get private IPs (10.0.x.x)

**Scaling:**
- Target Tracking: Scale based on CPU
- Threshold: 70% CPU utilization
- Scale out: Add 1 task when CPU > 70% for 3 min
- Scale in: Remove 1 task when CPU < 50% for 5 min
- Min healthy: 50% during deployment

### SESSION 2: Cost Analysis (45 min)

**Requirements:**

Calculate and understand ECS costs:

**Component 1: Fargate Pricing**
- Requirements: Calculate monthly costs
- Pricing factors: vCPU hours, GB-hours, Data transfer
- Your configuration: 0.5 vCPU, 1 GB memory, 2 tasks (24/7)
- What to figure out: Actual AWS Fargate pricing (varies by region)
- Document: Cost calculation

**Pricing Calculation:**
```
Fargate Pricing (us-east-1 example):
- vCPU: $0.04048 per vCPU per hour
- Memory: $0.004445 per GB per hour

Per Task (0.5 vCPU, 1 GB):
- vCPU cost: 0.5 × $0.04048 = $0.02024/hour
- Memory cost: 1 × $0.004445 = $0.004445/hour
- Total per task: $0.024685/hour

2 Tasks (24/7):
- Hourly: 2 × $0.024685 = $0.04937
- Daily: $0.04937 × 24 = $1.185
- Monthly: $1.185 × 30 = $35.54

(Actual: Verify current AWS pricing)
```

**Component 2: Additional Costs**
- Requirements: Calculate total AWS costs
- ALB: ~$25/month (fixed + per LCU)
- Data transfer: ~$9/month (100 GB out)
- CloudWatch Logs: ~$5/month (10 GB ingestion)
- ECR: ~$0.10/month (storage)
- What to figure out: Estimate data transfer volume
- Document: Total monthly cost breakdown

**Component 3: Cost Optimization**
- Requirements: Strategies to reduce costs
- Fargate Spot: 70% cheaper (can be interrupted)
- Right-sizing: Test with 0.25 vCPU (cheaper)
- Reserved capacity: Not available for Fargate
- Schedule scaling: Scale to 0 during off-hours (if acceptable)
- What to figure out: Trade-offs for each strategy
- Document: Optimization recommendations

**Component 4: ROI Comparison**
- Requirements: Compare deployment options
- On-premises: ~$200/month (EC2 t3.medium 24/7 + ops time)
- EKS: ~$150/month (EKS cluster + Fargate tasks)
- ECS Fargate: ~$75/month (calculated above)
- Lambda: Not suitable (long-running ML inference)
- What to figure out: Hidden costs (engineer time, maintenance)
- Document: Cost comparison analysis

**Success Criteria:**
- Understand ECS architecture (cluster, service, task)
- Calculated monthly costs accurately
- Identified cost optimization strategies
- Can explain Fargate vs EC2 trade-offs
- Justified ECS Fargate choice

---

## DAY 3 (WEDNESDAY): ECS Deployment

**Time:** 1.5 hours

### SESSION 1: Task Definition (45 min)

**Requirements:**

Create ECS task definition for fraud detection service:

**Component 1: Task Definition Basics**
- Requirements: Configure task-level settings
- Family name: fraud-detection
- Launch type: FARGATE
- Network mode: awsvpc (required for Fargate)
- CPU: 512 (.5 vCPU)
- Memory: 1024 MB (1 GB)
- What to figure out: Minimum CPU/memory for your application
- Document: Task definition structure

**Component 2: Container Definition**
- Requirements: Configure container settings
- Container name: fraud-detection-container
- Image URI: {account-id}.dkr.ecr.us-east-1.amazonaws.com/fraud-detection:latest
- Port mapping: 8000 (container) → 8000 (host)
- Essential: true (task fails if this container stops)
- What to figure out: ECR repository URI format
- Document: Container configuration

**Component 3: Environment Variables**
- Requirements: Pass configuration to container
- Variables needed:
  - ENVIRONMENT (prod/staging/dev)
  - DATABASE_URL (RDS endpoint)
  - OPENAI_API_KEY (from Secrets Manager)
  - LOG_LEVEL (INFO/DEBUG)
- Method: Use AWS Secrets Manager for secrets
- What to figure out: How to reference Secrets Manager in task definition
- Document: Environment configuration

**Component 4: Logging Configuration**
- Requirements: Send logs to CloudWatch
- Log driver: awslogs
- Log group: /ecs/fraud-detection
- Stream prefix: ecs
- Retention: 30 days
- What to figure out: How to create log group first
- Document: Logging setup

**Component 5: IAM Roles**
- Requirements: Two roles needed
- Task Role: Permissions for application (access RDS, Secrets Manager, OpenAI API)
- Execution Role: Permissions for ECS (pull ECR image, write CloudWatch logs)
- What to figure out: Specific IAM policies for each role
- Document: IAM role requirements

**Component 6: Health Check**
- Requirements: Container health monitoring
- Command: curl -f http://localhost:8000/health || exit 1
- Interval: 30 seconds
- Timeout: 5 seconds
- Retries: 3
- Start period: 60 seconds (grace period for startup)
- What to figure out: How to install curl in container
- Document: Health check configuration

### SESSION 2: Service Creation (45 min)

**Requirements:**

Create ECS service with load balancer:

**Component 1: Service Configuration**
- Requirements: Define service parameters
- Service name: fraud-detection-service
- Cluster: fraud-detection-cluster
- Task definition: fraud-detection:1
- Desired count: 2 tasks
- Launch type: FARGATE
- Platform version: LATEST
- What to figure out: How to create cluster first
- Document: Service setup

**Component 2: Network Configuration**
- Requirements: VPC and subnet setup
- VPC: Create fraud-detection-vpc (10.0.0.0/16)
- Subnets: 3 public subnets across 3 AZs
  - us-east-1a: 10.0.1.0/24
  - us-east-1b: 10.0.2.0/24
  - us-east-1c: 10.0.3.0/24
- Security group: fraud-detection-sg
  - Allow inbound: 8000 from ALB security group
  - Allow outbound: 443 (HTTPS), 5432 (PostgreSQL)
- What to figure out: How to configure VPC with subnets
- Document: Network architecture

**Component 3: Load Balancer Integration**
- Requirements: Create ALB and integrate
- ALB name: fraud-detection-alb
- Scheme: Internet-facing
- Listeners: HTTPS (443)
- Target group: fraud-detection-tg
  - Protocol: HTTP
  - Port: 8000
  - Health check: /health endpoint
  - Healthy threshold: 2
  - Unhealthy threshold: 3
- What to figure out: How to get SSL certificate (ACM)
- Document: Load balancer setup

**Component 4: Auto-Scaling Policy**
- Requirements: Scale based on CPU
- Metric: Average CPU utilization
- Target value: 70%
- Scale-out cooldown: 300 seconds
- Scale-in cooldown: 300 seconds
- Min capacity: 2 tasks
- Max capacity: 10 tasks
- What to figure out: Appropriate CPU threshold for your app
- Document: Auto-scaling configuration

**Component 5: Deployment Configuration**
- Requirements: Rolling update settings
- Deployment type: Rolling update
- Minimum healthy percent: 50% (1 task must stay running)
- Maximum percent: 200% (can have 4 tasks during deployment)
- What to figure out: How long deployments take
- Document: Deployment strategy

**Component 6: Service Discovery (Optional)**
- Requirements: Enable service discovery for internal communication
- Namespace: fraud-detection.local
- Service name: api
- Full DNS: api.fraud-detection.local
- When to use: If Java service needs to discover Python service
- What to figure out: Whether you need service discovery
- Document: Service discovery setup

**Success Criteria:**
- Task definition created with all components
- ECS cluster created
- Service deployed with 2 running tasks
- Load balancer routing traffic to tasks
- Health checks passing
- Auto-scaling configured
- Can access service via ALB DNS

---

## DAY 4 (THURSDAY): Java Integration

**Time:** 1.5 hours

### SESSION 1: Spring Boot REST Client (45 min)

**Learning Resources:**

**Reading:**
- "Spring RestTemplate" - Spring Documentation
- URL: https://docs.spring.io/spring-framework/reference/integration/rest-clients.html
- Duration: 20 min
- Focus: RestTemplate, error handling

**What You Need to Understand:**

**Java-Python Integration Pattern:**
```
Java Spring Boot → HTTP REST → Python FastAPI

Request Flow:
1. Transaction arrives at Java Core Banking
2. Java validates business rules
3. Java needs fraud check
4. Java calls Python ML service via REST
5. Python returns fraud assessment
6. Java makes decision (approve/block)
7. Java continues transaction processing
```

**Why REST API:**
- Language agnostic (Java ↔ Python)
- Simple HTTP protocol
- Standard JSON format
- Easy to test and debug
- Can add authentication (OAuth)

### SESSION 2: Build Integration Layer (45 min)

**Requirements:**

Create Java client for Python ML service:

**Component 1: RestTemplate Configuration**
- Requirements: Configure HTTP client
- Bean: RestTemplate with timeouts
- Connection timeout: 5 seconds
- Read timeout: 30 seconds (ML inference takes time)
- Error handler: Custom error handler for 4xx/5xx
- What to figure out: Appropriate timeout values
- Document: RestTemplate setup

**Component 2: ML Service Client**
- Requirements: Service class for ML calls
- Class: MLServiceClient
- Method: FraudResponse predictFraud(FraudRequest request)
- Base URL: Configure from properties (http://ml-service:8000)
- Endpoint: POST /api/v1/predict
- What to figure out: How to inject base URL from application.properties
- Document: Client class structure

**Component 3: Request DTO**
- Requirements: Java object for ML service request
- Class: FraudRequest
- Fields needed:
  - String transactionId
  - Double amount
  - String merchantName
  - String location
  - String timestamp
  - String customerId
- Annotations: Jackson annotations for JSON serialization
- What to figure out: Field names (camelCase in Java, snake_case in Python?)
- Document: DTO definition

**Component 4: Response DTO**
- Requirements: Java object for ML service response
- Class: FraudResponse
- Fields needed:
  - Boolean isFraud
  - Integer riskScore (0-100)
  - List<String> riskFactors
  - String recommendation ("APPROVE", "BLOCK", "REVIEW")
- Validation: Validate risk score range
- What to figure out: How to handle missing fields gracefully
- Document: Response DTO definition

**Component 5: Error Handling**
- Requirements: Handle ML service failures gracefully
- Exceptions to handle:
  - RestClientException (network error)
  - HttpStatusCodeException (4xx/5xx errors)
  - ResourceAccessException (timeout)
- Fallback: Use rule-based fraud detection if ML service down
- What to figure out: When to retry vs fail immediately
- Document: Error handling strategy

**Component 6: REST Controller**
- Requirements: Expose endpoint in Java API
- Endpoint: POST /api/v1/fraud/analyze
- Request: TransactionRequest (from Java client)
- Flow: Validate → Call MLServiceClient → Return result
- Response: FraudAssessment (Java response object)
- What to figure out: How to map transaction to FraudRequest
- Document: Controller implementation requirements

**Component 7: Integration Testing**
- Requirements: Test Java-Python integration
- Tool: WireMock or Testcontainers
- Tests:
  - Successful fraud detection
  - ML service timeout
  - ML service returns error
  - Invalid JSON response
- What to figure out: How to mock Python service
- Document: Test strategy

**Success Criteria:**
- RestTemplate configured with timeouts
- MLServiceClient class created
- Request/Response DTOs defined
- Error handling implemented
- REST controller exposed
- Can call Python ML service from Java
- Integration tests passing

---

## DAY 5 (FRIDAY): Blue-Green Deployment

**Time:** 1 hour

### SESSION 1: Blue-Green Concept (30 min)

**Learning Resources:**

**Video:**
- "Blue-Green Deployment Explained" - AWS
- URL: https://www.youtube.com/watch?v=lYx0rvh0pZE
- Duration: 5:12
- Focus: Blue-green strategy, benefits

**Reading:**
- "Blue/Green Deployments on AWS" - AWS Architecture Blog
- URL: https://aws.amazon.com/blogs/compute/bluegreen-deployments-with-amazon-ecs/
- Duration: 15 min
- Focus: ECS implementation

**What You Need to Understand:**

**Traditional Deployment Problems:**
```
Rolling Update Issues:
1. Downtime: Service unavailable during deployment
2. Partial state: Old + new versions running simultaneously
3. Rollback: Difficult, must redeploy old version
4. Testing: Can't test new version in production before switch
```

**Blue-Green Solution:**
```
Two Environments:
┌─────────────────────────────────┐
│  BLUE (v1.0 - Current)          │
│  Receives 100% of traffic       │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│  GREEN (v2.0 - New)             │
│  Receives 0% of traffic         │
│  (Deploy and test here)         │
└─────────────────────────────────┘

After testing GREEN:
1. Switch traffic: BLUE 0% → GREEN 100%
2. Instant cutover (< 1 second)
3. If issues: Switch back instantly
4. Zero downtime deployment
```

**ECS Blue-Green with CodeDeploy:**
- Two target groups: BLUE and GREEN
- ALB routes traffic to active target group
- CodeDeploy manages traffic shifting
- Can do gradual shift (Canary) or instant (AllAtOnce)

**Fintech Recommendation:**
- Use Canary deployment
- 10% traffic to GREEN for 5 minutes
- If no errors, shift remaining 90%
- Allows testing with real traffic before full switch

### SESSION 2: Implement Blue-Green (30 min)

**Requirements:**

Configure blue-green deployment for ECS service:

**Component 1: CodeDeploy Application**
- Requirements: Create CodeDeploy resources
- Application: fraud-detection-app
- Compute platform: ECS
- Deployment group: fraud-detection-dg
- What to figure out: IAM role for CodeDeploy
- Document: CodeDeploy setup

**Component 2: Target Groups**
- Requirements: Two target groups for blue-green
- Blue TG: fraud-detection-blue
- Green TG: fraud-detection-green
- Both: Same health check (/health), Same protocol (HTTP:8000)
- What to figure out: How to attach both TGs to ALB
- Document: Target group configuration

**Component 3: Deployment Configuration**
- Requirements: Define traffic shifting strategy
- Options:
  - AllAtOnce: Instant 100% shift
  - Linear: 10% every N minutes
  - Canary: 10% then 90% (recommended)
- Your choice: CodeDeployDefault.ECSCanary10Percent5Minutes
- What to figure out: Appropriate wait time between shifts
- Document: Deployment strategy

**Component 4: AppSpec File**
- Requirements: Define deployment steps
- File: appspec.yaml
- Sections needed:
  - version: 0.0
  - Resources: ECS task definition
  - Hooks: AfterAllowTestTraffic (validation tests)
- What to figure out: What validation to run in hooks
- Document: AppSpec structure

**Component 5: Automatic Rollback**
- Requirements: Rollback on failure
- Triggers:
  - Deployment failure
  - CloudWatch alarm triggers (5xx errors spike)
  - Manual rollback
- Action: Switch traffic back to BLUE
- What to figure out: Which CloudWatch alarms to monitor
- Document: Rollback configuration

**Component 6: Deployment Pipeline**
- Requirements: Automated deployment flow
- Steps:
  1. Developer pushes code to GitHub
  2. GitHub Actions builds Docker image
  3. Push image to ECR
  4. Register new task definition
  5. CodeDeploy starts blue-green deployment
  6. Traffic shifts to GREEN
  7. BLUE kept running for rollback
- What to figure out: How long to keep BLUE alive
- Document: Deployment pipeline

**Success Criteria:**
- CodeDeploy application configured
- Two target groups created
- Blue-green deployment working
- Can deploy new version with zero downtime
- Automatic rollback on errors
- Tested rollback manually

---

## DAY 6 (SATURDAY): Monitoring & Logging

**Time:** 2.5 hours

### SESSION 1: CloudWatch Dashboards (90 min)

**Requirements:**

Create comprehensive monitoring dashboards:

**Dashboard 1: Service Health**
- Requirements: High-level service status
- Widgets needed:
  - ECS task count (running vs desired)
  - CPU utilization (per task + average)
  - Memory utilization (per task + average)
  - Network in/out (bytes)
  - Target health (ALB healthy hosts)
- Purpose: Quick health check
- What to figure out: Thresholds for alerts (CPU > 80%?)
- Document: Service health dashboard

**Dashboard 2: Application Metrics**
- Requirements: Application performance
- Widgets needed:
  - Request count (per minute)
  - Request latency (P50, P95, P99)
  - Error rate (4xx, 5xx)
  - Success rate (2xx)
- Data source: ALB access logs or custom metrics
- What to figure out: How to publish custom metrics
- Document: Application metrics dashboard

**Dashboard 3: Load Balancer Metrics**
- Requirements: ALB performance
- Widgets needed:
  - Target response time
  - Healthy/unhealthy target count
  - Request count per target group
  - HTTP status code distribution
- Purpose: Identify load balancer issues
- What to figure out: Normal response time baseline
- Document: ALB dashboard

**Dashboard 4: Cost Tracking**
- Requirements: Track AWS costs
- Widgets needed:
  - Fargate cost (daily)
  - Data transfer cost
  - CloudWatch costs
  - Total daily spend
- Data source: AWS Cost Explorer API
- What to figure out: How to set budget alerts
- Document: Cost dashboard

**Dashboard 5: Business Metrics**
- Requirements: Fraud detection specific
- Widgets needed:
  - Fraud detections per hour
  - Risk score distribution
  - Model latency (GPT-4 calls)
  - Circuit breaker state
- Data source: Custom CloudWatch metrics from application
- What to figure out: Which business metrics to track
- Document: Business metrics dashboard

### SESSION 2: Logging & Log Analysis (60 min)

**Requirements:**

Configure comprehensive logging:

**Component 1: Structured Logging**
- Requirements: JSON formatted logs
- Log format:
  - timestamp
  - level (INFO, ERROR, etc.)
  - message
  - request_id (trace requests)
  - user_id
  - endpoint
  - duration
- Benefits: Easy to query with CloudWatch Logs Insights
- What to figure out: How to configure JSON logging in Python
- Document: Log format specification

**Component 2: Log Groups Organization**
- Requirements: Separate log groups
- Structure:
  - /ecs/fraud-detection/application (app logs)
  - /ecs/fraud-detection/access (access logs from ALB)
  - /aws/ecs/fraud-detection-cluster (ECS agent logs)
- Retention: 30 days (configurable)
- What to figure out: Appropriate retention for compliance
- Document: Log group structure

**Component 3: CloudWatch Logs Insights Queries**
- Requirements: Pre-built queries for troubleshooting
- Queries needed:
  - Error logs (last hour)
  - Slowest requests (P99)
  - Fraud detections per hour
  - Failed health checks
  - 5xx errors by endpoint
- What to figure out: Most useful queries for on-call
- Document: Saved queries

**Component 4: Log-Based Metrics**
- Requirements: Extract metrics from logs
- Metric filters:
  - Count ERROR level logs → ErrorCount metric
  - Extract request duration → LatencyMetric
  - Count fraud detections → FraudDetectionCount
- Alarms: Alert when ErrorCount > 10 in 5 minutes
- What to figure out: How to create metric filters
- Document: Metric filters configuration

**Component 5: ALB Access Logs**
- Requirements: Enable ALB access logs
- Storage: S3 bucket (fraud-detection-alb-logs)
- Format: Space-delimited with request details
- Analysis: Athena queries for deep analysis
- What to figure out: S3 bucket policy for ALB
- Document: Access log setup

**Success Criteria:**
- 5 CloudWatch dashboards created
- Structured JSON logging implemented
- Log groups organized properly
- Logs Insights queries saved
- Metric filters configured
- ALB access logs enabled
- Can troubleshoot issues via logs

---

## DAY 7 (SUNDAY): System Design Exercise

**Time:** 2 hours

### SESSION 1: Design High-Scale System (90 min)

**Requirements:**

Design fraud detection system for 10,000 TPS (transactions per second):

**Component 1: Requirements Gathering**
- Requirements: Define system requirements
- Throughput: 10,000 TPS sustained
- Latency: P95 < 200ms
- Availability: 99.9% uptime
- Geographic: US, EU, APAC regions
- Data residency: EU data stays in EU (GDPR)
- What to figure out: Peak vs average load
- Document: System requirements

**Component 2: Architecture Design**
- Requirements: Multi-region, high-scale architecture
- Components needed:
  - API Gateway (rate limiting, throttling)
  - Java backend (transaction processing)
  - Python ML service (fraud detection)
  - Database (PostgreSQL + read replicas)
  - Cache (Redis for embeddings)
  - Message queue (SQS for async processing)
- What to figure out: Which components synchronous vs asynchronous
- Document: Architecture diagram

**Component 3: Scalability Calculations**
- Requirements: Calculate required resources
- Calculation:
  - 1 ECS task handles 100 TPS
  - 10,000 TPS needs 100 tasks
  - Add 20% headroom = 120 tasks
  - Across 3 AZs = 40 tasks per AZ
- Database: 10,000 TPS × 2 queries each = 20,000 QPS
  - Need read replicas + connection pooling
- What to figure out: Cost at this scale
- Document: Capacity planning

**Component 4: Latency Optimization**
- Requirements: Achieve P95 < 200ms
- Latency breakdown:
  - API Gateway: 5ms
  - Java processing: 20ms
  - ML service (GPT-4): 150ms (bottleneck!)
  - Database: 10ms
  - Total: 185ms (within budget)
- Optimizations:
  - Cache embeddings (save 50ms)
  - Async inference (return immediately, callback later)
  - Use GPT-3.5 for low-risk (100ms instead of 150ms)
- What to figure out: Which optimizations most effective
- Document: Latency budget

**Component 5: High Availability Strategy**
- Requirements: 99.9% uptime (8.76 hours downtime/year)
- Strategies:
  - Multi-AZ deployment (3 AZs)
  - Blue-green deployment (zero downtime deploys)
  - Health checks (remove unhealthy tasks)
  - Auto-scaling (handle load spikes)
  - Circuit breakers (prevent cascade failures)
- Database: RDS Multi-AZ (automatic failover)
- What to figure out: Recovery time objective (RTO)
- Document: HA architecture

**Component 6: Multi-Region Architecture**
- Requirements: Deploy in US, EU, APAC
- Strategy:
  - Separate ECS clusters per region
  - Separate databases per region (GDPR)
  - Route53 geolocation routing (user → nearest region)
  - Cross-region replication for reference data only
- What to figure out: How to handle global customers
- Document: Multi-region design

**Component 7: Security Architecture**
- Requirements: Enterprise security layers
- Layers:
  - WAF (rate limiting, SQL injection prevention)
  - VPC (private subnets for ECS tasks)
  - Security groups (least privilege)
  - IAM roles (task-level permissions)
  - Secrets Manager (no hardcoded credentials)
  - TLS encryption (in transit)
  - KMS encryption (at rest)
- What to figure out: Compliance requirements (PCI-DSS?)
- Document: Security controls

**Component 8: Cost Estimation**
- Requirements: Calculate monthly cost at scale
- Calculation:
  - 120 Fargate tasks × $35/month = $4,200
  - ALB × 3 regions = $75/month
  - RDS Multi-AZ × 3 = $450/month
  - Data transfer: $500/month
  - OpenAI API: $5,000/month (10K TPS × $0.04/call)
  - Total: ~$10,000-15,000/month
- What to figure out: Cost per transaction
- Document: Cost breakdown

### SESSION 2: Week Summary (30 min)

**Requirements:**

Create WEEK23_SUMMARY.md:

**Section 1: What You Built**
- Optimized Docker images (multi-stage, 67% size reduction)
- ECS Fargate deployment (production-grade container orchestration)
- Java-Python integration (REST API bridge)
- Blue-green deployment (zero downtime)
- CloudWatch monitoring (5 dashboards)
- System design (10K TPS architecture)
- Document: Complete deliverables

**Section 2: Fintech Impact - CRITICAL**
- Hybrid Architecture: Bridge legacy Java Core Banking with modern Python ML
- 90% of banks: Run Java backends, need Python ML integration
- Rare skill: Bilingual Java + Python developers highly valuable
- Production-grade: ECS deployment demonstrates enterprise readiness
- Zero downtime: Blue-green deployment meets banking SLA requirements
- Document: Market differentiation

**Section 3: Technical Achievements**
- Docker: 1.2 GB → 400 MB (67% reduction)
- ECS: Auto-scaling 2-10 tasks based on CPU
- Integration: Java Spring Boot ↔ Python FastAPI via REST
- Deployment: Blue-green with automatic rollback
- Monitoring: 5 CloudWatch dashboards, 20+ metrics
- System Design: 10K TPS architecture with 99.9% uptime
- Document: Technical metrics

**Section 4: Cost Analysis**
- Development: ~$75/month (2 Fargate tasks)
- Production (10K TPS): ~$10K-15K/month
- ROI: 62% savings vs on-premises ($200/month)
- Optimization: Fargate Spot could save 70%
- Document: Cost breakdown

**Section 5: Interview Talking Points**
- Story 1: "Implemented hybrid Java-Python architecture using REST API, enabling legacy Spring Boot banking system to leverage modern ML fraud detection"
- Story 2: "Optimized Docker images using multi-stage builds, reducing size by 67% and improving deployment speed by 3x"
- Story 3: "Deployed ML service to AWS ECS Fargate with blue-green deployment strategy, achieving zero-downtime releases"
- Story 4: "Designed 10,000 TPS fraud detection system across 3 regions with 99.9% uptime SLA and sub-200ms P95 latency"
- Document: STAR format stories

**Success Criteria:**
- Week summary comprehensive
- Fintech differentiation clear
- Technical achievements quantified
- Interview stories ready
- System design documented

---

## 📚 ADDITIONAL RESOURCES

**Docker:**
- Multi-Stage Builds: https://docs.docker.com/build/building/multi-stage/
- Best Practices: https://docs.docker.com/develop/dev-best-practices/
- Security: https://docs.docker.com/engine/security/

**AWS ECS:**
- ECS Documentation: https://docs.aws.amazon.com/ecs/
- Fargate: https://aws.amazon.com/fargate/
- Blue-Green: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html

**Spring Boot:**
- RestTemplate: https://docs.spring.io/spring-framework/reference/integration/rest-clients.html
- Error Handling: https://www.baeldung.com/spring-rest-template-error-handling

**CloudWatch:**
- Dashboards: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
- Logs Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html

**System Design:**
- AWS Architecture Center: https://aws.amazon.com/architecture/
- System Design Primer: https://github.com/donnemartin/system-design-primer

---

## ✅ WEEK 23 DELIVERABLES

**Documentation:**
- DOCKER_OPTIMIZATION.md - Multi-stage build requirements
- ECS_DEPLOYMENT.md - Task definition and service setup requirements
- JAVA_INTEGRATION.md - REST client requirements
- BLUEGREEN_DEPLOYMENT.md - Deployment strategy requirements
- MONITORING_GUIDE.md - CloudWatch dashboard requirements
- SYSTEM_DESIGN.md - 10K TPS architecture requirements
- WEEK23_SUMMARY.md - Week summary

**Implementation Requirements (No Code):**
- Dockerfile requirements (multi-stage structure, security, optimization)
- Task definition requirements (CPU/memory, logging, IAM roles)
- Service requirements (networking, auto-scaling, load balancer)
- Java client requirements (DTOs, error handling, timeouts)
- Blue-green requirements (target groups, deployment config)
- Dashboard requirements (5 dashboards, metrics to track)
- System design requirements (scalability, HA, security)

**Architecture Diagrams:**
- Docker multi-stage build flow
- ECS deployment architecture
- Java-Python integration flow
- Blue-green deployment process
- Multi-region system design
- Network topology

**Understanding:**
- Docker optimization techniques
- Container orchestration with ECS
- Blue-green deployment pattern
- Java-Python integration via REST
- CloudWatch monitoring strategies
- System design for high-scale ML

---

## 🎯 SUCCESS CRITERIA

**By end of Week 23:**

**Conceptual:**
- Understand Docker multi-stage builds
- Know ECS architecture (cluster, service, task)
- Understand blue-green deployment
- Know Java-Python integration patterns
- Understand high-scale system design principles

**Practical:**
- Create optimized Dockerfile (requirements documented)
- Deploy to ECS Fargate (task definition + service requirements)
- Integrate Java and Python via REST (client requirements)
- Configure blue-green deployment (CodeDeploy requirements)
- Build CloudWatch dashboards (metrics requirements)
- Design 10K TPS system (architecture requirements)

**Portfolio Impact:**
- ✅ Production deployment expertise (ECS/Fargate)
- ✅ Zero-downtime capability (blue-green)
- ✅ Java-Python hybrid architecture (FINTECH CRITICAL)
- ✅ System design competency (10K TPS)
- ✅ Cloud infrastructure mastery (AWS)
- ✅ Monitoring and observability (CloudWatch)

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Bridges legacy banking with modern ML  
**Next Week:** Circuit Breakers + Resilience Engineering (Week 24)