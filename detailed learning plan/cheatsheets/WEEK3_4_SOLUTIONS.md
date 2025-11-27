# Week 3-4 Learning Schedule - Phase 1 Infrastructure & Data Pipeline

## Overview

Comprehensive 14-day plan covering Docker containerization, PostgreSQL database setup, OpenSearch implementation, Apache Airflow orchestration, and automated arXiv paper ingestion pipeline. Total commitment: ~26 hours (13 hrs/week).

---

## Week Schedule

### Week 3: Infrastructure Setup (Dec 1-7)

| Day | Date | Topic | Time |
|-----|------|-------|------|
| Mon | Dec 1 | Docker Fundamentals | 1.5h |
| Tue | Dec 2 | FastAPI in Docker + PostgreSQL Basics | 1.5h |
| Wed | Dec 3 | PostgreSQL Deep Dive + OpenSearch Intro | 1.5h |
| Thu | Dec 4 | OpenSearch Implementation + Airflow Basics | 1.5h |
| Fri | Dec 5 | Airflow Setup + Docker Compose Integration | 1.5h |
| Sat | Dec 6 | **Complete Docker Compose Stack** | 4h |
| Sun | Dec 7 | Health Checks, Testing & Documentation | 3h |

**Total Week 3:** ~14.5 hours

### Week 4: Data Pipeline (Dec 8-14)

| Day | Date | Topic | Time |
|-----|------|-------|------|
| Mon | Dec 8 | arXiv API Integration | 1.5h |
| Tue | Dec 9 | PDF Download Logic + Storage | 1.5h |
| Wed | Dec 10 | GROBID Setup + XML Parsing | 1.5h |
| Thu | Dec 11 | Docling Fallback Parser | 1.5h |
| Fri | Dec 12 | Airflow DAG Creation | 1.5h |
| Sat | Dec 13 | **Automated Daily Pipeline** | 4h |
| Sun | Dec 14 | Testing, Monitoring & Documentation | 3h |

**Total Week 4:** ~14.5 hours

---

## WEEK 3: INFRASTRUCTURE SETUP

### Day 1 (Mon Dec 1): Docker Fundamentals

#### Primary Video Resources

**Video 1: "Docker Tutorial for Beginners - TechWorld with Nana"**
- Link: https://www.youtube.com/watch?v=3c-iBn73dDE
- Duration: 2:17:00
- Watch: First 30 minutes (basics, containers, images)
- What you'll learn: Core Docker concepts, why containerization matters

**Video 2: "Docker in 100 Seconds"**
- Link: https://www.youtube.com/watch?v=Gjnup-PuquQ
- Duration: 2:32
- Quick refresher before diving in

**Video 3: "Docker Compose Tutorial"**
- Link: https://www.youtube.com/watch?v=SXwC9fSwct8
- Duration: 15:00
- Preview of what's coming this week

#### Reading Materials

**Docker Official Documentation:**
- Link: https://docs.docker.com/get-started/
- Section 1: Overview and Setup (15 min)
- Section 2: Containerize an application (20 min)

**Article: "Docker for ML Engineers"**
- Link: https://towardsdatascience.com/docker-for-machine-learning-engineers-a-complete-guide-e7f8a4f0c3d5
- Duration: 15 min read
- ML-specific use cases

#### Day 1 Schedule (90 minutes total)

**Part 1: Understanding Docker (30 min)**
1. Watch "Docker in 100 Seconds" (3 min)
2. Watch TechWorld with Nana (first 20 min)
3. Read Docker overview docs (7 min)

**Part 2: Installation & Setup (20 min)**
1. Install Docker Desktop (Windows/Mac) or Docker Engine (Linux)
2. Verify installation: `docker --version`
3. Run hello-world: `docker run hello-world`
4. Test: `docker ps`, `docker images`

**Part 3: Hands-on Practice (30 min)**
1. Pull Ubuntu image: `docker pull ubuntu:22.04`
2. Run interactive container: `docker run -it ubuntu bash`
3. Install package inside container (python3)
4. Exit and see container stopped
5. Understand ephemeral nature of containers

**Part 4: Reflection (10 min)**
- Document what containers are vs VMs
- Why Docker matters for ML pipelines
- How you'll use it this week

#### Key Concepts to Master

**Container vs Image:**
- Image = blueprint (like a class)
- Container = running instance (like an object)
- Images are immutable, containers are ephemeral

**Why Docker for ML?**
- Consistent environments across machines
- Easy dependency management
- Reproducible experiments
- Easy deployment
- Isolation from host system

**Core Commands:**
```bash
docker pull <image>        # Download image
docker images              # List images
docker ps                  # List running containers
docker ps -a               # List all containers
docker run <image>         # Create and start container
docker stop <id>           # Stop container
docker rm <id>             # Remove container
docker rmi <image>         # Remove image
docker exec -it <id> bash  # Enter running container
```

**Ports and Volumes:**
- Ports: Map container port to host: `-p 8000:8000`
- Volumes: Persist data: `-v /host/path:/container/path`
- Without volumes, data lost when container stops

#### Practice Requirements

**Exercise 1: Python Container**
- Pull python:3.11 image
- Run container with interactive shell
- Create simple Python script inside
- Run the script
- Exit and verify script is gone

**Exercise 2: Port Mapping**
- Run python HTTP server in container
- Map to host port 8080
- Access from browser on host machine
- Understand port mapping concept

**Exercise 3: Volume Mounting**
- Create directory on host with Python script
- Mount as volume when running container
- Modify script on host
- See changes reflected in container

#### End of Day 1 Checklist

- [ ] Docker Desktop/Engine installed
- [ ] Ran hello-world successfully
- [ ] Understand container vs image
- [ ] Can pull images
- [ ] Can run containers (interactive and detached)
- [ ] Understand port mapping
- [ ] Understand volume mounting
- [ ] Know why Docker matters for ML
- [ ] Spent approximately 90 minutes

---

### Day 2 (Tue Dec 2): FastAPI in Docker + PostgreSQL Basics

#### Primary Video Resources

**Video 1: "Dockerize FastAPI Application"**
- Link: https://www.youtube.com/watch?v=0H2miBK_gAk
- Duration: 15:00
- Practical FastAPI containerization

**Video 2: "PostgreSQL Crash Course"**
- Link: https://www.youtube.com/watch?v=qw--VYLpxG4
- Duration: 1:16:00
- Watch: First 20 minutes (basics, installation, SQL fundamentals)

#### Reading Materials

**Dockerfile Best Practices:**
- Link: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Duration: 15 min
- Critical for production images

**PostgreSQL Official Tutorial:**
- Link: https://www.postgresql.org/docs/current/tutorial.html
- Sections 1-3: Getting Started, SQL Language, Advanced Features intro
- Duration: 25 min

#### Day 2 Schedule (90 minutes total)

**Part 1: Create Dockerfile for FastAPI (35 min)**

**Requirements:**
- Start with python:3.11-slim base image
- Copy requirements.txt first (layer caching)
- Install dependencies
- Copy application code
- Expose port 8000
- Set CMD to run uvicorn

**What to figure out:**
- Dockerfile syntax (FROM, COPY, RUN, EXPOSE, CMD)
- Layer caching optimization
- Why copy requirements before code
- Difference between CMD and ENTRYPOINT

**Test:**
- Build image: `docker build -t transaction-api .`
- Run container: `docker run -p 8000:8000 transaction-api`
- Access API at localhost:8000/docs
- Verify all endpoints work

**Success criteria:**
- Image builds without errors
- Container runs and is accessible
- API fully functional in container
- Can stop and restart without issues

---

**Part 2: PostgreSQL Basics (35 min)**

**Requirements:**

**1. Install PostgreSQL Locally (10 min)**
- Install PostgreSQL 15 or 16
- Set up initial admin password
- Verify psql command works

**2. Create First Database (10 min)**
```sql
CREATE DATABASE transactions_db;
\c transactions_db
CREATE TABLE test_transactions (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10,2),
    merchant VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);
```

**3. Basic SQL Operations (15 min)**
- INSERT: Add 5 test transactions
- SELECT: Retrieve all, filter by amount
- UPDATE: Modify merchant name
- DELETE: Remove one transaction
- Understand CRUD operations

**What to figure out:**
- Connect to database: `psql -U postgres`
- Switch databases: `\c database_name`
- List tables: `\dt`
- Describe table: `\d table_name`
- Exit psql: `\q`

---

**Part 3: Reflection (20 min)**

**Document:**
1. Why Dockerfile layers matter (caching)
2. How FastAPI runs in Docker vs locally
3. Basic SQL commands you learned
4. How PostgreSQL will store paper metadata
5. Questions for tomorrow's integration

