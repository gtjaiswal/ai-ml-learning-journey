# WEEK 23 LEARNING GUIDE: ECS Deployment + Java Integration

**Timeline:** April 20-26, 2026  
**Total Time:** ~11-12 hours  
**Focus:** AWS ECS/Fargate deployment, Docker optimization, Java Spring Boot integration, blue-green deployment

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Dockerized ML application with multi-stage builds
- AWS ECS/Fargate deployment
- Load balancer with auto-scaling
- Java Spring Boot integration layer
- Blue-green deployment pipeline
- Monitoring and logging infrastructure

**What You'll Learn:**
- Docker multi-stage builds for optimization
- AWS ECS/Fargate architecture
- Container orchestration fundamentals
- Load balancing and auto-scaling
- Java-Python REST integration
- Blue-green deployment strategies
- CloudWatch monitoring
- Cost optimization for containers

**Fintech Application - CRITICAL:**

**The Business Problem:**
```
Legacy Banking Architecture:
┌─────────────────────────────────────────────┐
│  Core Banking System (Java/Spring Boot)    │
│  - Transaction processing                   │
│  - Account management                       │
│  - Payment rails                            │
│  - ALL business logic in Java               │
└─────────────────────────────────────────────┘

AI/ML Challenge:
- Core Banking is Java (20+ years of code)
- ML libraries are Python (scikit-learn, PyTorch, HuggingFace)
- Can't rewrite Core Banking in Python (impossible)
- Can't do ML in Java (library ecosystem weak)

Solution: Hybrid Architecture
┌──────────────────┐        REST API        ┌──────────────────┐
│  Core Banking    │ ───────────────────>   │  ML Service      │
│  (Spring Boot)   │ <───────────────────   │  (FastAPI)       │
│  Port 8080       │     JSON Response      │  Port 8000       │
└──────────────────┘                        └──────────────────┘
     │                                              │
     │                                              │
     v                                              v
PostgreSQL                                   OpenSearch + Models
(transactions)                               (vectors, search)
```

**Why This Matters:**
- **Enterprise Reality:** 90% of banks run Java Core Banking systems
- **Integration Pattern:** Python ML services must integrate with Java backends
- **Your Advantage:** You know BOTH Java and Python (rare combination)
- **Market Value:** Developers who bridge legacy + modern = highly valuable
- **Deployment Need:** ML service needs production infrastructure (ECS)

**Week 23 Achieves:**
1. Containerize Python ML service (FastAPI)
2. Deploy to AWS ECS/Fargate (production-grade)
3. Integrate with Java Spring Boot application
4. Implement blue-green deployment (zero downtime)
5. Monitor with CloudWatch (observability)

---

## DAY 1 (MONDAY): Docker Multi-Stage Builds

**Time:** 1.5 hours

### SESSION 1: Docker Optimization Fundamentals (45 min)

**Learning Resources:**

**Video:**
- "Docker Multi-Stage Builds Explained" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=zpkqNPwEzac
- Duration: 12:45
- Focus: Multi-stage build concept, size reduction

**Reading:**
- "Best Practices for Writing Dockerfiles" - Docker Documentation
- URL: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Duration: 25 min
- Focus: Multi-stage builds, layer caching, security

**What You Need to Understand:**

**The Problem - Fat Docker Images:**
```dockerfile
# Bad: Single-stage build
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# Installs: pytest, dev tools, build dependencies
# Size: 1.2 GB (includes unnecessary dev dependencies)
```

**The Solution - Multi-Stage Builds:**
```dockerfile
# Good: Multi-stage build
# Stage 1: Builder (includes dev dependencies)
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime (production only)
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
# Size: 400 MB (67% smaller!)
```

**Multi-Stage Benefits:**
- **Size Reduction:** 1.2 GB → 400 MB (3x smaller)
- **Security:** No dev tools in production image
- **Speed:** Faster deployment, lower network transfer
- **Cost:** Lower storage, faster scaling

**Layer Caching Strategy:**
```dockerfile
# Optimize layer order for caching
FROM python:3.11-slim

# 1. Copy dependencies first (changes rarely)
COPY requirements.txt .
RUN pip install -r requirements.txt
# ↑ This layer cached until requirements.txt changes

# 2. Copy application code last (changes frequently)
COPY . .
# ↑ This layer rebuilds on every code change
# But previous layers reused from cache = faster builds
```

**Base Image Selection:**
- `python:3.11` (1 GB): Full Debian, all tools
- `python:3.11-slim` (150 MB): Minimal Debian, production-ready
- `python:3.11-alpine` (50 MB): Alpine Linux, very small but compatibility issues
- **Recommendation:** Use `python:3.11-slim` (best balance)

**Security Best Practices:**
- Run as non-root user
- Don't include secrets in image
- Scan for vulnerabilities
- Use official base images

### SESSION 2: Build Production Dockerfile (45 min)

**Requirements:**

Create optimized multi-stage Dockerfile for ML service:

**Component 1: Builder Stage**
- Requirements: Install all dependencies including build tools
- Base: python:3.11 (full image with compilers)
- Tasks: Copy requirements.txt, Install Python packages, Install system dependencies for ML libraries
- What to figure out: Which system packages needed (gcc, g++, etc.)
- Document: Build dependencies rationale

**Component 2: Runtime Stage**
- Requirements: Minimal production image
- Base: python:3.11-slim (150 MB vs 1 GB)
- Tasks: Copy installed packages from builder, Copy application code, Set non-root user, Expose port
- What to figure out: How to copy only necessary files
- Document: Runtime optimization

