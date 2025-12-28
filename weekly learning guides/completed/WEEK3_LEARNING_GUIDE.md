# 📚 WEEK 3 LEARNING GUIDE: Infrastructure Fundamentals

**Foundation Knowledge for Steps 1-4**

This guide covers all the theoretical knowledge you need BEFORE and DURING your hands-on implementation of Steps 1-4.

---

## **📋 Overview**

**Total Learning Time: 4-5 hours**

This learning guide is organized to be completed alongside your hands-on work:
- Some learning happens BEFORE implementation (prerequisites)
- Some learning happens DURING implementation (just-in-time)
- Some learning happens AFTER implementation (deepening understanding)

---

## **🎯 Learning Objectives**

By the end of this learning guide, you will understand:

1. **Docker & Containers** - What they are, why we use them, how they work
2. **Docker Compose** - Orchestrating multiple services
3. **PostgreSQL** - Relational database fundamentals and advanced features
4. **SQLAlchemy** - ORM concepts and async patterns
5. **Async Programming** - Event loops, async/await, when to use async
6. **OpenSearch** - Full-text search engine basics
7. **Apache Airflow** - Workflow orchestration concepts
8. **FastAPI Advanced** - Dependency injection, async endpoints, testing

---

## **📅 When to Learn What**

### **BEFORE Step 1:**
- Nothing! Step 1 is just project setup

### **BEFORE Step 2:**
- ✅ Docker fundamentals (45 min)
- ✅ Docker Compose basics (30 min)
- ✅ Total: 75 minutes

### **BEFORE Step 3:**
- ✅ Async Python fundamentals (30 min)
- ✅ PostgreSQL basics (30 min) - *You did this yesterday!*
- ✅ SQLAlchemy ORM concepts (30 min)
- ✅ Total: 90 minutes

### **BEFORE Step 4:**
- ✅ FastAPI dependency injection (20 min)
- ✅ Pydantic advanced (20 min)
- ✅ Total: 40 minutes

### **DURING Week 3 (Flexible timing):**
- ✅ OpenSearch basics (30 min) - Can defer to Week 7
- ✅ Airflow fundamentals (60 min) - Do on Saturday

### **OPTIONAL (Week 4 or later):**
- Testing with pytest (30 min)
- Redis basics (20 min)

---

## **SECTION 1: Docker Fundamentals** 🐳

**When to learn:** BEFORE Step 2  
**Time required:** 45 minutes  
**Priority:** CRITICAL

---

### **1.1 What is Docker? (15 min)**

**Core Concept:**
Docker is a platform for developing, shipping, and running applications in containers.

**Key Questions to Answer:**
- What problem does Docker solve?
- What is a container?
- How is a container different from a virtual machine?
- Why do developers use Docker?

**Video Learning:**
📺 **"Docker in 100 Seconds"** - Fireship (2 min)
- URL: https://www.youtube.com/watch?v=Gjnup-PuquQ
- Quick overview of what Docker is

📺 **"Docker Tutorial for Beginners"** - TechWorld with Nana (First 15 minutes)
- URL: https://www.youtube.com/watch?v=3c-iBn73dDE
- Watch 0:00 - 15:00 (Introduction, containers vs VMs, basic concepts)

**Key Concepts to Understand:**

**Container vs Virtual Machine:**
```
Virtual Machine:
┌─────────────────────────────┐
│     Application             │
│     Libraries               │
│     Guest OS (Full)         │ ← Heavy (GBs)
│     Hypervisor              │
│     Host OS                 │
│     Hardware                │
└─────────────────────────────┘

Container:
┌─────────────────────────────┐
│     Application             │
│     Libraries               │ ← Lightweight (MBs)
│     Docker Engine           │
│     Host OS                 │
│     Hardware                │
└─────────────────────────────┘
```

**Why Containers?**
- **Consistency:** "Works on my machine" → "Works everywhere"
- **Isolation:** Each container is independent
- **Efficiency:** Share OS kernel, lightweight
- **Portability:** Run anywhere Docker runs
- **Scalability:** Easy to replicate

**Docker Terminology:**
- **Image:** Blueprint for a container (like a class in OOP)
- **Container:** Running instance of an image (like an object)
- **Dockerfile:** Text file with instructions to build an image
- **Registry:** Storage for Docker images (Docker Hub, like GitHub for images)
- **Volume:** Persistent storage for containers
- **Network:** Communication between containers

---

### **1.2 Docker Images and Containers (10 min)**

**Reading:**
📖 **Docker Official Docs - Overview**
- URL: https://docs.docker.com/get-started/overview/
- Read: "Docker architecture" section

**Key Concepts:**

**Docker Images:**
- Read-only template with instructions
- Built in layers (each layer = one instruction)
- Layers are cached for efficiency
- Base image + your modifications = final image

**Layer Example:**
```
Layer 5: Copy your source code      ← Your app
Layer 4: Install Python packages     ← Dependencies
Layer 3: Install Python              ← Runtime
Layer 2: Install system packages     ← OS tools
Layer 1: Base OS (Ubuntu/Alpine)     ← Foundation
```

**Containers:**
- Running instance of an image
- Writable layer on top of image (ephemeral)
- Has its own filesystem, networking, process tree
- Can be started, stopped, deleted
- Data in container is lost when deleted (unless using volumes)

**Volume Concept:**
```
Container (Ephemeral)              Host Machine (Persistent)
┌──────────────────┐              ┌──────────────────┐
│  /app/data/   ────────────────> │  /data/volume/   │
│  (container)     │   Volume     │  (host)          │
└──────────────────┘              └──────────────────┘
       ↓                                  ↓
   Deleted → Lost                    Persisted!
```