#### Key Concepts to Master

**Dockerfile Structure:**
- Base image specification
- Working directory setup
- Copy requirements file first for layer caching
- Install dependencies
- Copy application code last
- Expose port for documentation
- Define startup command for uvicorn server

**Layer Caching:**
- Each Dockerfile instruction creates a layer
- Layers are cached
- If nothing changes, cache used
- Order matters: Put rarely-changing stuff first
- requirements.txt before code = faster rebuilds

**PostgreSQL Basics:**
- **Database:** Container for tables
- **Table:** Structured data storage (rows and columns)
- **Primary Key:** Unique identifier for each row
- **Foreign Key:** Reference to another table's primary key

**SQL CRUD:**
- CREATE TABLE: Define structure with columns and data types
- INSERT: Add new rows with values
- SELECT: Query data with filtering conditions
- UPDATE: Modify existing rows based on conditions
- DELETE: Remove rows based on conditions

#### Practice Requirements

**Exercise 1: Multi-Stage Build (Advanced)**
- Create Dockerfile with builder and runtime stages
- Install build dependencies in builder
- Copy only artifacts to runtime
- Compare image sizes

**Exercise 2: Environment Variables**
- Add .env file with configuration
- Use ENV in Dockerfile
- Pass environment variables at runtime: `-e VAR=value`
- Access in FastAPI code

**Exercise 3: SQL Transactions**
```sql
BEGIN;
INSERT INTO transactions VALUES (...);
INSERT INTO transactions VALUES (...);
-- If error happens, nothing saved
COMMIT;  -- Or ROLLBACK if error
```

#### End of Day 2 Checklist

- [ ] Created Dockerfile for FastAPI app
- [ ] Built Docker image successfully
- [ ] Ran containerized FastAPI
- [ ] API accessible from host browser
- [ ] PostgreSQL installed locally
- [ ] Created test database and table
- [ ] Performed CRUD operations in SQL
- [ ] Understand Dockerfile layer caching
- [ ] Know basic SQL commands
- [ ] Spent approximately 90 minutes

---

### Day 3 (Wed Dec 3): PostgreSQL Deep Dive + OpenSearch Intro

#### Primary Video Resources

**Video 1: "PostgreSQL Advanced Features"**
- Link: https://www.youtube.com/watch?v=qw--VYLpxG4
- Duration: Continue from 20:00 to 45:00
- Indexes, relationships, transactions

**Video 2: "What is Elasticsearch/OpenSearch"**
- Link: https://www.youtube.com/watch?v=gS_nHTWZEJ8
- Duration: 10:00
- Search engine fundamentals

**Video 3: "OpenSearch Tutorial"**
- Link: https://www.youtube.com/watch?v=hDC_QkfYPLU
- Duration: 20:00
- Hands-on introduction

#### Reading Materials

**psycopg3 Documentation:**
- Link: https://www.psycopg.org/psycopg3/docs/
- Basic usage section
- Duration: 20 min
- Python PostgreSQL connector

**OpenSearch Getting Started:**
- Link: https://opensearch.org/docs/latest/getting-started/
- Quickstart section
- Duration: 15 min

#### Day 3 Schedule (90 minutes total)

**Part 1: Python + PostgreSQL Integration (40 min)**

**Requirements:**

**1. Install psycopg3**
```bash
pip install psycopg[binary]
```

**2. Create database connection module**
- Database connection configuration
- Connection pooling setup
- Connection context manager
- Error handling for connection failures

**3. Implement paper metadata storage**

**Table Schema:**
```sql
CREATE TABLE papers (
    paper_id VARCHAR(50) PRIMARY KEY,
    arxiv_id VARCHAR(20) UNIQUE NOT NULL,
    title TEXT NOT NULL,
    authors TEXT[],
    abstract TEXT,
    categories VARCHAR(50)[],
    published_date DATE,
    pdf_url TEXT,
    downloaded_at TIMESTAMP,
    parsed_at TIMESTAMP,
    parsing_status VARCHAR(20),
    INDEX ON (published_date),
    INDEX ON (parsing_status)
);
```

**4. Create CRUD operations**
- Insert new paper metadata
- Get paper by arxiv_id
- Update parsing status
- Query papers by date range
- Query papers by category
- Handle duplicate inserts gracefully

**What to figure out:**
- Connection string format
- Using context managers (with statement)
- Parameterized queries (prevent SQL injection)
- Handling PostgreSQL arrays
- Date/time handling
- Error handling (connection errors, constraint violations)

**Test:**
- Insert 5 paper records
- Query by arxiv_id
- Update parsing status
- Query papers from last week
- Handle duplicate arxiv_id insertion

---

**Part 2: OpenSearch Introduction (35 min)**

**Requirements:**

**1. Understanding OpenSearch (15 min)**
- What is full-text search
- Inverted index concept
- Why PostgreSQL isn't enough for search
- OpenSearch vs Elasticsearch (they're forks)
- When to use OpenSearch vs vector databases

**2. Install OpenSearch with Docker (10 min)**
```bash
docker run -d \
  -p 9200:9200 \
  -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=Admin123!" \
  opensearchproject/opensearch:latest
```

**3. Basic OpenSearch operations (10 min)**
- Access OpenSearch: `curl http://localhost:9200`
- Create index
- Index a document
- Search documents
- Understand JSON responses

**What to figure out:**
- Index = database in SQL terms
- Document = row in SQL terms
- Mapping = schema in SQL terms
- Query DSL = SQL equivalent
- Relevance scoring (BM25 algorithm)

---

**Part 3: Reflection (15 min)**

**Document:**
1. PostgreSQL for structured data vs OpenSearch for search
2. When to use arrays vs separate tables
3. Why indexes matter for query performance
4. How full-text search works differently than SQL LIKE
5. Integration plan: PostgreSQL + OpenSearch together

#### Key Concepts to Master

**PostgreSQL Connection:**
```python
import psycopg

# Context manager (recommended)
with psycopg.connect(
    "dbname=papers user=postgres password=xxx"
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM papers")
        results = cur.fetchall()
```

**Parameterized Queries (Prevent SQL Injection):**
```python
# BAD - SQL injection vulnerability
cur.execute(f"SELECT * FROM papers WHERE arxiv_id = '{arxiv_id}'")

# GOOD - parameterized query
cur.execute(
    "SELECT * FROM papers WHERE arxiv_id = %s",
    (arxiv_id,)
)
```

**PostgreSQL Arrays:**
```python
# Insert array
cur.execute(
    "INSERT INTO papers (authors) VALUES (%s)",
    (['Smith, J.', 'Jones, A.'],)  # List becomes array
)

# Query with array contains
cur.execute(
    "SELECT * FROM papers WHERE 'cs.AI' = ANY(categories)"
)
```

**OpenSearch Basics:**
```python
# Index a document
PUT /papers/_doc/1
{
  "title": "Attention Is All You Need",
  "abstract": "The dominant sequence transduction...",
  "arxiv_id": "1706.03762"
}

# Search documents
GET /papers/_search
{
  "query": {
    "match": {
      "abstract": "transformer"
    }
  }
}
```

**Why Both Databases?**
- PostgreSQL: Structured metadata, relationships, transactions
- OpenSearch: Full-text search, relevance ranking, filters

#### Practice Requirements

**Exercise 1: Database Connection Pool**
- Create connection pool configuration
- Handle max connections limit
- Implement retry logic for failed connections
- Test concurrent access

**Exercise 2: Transaction Management**
```python
with conn:  # Automatic commit on success, rollback on error
    with conn.cursor() as cur:
        cur.execute("INSERT INTO papers ...")
        cur.execute("INSERT INTO sections ...")
        # Both succeed or both fail (atomic)
```

**Exercise 3: Complex Queries**
- Get papers published in last 7 days with specific category
- Count papers by category
- Find papers with specific author
- Update batch of papers' parsing status

**Exercise 4: OpenSearch Mapping**
```json
PUT /papers
{
  "mappings": {
    "properties": {
      "title": {"type": "text"},
      "abstract": {"type": "text"},
      "arxiv_id": {"type": "keyword"},
      "published_date": {"type": "date"}
    }
  }
}
```

#### End of Day 3 Checklist

- [ ] Installed psycopg3
- [ ] Created database connection module
- [ ] Implemented paper metadata table
- [ ] Created CRUD operations for papers
- [ ] Tested with sample data
- [ ] Understand parameterized queries
- [ ] Know how to handle PostgreSQL arrays
- [ ] OpenSearch running in Docker
- [ ] Created first OpenSearch index
- [ ] Indexed sample documents
- [ ] Performed basic searches
- [ ] Understand PostgreSQL vs OpenSearch use cases
- [ ] Spent approximately 90 minutes

---

### Day 4 (Thu Dec 4): OpenSearch Implementation + Airflow Basics

#### Primary Video Resources

**Video 1: "OpenSearch Python Client"**
- Link: https://opensearch.org/docs/latest/clients/python/
- Read documentation examples
- Duration: 20 min

**Video 2: "Apache Airflow Tutorial"**
- Link: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Duration: 51:00
- Watch: First 25 minutes (what is Airflow, DAGs, operators)

**Video 3: "Airflow in 100 Seconds"**
- Link: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Quick overview before deep dive

#### Reading Materials

**OpenSearch Python Client Guide:**
- Link: https://opensearch.org/docs/latest/clients/python/
- All basic examples
- Duration: 25 min

**Airflow Documentation:**
- Link: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
- Fundamental concepts
- Duration: 20 min

#### Day 4 Schedule (90 minutes total)

**Part 1: OpenSearch Python Integration (45 min)**

**Requirements:**

**1. Install OpenSearch Python client**
```bash
pip install opensearch-py
```

**2. Create OpenSearch connection module**
- Connect to OpenSearch cluster
- Handle authentication
- Error handling for connection failures
- Connection pooling configuration

**3. Implement paper search functionality**

**Index Mapping for Papers:**
```json
{
  "mappings": {
    "properties": {
      "arxiv_id": {"type": "keyword"},
      "title": {
        "type": "text",
        "analyzer": "english"
      },
      "abstract": {
        "type": "text",
        "analyzer": "english"
      },
      "full_text": {
        "type": "text",
        "analyzer": "english"
      },
      "authors": {"type": "text"},
      "categories": {"type": "keyword"},
      "published_date": {"type": "date"},
      "citation_count": {"type": "integer"}
    }
  }
}
```

**4. Implement operations**
- Index new paper (add to search)
- Bulk index multiple papers
- Search by keywords
- Filter by date range
- Filter by categories
- Sort by relevance or date
- Pagination for results

**What to figure out:**
- OpenSearch client initialization
- Document indexing (single and bulk)
- Query DSL structure
- Match queries vs term queries
- Boolean queries (must, should, filter)
- Pagination (from, size)
- Aggregations for statistics

**Test:**
- Index 10 sample papers
- Search for "transformer"
- Filter results by category "cs.AI"
- Get papers from last month
- Sort by publication date
- Paginate through results

---

**Part 2: Apache Airflow Fundamentals (30 min)**

**Requirements:**

**1. Understanding Airflow Concepts (15 min)**

**What to learn:**
- What is workflow orchestration
- Why not just cron jobs
- DAG (Directed Acyclic Graph) concept
- Operators and Tasks
- Task dependencies
- Scheduling and execution

**Core Concepts:**
- **DAG:** Workflow definition
- **Task:** Single unit of work
- **Operator:** Defines what a task does
- **Dependency:** Execution order between tasks
- **Schedule:** When DAG runs (cron expression)

**2. Install Airflow with Docker (15 min)**

**Using official Docker Compose:**
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up -d
```

**What this creates:**
- Airflow webserver (UI)
- Airflow scheduler (runs tasks)
- PostgreSQL (Airflow metadata)
- Redis (task queue)
- Worker (executes tasks)

**Access:**
- UI: http://localhost:8080
- Username: airflow
- Password: airflow

---

**Part 3: Reflection (15 min)**

**Document:**
1. How OpenSearch complements PostgreSQL
2. BM25 relevance scoring concept
3. What Airflow solves (vs manual scripts)
4. How you'll use Airflow for paper ingestion
5. DAG structure you'll build next week

#### Key Concepts to Master

**OpenSearch Client:**
```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'admin'),
    use_ssl=False
)