**Component 3: Security Hardening**
- Requirements: Run as non-root, no secrets in image
- Tasks: Create app user (UID 1000), Set ownership correctly, Use .dockerignore for secrets
- What to figure out: Proper file permissions
- Document: Security measures

**Component 4: Health Check**
- Requirements: Container health monitoring
- Endpoint: GET /health returns 200 OK
- Frequency: Every 30 seconds
- What to figure out: Timeout and retry values
- Document: Health check configuration

**Component 5: Environment Configuration**
- Requirements: Externalize all configuration
- Method: Environment variables (not hardcoded)
- Examples: DATABASE_URL, OPENAI_API_KEY, MODEL_PATH
- What to figure out: Which configs need to be external
- Document: Environment variables list

**Dockerfile Template:**
```dockerfile
# Stage 1: Builder
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy application code
COPY ./app ./app

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and Test:**
```bash
# Build image
docker build -t fraud-detection-ml:latest .

# Check image size
docker images fraud-detection-ml

# Run container
docker run -p 8000:8000 fraud-detection-ml:latest

# Test health endpoint
curl http://localhost:8000/health
```

**Success Criteria:**
- Image builds successfully
- Size < 500 MB (multi-stage optimization)
- Runs as non-root user
- Health check passes
- Application accessible on port 8000
- No secrets in image layers

---

## DAY 2 (TUESDAY): AWS ECS Fundamentals

**Time:** 1.5 hours

### SESSION 1: ECS Architecture (45 min)

**Learning Resources:**

**Video:**
- "AWS ECS Explained" - Be A Better Dev
- URL: https://www.youtube.com/watch?v=I9VAMGEjW-Q
- Duration: 17:30
- Focus: ECS concepts, Fargate vs EC2, task definitions

**Reading:**
- "What is Amazon ECS?" - AWS Documentation
- URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- Duration: 20 min
- Focus: ECS components, architecture patterns

**What You Need to Understand:**

**ECS Core Concepts:**

**1. Cluster:**
- Logical grouping of tasks/services
- Can run on Fargate (serverless) or EC2 (you manage)
- Your cluster: `fraud-detection-cluster`

**2. Task Definition:**
- Blueprint for your application (like Dockerfile++)
- Defines: Container image, CPU/memory, Environment variables, Networking, IAM role
- Version controlled (task-def:1, task-def:2, etc.)
- Your task: `fraud-detection-task`

**3. Task:**
- Running instance of task definition
- Ephemeral (can be stopped/started)
- Like: Container instance

**4. Service:**
- Manages multiple tasks (desired count)
- Ensures tasks keep running (restarts on failure)
- Integrates with load balancer
- Your service: `fraud-detection-service`

**5. Fargate vs EC2:**

**Fargate (Serverless):**
- ✅ AWS manages servers (no EC2 to maintain)
- ✅ Pay per task (per-second billing)
- ✅ Auto-scaling built-in
- ✅ No server patching/maintenance
- ❌ Slightly more expensive per hour
- **Use for:** Most applications, especially starting out

**EC2 (You manage servers):**
- ✅ More control over instances
- ✅ Cheaper at very high scale
- ❌ You manage EC2 instances (patching, scaling)
- ❌ More complex setup
- **Use for:** Very large scale (100+ tasks)

**Recommendation:** Start with Fargate (your Week 23 approach)

**Architecture Diagram:**
```
Internet
   │
   v
Application Load Balancer (ALB)
   │
   ├─────────┬─────────┬─────────┐
   v         v         v         v
ECS Service (3 tasks across 3 AZs)
   │         │         │
   v         v         v