---

### **1.3 Docker Networking (10 min)**

**Key Concept:**
Containers need to communicate with each other and the outside world.

**Network Types:**
1. **Bridge (default):** Containers on same host communicate
2. **Host:** Container uses host's network directly
3. **None:** No networking

**How Containers Find Each Other:**
```
Inside Docker Network:
┌──────────────────────────────────────┐
│  Container: fastapi                  │
│  Can connect to: postgres:5432       │ ← Uses service name!
│                 opensearch:9200      │
│                 redis:6379           │
└──────────────────────────────────────┘

From Host Machine:
Your computer can connect to: localhost:8000  ← Port mapping
                              localhost:5432
```

**Port Mapping:**
```
Container Port → Host Port
postgres:5432  → localhost:5432
```

**Why This Matters:**
- Inside containers: Use service names (`postgres`, `redis`)
- From your computer: Use `localhost` with mapped ports
- Containers on same network see each other automatically

---

### **1.4 Docker Volumes (10 min)**

**Reading:**
📖 **Docker Volumes Explained**
- URL: https://docs.docker.com/storage/volumes/
- Read: "Choose the right type of mount" section

**Key Concepts:**

**Why Volumes?**
- Containers are ephemeral (deleted = data lost)
- Volumes persist data outside container lifecycle
- Multiple containers can share volumes

**Types of Storage:**

1. **Named Volumes (Recommended for databases):**
```
postgres-data:/var/lib/postgresql/data
↑              ↑
Volume name    Container path
```

2. **Bind Mounts (Good for source code in development):**
```
./src:/app/src
↑         ↑
Host path Container path
```

3. **tmpfs (Temporary, in-memory):**
- Fast but not persistent
- Good for caches, temp files

**When to Use What:**
- **Database data:** Named volumes (managed by Docker)
- **Source code (dev):** Bind mounts (live editing)
- **Config files:** Bind mounts
- **Temporary data:** tmpfs or don't persist

---

## **SECTION 2: Docker Compose** 🎼

**When to learn:** BEFORE Step 2  
**Time required:** 30 minutes  
**Priority:** CRITICAL

---

### **2.1 What is Docker Compose? (10 min)**

**Core Concept:**
Docker Compose is a tool for defining and running multi-container Docker applications.

**Video Learning:**
📺 **"Docker Compose in 12 Minutes"** - Jake Wright
- URL: https://www.youtube.com/watch?v=Qw9zlE3t8Ko
- Complete overview of Docker Compose

**Key Questions:**
- Why not just run multiple `docker run` commands?
- What is a `compose.yml` file?
- How do services communicate?

**Problem Docker Compose Solves:**

**Without Compose:**
```bash
# Start 7 services manually
docker run -d --name postgres ...
docker run -d --name opensearch ...
docker run -d --name redis ...
docker run -d --name airflow ...
# ... and so on
# Then configure networking between them
# Then manage startup order
# Then handle dependencies
```

**With Compose:**
```bash
# Start all services
docker compose up

# Stop all services
docker compose down
```

---

### **2.2 Docker Compose File Structure (10 min)**

**Reading:**
📖 **Docker Compose File Reference**
- URL: https://docs.docker.com/compose/compose-file/
- Read: "Introduction" and "Services" sections

**Key Sections:**

```yaml
services:           # Define containers
  postgres:         # Service name
    image: ...      # What image to use
    ports: ...      # Port mapping
    volumes: ...    # Data persistence
    environment: ...# Environment variables
    networks: ...   # Which network to join

volumes:           # Named volumes definition
  postgres-data:

networks:          # Custom networks
  app-network:
```

**Service Dependencies:**
```yaml
services:
  api:
    depends_on:
      - postgres    # Start postgres first
      - redis       # Start redis first
```

**Why This Matters:**
- Single file defines entire infrastructure
- Version controlled
- Reproducible across machines
- Easy to share with team

---

### **2.3 Docker Compose Commands (10 min)**

**Essential Commands:**

**Starting Services:**
```bash
docker compose up           # Start in foreground
docker compose up -d        # Start in background (detached)
docker compose up --build   # Rebuild images first
```

**Stopping Services:**
```bash
docker compose down         # Stop and remove containers
docker compose down -v      # Also remove volumes (data loss!)
docker compose stop         # Stop without removing
```

**Viewing Status:**
```bash
docker compose ps           # List running services
docker compose logs         # View logs from all services
docker compose logs -f api  # Follow logs from specific service
docker compose top          # View running processes
```

**Managing Services:**
```bash
docker compose restart api      # Restart one service
docker compose exec api bash    # Execute command in container
docker compose build           # Rebuild all images
```

**Why Learn These:**
- You'll use these daily during development
- Essential for troubleshooting
- Managing multi-service applications

---

## **SECTION 3: Async Programming in Python** ⚡

**When to learn:** BEFORE Step 3  
**Time required:** 30 minutes  
**Priority:** CRITICAL

---

### **3.1 Why Async? (10 min)**

**Core Concept:**
Async programming allows a program to do other work while waiting for I/O operations.

**Video Learning:**
📺 **"Async IO in Python: A Complete Walkthrough"** - ArjanCodes
- URL: https://www.youtube.com/watch?v=2IW-ZEui4h4
- Watch: First 10 minutes (introduction and basics)

**The Problem Async Solves:**