# Index document
client.index(
    index='papers',
    id='arxiv-1706.03762',
    body={
        'title': 'Attention Is All You Need',
        'abstract': '...',
        'arxiv_id': '1706.03762'
    }
)

# Search
response = client.search(
    index='papers',
    body={
        'query': {
            'match': {'abstract': 'transformer'}
        }
    }
)
```

**Bulk Indexing (Efficient):**
```python
from opensearchpy import helpers

actions = [
    {
        '_index': 'papers',
        '_id': paper['arxiv_id'],
        '_source': paper
    }
    for paper in papers_list
]

helpers.bulk(client, actions)
```

**Search with Filters:**
```python
{
    "query": {
        "bool": {
            "must": {
                "match": {"abstract": "deep learning"}
            },
            "filter": [
                {"term": {"categories": "cs.AI"}},
                {"range": {
                    "published_date": {
                        "gte": "2023-01-01"
                    }
                }}
            ]
        }
    },
    "from": 0,
    "size": 10
}
```

**Airflow DAG Structure:**
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'paper_ingestion',
    default_args=default_args,
    schedule='0 2 * * *',  # Daily at 2 AM
    start_date=datetime(2024, 12, 1),
    catchup=False
)

task1 = PythonOperator(
    task_id='fetch_papers',
    python_callable=fetch_from_arxiv,
    dag=dag
)

task2 = PythonOperator(
    task_id='download_pdfs',
    python_callable=download_pdfs,
    dag=dag
)

task1 >> task2  # task1 runs before task2
```

**Airflow Architecture:**
1. **Scheduler:** Monitors DAGs, triggers tasks
2. **Executor:** Runs tasks (sequential, parallel, distributed)
3. **Worker:** Executes task logic
4. **Metadata DB:** Stores DAG runs, task status
5. **Web UI:** Monitor, trigger, debug

#### Practice Requirements

**Exercise 1: Complex Search Query**
- Search papers with "attention mechanism"
- Filter: cs.AI category only
- Published after 2020
- Sort by date (newest first)
- Return top 20 results

**Exercise 2: Aggregations**
```python
{
    "aggs": {
        "papers_per_category": {
            "terms": {"field": "categories"}
        },
        "papers_per_month": {
            "date_histogram": {
                "field": "published_date",
                "calendar_interval": "month"
            }
        }
    }
}
```

**Exercise 3: First Airflow DAG**
- Create simple DAG
- Two tasks: task1 prints date, task2 prints success
- task2 depends on task1
- Schedule: daily
- Test in UI

#### End of Day 4 Checklist

- [ ] OpenSearch Python client installed
- [ ] Created OpenSearch connection module
- [ ] Implemented paper search functionality
- [ ] Tested keyword search
- [ ] Tested filtering by category and date
- [ ] Understand query DSL structure
- [ ] Know difference between match and term queries
- [ ] Airflow running via Docker Compose
- [ ] Accessed Airflow UI successfully
- [ ] Understand DAG, Task, Operator concepts
- [ ] Know Airflow use cases
- [ ] Spent approximately 90 minutes

---

### Day 5 (Fri Dec 5): Airflow Setup + Docker Compose Integration

#### Primary Video Resources

**Video 1: "Airflow DAGs Deep Dive"**
- Link: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Continue from 25:00 to 51:00
- Task dependencies, scheduling, error handling

**Video 2: "Docker Compose Tutorial"**
- Link: https://www.youtube.com/watch?v=Qw9zlE3t8Ko
- Duration: 31:00
- Watch: First 20 minutes

#### Reading Materials

**Airflow Best Practices:**
- Link: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
- Duration: 20 min

**Docker Compose Documentation:**
- Link: https://docs.docker.com/compose/
- Getting Started section
- Duration: 15 min

#### Day 5 Schedule (90 minutes total)

**Part 1: Advanced Airflow Concepts (35 min)**

**Requirements:**

**1. Task Dependencies Patterns (15 min)**

**What to learn:**
- Linear dependencies: A >> B >> C
- Fan-out: A >> [B, C, D] (A runs first, then B/C/D in parallel)
- Fan-in: [A, B, C] >> D (A/B/C run in parallel, then D)
- Conditional execution: BranchOperator
- Task groups for organization

**Examples:**
```python
# Linear
download >> parse >> index

# Fan-out (parallel downloads)
fetch >> [download_pdf1, download_pdf2, download_pdf3] >> combine

# Fan-in (parallel parsing, then index)
[parse_intro, parse_methods, parse_results] >> index_paper

# Conditional
check_file_size >> [process_large, process_small]
```

**2. Airflow Operators (20 min)**

**What to learn:**
- PythonOperator: Run Python function
- BashOperator: Run bash command
- PostgresOperator: Run SQL query
- HttpOperator: Make API calls
- CustomOperator: Create your own

**When to use each:**
- PythonOperator: Complex logic, API calls, data processing
- BashOperator: System commands, curl, file operations
- PostgresOperator: Database operations
- HttpOperator: REST API calls