Fargate    Fargate   Fargate
Task 1     Task 2     Task 3
(Container)(Container)(Container)
```

**Networking:**
- VPC: Your own private network in AWS
- Subnets: Divide VPC by availability zone
- Security Groups: Firewall rules (allow port 8000)
- Load Balancer: Distributes traffic across tasks

**Scaling:**
- Target tracking: Keep CPU at 70% (scale up/down automatically)
- Min tasks: 2 (high availability)
- Max tasks: 10 (cost limit)
- CloudWatch triggers: Scale based on custom metrics

### SESSION 2: ECS Cost Estimation (45 min)

**Requirements:**

Calculate monthly AWS costs:

**Cost Component 1: Fargate Compute**
- Requirements: Calculate task compute costs
- Pricing (us-east-1): vCPU: $0.04048/hour, Memory: $0.004445/GB/hour
- Your task: 0.5 vCPU, 1 GB memory
- Calculation: (0.5 × $0.04048) + (1 × $0.004445) = $0.024685/hour per task
- 2 tasks running 24/7: 2 × $0.024685 × 730 hours = $36.04/month
- What to figure out: Right-size CPU/memory for workload
- Document: Fargate cost breakdown

**Cost Component 2: Application Load Balancer**
- Requirements: Load balancer in front of ECS
- Pricing: ALB: $0.0225/hour = $16.43/month, LCU: $0.008/hour (traffic-based)
- Estimate: ~$25/month for low-medium traffic
- What to figure out: LCU consumption based on requests/second
- Document: Load balancer costs

**Cost Component 3: Data Transfer**
- Requirements: Outbound traffic from AWS
- Pricing: First 1 GB free, Next 9.999 TB: $0.09/GB
- Estimate: 100 GB/month = $9/month
- What to figure out: Actual traffic volume
- Document: Data transfer costs

**Cost Component 4: CloudWatch Logs**
- Requirements: Application and container logs
- Pricing: Ingestion: $0.50/GB, Storage: $0.03/GB/month
- Estimate: 10 GB logs/month = $5.30/month
- What to figure out: Log retention period
- Document: Logging costs

**Cost Component 5: ECR (Container Registry)**
- Requirements: Store Docker images
- Pricing: Storage: $0.10/GB/month
- Estimate: 3 images × 0.5 GB = $0.15/month (negligible)
- What to figure out: Image retention policy
- Document: Registry costs

**Total Monthly Cost:**
```
Fargate (2 tasks):          $36.04
Load Balancer:              $25.00
Data Transfer:              $9.00
CloudWatch Logs:            $5.30
ECR:                        $0.15
────────────────────────────────
TOTAL:                      $75.49/month
```

**Cost Optimization Strategies:**
- Use Fargate Spot (70% cheaper, but can be interrupted)
- Right-size tasks (don't over-provision CPU/memory)
- Reduce log verbosity (less CloudWatch ingestion)
- Use S3 for log archival (cheaper than CloudWatch storage)
- Scale to zero during off-hours if possible

**ROI Comparison:**
- On-premises server: $200/month (EC2 t3.medium + maintenance)
- Managed Kubernetes (EKS): $150/month (cluster + nodes)
- ECS Fargate: $75/month (serverless, no maintenance)
- **Savings:** 62% vs on-premises, 50% vs EKS

**Success Criteria:**
- All 5 cost components calculated
- Total monthly cost estimated
- Optimization strategies identified
- ROI comparison documented
- Cost monitoring plan defined

---

## DAY 3 (WEDNESDAY): ECS Deployment

**Time:** 1.5 hours

### SESSION 1: Task Definition Creation (45 min)

**Requirements:**

Create ECS task definition for ML service:

**Component 1: Container Definition**
- Requirements: Define container configuration
- Image: Your ECR image URI
- Port: 8000 (FastAPI default)
- Environment variables: All configuration externalized
- What to figure out: Which secrets need AWS Secrets Manager
- Document: Container configuration

**Component 2: Resource Allocation**
- Requirements: Define CPU and memory limits
- Task-level: 0.5 vCPU, 1 GB memory (Fargate minimum)
- Container-level: Match task-level
- What to figure out: Actual resource needs (test locally first)
- Document: Resource sizing rationale

**Component 3: Logging Configuration**
- Requirements: Send logs to CloudWatch
- Log driver: awslogs
- Log group: /ecs/fraud-detection
- Log stream: ecs/{task-id}
- What to figure out: Log retention period (7 days, 30 days?)
- Document: Logging configuration

**Component 4: IAM Roles**
- Requirements: Two roles needed
- Task Role: Permissions for application (access S3, Secrets Manager, etc.)
- Execution Role: Permissions for ECS to pull image, write logs
- What to figure out: Minimal permissions needed (least privilege)
- Document: IAM role policies

**Component 5: Health Check**
- Requirements: Container health monitoring
- Command: `CMD-SHELL, curl -f http://localhost:8000/health || exit 1`
- Interval: 30 seconds
- Timeout: 5 seconds
- Retries: 3
- What to figure out: Appropriate timeout for ML service
- Document: Health check configuration

**Task Definition JSON:**
```json
{
  "family": "fraud-detection-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "taskRoleArn": "arn:aws:iam::ACCOUNT:role/fraud-detection-task-role",
  "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "fraud-detection-container",
      "image": "ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/fraud-detection:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {"name": "ENVIRONMENT", "value": "production"},
        {"name": "LOG_LEVEL", "value": "info"}
      ],
      "secrets": [
        {
          "name": "DATABASE_URL",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:fraud-db-url"
        },
        {
          "name": "OPENAI_API_KEY",
          "valueFrom": "arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:openai-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/fraud-detection",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:8000/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

### SESSION 2: Service Creation & Load Balancing (45 min)

**Requirements:**

Create ECS service with load balancer:

**Component 1: Service Configuration**
- Requirements: Define service parameters
- Desired count: 2 tasks (high availability)
- Launch type: Fargate
- Platform version: Latest
- What to figure out: Update strategy (rolling, blue-green)
- Document: Service configuration

**Component 2: Load Balancer Setup**
- Requirements: Application Load Balancer in front of service
- Type: Application Load Balancer (ALB)
- Scheme: Internet-facing
- Target group: fraud-detection-targets (port 8000)
- Health check: /health endpoint
- What to figure out: Health check thresholds
- Document: Load balancer configuration

**Component 3: Auto-Scaling**
- Requirements: Scale tasks based on load
- Metric: CPU utilization
- Target: 70% CPU
- Min tasks: 2
- Max tasks: 10
- Scale-out: +1 task when CPU > 70% for 3 minutes
- Scale-in: -1 task when CPU < 50% for 5 minutes
- What to figure out: Appropriate cooldown periods
- Document: Auto-scaling policy

**Component 4: Network Configuration**
- Requirements: VPC, subnets, security groups
- VPC: Your existing VPC or create new
- Subnets: 3 public subnets (multi-AZ for HA)
- Security group: Allow inbound 8000 from ALB, Allow outbound all (for API calls)
- What to figure out: VPC CIDR blocks
- Document: Network architecture

**Component 5: Service Discovery (Optional)**
- Requirements: DNS-based service discovery
- Namespace: fraud-detection.local
- Service: ml-service.fraud-detection.local
- Use case: Java service can call ml-service.fraud-detection.local:8000
- What to figure out: When to use vs direct ALB DNS
- Document: Service discovery setup

**Deployment Commands:**
```bash
# 1. Create ECR repository
aws ecr create-repository --repository-name fraud-detection