**Synchronous (Blocking):**
```
Request 1 → [Wait for DB] → [Process] → Response 1
                ↓
            Blocked! Can't handle Request 2 yet
```

**Asynchronous (Non-blocking):**
```
Request 1 → [Wait for DB] ←───────┐
               ↓                   │
Request 2 → [Wait for DB]         │
               ↓                   │
Request 3 → [Wait for DB]         │
               ↓                   │
            [Process 1] ←──────────┘
            [Process 2]
            [Process 3]
```

**Key Insight:**
- Database queries take time (10-100ms)
- Network requests take time (100-1000ms)
- During that waiting, CPU is idle
- Async lets you handle other requests during waits

---

### **3.2 Async/Await Syntax (10 min)**

**Video Learning:** Corey Schafer's best animated expalination of sync/awate
https://www.youtube.com/watch?v=oAkLSJNr5zY
- Animated view : https://coreyms.com/asyncio/example_1.html
- change the example_1 through example_5

**Reading:**
📖 **Real Python - Async IO in Python**
- URL: https://realpython.com/async-io-python/
- Read: "The async/await Syntax" section

**Key Syntax:**

**Defining Async Function:**
```python
# Regular function (synchronous)
def get_data():
    return fetch_from_db()

# Async function
async def get_data():
    return await fetch_from_db()
#      ↑              ↑
#   Makes it      Waits for
#   async         async operation
```

**Rules:**
1. `async def` creates an async function (coroutine)
2. `await` can only be used inside `async def`
3. `await` pauses execution until operation completes
4. While paused, event loop can run other code

**Event Loop:**
```
Event Loop (The Manager)
┌─────────────────────────────────┐
│  Running: Task 1               │
│  Waiting: Task 2, Task 3       │
│  Completed: Task 4             │
└─────────────────────────────────┘
     ↓           ↓           ↓
  Active    Paused on    Finished
            await
```

---

### **3.3 When to Use Async (10 min)**

**Key Decision Points:**

**Use Async When:**
- ✅ I/O-bound operations (database, network, files)
- ✅ Handling many concurrent requests (web servers)
- ✅ Waiting for external services
- ✅ Need high throughput with single thread

**Don't Use Async When:**
- ❌ CPU-bound operations (calculations, processing)
- ❌ Blocking libraries (no async support)
- ❌ Simple scripts that run once
- ❌ Learning basic Python (adds complexity)

**Your Use Case (Week 3-4):**
- ✅ **FastAPI endpoints** → Async (many concurrent requests)
- ✅ **Database queries** → Async (I/O waiting)
- ✅ **arXiv API calls** → Async (network I/O)
- ✅ **PDF downloads** → Async (network I/O)

**Common Patterns:**

**Async Database Query:**
```python
async def get_papers():
    async with AsyncSession() as session:
        result = await session.execute(select(Paper))
        #          ↑
        #     Wait for database
        return result.scalars().all()
```

**Async FastAPI Endpoint:**
```python
@app.get("/papers")
async def list_papers(session: AsyncSession = Depends(get_db)):
    #     ↑                                      ↑
    # Async endpoint                    Async dependency
    papers = await get_papers(session)
    #           ↑
    #       Wait for query
    return papers
```

---

## **SECTION 4: PostgreSQL Fundamentals** 🐘

**When to learn:** BEFORE Step 3  
**Time required:** 30 minutes  
**Priority:** HIGH (but you did some yesterday!)

---

### **4.1 PostgreSQL vs Other Databases (5 min)**

**Reading:**
📖 **PostgreSQL Introduction**
- URL: https://www.postgresql.org/about/
- Read: "What is PostgreSQL?" section

**Key Points:**
- Open-source relational database
- SQL compliant
- ACID transactions (Atomicity, Consistency, Isolation, Durability)
- Advanced features: arrays, JSON, full-text search, custom types

**Why PostgreSQL for Your Project:**
- ✅ Arrays for storing authors/categories (no separate tables needed)
- ✅ JSONB for flexible metadata storage
- ✅ Excellent with Python (SQLAlchemy, asyncpg)
- ✅ Production-ready and scalable
- ✅ Strong community and documentation

---

### **4.2 PostgreSQL Array Type (10 min)**

**Video:**
📺 **PostgreSQL Arrays Explained**
- URL: https://www.youtube.com/watch?v=lFKKiMFq6Ao (or search "PostgreSQL arrays tutorial")

**Key Concepts:**

**Why Use Arrays?**
- Store multiple values in single column
- Simpler than junction tables for simple cases
- Fast queries with array operators

**Array Operations:**
```sql
-- Create table with array
CREATE TABLE papers (
    authors TEXT[],
    categories TEXT[]
);

-- Insert array
INSERT INTO papers VALUES (
    ARRAY['John Doe', 'Jane Smith'],
    ARRAY['cs.AI', 'cs.LG']
);

-- Query by array element
SELECT * FROM papers 
WHERE 'cs.AI' = ANY(categories);

-- Array contains
SELECT * FROM papers
WHERE categories @> ARRAY['cs.AI'];
```

**Array vs Separate Table:**

**Arrays (Simple):**
```
papers table:
id | authors[]              | categories[]
1  | [Alice, Bob]          | [cs.AI, cs.LG]
2  | [Charlie]             | [cs.CV]
```

**Separate Tables (Normalized):**
```
papers:        authors:      papers_authors:
id | title     id | name     paper_id | author_id
1  | ...       1  | Alice    1        | 1
2  | ...       2  | Bob      1        | 2
               3  | Charlie  2        | 3
```