**Practice:**
- Create DAG with PythonOperator
- Create DAG with BashOperator
- Create DAG combining both
- Implement error handling (on_failure_callback)

---

**Part 2: Docker Compose for Full Stack (40 min)**

**Requirements:**

**1. Create docker-compose.yml for entire system**

**Services to define:**
- FastAPI application
- PostgreSQL database
- OpenSearch cluster
- Airflow (webserver, scheduler, worker)
- Redis (for Airflow)

**What to figure out:**
- Service definitions
- Port mappings
- Volume mounts for persistence
- Environment variables
- Network configuration (services communicate)
- Health checks
- Startup order (depends_on)

**2. Environment variable management**
- Create .env file for secrets
- Database credentials
- API keys
- OpenSearch password
- Don't commit .env to git

**3. Data persistence**
- PostgreSQL data volume
- OpenSearch data volume
- Airflow logs volume
- Downloaded PDFs volume

**Test:**
- Start all services: `docker-compose up -d`
- Verify each service healthy: `docker-compose ps`
- FastAPI accessible
- PostgreSQL accepting connections
- OpenSearch responding
- Airflow UI accessible
- Stop all: `docker-compose down`

---

**Part 3: Reflection (15 min)**

**Document:**
1. Task dependency patterns you'll use
2. Which operators for which tasks
3. Why Docker Compose is better than manual Docker
4. Data persistence strategy
5. Network configuration understanding

#### Key Concepts to Master

**docker-compose.yml Structure:**
```yaml
version: '3.8'

services:
  # FastAPI application
  api:
    build: ./api
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:password@postgres:5432/papers
    depends_on:
      - postgres
      - opensearch
    volumes:
      - ./api:/app
    networks:
      - paper-network

  # PostgreSQL
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: papers
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - paper-network

  # OpenSearch
  opensearch:
    image: opensearchproject/opensearch:latest
    environment:
      - discovery.type=single-node
      - OPENSEARCH_INITIAL_ADMIN_PASSWORD=Admin123!
    volumes:
      - opensearch-data:/usr/share/opensearch/data
    ports:
      - "9200:9200"
    networks:
      - paper-network

volumes:
  postgres-data:
  opensearch-data:

networks:
  paper-network:
    driver: bridge
```

**Service Communication:**
- Services on same network use service name as hostname
- FastAPI connects to `postgres:5432` not `localhost:5432`
- Inside container, service names resolve to IP addresses

**Environment Variables:**
```yaml
# In docker-compose.yml
environment:
  DATABASE_URL: ${DATABASE_URL}

# Or use env_file
env_file:
  - .env
```

**Health Checks:**
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:9200"]
  interval: 30s
  timeout: 10s
  retries: 5
  start_period: 40s
```

**Startup Order:**
```yaml
depends_on:
  postgres:
    condition: service_healthy
  opensearch:
    condition: service_healthy
```

**Airflow DAG Best Practices:**
- Keep DAGs simple and readable
- Use meaningful task_ids
- Set proper retries and retry_delay
- Use execution_date for idempotency
- Don't process data in DAG file (only in operators)
- Use XCom for small data between tasks
- Use external storage for large data

**Task Dependencies:**
```python
# Method 1: Bitshift operators
task1 >> task2 >> task3

# Method 2: set_downstream/set_upstream
task1.set_downstream(task2)
task2.set_downstream(task3)

# Method 3: List
task1 >> [task2, task3] >> task4

# Method 4: chain (for linear dependencies)
from airflow.models.baseoperator import chain
chain(task1, task2, task3, task4)
```

#### Practice Requirements

**Exercise 1: Complete docker-compose.yml**
- Define all 5 services
- Configure networking
- Set up volumes
- Add health checks
- Test: bring up stack, verify all services

**Exercise 2: Multi-Stage DAG**
- Stage 1: Check arXiv for new papers
- Stage 2: Download PDFs (3 parallel tasks)
- Stage 3: Combine results
- Stage 4: Update database
- Implement with proper dependencies

**Exercise 3: Error Handling**
- Add on_failure_callback
- Add on_retry_callback
- Add on_success_callback
- Test by forcing task failure

#### End of Day 5 Checklist

- [ ] Understand all Airflow operators
- [ ] Know task dependency patterns
- [ ] Can create DAGs with multiple tasks
- [ ] Implemented error handling in DAG
- [ ] Created complete docker-compose.yml
- [ ] Defined all required services
- [ ] Configured networking between services
- [ ] Set up data persistence volumes
- [ ] Services can communicate via service names
- [ ] Understand depends_on and health checks
- [ ] Tested starting/stopping full stack
- [ ] Spent approximately 90 minutes

---

### Day 6 (Sat Dec 6): Complete Docker Compose Stack

#### Day 6 Schedule (4 hours total)

**Hour 1: Build Complete docker-compose.yml (60 min)**
**Hour 2: Service Integration & Testing (60 min)**
**Hour 3: Health Checks & Monitoring (60 min)**
**Hour 4: Polish & Documentation (60 min)**

---

### HOUR 1: Build Complete docker-compose.yml

**Requirements:**

**Complete Stack Definition**

**Services needed:**
1. FastAPI application
2. PostgreSQL database
3. OpenSearch cluster
4. Airflow webserver
5. Airflow scheduler
6. Airflow worker
7. Redis (for Airflow)

**For EACH service, define:**
- Base image or build context
- Container name
- Port mappings (host:container)
- Environment variables
- Volume mounts
- Network assignment
- Health check configuration
- Restart policy
- Dependencies (depends_on)
- Resource limits (optional but recommended)

**Networking requirements:**
- Create bridge network: paper-network
- All services on same network
- Services access each other by service name
- Expose only necessary ports to host

**Volume requirements:**
- postgres-data: PostgreSQL data persistence
- opensearch-data: OpenSearch index persistence
- airflow-logs: Airflow execution logs
- airflow-dags: DAG files (bind mount to local)
- pdfs-storage: Downloaded PDFs persistence

**Environment variables:**
- PostgreSQL: DB name, user, password
- OpenSearch: admin password, memory settings
- Airflow: executor type, database connection
- FastAPI: database URL, OpenSearch URL, environment (dev/prod)

**What to figure out:**
- Correct image versions to use
- Port mapping without conflicts
- Volume mount paths in each container
- Environment variable formats for each service
- Proper health check commands
- Startup order to prevent failures

**Success criteria:**
- All services defined
- No port conflicts
- Proper network configuration
- All volumes declared
- Environment variables parameterized
- Health checks for critical services
- Clear, readable YAML structure

---

### HOUR 2: Service Integration & Testing

**Task 1: Verify Service Communication (30 min)**

**Requirements:**

**Test PostgreSQL connectivity:**
- FastAPI can connect to postgres:5432
- Airflow can connect for metadata storage
- Run test query from each service
- Verify connection pooling works

**Test OpenSearch connectivity:**
- FastAPI can reach opensearch:9200
- Can create index from FastAPI
- Can search documents
- Verify authentication works

**Test Redis connectivity:**
- Airflow can use Redis for task queue
- Verify Celery executor working

**What to test:**
- From FastAPI container: Test Python can connect to PostgreSQL
- From Airflow scheduler: Run Airflow database check command
- Test OpenSearch health endpoint accessibility
- Verify each service can reach others by service name

---

**Task 2: End-to-End Workflow Test (30 min)**

**Requirements:**

**Create test workflow:**
1. Insert test paper metadata via FastAPI endpoint
2. Verify stored in PostgreSQL
3. Index same paper in OpenSearch via API
4. Search for paper in OpenSearch
5. Retrieve paper metadata from PostgreSQL
6. Verify consistency

**Test scenarios:**
- Happy path: All services working
- PostgreSQL down: FastAPI handles gracefully
- OpenSearch down: Search returns error but app doesn't crash
- Restart services: Data persists

**What to verify:**
- Data persistence after restart
- Error handling for service failures
- Connection retry logic
- Timeout handling

---

### HOUR 3: Health Checks & Monitoring

**Task 1: Implement Comprehensive Health Checks (30 min)**

**Requirements:**

**For each service:**

**PostgreSQL:**
```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U postgres"]
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 10s
```

**OpenSearch:**
```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost:9200/_cluster/health || exit 1"]
  interval: 30s
  timeout: 10s
  retries: 5
  start_period: 60s
```

**FastAPI:**
```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost:8000/health || exit 1"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

**Airflow Webserver:**
```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 60s
```

**What to figure out:**
- Appropriate intervals for each service
- Correct health endpoints
- Startup periods (services need time to initialize)
- Retry counts
- Timeout values

---

**Task 2: Create Monitoring Endpoints (30 min)**