# 2. Build and push image
docker build -t fraud-detection:latest .
docker tag fraud-detection:latest ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/fraud-detection:latest
aws ecr get-login-password | docker login --username AWS --password-stdin ACCOUNT.dkr.ecr.us-east-1.amazonaws.com
docker push ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/fraud-detection:latest

# 3. Register task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# 4. Create ECS cluster
aws ecs create-cluster --cluster-name fraud-detection-cluster

# 5. Create service
aws ecs create-service \
  --cluster fraud-detection-cluster \
  --service-name fraud-detection-service \
  --task-definition fraud-detection-task:1 \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx,subnet-yyy],securityGroups=[sg-xxx],assignPublicIp=ENABLED}" \
  --load-balancers "targetGroupArn=arn:aws:elasticloadbalancing:...,containerName=fraud-detection-container,containerPort=8000"
```

**Success Criteria:**
- Task definition registered
- ECS service created
- 2 tasks running healthy
- Load balancer health checks passing
- Application accessible via ALB DNS
- Auto-scaling configured

---

## DAY 4 (THURSDAY): Java Spring Boot Integration

**Time:** 1.5 hours

### SESSION 1: Spring Boot REST Client (45 min)

**Learning Resources:**

**Reading:**
- "Calling REST Services with RestTemplate" - Spring Documentation
- URL: https://spring.io/guides/gs/consuming-rest/
- Duration: 15 min
- Focus: RestTemplate basics, error handling

**Video:**
- "Spring Boot RestTemplate Tutorial" - Java Brains
- URL: https://www.youtube.com/watch?v=PiF8s8Y-uVc
- Duration: 20 min
- Focus: RestTemplate configuration, integration

**What You Need to Understand:**

**The Integration Pattern:**
```
User Request
   │
   v
┌─────────────────────────────────┐
│  Spring Boot Application        │
│  (Port 8080)                    │
│                                 │
│  @RestController                │
│  public class FraudController { │
│    @PostMapping("/analyze")     │
│    public FraudResult analyze() {│
│      // Call ML service         │
│      return mlClient.predict(); │
│    }                            │
│  }                              │
└─────────────────────────────────┘
   │
   │ HTTP POST
   │ Content-Type: application/json
   │ Body: {"transaction": {...}}
   v
┌─────────────────────────────────┐
│  FastAPI ML Service             │
│  (Port 8000)                    │
│                                 │
│  @app.post("/predict")          │
│  async def predict():           │
│    # ML inference               │
│    return {"fraud": true}       │
└─────────────────────────────────┘
```

**RestTemplate Configuration:**
```java
@Configuration
public class RestTemplateConfig {
    
    @Bean
    public RestTemplate restTemplate() {
        HttpComponentsClientHttpRequestFactory factory = 
            new HttpComponentsClientHttpRequestFactory();
        
        // Timeouts (critical for production)
        factory.setConnectTimeout(5000);  // 5 seconds
        factory.setReadTimeout(30000);     // 30 seconds
        
        return new RestTemplate(factory);
    }
}
```

**ML Service Client:**
```java
@Service
public class MLServiceClient {
    
    @Value("${ml.service.url}")
    private String mlServiceUrl;
    
    private final RestTemplate restTemplate;
    
    public MLServiceClient(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
    
    public FraudPrediction analyzeFraud(Transaction transaction) {
        String url = mlServiceUrl + "/predict";
        
        try {
            // Prepare request
            FraudRequest request = new FraudRequest(transaction);
            
            // Call ML service
            ResponseEntity<FraudResponse> response = restTemplate.postForEntity(
                url, 
                request, 
                FraudResponse.class
            );
            
            // Parse response
            FraudResponse body = response.getBody();
            return mapToFraudPrediction(body);
            
        } catch (RestClientException e) {
            // Handle errors (circuit breaker in Week 24)
            log.error("ML service call failed", e);
            throw new MLServiceException("Fraud analysis unavailable", e);
        }
    }
}
```

**Request/Response DTOs:**
```java
// Request to ML service
public class FraudRequest {
    private String transactionId;
    private BigDecimal amount;
    private String merchant;
    private String location;
    private LocalDateTime timestamp;
    // ... getters/setters
}

// Response from ML service
public class FraudResponse {
    private boolean isFraud;
    private int riskScore;
    private List<String> redFlags;
    private String reasoning;
    // ... getters/setters
}
```

### SESSION 2: Build Java Integration Layer (45 min)

**Requirements:**

Create Spring Boot service that calls ML API:

**Component 1: Configuration**
- Requirements: Externalize ML service URL
- File: application.yml
- Properties: ml.service.url, ml.service.timeout.connect, ml.service.timeout.read
- What to figure out: Different URLs for dev/staging/prod
- Document: Configuration management

**Component 2: ML Client Service**
- Requirements: Service that calls FastAPI
- Methods: analyzeFraud(Transaction), batchAnalyze(List<Transaction>), getHealth()
- Error handling: Timeout, Connection refused, 5xx errors
- What to figure out: Retry strategy (Week 24 circuit breaker)
- Document: Client implementation

**Component 3: REST Controller**
- Requirements: Expose fraud analysis endpoint
- Endpoint: POST /api/v1/fraud/analyze
- Input: Transaction JSON
- Output: FraudResult JSON (combines transaction + ML prediction)
- What to figure out: Request validation
- Document: API contract

**Component 4: DTO Mapping**
- Requirements: Map between Java and Python models
- Java side: Transaction (entity), FraudRequest/Response (DTOs)
- Python side: Pydantic models
- Naming: Java camelCase ↔ Python snake_case
- What to figure out: Jackson configuration for snake_case
- Document: Mapping strategy

**Component 5: Integration Test**
- Requirements: Test Java → Python integration
- Setup: Mock ML service OR use WireMock
- Test cases: Successful fraud detection, Legitimate transaction, ML service timeout, ML service error
- What to figure out: How to run integration tests in CI/CD
- Document: Test strategy

**Example Controller:**
```java
@RestController
@RequestMapping("/api/v1/fraud")
public class FraudAnalysisController {
    