**Decision Guide:**
- **Use arrays when:** Simple list, no metadata, querying by element
- **Use separate tables when:** Need author metadata, complex queries, relationships

**For your project:** Arrays are perfect! ✅

---

### **4.3 Indexes and Performance (10 min)**

**Reading:**
📖 **PostgreSQL Indexes**
- URL: https://www.postgresql.org/docs/current/indexes.html
- Read: "Introduction" section

**Key Concepts:**

**What is an Index?**
- Like a book's index
- Speeds up queries
- Makes writes slightly slower
- Takes disk space

**When to Index:**
```sql
-- Primary key (auto-indexed)
id SERIAL PRIMARY KEY

-- Unique constraint (auto-indexed)
arxiv_id VARCHAR UNIQUE

-- Frequently queried columns
CREATE INDEX idx_published_date ON papers(published_date);

-- Array columns (GIN index)
CREATE INDEX idx_categories ON papers USING GIN(categories);
```

**GIN Index for Arrays:**
- Generalized Inverted Index
- Fast array containment queries
- Essential for array columns you'll query

**Your Paper Table Needs:**
- ✅ Primary key on `id` (automatic)
- ✅ Unique index on `arxiv_id` (fast lookup, prevent duplicates)
- ✅ GIN index on `categories` (array queries)
- ✅ Index on `published_date` (sorting, filtering)

---

### **4.4 Timestamps and Timezones (5 min)**

**Key Concept:**
Always store timestamps with timezone in UTC.

**Best Practices:**
```sql
-- Good: Timezone aware
created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()

-- Bad: Timezone naive
created_at TIMESTAMP
```

**Why This Matters:**
- Your app might serve users in different timezones
- Server might be in different timezone
- Daylight saving time issues
- International collaboration

**Rule:** Store in UTC, display in user's timezone

---

## **SECTION 5: SQLAlchemy ORM** 🗃️

**When to learn:** BEFORE Step 3  
**Time required:** 30 minutes  
**Priority:** CRITICAL

---

### **5.1 What is an ORM? (10 min)**

**Core Concept:**
ORM (Object-Relational Mapping) translates between database tables and Python objects.

**Video:**
📺 **"What is an ORM?"** - Corey Schafer
- URL: https://www.youtube.com/watch?v=AJHzSU0BBBU (or search "ORM explained")

**The Problem ORM Solves:**

**Without ORM (Raw SQL):**
```python
# Execute SQL
cursor.execute("SELECT * FROM papers WHERE id = %s", (1,))
row = cursor.fetchone()

# Manually extract data
paper_id = row[0]
title = row[1]
abstract = row[2]
# ... tedious!
```

**With ORM (SQLAlchemy):**
```python
# Query returns Python objects
paper = session.get(Paper, 1)

# Access as attributes
print(paper.id)
print(paper.title)
print(paper.abstract)
# ... clean!
```

**Benefits:**
- ✅ Write Python, not SQL
- ✅ Type safety and IDE autocomplete
- ✅ Prevents SQL injection
- ✅ Database agnostic (switch databases easier)
- ✅ Relationship management

**Tradeoffs:**
- ❌ Adds abstraction layer
- ❌ Can generate inefficient queries if misused
- ❌ Need to learn ORM syntax

---

### **5.2 SQLAlchemy Core Concepts (10 min)**

**Reading:**
📖 **SQLAlchemy Tutorial - Introduction**
- URL: https://docs.sqlalchemy.org/en/20/tutorial/index.html
- Read: "Overview" section

**Key Components:**

**1. Engine:**
- Connection to database
- Manages connection pool
```python
engine = create_async_engine("postgresql+asyncpg://...")
```

**2. Session:**
- Transaction manager
- "Shopping cart" for changes
```python
async with AsyncSession(engine) as session:
    session.add(paper)
    await session.commit()
```

**3. Model (Declarative Base):**
- Python class representing table
```python
class Paper(Base):
    __tablename__ = "papers"
    id = Column(Integer, primary_key=True)
    title = Column(String)
```

**4. Query:**
- Retrieve data
```python
result = await session.execute(select(Paper))
papers = result.scalars().all()
```

**Session Lifecycle:**
```
1. Create Session
2. Query/Add/Modify objects
3. Commit (saves to database)
4. Close Session
```

---

### **5.3 SQLAlchemy Async Patterns (10 min)**

**Reading:**
📖 **SQLAlchemy Async Documentation**
- URL: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- Read: "Synopsis - Core" and "Synopsis - ORM" sections

**Key Differences from Sync:**

**Imports:**
```python
# Sync
from sqlalchemy import create_engine, Session

# Async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
```

**Engine Creation:**
```python
# Sync
engine = create_engine("postgresql://...")

# Async
engine = create_async_engine("postgresql+asyncpg://...")
#                                         ↑
#                                    Async driver
```

**Session Usage:**
```python
# Sync
with Session(engine) as session:
    paper = session.get(Paper, 1)
    session.commit()

# Async
async with AsyncSession(engine) as session:
    #     ↑                          ↑
    # async context          Await everything!
    paper = await session.get(Paper, 1)
    await session.commit()
```

**Query Execution:**
```python
# Sync
papers = session.query(Paper).all()

# Async (SQLAlchemy 2.0 style)
result = await session.execute(select(Paper))
papers = result.scalars().all()
```

**Why Async SQLAlchemy?**
- FastAPI is async
- Better concurrency for web apps
- Non-blocking database operations
- Modern best practice