**Requirements:**

**Add to FastAPI application:**

**GET /health**
- Returns 200 if service healthy
- Checks PostgreSQL connection
- Checks OpenSearch connection
- Returns JSON with service status
```json
{
  "status": "healthy",
  "postgres": "connected",
  "opensearch": "connected",
  "timestamp": "2024-12-06T10:30:00Z"
}
```

**GET /metrics**
- Total papers in database
- Total papers in OpenSearch
- Last ingestion time
- Storage usage
- Service uptime

**Implement in each service:**
- Graceful shutdown handlers
- Log rotation configuration
- Error logging to files
- Service startup logs

**Test:**
- Verify health endpoint returns 200
- Verify metrics endpoint returns valid data
- Check logs are being written
- Test health check during service restart

---

### HOUR 4: Polish & Documentation

**Task 1: Create Comprehensive README (30 min)**

**Requirements:**

**Document structure:**

**1. System Architecture Section**
- Architecture diagram (ASCII or image)
- Service descriptions
- Port mappings reference
- Network diagram
- Data flow explanation

**2. Prerequisites Section**
- Docker Desktop/Engine version
- Docker Compose version
- System requirements (RAM, disk)
- Operating system compatibility

**3. Installation Section**
```bash
# Clone repository
git clone <repo>
cd paper-rag-system

# Create environment file
cp .env.example .env
# Edit .env with your values

# Build and start services
docker-compose up -d

# Verify all services running
docker-compose ps

# Check logs
docker-compose logs -f
```

**4. Configuration Section**
- Environment variables explanation
- Each variable's purpose
- Default values
- Required vs optional
- Security considerations

**5. Usage Section**
- Accessing each service
- FastAPI: http://localhost:8000/docs
- Airflow: http://localhost:8080
- OpenSearch: http://localhost:9200
- PostgreSQL: localhost:5432

**6. Troubleshooting Section**
- Common issues and solutions
- "Service unhealthy": Check health endpoint
- "Port already in use": Change ports in docker-compose.yml
- "Can't connect to PostgreSQL": Check connection string
- How to view logs: `docker-compose logs <service>`
- How to restart service: `docker-compose restart <service>`

**7. Maintenance Section**
- Backup procedures
- Update procedures
- Scaling considerations
- Data cleanup

---

**Task 2: Create .env.example (10 min)**

**Requirements:**

```bash
# PostgreSQL Configuration
POSTGRES_DB=papers_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=change_me_in_production
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# OpenSearch Configuration
OPENSEARCH_HOST=opensearch
OPENSEARCH_PORT=9200
OPENSEARCH_USER=admin
OPENSEARCH_PASSWORD=Admin123!
OPENSEARCH_INITIAL_ADMIN_PASSWORD=Admin123!

# FastAPI Configuration
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=development

# Airflow Configuration
AIRFLOW__CORE__EXECUTOR=CeleryExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:password@postgres/airflow
AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://postgres:password@postgres/airflow
AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0
AIRFLOW__CORE__FERNET_KEY=<generate_key>
AIRFLOW__WEBSERVER__SECRET_KEY=<generate_key>

# arXiv Configuration (for Week 4)
ARXIV_API_BASE=http://export.arxiv.org/api/query
ARXIV_MAX_RESULTS=100
ARXIV_CATEGORIES=cs.AI,cs.CL,cs.LG

# Storage Configuration
PDF_STORAGE_PATH=/app/data/pdfs
```

**Document:**
- How to generate Fernet key
- Security warning about default passwords
- Which values must be changed for production

---

**Task 3: Final Testing & Validation (20 min)**

**Requirements:**

**Complete test checklist:**
- [ ] `docker-compose up -d` succeeds
- [ ] All services show "healthy" in `docker-compose ps`
- [ ] FastAPI /health endpoint returns 200
- [ ] Airflow UI accessible at localhost:8080
- [ ] PostgreSQL accepting connections
- [ ] OpenSearch responding to queries
- [ ] Can create test paper via API
- [ ] Paper stored in PostgreSQL
- [ ] Paper indexed in OpenSearch
- [ ] Can retrieve paper via both databases
- [ ] `docker-compose down` cleans up properly
- [ ] `docker-compose up -d` again, data persists
- [ ] Logs accessible: `docker-compose logs`

**Test failure scenarios:**
- Stop PostgreSQL: FastAPI handles gracefully
- Stop OpenSearch: Search fails but app doesn't crash
- Restart one service: Others continue working
- Kill container: Docker restarts automatically

---

### Day 6 Deliverables

**Working Infrastructure:**
- [ ] Complete docker-compose.yml with all services
- [ ] All services running and healthy
- [ ] Service-to-service communication working
- [ ] Data persistence configured
- [ ] Health checks implemented
- [ ] Monitoring endpoints functional

**Documentation:**
- [ ] README.md with full instructions
- [ ] .env.example with all variables
- [ ] Architecture diagram/description
- [ ] Troubleshooting guide
- [ ] Usage instructions

**Code Quality:**
- [ ] Clean YAML formatting
- [ ] Meaningful service names
- [ ] Proper indentation
- [ ] Comments for complex configurations
- [ ] Security considerations documented

**Testing:**
- [ ] End-to-end workflow tested
- [ ] Failure scenarios tested
- [ ] Data persistence verified
- [ ] Restart tested
- [ ] All health checks passing

### Common Issues & Solutions

**Issue: "Port 5432 already in use"**
- Solution: Change host port in docker-compose.yml: "5433:5432"
- Or stop local PostgreSQL: `sudo service postgresql stop`

**Issue: "OpenSearch won't start - vm.max_map_count too low"**
- Solution: `sudo sysctl -w vm.max_map_count=262144`
- Make permanent: Add to /etc/sysctl.conf

**Issue: "Airflow webserver healthy but can't access UI"**
- Solution: Check firewall, verify port mapping, check logs

**Issue: "Services can't communicate"**
- Solution: Verify all on same network, use service names not localhost

**Issue: "Out of disk space"**
- Solution: Prune unused data: `docker system prune -a --volumes`

---

### Day 7 (Sun Dec 7): Health Checks, Testing & Documentation

#### Day 7 Schedule (3 hours total)

**Hour 1: System Testing & Validation (60 min)**
**Hour 2: Documentation & Examples (60 min)**
**Hour 3: Week 3 Reflection & Week 4 Prep (60 min)**

---

### HOUR 1: System Testing & Validation

**Task 1: Comprehensive Integration Tests (30 min)**

**Requirements:**

**Test Suite 1: Basic Connectivity**
- [ ] PostgreSQL accessible from host
- [ ] OpenSearch accessible from host
- [ ] FastAPI accessible from host
- [ ] Airflow UI accessible from host
- [ ] All services see each other (internal network)

**Test Suite 2: Data Flow**
- [ ] Create paper via FastAPI API
- [ ] Verify in PostgreSQL database
- [ ] Index same paper in OpenSearch
- [ ] Search via OpenSearch API
- [ ] Retrieve via FastAPI API
- [ ] Verify data consistency

**Test Suite 3: Persistence**
- [ ] Create test data
- [ ] `docker-compose down`
- [ ] `docker-compose up -d`
- [ ] Verify data still exists
- [ ] Test volumes are working

**Test Suite 4: Error Handling**
- [ ] Stop PostgreSQL, FastAPI handles error
- [ ] Stop OpenSearch, search returns error
- [ ] Invalid data to API, proper error response
- [ ] Duplicate paper, conflict handling

**Test Suite 5: Performance**
- [ ] Bulk insert 100 papers
- [ ] Measure insert time
- [ ] Bulk search 50 queries
- [ ] Measure search time
- [ ] Verify no memory leaks

**What to document:**
- Test results for each suite
- Any failures and fixes
- Performance baseline metrics
- Known issues or limitations

---

**Task 2: Create Test Scripts (30 min)**

**Requirements:**

**Create test_infrastructure.py:**
- Test database connection
- Test OpenSearch connection
- Test FastAPI endpoints
- Test Airflow API
- Run all tests with pytest
- Generate test report

**Create test_data_flow.py:**
- Insert test paper
- Verify in database
- Index in OpenSearch
- Search for paper
- Delete paper
- Verify cleanup

**Create load_test.py:**
- Insert 1000 test papers
- Measure throughput
- Check error rate
- Verify system stability

**Run tests:**
```bash
pytest tests/test_infrastructure.py -v
pytest tests/test_data_flow.py -v
pytest tests/load_test.py -v
```

**Success criteria:**
- All tests pass
- Clear error messages for failures
- Tests are repeatable
- Tests clean up after themselves

---

### HOUR 2: Documentation & Examples

**Task 1: Create API Examples (30 min)**