    private final TransactionService transactionService;
    private final MLServiceClient mlClient;
    
    @PostMapping("/analyze")
    public ResponseEntity<FraudAnalysisResult> analyzeFraud(
            @RequestBody @Valid TransactionRequest request) {
        
        // 1. Save transaction to database
        Transaction transaction = transactionService.save(request);
        
        // 2. Call ML service for fraud prediction
        FraudPrediction prediction = mlClient.analyzeFraud(transaction);
        
        // 3. Combine results
        FraudAnalysisResult result = FraudAnalysisResult.builder()
            .transactionId(transaction.getId())
            .amount(transaction.getAmount())
            .merchant(transaction.getMerchant())
            .isFraud(prediction.isFraud())
            .riskScore(prediction.getRiskScore())
            .redFlags(prediction.getRedFlags())
            .reasoning(prediction.getReasoning())
            .analyzedAt(LocalDateTime.now())
            .build();
        
        return ResponseEntity.ok(result);
    }
}
```

**Success Criteria:**
- Spring Boot application compiles
- ML client successfully calls FastAPI
- Integration tests pass
- Error handling works (timeout, errors)
- JSON mapping correct (camelCase ↔ snake_case)

---

## DAY 5 (FRIDAY): Blue-Green Deployment

**Time:** 1 hour

### SESSION 1: Blue-Green Deployment Concept (30 min)

**Learning Resources:**

**Video:**
- "Blue-Green Deployment Explained" - TechWorld with Nana
- URL: https://www.youtube.com/watch?v=3r3i42p13mA
- Duration: 9:15
- Focus: Blue-green concept, benefits, challenges

**Reading:**
- "Blue/Green Deployments on ECS" - AWS Blog
- URL: https://aws.amazon.com/blogs/compute/bluegreen-deployments-with-amazon-ecs/
- Duration: 15 min
- Focus: ECS blue-green implementation

**What You Need to Understand:**

**Traditional Deployment (Risky):**
```
Step 1: Stop old version (downtime starts)
Step 2: Deploy new version
Step 3: Start new version (downtime ends)
Problem: Downtime + rollback requires redeploy
```

**Blue-Green Deployment (Zero Downtime):**
```
Current State:
BLUE environment (v1.0) ← 100% of traffic
GREEN environment (idle)

Deploy New Version:
BLUE environment (v1.0) ← 100% of traffic
GREEN environment (v2.0 deployed) ← 0% of traffic
(Test GREEN thoroughly)

Switch Traffic:
BLUE environment (v1.0) ← 0% of traffic (standby)
GREEN environment (v2.0) ← 100% of traffic
(If issues: instant rollback by switching back to BLUE)

After Stability:
GREEN becomes new BLUE
Old BLUE environment retired or kept for next deployment
```

**Benefits:**
- **Zero Downtime:** Traffic switches instantly (< 1 second)
- **Instant Rollback:** Switch back to BLUE if issues
- **Safe Testing:** Test GREEN with 0% traffic before switch
- **Canary Option:** Route 10% to GREEN, 90% to BLUE initially

**ECS Blue-Green with CodeDeploy:**
```
┌─────────────────────────────────┐
│  Application Load Balancer      │
│                                 │
│  Listener: Port 443             │
└─────────┬───────────────────────┘
          │
          ├──────────┬──────────┐
          v          v          v
    Target Group 1   Target Group 2
    (BLUE)          (GREEN)
          │              │
          v              v
    ECS Service    ECS Service
    (v1.0)        (v2.0)
    2 tasks       2 tasks
```

**CodeDeploy Traffic Shifting:**
- AllAtOnce: 100% instant switch
- Linear: 10% every minute (10 minutes total)
- Canary: 10% immediately, 90% after 5 minutes
- **Fintech Recommendation:** Canary (detect issues with 10% before full rollout)

### SESSION 2: Implement Blue-Green Pipeline (30 min)

**Requirements:**

Set up CodeDeploy for ECS blue-green:

**Component 1: CodeDeploy Application**
- Requirements: Create CodeDeploy application
- Compute platform: ECS
- What to figure out: Application naming convention
- Document: CodeDeploy setup

**Component 2: Deployment Group**
- Requirements: Define deployment configuration
- ECS cluster: fraud-detection-cluster
- ECS service: fraud-detection-service
- Load balancer: Your ALB
- Target groups: Blue and Green
- Deployment config: CodeDeployDefault.ECSCanary10Percent5Minutes
- What to figure out: Rollback triggers (CloudWatch alarms)
- Document: Deployment group configuration

**Component 3: AppSpec File**
- Requirements: Define deployment specification
- Format: YAML (for ECS deployments)
- Contents: Task definition, Container name/port, Hooks for testing
- What to figure out: Hook scripts for automated testing
- Document: AppSpec structure

**Component 4: Automated Rollback**
- Requirements: Auto-rollback on failure
- Triggers: CloudWatch alarm (5xx errors > threshold), Deployment failure
- Action: Rollback to previous version (switch back to BLUE)
- What to figure out: Appropriate alarm thresholds
- Document: Rollback strategy

**Component 5: Deployment Pipeline**
- Requirements: Automated deployment on code push
- Trigger: Git push to main branch
- Steps: Build Docker image, Push to ECR, Update task definition, CodeDeploy blue-green deployment
- What to figure out: CI/CD tool (GitHub Actions, GitLab CI, AWS CodePipeline)
- Document: Pipeline definition

**AppSpec.yaml Example:**
```yaml
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:us-east-1:ACCOUNT:task-definition/fraud-detection-task:2"
        LoadBalancerInfo:
          ContainerName: "fraud-detection-container"
          ContainerPort: 8000
        PlatformVersion: "LATEST"
Hooks:
  - BeforeInstall: "LambdaFunctionToValidateBeforeInstall"
  - AfterInstall: "LambdaFunctionToValidateAfterInstall"
  - AfterAllowTestTraffic: "LambdaFunctionToValidateTestTraffic"
  - BeforeAllowTraffic: "LambdaFunctionToValidateBeforeAllowingProdTraffic"
  - AfterAllowTraffic: "LambdaFunctionToValidateAfterAllowingProdTraffic"
```

**Success Criteria:**
- CodeDeploy application created
- Deployment group configured with canary
- AppSpec file written
- Automated rollback configured
- Can deploy new version with zero downtime

---

## DAY 6 (SATURDAY): Monitoring & Logging

**Time:** 2.5 hours

### SESSION 1: CloudWatch Dashboards (90 min)

**Requirements:**

Create comprehensive monitoring dashboard:

**Dashboard 1: Service Health**
- Requirements: High-level service metrics
- Widgets: Task count (running/stopped/pending), CPU utilization (per task + average), Memory utilization (per task + average), Network in/out
- Alerts: Task count < 2 (high availability risk), CPU > 80% for 5 minutes, Memory > 90%
- What to figure out: Alert notification channels (SNS → email/Slack)
- Document: Health monitoring

**Dashboard 2: Application Metrics**
- Requirements: Business-level metrics
- Widgets: Request count (per minute), Latency (P50, P95, P99), Error rate (5xx responses), Success rate (2xx responses)
- Alerts: Error rate > 1%, P95 latency > 5 seconds
- What to figure out: Custom application metrics (fraud detected count, etc.)
- Document: Application monitoring

**Dashboard 3: Load Balancer**
- Requirements: Traffic and load balancer health
- Widgets: Target health (healthy/unhealthy), Request count per target, Response time per target, 4xx/5xx errors
- Alerts: Unhealthy targets > 0, 5xx errors > threshold
- What to figure out: Load balancer access logs (S3)
- Document: Load balancer monitoring

**Dashboard 4: Cost Tracking**
- Requirements: Monitor AWS spend
- Widgets: Fargate compute hours, Data transfer, Load balancer costs, CloudWatch costs
- Budget: Alert if monthly cost > $100
- What to figure out: Cost allocation tags
- Document: Cost monitoring

**Dashboard 5: Business Metrics (Custom)**
- Requirements: Fraud detection specific metrics
- Metrics: Fraud detections per hour, Average risk score, False positive rate (if feedback available), Model latency
- Source: Custom CloudWatch metrics from application
- What to figure out: How to emit custom metrics from FastAPI
- Document: Business metrics

**Custom Metrics from FastAPI:**
```python
import boto3
cloudwatch = boto3.client('cloudwatch')

async def analyze_fraud(transaction):
    start = time.time()
    