---

## **SECTION 6: OpenSearch Basics** 🔍

**When to learn:** Flexible - during Week 3 or defer to Week 7  
**Time required:** 30 minutes  
**Priority:** MEDIUM (not needed until Week 7)

---

### **6.1 What is OpenSearch? (10 min)**

**Core Concept:**
OpenSearch is a search and analytics engine for full-text search, logging, and real-time analytics.

**Video:**
📺 **"Introduction to OpenSearch"** - OpenSearch Project
- URL: https://www.youtube.com/watch?v=0WZ4VtKemCc (or search "OpenSearch introduction")

**Key Points:**
- Fork of Elasticsearch
- Full-text search engine
- Distributed and scalable
- RESTful API
- Document-oriented (stores JSON)

**Why OpenSearch in Your Project:**
- ✅ BM25 algorithm for keyword search (Week 7)
- ✅ Vector search for embeddings (Week 8)
- ✅ Hybrid search combining both
- ✅ Fast full-text search in papers
- ✅ Filtering and faceting

---

### **6.2 OpenSearch Core Concepts (10 min)**

**Reading:**
📖 **OpenSearch Documentation - Core Concepts**
- URL: https://opensearch.org/docs/latest/
- Read: "About OpenSearch" section

**Key Concepts:**

**1. Index:**
- Like a database table
- Collection of documents
- Your project: `arxiv-papers` index

**2. Document:**
- JSON object
- Like a database row
- Your project: Each paper is a document

**3. Field:**
- Key-value pair in document
- Like a column
- Your project: title, abstract, categories, etc.

**4. Mapping:**
- Schema definition
- Defines field types
- Like database table schema

**Example:**
```json
{
  "arxiv_id": "2401.12345",
  "title": "Sample Paper",
  "abstract": "This is the abstract...",
  "categories": ["cs.AI", "cs.LG"],
  "vector_embedding": [0.123, 0.456, ...]
}
```

---

### **6.3 BM25 Search Algorithm (10 min)**

**Reading:**
📖 **Understanding BM25**
- URL: Search for "BM25 algorithm explained" or check Wikipedia
- Understand: What it does, not the math

**Key Concepts:**

**What is BM25?**
- Best Match 25 (ranking function)
- Ranks documents by relevance to query
- Considers:
  - Term frequency (TF): How often word appears in document
  - Inverse document frequency (IDF): How rare the word is overall
  - Document length: Longer documents penalized slightly

**Example:**
```
Query: "attention mechanism neural networks"

Paper 1: Mentions "attention" 10 times, short paper
Score: 15.2 (high)

Paper 2: Mentions "attention" 3 times, very long paper  
Score: 8.1 (medium)

Paper 3: Mentions "attention" 1 time, short paper
Score: 3.5 (low)
```

**Why BM25?**
- ✅ Simple and fast
- ✅ Works well for keyword search
- ✅ Industry standard
- ✅ Better than TF-IDF

**Your Usage (Week 7):**
- Papers indexed in OpenSearch
- User searches: "transformer attention"
- BM25 ranks papers by relevance
- Return top 10 results

---

## **SECTION 7: Apache Airflow** 🌬️

**When to learn:** Saturday (during Week 3) or before Week 4  
**Time required:** 60 minutes  
**Priority:** CRITICAL for Week 4

---

### **7.1 What is Workflow Orchestration? (15 min)**

**Core Concept:**
Orchestration = Coordinating multiple tasks to run in a specific order or schedule.

**Video:**
📺 **"Apache Airflow in 5 Minutes"** - Astronomer
- URL: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Quick overview

**The Problem Airflow Solves:**

**Without Orchestration:**
```
Cron Job 1: Fetch papers at 2am
Cron Job 2: Parse PDFs at 3am (but what if Job 1 fails?)
Cron Job 3: Index in OpenSearch at 4am (but what if Job 2 fails?)
```

**With Airflow:**
```
DAG: Paper Ingestion Pipeline
  ↓
Task 1: Fetch papers → If success → Task 2: Parse PDFs
                                        ↓
                              If success → Task 3: Index
```

**Benefits:**
- ✅ Task dependencies (run B only if A succeeds)
- ✅ Retry logic (auto-retry on failure)
- ✅ Scheduling (daily, hourly, custom)
- ✅ Monitoring (see what failed and why)
- ✅ Backfilling (rerun historical data)

---

### **7.2 Airflow Core Concepts (20 min)**

**Video:**
📺 **"Airflow Tutorial for Beginners"** - Marc Lamberti
- URL: https://www.youtube.com/watch?v=K9AnJ9_ZAXE
- Watch: First 20 minutes (architecture and DAGs)

**Key Concepts:**