**Requirements:**

**Create EXAMPLES.md with:**

**Example 1: Create Paper**
```bash
curl -X POST http://localhost:8000/papers \
  -H "Content-Type: application/json" \
  -d '{
    "arxiv_id": "1706.03762",
    "title": "Attention Is All You Need",
    "authors": ["Vaswani, A.", "Shazeer, N."],
    "abstract": "The dominant sequence transduction...",
    "categories": ["cs.LG", "cs.AI"],
    "published_date": "2017-06-12"
  }'
```

**Example 2: Search Papers**
```bash
curl -X GET "http://localhost:8000/papers/search?query=transformer&category=cs.AI"
```

**Example 3: Get Paper by ID**
```bash
curl http://localhost:8000/papers/1706.03762
```

**Example 4: Update Paper Status**
```bash
curl -X PATCH http://localhost:8000/papers/1706.03762/status \
  -H "Content-Type: application/json" \
  -d '{"status": "parsed"}'
```

**Example 5: Direct PostgreSQL Query**
```bash
docker exec -it postgres psql -U postgres -d papers_db \
  -c "SELECT arxiv_id, title FROM papers LIMIT 5;"
```

**Example 6: Direct OpenSearch Query**
```bash
curl -X GET "http://localhost:9200/papers/_search?q=transformer"
```

---

**Task 2: Create Architecture Documentation (30 min)**

**Requirements:**

**Create ARCHITECTURE.md:**

**Section 1: System Overview**
- High-level architecture diagram
- Component descriptions
- Technology stack
- Design decisions

**Section 2: Service Details**

**For each service document:**
- Purpose and responsibility
- Technology used
- Port mappings
- Environment variables
- Data storage
- Dependencies

**Section 3: Data Flow**
- Paper ingestion flow (Week 4 preview)
- Search flow
- API request flow
- Database interactions

**Section 4: Database Schemas**

**PostgreSQL tables:**
```sql
CREATE TABLE papers (
    paper_id VARCHAR(50) PRIMARY KEY,
    arxiv_id VARCHAR(20) UNIQUE NOT NULL,
    title TEXT NOT NULL,
    authors TEXT[],
    abstract TEXT,
    categories VARCHAR(50)[],
    published_date DATE,
    pdf_url TEXT,
    pdf_path TEXT,
    downloaded_at TIMESTAMP,
    parsed_at TIMESTAMP,
    parsing_status VARCHAR(20) CHECK (parsing_status IN ('pending', 'downloaded', 'parsed', 'failed')),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_published_date ON papers(published_date);
CREATE INDEX idx_parsing_status ON papers(parsing_status);
CREATE INDEX idx_categories ON papers USING GIN (categories);
```

**OpenSearch mappings:**
```json
{
  "papers": {
    "mappings": {
      "properties": {
        "arxiv_id": {"type": "keyword"},
        "title": {"type": "text", "analyzer": "english"},
        "abstract": {"type": "text", "analyzer": "english"},
        "full_text": {"type": "text", "analyzer": "english"},
        "authors": {"type": "text"},
        "categories": {"type": "keyword"},
        "published_date": {"type": "date"}
      }
    }
  }
}
```

**Section 5: Network Architecture**
- Bridge network configuration
- Service discovery
- Port mappings
- Security considerations

**Section 6: Volume Architecture**
- Data persistence strategy
- Backup considerations
- Volume locations
- Cleanup procedures

---

### HOUR 3: Week 3 Reflection & Week 4 Prep

**Task 1: Week 3 Reflection (30 min)**

**Requirements:**

**Create WEEK3_REFLECTION.md:**

**What you learned:**
- Docker containerization concepts
- Docker Compose orchestration
- PostgreSQL relational database
- OpenSearch full-text search
- Apache Airflow workflow orchestration
- Service networking
- Data persistence
- Health checks and monitoring

**What was challenging:**
- Most difficult concepts
- Bugs encountered
- Time management
- Balance between depth and breadth

**What clicked:**
- "Aha!" moments
- Concepts that made sense suddenly
- Connections between technologies

**How it connects to ML/AI:**
- Why these tools matter for ML pipelines
- Production ML infrastructure
- Scalability considerations
- Real-world applications in fintech

**Skills assessment:**
- Docker proficiency: 1-10
- PostgreSQL proficiency: 1-10
- OpenSearch proficiency: 1-10
- Airflow proficiency: 1-10
- Overall confidence: 1-10

---

**Task 2: Week 4 Preparation (30 min)**

**Requirements:**

**Review Week 4 Plan:**
- Day 8 (Mon): arXiv API Integration
- Day 9 (Tue): PDF Download Logic
- Day 10 (Wed): GROBID Setup + XML Parsing
- Day 11 (Thu): Docling Fallback Parser
- Day 12 (Fri): Airflow DAG Creation
- Day 13 (Sat): Automated Daily Pipeline
- Day 14 (Sun): Testing, Monitoring & Documentation

**Prepare for arXiv API (Day 8):**
- Read arXiv API documentation: https://arxiv.org/help/api/user-manual
- Understand query parameters
- Look at example responses (XML format)
- Identify fields you'll extract
- Plan data validation

**Prepare for PDF processing:**
- Research GROBID (academic PDF parser)
- Understand why PDF parsing is hard
- Review Docling as fallback
- Plan storage strategy for PDFs

**Prepare for Airflow DAG:**
- Sketch out task flow on paper
- Identify all steps in pipeline
- Plan error handling
- Think about scheduling (daily at 2 AM?)

**Set up accounts/access:**
- No API key needed for arXiv
- GROBID runs locally (Docker)
- Docling is open source

**Mental preparation:**
- Week 4 is implementation-heavy
- You have all infrastructure ready
- Focus on data pipeline logic
- Debugging will be important

---

## Week 3 Summary

### What You've Completed

**Infrastructure:**
- ✅ Docker fundamentals and containerization
- ✅ FastAPI containerized application
- ✅ PostgreSQL database setup and integration
- ✅ OpenSearch full-text search engine
- ✅ Apache Airflow workflow orchestration
- ✅ Complete Docker Compose stack

**Skills:**
- ✅ Docker commands and Dockerfile creation
- ✅ PostgreSQL table design and SQL operations
- ✅ Python database integration (psycopg3)
- ✅ OpenSearch indexing and searching
- ✅ Airflow DAG creation and task dependencies
- ✅ Service networking and communication

**Deliverables:**
- ✅ Working Docker Compose infrastructure
- ✅ All services communicating
- ✅ Data persistence configured
- ✅ Health checks implemented
- ✅ Comprehensive documentation

**Total Time:** ~14.5 hours
- Weekdays: 7.5 hours (1.5h/day)
- Weekend: 7 hours (4h Sat, 3h Sun)

---

## WEEK 4: DATA PIPELINE

### Day 8 (Mon Dec 8): arXiv API Integration

#### Primary Video Resources

**Video 1: "Working with arXiv API"**
- Link: https://www.youtube.com/watch?v=I1Z7aHvFGFk
- Duration: 12:00
- Practical examples

**Video 2: "XML Parsing in Python"**
- Link: https://www.youtube.com/watch?v=j0xr0-IAqyk
- Duration: 15:00
- ElementTree basics

#### Reading Materials

**arXiv API Documentation:**
- Link: https://arxiv.org/help/api/user-manual
- Duration: 45 min
- Complete guide to API

**Article: "Building Data Pipelines"**
- Link: https://realpython.com/python-data-pipeline/
- Duration: 20 min

#### Day 8 Schedule (90 minutes total)

**Part 1: Understanding arXiv API (30 min)**

**Requirements:**

**1. Read API documentation (15 min)**

**What to understand:**
- Base URL: http://export.arxiv.org/api/query
- Query parameters (search_query, max_results, start)
- Response format (Atom XML)
- Rate limits (3 seconds between requests)
- Search field codes (ti: title, au: author, cat: category, abs: abstract)

**2. Test API manually (15 min)**

**Test queries:**
```bash
# Get latest AI papers
curl "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=5"

# Search by keyword
curl "http://export.arxiv.org/api/query?search_query=all:transformer&max_results=5"

# Multiple categories
curl "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG&max_results=5"

# Date range
curl "http://export.arxiv.org/api/query?search_query=cat:cs.AI+AND+submittedDate:[20240101+TO+20240131]&max_results=5"
```

**Examine response:**
- Entry structure
- Available fields (id, title, summary, authors, category, published, updated)
- PDF link location
- How to parse XML

---

**Part 2: Create arXiv Client (45 min)**

**Requirements:**

**Create arxiv_client.py module:**

**Class: ArxivClient**

**Methods to implement:**