    # ML inference
    prediction = model.predict(transaction)
    
    # Emit custom metrics
    cloudwatch.put_metric_data(
        Namespace='FraudDetection',
        MetricData=[
            {
                'MetricName': 'FraudDetected',
                'Value': 1 if prediction.is_fraud else 0,
                'Unit': 'Count'
            },
            {
                'MetricName': 'RiskScore',
                'Value': prediction.risk_score,
                'Unit': 'None'
            },
            {
                'MetricName': 'ModelLatency',
                'Value': time.time() - start,
                'Unit': 'Seconds'
            }
        ]
    )
    
    return prediction
```

### SESSION 2: Centralized Logging (60 min)

**Requirements:**

Set up comprehensive logging:

**Component 1: Application Logs**
- Requirements: Structured JSON logging from FastAPI
- Format: `{"timestamp": "...", "level": "INFO", "message": "...", "transaction_id": "...", "user_id": "..."}`
- Destination: CloudWatch Logs `/ecs/fraud-detection`
- Retention: 30 days
- What to figure out: Log sampling for high-volume (100% errors, 10% info)
- Document: Application logging

**Component 2: Access Logs**
- Requirements: Load balancer access logs
- Destination: S3 bucket `fraud-detection-alb-logs`
- Format: ELB standard format
- Retention: 90 days (compliance requirement)
- What to figure out: Athena queries for analysis
- Document: Access logging

**Component 3: Log Insights Queries**
- Requirements: Pre-built queries for troubleshooting
- Query 1: Error rate by endpoint
- Query 2: Slowest requests (P99 latency)
- Query 3: Fraud detections per hour
- Query 4: Failed health checks
- What to figure out: Query optimization (field extraction)
- Document: Useful queries

**Component 4: Log Aggregation**
- Requirements: Combine logs from all sources
- Sources: Application logs, ALB logs, ECS task logs, CloudWatch Container Insights
- Tool: CloudWatch Logs Insights OR export to Elasticsearch
- What to figure out: Need for separate log aggregation tool
- Document: Aggregation strategy

**Component 5: Log Alarms**
- Requirements: Alerts based on log patterns
- Alarm 1: "ERROR" count > 10 in 5 minutes
- Alarm 2: "ML service unavailable" appears
- Alarm 3: "Database connection failed"
- Action: SNS notification → PagerDuty/Slack
- What to figure out: Alarm vs metric (when to use each)
- Document: Log-based alerting

**Success Criteria:**
- All 5 dashboards created
- Custom metrics emitted from application
- Structured logging implemented
- Log Insights queries working
- Alerts configured and tested

---

## DAY 7 (SUNDAY): Week Summary & System Design

**Time:** 2 hours

### SESSION 1: System Design Exercise (60 min)

**Requirements:**

Design complete production architecture:

**Exercise: "Design a Fraud Detection System with ML"**

**Scenario:**
- 10,000 transactions/second at peak
- Sub-200ms latency requirement (P95)
- 99.9% uptime SLA
- Global user base (US, EU, APAC)
- Regulatory requirement: Data residency per region

**Design Requirements:**

**1. High-Level Architecture**
- Components: API Gateway, Java Backend, Python ML Service, Databases, Cache, Message Queue
- What to figure out: Where each component fits
- Draw: Architecture diagram
- Document: Component responsibilities

**2. Scalability**
- Requirements: Handle 10K TPS (transactions per second)
- ECS: How many tasks needed?
- Calculation: 1 task handles 100 TPS → Need 100 tasks at peak
- Auto-scaling: Min 20 tasks, Max 150 tasks
- What to figure out: Right-size task CPU/memory
- Document: Scaling strategy

**3. Latency Optimization**
- Requirements: P95 < 200ms
- Optimizations: Cache common fraud rules in Redis (50ms saved), Async ML inference where possible, Load balancer in same region, Database read replicas
- What to figure out: What to cache, what to compute
- Document: Latency breakdown

**4. High Availability**
- Requirements: 99.9% uptime (8.76 hours downtime/year)
- Strategy: Multi-AZ deployment (3 availability zones), Blue-green deployments (zero downtime), Health checks with auto-recovery, Database failover (RDS Multi-AZ)
- What to figure out: Disaster recovery (cross-region)
- Document: HA architecture

**5. Data Residency**
- Requirements: EU data in EU, US data in US
- Strategy: Separate ECS clusters per region, Separate databases per region, Route53 geolocation routing
- What to figure out: Data synchronization needs
- Document: Multi-region setup

**6. Security**
- Requirements: Enterprise-grade security
- Components: WAF (Web Application Firewall) in front of ALB, VPC with private subnets, Secrets Manager for credentials, IAM roles with least privilege, Encryption in transit (TLS) and at rest (KMS)
- What to figure out: Network segmentation (public/private subnets)
- Document: Security layers

**7. Monitoring**
- Requirements: Full observability
- Metrics: CloudWatch custom metrics, X-Ray tracing (track requests through system), CloudWatch Logs for all components
- Alerts: PagerDuty for critical, Email for warnings
- What to figure out: Alert thresholds and on-call rotation
- Document: Observability strategy

**8. Cost Estimation**
- Requirements: Estimate monthly AWS cost at scale
- Components: Fargate (100 tasks avg), Load balancers (2 ALBs, multi-region), Databases (RDS, OpenSearch), Data transfer, CloudWatch
- Calculation: Rough estimate $10K-15K/month at scale
- What to figure out: Cost optimization strategies
- Document: Cost breakdown

**Deliverable: Architecture Diagram**
```
                          Route53 (Geolocation Routing)
                                     │
                   ┌─────────────────┼─────────────────┐
                   │                 │                 │
                   v                 v                 v
                US Region          EU Region         APAC Region
                   │                 │                 │
         ┌─────────┴─────────┐      │                 │
         │                   │      │                 │
         v                   v      v                 v
    CloudFront CDN          WAF   (Same architecture   
         │                   │     repeated per region)
         v                   v
    Application Load Balancer
         │
    ┌────┴────┬─────────┬──────────┐
    v         v         v          v
  ECS Fargate (Auto-scaled 20-150 tasks)
  │         │         │          │
  v         v         v          v
Java      Java      Java       Java
+Python   +Python   +Python    +Python
Service   Service   Service    Service
  │                            │
  └─────────┬──────────────────┘
            │
    ┌───────┼───────┐
    v       v       v
  RDS   OpenSearch Redis
(Multi-AZ) (3-node) (ElastiCache)
```

### SESSION 2: Week Summary & Portfolio (60 min)

**Requirements:**

Create WEEK23_SUMMARY.md:

**Section 1: What You Built**
- Docker multi-stage build (image reduced 67%)
- ECS Fargate deployment (production infrastructure)
- Java Spring Boot integration (hybrid architecture)
- Blue-green deployment pipeline (zero downtime)
- CloudWatch monitoring (5 dashboards + custom metrics)
- Load balancer with auto-scaling
- Document: Complete build inventory

**Section 2: Fintech Impact - CRITICAL**
- Hybrid Java+Python: Bridges legacy Core Banking with modern ML
- Your unique value: Know both Java and Python ecosystems
- Market reality: 90% of banks run Java core systems
- Integration pattern: Production-grade cross-language communication
- Deployment: Enterprise-ready cloud infrastructure
- Document: Business value

**Section 3: Technical Achievements**
- Image size: 1.2 GB → 400 MB (67% reduction)
- Deployment: Zero-downtime blue-green with instant rollback
- Scalability: 2-10 tasks auto-scaled on CPU (70% target)
- Availability: Multi-AZ (99.9% uptime)
- Monitoring: 20+ metrics tracked, 10+ alarms configured
- Cost: $75/month (vs $200/month on-premises)
- Document: Technical metrics

**Section 4: System Design Competency**
- Designed: 10K TPS fraud detection system
- Addressed: Scalability, latency, HA, multi-region, security, cost
- Architecture: Production-ready distributed system
- Document: System design capability

**Section 5: Java-Python Bridge**
- Why critical: Most financial systems are Java
- Your advantage: Bilingual developer (rare in ML)
- Integration: RestTemplate → FastAPI (proven pattern)
- Career value: Can work on ML in existing banking systems
- Document: Hybrid architecture value

**Section 6: Interview Talking Points**
- Story 1: "Deployed ML service on ECS with zero-downtime blue-green deployment"
- Story 2: "Reduced Docker image 67%, saving deployment time and storage costs"
- Story 3: "Integrated Python ML service with Java Spring Boot banking application"
- Story 4: "Designed 10K TPS fraud detection system with multi-region deployment"
- Document: STAR format stories

**Success Criteria:**
- Summary comprehensive
- Fintech impact articulated
- Technical details accurate
- System design documented
- Interview stories ready

---

## 📚 ADDITIONAL RESOURCES

**Docker:**
- Multi-Stage Builds: https://docs.docker.com/build/building/multi-stage/
- Best Practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Security: https://docs.docker.com/engine/security/

**AWS ECS:**
- ECS Documentation: https://docs.aws.amazon.com/ecs/
- Fargate: https://aws.amazon.com/fargate/
- Task Definitions: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html

**AWS CodeDeploy:**
- ECS Blue-Green: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups-create-blue-green.html
- AppSpec Reference: https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html

**Spring Boot:**
- RestTemplate: https://spring.io/guides/gs/consuming-rest/
- Configuration: https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html

**Monitoring:**
- CloudWatch: https://docs.aws.amazon.com/cloudwatch/
- Container Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html

---

## ✅ WEEK 23 DELIVERABLES

**Documentation:**
- DOCKER_OPTIMIZATION.md - Multi-stage build guide
- ECS_DEPLOYMENT.md - Complete ECS setup
- JAVA_INTEGRATION.md - Spring Boot integration
- BLUEGREEN_DEPLOYMENT.md - Deployment strategy
- MONITORING_GUIDE.md - CloudWatch setup
- SYSTEM_DESIGN.md - Architecture documentation
- WEEK23_SUMMARY.md - Week summary

**Implementation Files (Requirements):**
- Dockerfile - Multi-stage optimized (requirements documented)
- task-definition.json - ECS task definition (requirements documented)
- appspec.yaml - CodeDeploy specification (requirements documented)
- MLServiceClient.java - Java REST client (requirements documented)
- cloudwatch-dashboard.json - Monitoring dashboard (requirements documented)

**Architecture Diagrams:**
- ECS deployment architecture
- Java-Python integration flow
- Blue-green deployment process
- Multi-region system design
- Network topology (VPC, subnets, security groups)

**Understanding:**
- Docker multi-stage builds and optimization
- ECS/Fargate architecture and deployment
- Load balancing and auto-scaling
- Blue-green deployment patterns
- Java-Python REST integration
- CloudWatch monitoring and alerting
- System design for high-scale ML systems

---

## 🎯 SUCCESS CRITERIA

**By end of Week 23:**

**Conceptual:**
- Understand container orchestration with ECS
- Know blue-green deployment benefits
- Understand Java-Python integration patterns
- Can design high-scale distributed systems
- Know AWS cost optimization strategies

**Practical:**
- Build optimized Docker images (<500 MB)
- Deploy applications on ECS Fargate
- Configure load balancers and auto-scaling
- Integrate Java Spring Boot with Python FastAPI
- Implement blue-green deployments
- Set up comprehensive CloudWatch monitoring
- Design production-grade architectures

**Portfolio Impact:**
- ✅ Production deployment expertise (ECS/Fargate)
- ✅ Zero-downtime deployment capability
- ✅ Java-Python hybrid architecture (FINTECH CRITICAL)
- ✅ System design competency demonstrated
- ✅ Cloud infrastructure mastery
- ✅ Monitoring and observability skills
- ✅ Cost-conscious engineering

---

**Total Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Java+Python bridge = rare & valuable skill  
**Next Week:** Circuit Breakers + Resilience Engineering