**1. DAG (Directed Acyclic Graph):**
- Collection of tasks
- Defines workflow
- No cycles (can't loop back)

```
DAG: Daily Paper Ingestion
┌──────────┐
│ Fetch    │
│ Papers   │
└────┬─────┘
     ↓
┌────┴─────┐
│ Parse    │
│ PDFs     │
└────┬─────┘
     ↓
┌────┴─────┐
│ Store in │
│ Database │
└──────────┘
```

**2. Task:**
- Single unit of work
- Python function or operator
- Can succeed or fail

**3. Operator:**
- Template for a task
- PythonOperator, BashOperator, etc.

**4. Scheduler:**
- Monitors DAGs
- Triggers tasks when ready
- Manages dependencies

**5. Executor:**
- Runs tasks
- LocalExecutor (your setup): Tasks run on same machine
- CeleryExecutor (production): Distributed task execution

---

### **7.3 DAG Structure (15 min)**

**Reading:**
📖 **Airflow DAG Tutorial**
- URL: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
- Read: "Example DAG definition" section

**Basic DAG Structure:**

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define DAG
dag = DAG(
    dag_id='arxiv_ingestion',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # Run once per day
    catchup=False
)

# Define tasks
def fetch_papers():
    # Fetch from arXiv
    pass

def parse_papers():
    # Parse PDFs
    pass

task1 = PythonOperator(
    task_id='fetch',
    python_callable=fetch_papers,
    dag=dag
)

task2 = PythonOperator(
    task_id='parse',
    python_callable=parse_papers,
    dag=dag
)

# Define dependencies
task1 >> task2  # task2 runs after task1
```

**Key Parameters:**

- `dag_id`: Unique name for DAG
- `start_date`: When DAG becomes active
- `schedule_interval`: How often to run (`@daily`, `@hourly`, cron expression)
- `catchup`: Run missed schedules (False = skip missed runs)

---

### **7.4 Your Week 4 Use Case (10 min)**

**What You'll Build:**

**DAG Name:** `arxiv_paper_ingestion`

**Tasks:**
1. **Fetch Metadata** - Call arXiv API for new papers
2. **Download PDFs** - Download paper PDFs
3. **Parse Papers** - Extract text with Docling
4. **Store in Database** - Save to PostgreSQL
5. **Index in OpenSearch** - Add to search engine

**Dependencies:**
```
Fetch → Download → Parse → Store → Index
```

**Schedule:** Daily at 2 AM (weekdays only)

**Error Handling:**
- Retry failed tasks 3 times
- Send alert if all retries fail
- Continue with successful papers even if some fail

**Why Learn Now:**
- Week 4 is all about building this pipeline
- Understanding DAGs helps design the workflow
- Knowing Airflow concepts speeds up implementation

---

## **SECTION 8: FastAPI Advanced Patterns** 🚀

**When to learn:** BEFORE Step 4  
**Time required:** 40 minutes  
**Priority:** MEDIUM-HIGH

---

### **8.1 Dependency Injection (15 min)**

**Reading:**
📖 **FastAPI Dependencies**
- URL: https://fastapi.tiangolo.com/tutorial/dependencies/
- Read: "First Steps" and "Classes as Dependencies"

**Core Concept:**
Dependency injection = Providing dependencies to functions automatically.

**Why Use It?**

**Without DI (Manual):**
```python
@app.get("/papers")
async def get_papers():
    # Manually create session every time
    async with AsyncSession(engine) as session:
        result = await session.execute(select(Paper))
        return result.scalars().all()
```

**With DI (Automatic):**
```python
async def get_db():
    async with AsyncSession(engine) as session:
        yield session

@app.get("/papers")
async def get_papers(db: AsyncSession = Depends(get_db)):
    # Session provided automatically!
    result = await db.execute(select(Paper))
    return result.scalars().all()
```

**Benefits:**
- ✅ Reusable across endpoints
- ✅ Easier testing (mock dependencies)
- ✅ Cleaner code
- ✅ Automatic cleanup

**Common Dependencies:**
- Database sessions
- Authentication/authorization
- Configuration
- Repositories

---

### **8.2 Pydantic Advanced (15 min)**

**Reading:**
📖 **Pydantic Field Validation**
- URL: https://docs.pydantic.dev/latest/concepts/fields/
- Read: "Field customization" section

**Key Concepts:**

**Field Validation:**
```python
from pydantic import BaseModel, Field

class PaperCreate(BaseModel):
    arxiv_id: str = Field(
        ...,  # Required
        pattern=r"^\d{4}\.\d{5}$",  # Regex validation
        description="arXiv ID format: YYMM.NNNNN"
    )
    title: str = Field(..., min_length=1, max_length=500)
    authors: List[str] = Field(..., min_items=1)  # At least one
```

**Custom Validators:**
```python
from pydantic import validator

class PaperCreate(BaseModel):
    published_date: datetime
    
    @validator('published_date')
    def date_not_future(cls, v):
        if v > datetime.now():
            raise ValueError('Published date cannot be in future')
        return v
```

**from_attributes Configuration:**
```python
class PaperResponse(BaseModel):
    id: int
    title: str
    
    model_config = ConfigDict(from_attributes=True)
    # Allows: PaperResponse.model_validate(sqlalchemy_object)
```

**Why This Matters:**
- ✅ Automatic request validation
- ✅ Clear error messages
- ✅ Type safety
- ✅ Self-documenting API

---

### **8.3 Response Models and Status Codes (10 min)**

**Reading:**
📖 **FastAPI Response Models**
- URL: https://fastapi.tiangolo.com/tutorial/response-model/
- Read: Complete page

**Key Concepts:**

**Response Model:**
```python
@app.get("/papers/{paper_id}", response_model=PaperResponse)
async def get_paper(paper_id: int):
    # FastAPI validates response matches PaperResponse
    paper = await get_from_db(paper_id)
    return paper  # Auto-converted to PaperResponse
```

**Status Codes:**
```python
from fastapi import status

@app.post(
    "/papers", 
    response_model=PaperResponse,
    status_code=status.HTTP_201_CREATED  # Return 201 for creation
)
async def create_paper(paper: PaperCreate):
    return await save_to_db(paper)

@app.delete("/papers/{paper_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_paper(paper_id: int):
    await delete_from_db(paper_id)
    return  # No content returned
```

**Common Status Codes:**
- 200 OK - Successful GET/PUT
- 201 Created - Successful POST
- 204 No Content - Successful DELETE
- 400 Bad Request - Client error
- 404 Not Found - Resource not found
- 422 Unprocessable Entity - Validation error
- 500 Internal Server Error - Server error

---

## **SECTION 9: Redis Basics (Optional)** 💾

**When to learn:** Week 6 or when needed  
**Time required:** 20 minutes  
**Priority:** LOW (defer until Week 6)

---

### **9.1 What is Redis? (10 min)**

**Core Concept:**
Redis is an in-memory data store used as a cache, message broker, or database.

**Video:**
📺 **"Redis in 100 Seconds"** - Fireship
- URL: https://www.youtube.com/watch?v=G1rOthIU-uo

**Key Points:**
- In-memory (very fast)
- Key-value store
- Supports various data types (strings, lists, sets, hashes)
- Persistence optional
- Common use: Caching

**Why Redis in Your Project (Week 6):**
- ✅ Cache expensive LLM responses
- ✅ Cache search results
- ✅ Store session data
- ✅ Rate limiting

---

### **9.2 Redis Use Cases (10 min)**

**Reading:**
📖 **Redis Use Cases**
- URL: https://redis.io/docs/about/
- Read: "Use cases" section

**Common Patterns:**

**Caching:**
```
User Query → Check Redis → Cache Hit? Return cached response
                               ↓
                          Cache Miss? Query database → Cache result → Return
```

**Your Week 6 Usage:**
```python
# Cache RAG response
query = "What are transformers?"
cache_key = f"rag:{hash(query)}"

# Check cache
cached = await redis.get(cache_key)
if cached:
    return cached  # Fast! (~1ms)

# Generate response (slow, ~15s)
response = await generate_rag_response(query)

# Cache for future
await redis.set(cache_key, response, ex=3600)  # Expire in 1 hour
return response
```

**Benefits:**
- ✅ 150-400x faster responses for cached queries
- ✅ Reduce LLM API costs
- ✅ Better user experience

---

## **SECTION 10: Testing with Pytest (Optional)** 🧪

**When to learn:** Week 4 or later  
**Time required:** 30 minutes  
**Priority:** MEDIUM (defer to Week 4)

---

### **10.1 Why Test? (10 min)**

**Core Concept:**
Automated tests verify your code works correctly and prevent regressions.

**Video:**
📺 **"Pytest Tutorial"** - Socratica
- URL: https://www.youtube.com/watch?v=bbp_849-RZ4

**Benefits:**
- ✅ Catch bugs early
- ✅ Safe refactoring
- ✅ Documentation of expected behavior
- ✅ Confidence in deployments

**Types of Tests:**
1. **Unit tests:** Test individual functions
2. **Integration tests:** Test multiple components together
3. **End-to-end tests:** Test entire system

---

### **10.2 Testing Async Code (10 min)**

**Reading:**
📖 **Pytest Async**
- URL: https://pytest-asyncio.readthedocs.io/
- Read: "Quick Start"

**Key Points:**

**Install:**
```bash
pip install pytest pytest-asyncio
```

**Test Async Function:**
```python
import pytest

@pytest.mark.asyncio
async def test_get_paper():
    paper = await get_paper_from_db(1)
    assert paper.id == 1
    assert paper.title is not None
```

**Test FastAPI Endpoint:**
```python
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_list_papers():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/papers")
        assert response.status_code == 200
        assert len(response.json()) > 0
```

---

### **10.3 Testing Best Practices (10 min)**

**Key Principles:**

1. **Arrange-Act-Assert Pattern:**
```python
def test_create_paper():
    # Arrange - Setup test data
    paper_data = {"arxiv_id": "2401.12345", ...}
    
    # Act - Execute the code
    paper = create_paper(paper_data)
    
    # Assert - Verify results
    assert paper.arxiv_id == "2401.12345"
```

2. **Use Fixtures:**
```python
@pytest.fixture
async def test_db():
    # Setup: Create test database
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    yield engine
    # Teardown: Clean up
    await engine.dispose()
```

3. **Test Edge Cases:**
- Valid inputs
- Invalid inputs
- Boundary conditions
- Error conditions

**Your Week 4 Testing:**
- Test arXiv API client
- Test PDF parsing
- Test database operations
- Test API endpoints

---

## **📚 SUPPLEMENTARY RESOURCES**

### **Official Documentation:**

**Docker:**
- https://docs.docker.com/get-started/
- https://docs.docker.com/compose/

**PostgreSQL:**
- https://www.postgresql.org/docs/current/
- https://www.postgresqltutorial.com/

**SQLAlchemy:**
- https://docs.sqlalchemy.org/en/20/
- Async guide: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html

**FastAPI:**
- https://fastapi.tiangolo.com/
- Async dependencies: https://fastapi.tiangolo.com/async/

**OpenSearch:**
- https://opensearch.org/docs/latest/
- Python client: https://opensearch.org/docs/latest/clients/python/

**Apache Airflow:**
- https://airflow.apache.org/docs/
- Tutorial: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html

**Pydantic:**
- https://docs.pydantic.dev/latest/

**Pytest:**
- https://docs.pytest.org/
- Pytest-asyncio: https://pytest-asyncio.readthedocs.io/

---

## **📋 LEARNING CHECKLIST**

### **Critical (Do Before Implementation):**
- [ ] Docker fundamentals (45 min) - BEFORE Step 2
- [ ] Docker Compose basics (30 min) - BEFORE Step 2
- [ ] Async Python fundamentals (30 min) - BEFORE Step 3
- [ ] SQLAlchemy ORM concepts (30 min) - BEFORE Step 3
- [ ] FastAPI dependency injection (15 min) - BEFORE Step 4

### **Important (Do During Week 3):**
- [ ] PostgreSQL arrays (15 min) - BEFORE Step 3
- [ ] PostgreSQL indexes (10 min) - BEFORE Step 3
- [ ] Airflow fundamentals (60 min) - Saturday or before Week 4
- [ ] Pydantic advanced (15 min) - BEFORE Step 4

### **Optional (Can Defer):**
- [ ] OpenSearch basics (30 min) - Week 7 is fine
- [ ] Redis basics (20 min) - Week 6 is fine
- [ ] Testing with pytest (30 min) - Week 4 is fine

---

## **🎯 RECOMMENDED LEARNING SCHEDULE**

### **Thursday Evening (Tonight) - 90 min:**
**BEFORE Steps 1-2:**
- Docker fundamentals (45 min)
- Docker Compose basics (30 min)
- Async Python overview (15 min)

### **Friday Evening - 30 min:**
**DURING Step 2:**
- Docker troubleshooting (as needed)
- Review Docker Compose reference

### **Saturday Morning - 90 min:**
**BEFORE Step 3:**
- Async Python deep dive (30 min)
- SQLAlchemy ORM concepts (30 min)
- Airflow fundamentals (30 min)

### **Saturday Afternoon - 60 min:**
**BEFORE Step 4:**
- Airflow DAG structure (30 min)
- FastAPI advanced patterns (30 min)

### **Sunday - As Needed:**
- Reference documentation during implementation
- Deep dive on any unclear concepts

---

## **💡 LEARNING TIPS**

### **Active Learning:**
- ✅ Take notes while watching videos
- ✅ Pause and try concepts in Python REPL
- ✅ Draw diagrams to visualize concepts
- ✅ Explain concepts out loud (Feynman technique)

### **Don't Over-Learn:**
- ✅ Understand concepts, not memorize
- ✅ Learn what you need now, defer deep dives
- ✅ Reference docs exist for details
- ✅ Hands-on practice reinforces learning

### **When Stuck:**
- ✅ Re-watch video section
- ✅ Check official documentation
- ✅ Draw it out / explain to rubber duck
- ✅ Try simple example first
- ✅ Ask specific questions

---

## **🎓 SUCCESS CRITERIA**

After completing this learning guide, you should be able to:

**Docker & Compose:**
- ✅ Explain what Docker containers are and why they're useful
- ✅ Understand Docker images, volumes, and networks
- ✅ Read and understand a docker-compose.yml file
- ✅ Use Docker Compose commands confidently

**Async Programming:**
- ✅ Explain when to use async vs sync
- ✅ Understand async/await syntax
- ✅ Write async functions and use await correctly
- ✅ Understand event loop concept

**PostgreSQL:**
- ✅ Understand PostgreSQL arrays and when to use them
- ✅ Know how to query arrays
- ✅ Understand indexes and when to create them
- ✅ Handle timestamps with timezones correctly

**SQLAlchemy:**
- ✅ Explain what an ORM is and its benefits
- ✅ Understand SQLAlchemy models and sessions
- ✅ Know difference between sync and async SQLAlchemy
- ✅ Write basic queries with SQLAlchemy

**Airflow:**
- ✅ Explain what workflow orchestration is
- ✅ Understand DAGs, tasks, and operators
- ✅ Know when to use Airflow
- ✅ Can design a simple workflow

**FastAPI Advanced:**
- ✅ Understand dependency injection
- ✅ Know how to validate requests with Pydantic
- ✅ Use proper HTTP status codes
- ✅ Structure endpoints correctly

---

## **📊 PROGRESS TRACKING**

### **Use This Checklist:**

**Week 3 Learning Progress:**

```
Day 1 (Thursday):
[ ] Docker fundamentals (45 min)
[ ] Docker Compose basics (30 min)
[ ] Async Python basics (15 min)

Day 2 (Friday):
[ ] Docker troubleshooting practice

Day 3 (Saturday):
[ ] Async Python deep dive (30 min)
[ ] SQLAlchemy concepts (30 min)
[ ] Airflow fundamentals (30 min)
[ ] Airflow DAGs (30 min)

Day 4 (Sunday):
[ ] FastAPI advanced (40 min)
[ ] Reference docs as needed during implementation

TOTAL LEARNING TIME: 4-5 hours
BALANCED WITH: 8-9 hours hands-on (Steps 1-4)
```

---

## **🎯 FINAL THOUGHTS**

**Learning is Iterative:**
- First pass: Understand concepts (this guide)
- Second pass: Apply in practice (Steps 1-4)
- Third pass: Deepen through use (Weeks 4+)

**You Don't Need to Master Everything:**
- Understand enough to implement
- Reference docs for details
- Learn deeper as you build

**The Goal:**
Build working systems while understanding WHY they work, not just HOW to make them work.

---

**Document Generated:** December 5, 2025  
**Part of:** 8.5-Month AI/ML Career Transition Plan  
**Current Phase:** Week 3 Infrastructure Learning  
**Companion Documents:** STEP1-4 Hands-On Guides  
**Total Learning Time:** 4-5 hours across Week 3  
**Next:** Integrated Week 3 Master Schedule combining learning + hands-on