**1. `__init__(self, base_url, rate_limit_seconds)`**
- Initialize with base URL
- Set rate limit (3 seconds default)
- Track last request time

**2. `search(category, max_results, start=0)`**
- Build query URL
- Respect rate limits (sleep if needed)
- Make GET request
- Handle HTTP errors
- Return XML response
- Log request details

**3. `parse_entry(entry_xml)`**
- Extract arxiv_id from entry ID
- Extract title (clean whitespace)
- Extract authors (list of author objects)
- Extract abstract/summary
- Extract categories
- Extract published date
- Extract PDF URL
- Extract updated date
- Return dictionary

**4. `fetch_papers(category, max_results)`**
- Call search method
- Parse XML response (use xml.etree.ElementTree)
- Loop through entries
- Parse each entry
- Collect papers list
- Handle parsing errors
- Return list of paper dictionaries

**5. `fetch_recent_papers(categories, days=7, max_per_category=100)`**
- Calculate date range (today - days)
- For each category in categories list
- Build date-filtered query
- Fetch papers
- Collect all results
- Remove duplicates (same arxiv_id)
- Sort by published date (newest first)
- Return combined list

**Error handling:**
- HTTP errors (network issues, API down)
- XML parsing errors (malformed response)
- Missing fields in entries (handle gracefully)
- Rate limit errors (429 status code)
- Timeout errors

**What to figure out:**
- XML namespace handling in arXiv responses
- Proper date parsing (ISO 8601 format)
- Rate limiting implementation (time.sleep)
- Logging best practices
- Request retries with exponential backoff
- Clean data extraction (strip whitespace, handle None)

---

**Part 3: Testing & Validation (15 min)**

**Requirements:**

**Test script: test_arxiv_client.py**

**Test cases:**

**1. Test single category fetch**
- Fetch 5 cs.AI papers
- Verify 5 papers returned
- Verify required fields present
- Print sample paper

**2. Test multiple categories**
- Fetch from ['cs.AI', 'cs.LG']
- Verify papers from both categories
- Verify no duplicates

**3. Test recent papers**
- Fetch papers from last 7 days
- Verify date filtering works
- Verify sorted by date

**4. Test error handling**
- Invalid category (empty results OK)
- Network timeout (should retry)
- Malformed response (should log and continue)

**5. Test rate limiting**
- Make 3 requests rapidly
- Verify 3 second gaps between requests
- Check logs for rate limit enforcement

**Success criteria:**
- All tests pass
- No crashes on errors
- Rate limits respected
- Clean data extraction
- Logging informative

#### Key Concepts to Master

**arXiv API Query Structure:**
```
http://export.arxiv.org/api/query?
  search_query=cat:cs.AI&
  start=0&
  max_results=10&
  sortBy=submittedDate&
  sortOrder=descending
```

**XML Parsing with ElementTree:**
```python
import xml.etree.ElementTree as ET

# Parse XML string
root = ET.fromstring(xml_string)

# Namespace handling (arXiv uses Atom namespace)
ns = {'atom': 'http://www.w3.org/2005/Atom'}

# Find all entries
entries = root.findall('atom:entry', ns)

# Extract text from element
title = entry.find('atom:title', ns).text.strip()

# Handle missing elements
category = entry.find('atom:category', ns)
if category is not None:
    category_text = category.get('term')
```

**Rate Limiting:**
```python
import time

class RateLimiter:
    def __init__(self, min_interval):
        self.min_interval = min_interval
        self.last_request = 0
    
    def wait(self):
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request = time.time()
```

**Retry Logic:**
```python
import requests
from time import sleep

def fetch_with_retry(url, max_retries=3, backoff=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = backoff ** attempt
            print(f"Retry {attempt + 1} after {wait_time}s")
            sleep(wait_time)
```

**Data Validation:**
```python
def validate_paper(paper_dict):
    required_fields = ['arxiv_id', 'title', 'abstract', 'published_date']
    
    for field in required_fields:
        if field not in paper_dict or not paper_dict[field]:
            return False, f"Missing {field}"
    
    # Validate arxiv_id format
    if not paper_dict['arxiv_id'].startswith(('http://arxiv.org/abs/', '1', '2')):
        return False, "Invalid arxiv_id format"
    
    return True, "Valid"
```

#### Practice Requirements

**Exercise 1: Build Query String**
- Function that builds arXiv query URL
- Parameters: category, max_results, start, date_from, date_to
- Returns properly formatted URL string

**Exercise 2: Parse Authors**
- arXiv returns multiple author elements
- Extract all author names
- Return as list of strings
- Handle cases with 1, 5, or 20 authors

**Exercise 3: Extract arXiv ID**
- From: http://arxiv.org/abs/1706.03762v2
- Extract: 1706.03762
- Remove version suffix (v2)
- Handle different ID formats

**Exercise 4: Date Range Query**
- Fetch papers published between two dates
- Use submittedDate filter in query
- Parse and format dates correctly

#### End of Day 8 Checklist

- [ ] Understand arXiv API structure
- [ ] Know query parameters and format
- [ ] Created ArxivClient class
- [ ] Implemented search method with rate limiting
- [ ] Implemented XML parsing
- [ ] Implemented data extraction
- [ ] Handle errors gracefully
- [ ] Created test script
- [ ] All tests passing
- [ ] Can fetch papers from arXiv
- [ ] Data validation working
- [ ] Spent approximately 90 minutes

---

### Day 9 (Tue Dec 9): PDF Download Logic + Storage

#### Primary Video Resources

**Video 1: "Downloading Files with Python"**
- Link: https://www.youtube.com/watch?v=_Zr1z_FVpHs
- Duration: 15:00
- requests library file downloads

**Video 2: "File Management in Python"**
- Link: https://realpython.com/working-with-files-in-python/
- Duration: 20 min reading
- File I/O, paths, organization

#### Reading Materials

**Article: "Downloading Large Files"**
- Link: https://www.geeksforgeeks.org/downloading-files-web-using-python/
- Duration: 10 min

**Article: "Python Path Management"**
- Link: https://realpython.com/python-pathlib/
- Duration: 15 min

#### Day 9 Schedule (90 minutes total)

**Part 1: PDF Download Manager (45 min)**

**Requirements:**

**Create pdf_downloader.py module:**

**Class: PDFDownloader**

**Methods to implement:**

**1. `__init__(self, storage_path, rate_limit_seconds)`**
- Set base storage directory
- Set rate limit between downloads
- Track last download time
- Create storage directories if needed

**2. `generate_filepath(arxiv_id)`**
- Generate organized file path
- Structure: /storage/YYYY/MM/arxiv_id.pdf
- Extract year/month from arxiv_id
- Create subdirectories if needed
- Return Path object

**3. `download_pdf(pdf_url, arxiv_id)`**
- Check if already downloaded (skip if exists)
- Respect rate limits
- Stream download (don't load entire file to memory)
- Save to generated filepath
- Verify download (check file size > 0)
- Handle download errors
- Return filepath if success, None if failure

**4. `batch_download(papers_list)`**
- Loop through papers
- Extract PDF URL for each
- Download with rate limiting
- Track successes and failures
- Return statistics (downloaded, failed, skipped)
- Log progress

**5. `verify_pdf(filepath)`**
- Check file exists
- Check file size reasonable (> 1KB, < 50MB typically)
- Try to open with PyPDF2 (verify it's valid PDF)
- Return True/False

**What to figure out:**
- Streaming downloads for large files
- File organization strategy
- Handling partial downloads
- Checking existing files before re-downloading
- Progress tracking for batches
- Error handling (network errors, disk full, corrupted downloads)
- Logging download statistics

---

**Part 2: Storage Organization (25 min)**

**Requirements:**

**1. Design directory structure**

**Proposed structure:**
```
/data/pdfs/
├── 2024/
│   ├── 01/
│   │   ├── 2401.00001.pdf
│   │   └── 2401.00002.pdf
│   ├── 02/
│   └── 12/
├── 2023/
└── failed/     # PDFs that failed to download after retries
```

**Benefits:**
- Easy to navigate by date
- Reasonable number of files per directory
- Can process by month
- Can clean up old data easily

**2. Implement storage manager**

**Class: StorageManager**

**Methods:**
- `get_storage_stats()`: Total files, total size, by year/month
- `find_pdf(arxiv_id)`: Locate PDF by arxiv_id
- `cleanup_failed()`: Remove failed downloads
- `get_pdfs_by_date_range(start, end)`: Get all PDFs in date range
- `verify_all_pdfs()`: Check all PDFs are valid

**3. Database integration**

**Update papers table:**
```sql
ALTER TABLE papers
ADD COLUMN pdf_path TEXT,
ADD COLUMN pdf_size_bytes BIGINT,
ADD COLUMN download_attempts INTEGER DEFAULT 0,
ADD COLUMN download_error TEXT;
```

**After successful download:**
- Update pdf_path in database
- Update pdf_size_bytes
- Update downloaded_at timestamp
- Set parsing_status to 'downloaded'

**After failed download:**
- Increment download_attempts
- Store download_error message
- Set parsing_status to 'failed' if max attempts reached

---

**Part 3: Testing & Integration (20 min)**

**Requirements:**

**Test script: test_pdf_download.py**

**Test cases:**

**1. Test single download**
- Pick one paper's PDF URL
- Download using PDFDownloader
- Verify file exists
- Verify file valid PDF
- Verify database updated

**2. Test batch download**
- Download 5 papers
- Track statistics
- Verify all 5 downloaded
- Verify file organization correct

**3. Test resume capability**
- Download 5 papers
- Try downloading same 5 again
- Should skip existing (fast)
- Verify skip count correct

**4. Test error handling**
- Invalid PDF URL (404 error)
- Network timeout simulation
- Disk space simulation (if possible)
- Corrupted PDF handling

**5. Test storage stats**
- Download 10 papers
- Get storage statistics
- Verify counts and sizes correct
- Group by year/month

**Success criteria:**
- Downloads work reliably
- Rate limiting enforced
- Database updated correctly
- Error handling robust
- Can resume interrupted downloads
- Storage organized properly

#### Key Concepts to Master

**Streaming Downloads:**
```python
import requests

def download_file(url, filepath):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
```

**Path Management:**
```python
from pathlib import Path

# Create nested directories
storage_path = Path('/data/pdfs/2024/01')
storage_path.mkdir(parents=True, exist_ok=True)

# Build filepath
filepath = storage_path / f'{arxiv_id}.pdf'

# Check if exists
if filepath.exists():
    print("Already downloaded")

# Get file size
size_bytes = filepath.stat().st_size
```

**PDF Validation:**
```python
from PyPDF2 import PdfReader

def is_valid_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        return num_pages > 0
    except Exception:
        return False
```

**Database Update After Download:**
```python
def update_paper_download_status(arxiv_id, pdf_path, size_bytes):
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE papers 
                SET pdf_path = %s,
                    pdf_size_bytes = %s,
                    downloaded_at = NOW(),
                    parsing_status = 'downloaded'
                WHERE arxiv_id = %s
            """, (pdf_path, size_bytes, arxiv_id))
```

**Batch Processing with Progress:**
```python
from tqdm import tqdm

def batch_download(papers, downloader):
    results = {'success': 0, 'failed': 0, 'skipped': 0}
    
    for paper in tqdm(papers, desc="Downloading PDFs"):
        if downloader.already_exists(paper['arxiv_id']):
            results['skipped'] += 1
            continue
        
        filepath = downloader.download_pdf(
            paper['pdf_url'], 
            paper['arxiv_id']
        )
        
        if filepath:
            results['success'] += 1
        else:
            results['failed'] += 1
    
    return results
```

#### Practice Requirements

**Exercise 1: Extract Year/Month from arXiv ID**
- arXiv ID format: YYMM.NNNNN (e.g., 2401.00123 = January 2024)
- Older format: arxiv-category/YYMMNNN
- Extract year and month for directory organization

**Exercise 2: Implement Retry Logic**
- Max 3 download attempts
- Exponential backoff (wait 2s, 4s, 8s)
- Log each attempt
- Update database with attempt count

**Exercise 3: Storage Cleanup**
- Find PDFs with failed status in database
- Check if files exist on disk
- Delete orphaned files
- Update database if needed

**Exercise 4: Parallel Downloads (Optional)**
- Use ThreadPoolExecutor
- Download 10 PDFs concurrently
- Maintain rate limiting globally
- Handle thread-safe file writes

#### End of Day 9 Checklist

- [ ] Created PDFDownloader class
- [ ] Implemented download method
- [ ] Streaming downloads working
- [ ] Rate limiting implemented
- [ ] File organization by year/month
- [ ] Database updates after download
- [ ] Created StorageManager class
- [ ] Implemented storage statistics
- [ ] Error handling for download failures
- [ ] Can resume interrupted downloads
- [ ] PDF validation working
- [ ] Test script with all test cases
- [ ] All tests passing
- [ ] Spent approximately 90 minutes

---

### Remaining Days (Wed-Sun) Preview

**Day 10 (Wed): GROBID Setup + XML Parsing**
- Install GROBID via Docker
- Understand GROBID output format (TEI XML)
- Parse sections, citations, figures
- Extract structured content

**Day 11 (Thu): Docling Fallback Parser**
- Install Docling
- Implement fallback logic (try GROBID first, then Docling)
- Compare output quality
- Store parsed content in PostgreSQL

**Day 12 (Fri): Airflow DAG Creation**
- Design complete pipeline DAG
- Task 1: Fetch papers from arXiv
- Task 2: Download PDFs (parallel)
- Task 3: Parse with GROBID/Docling
- Task 4: Index in OpenSearch
- Task dependencies and error handling

**Day 13 (Sat): Automated Daily Pipeline (4h)**
- Complete DAG implementation
- Schedule for daily 2 AM execution
- Monitoring and alerting
- Test end-to-end pipeline

**Day 14 (Sun): Testing, Monitoring & Documentation (3h)**
- Comprehensive testing
- Create monitoring dashboard
- Complete documentation
- Week 4 reflection

---

## Additional Resources

### Tools

**Postman/Insomnia:**
- API testing tools

**DBeaver:**
- Database GUI for PostgreSQL
- https://dbeaver.io/

**OpenSearch Dashboards:**
- Visualization and monitoring
- Bundled with OpenSearch

### Supplementary Learning

**Docker Documentation:**
- https://docs.docker.com/
- Reference for all Docker commands

**PostgreSQL Tutorial:**
- https://www.postgresqltutorial.com/
- Comprehensive SQL guide

**Airflow Best Practices:**
- https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html

### Community

**Docker Community:**
- https://forums.docker.com/

**Airflow Slack:**
- https://apache-airflow-slack.herokuapp.com/

---

## Success Metrics

### By End of Week 3-4

You should be able to:

**Infrastructure:**
- ✅ Run multi-container applications with Docker Compose
- ✅ Design and implement database schemas
- ✅ Implement full-text search with OpenSearch
- ✅ Create workflow orchestration with Airflow

**Data Engineering:**
- ✅ Integrate with external APIs
- ✅ Download and store large files
- ✅ Parse and extract structured data
- ✅ Build automated data pipelines

**Production Skills:**
- ✅ Health checks and monitoring
- ✅ Error handling and retry logic
- ✅ Logging and debugging
- ✅ Documentation and testing

### You do NOT need to:

- ❌ Master every Docker feature
- ❌ Become a PostgreSQL DBA
- ❌ Optimize for 100k papers (start small)
- ❌ Perfect the system (iterate later)

---

## Looking Ahead: Week 5

### You're Ready Because:

- ✅ Infrastructure is production-ready
- ✅ Data pipeline is automated
- ✅ You understand orchestration
- ✅ Error handling is robust

### Week 5 Preview: LLM Fundamentals

- Monday: Andrej Karpathy LLM lectures
- Tuesday: Transformer architecture overview
- Wednesday: Embeddings deep-dive
- Thursday: OpenAI API basics
- Weekend: Prompt engineering for paper search

**You've built the foundation. Now we add intelligence! 🚀**

---

## Tips for Success

### General Advice

1. **Start Simple**: Get basic version working first
2. **Test Frequently**: Don't build everything then test
3. **Document as You Go**: Don't wait until end
4. **Ask for Help**: When stuck > 30 min, seek help
5. **Take Breaks**: Complex systems need fresh eyes

### If You Get Stuck

**Docker issues:**
- Check logs: `docker-compose logs service_name`
- Restart specific service: `docker-compose restart service_name`
- Rebuild: `docker-compose up -d --build`

**Database issues:**
- Connect directly: `docker exec -it postgres psql -U postgres`
- Check connections: `docker exec postgres pg_isready`
- View tables: `\dt` in psql

**Network issues:**
- Verify network: `docker network ls`
- Inspect network: `docker network inspect paper-network`
- Check service names resolve

**Airflow issues:**
- Check scheduler logs: `docker-compose logs airflow-scheduler`
- Test Python function independently first
- Use print statements, check logs
- Trigger DAG manually in UI

---

## License

This learning plan is for personal educational use.

---

**Last Updated:** November 2025
**Plan Version:** Final 8.5-Month Plan
**Current Status:** Week 3-4 Infrastructure & Pipeline