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
2. Verify installation using version command
3. Run hello-world test container
4. Test listing containers and images commands

**Part 3: Hands-on Practice (30 min)**
1. Pull Ubuntu 22.04 image from Docker Hub
2. Run interactive container with Ubuntu image
3. Install package inside container (python3)
4. Exit and observe container has stopped
5. Understand ephemeral nature of containers

**Part 4: Reflection (10 min)**
- Document what containers are vs VMs
- Why Docker matters for ML pipelines
- How you'll use it this week

#### Key Concepts to Master

**Container vs Image:**
- Image = blueprint (immutable template)
- Container = running instance (ephemeral process)
- Multiple containers can run from same image
- Images are layers built on top of each other

**Why Docker for ML?**
- Consistent environments across machines
- Easy dependency management
- Reproducible experiments
- Easy deployment
- Isolation from host system

**Core Commands:**
- Pull image from registry
- List downloaded images
- List running containers
- List all containers including stopped
- Create and start container from image
- Stop running container
- Remove stopped container
- Remove image
- Enter running container with interactive shell

**Ports and Volumes:**
- Port mapping: Connect container port to host port
- Without port mapping, services inside container not accessible from host
- Volumes: Persist data beyond container lifecycle
- Without volumes, all data lost when container removed
- Bind mounts: Mount host directory into container

#### Practice Requirements

**Exercise 1: Python Container**
- Pull python:3.11 image from Docker Hub
- Run container with interactive shell access
- Create simple Python script inside container
- Run the script
- Exit container
- Verify script is gone after container stopped

**Exercise 2: Port Mapping**
- Run python HTTP server in container
- Map container port to host port 8080
- Access server from browser on host machine
- Understand how port mapping enables external access

**Exercise 3: Volume Mounting**
- Create directory on host with Python script
- Mount directory as volume when running container
- Modify script on host machine
- See changes reflected immediately in container
- Understand how volumes enable data persistence

#### End of Day 1 Checklist

- [ ] Docker Desktop/Engine installed and running
- [ ] Ran hello-world container successfully
- [ ] Understand fundamental difference between container and image
- [ ] Can pull images from Docker Hub
- [ ] Can run containers in interactive and detached modes
- [ ] Understand port mapping concept and usage
- [ ] Understand volume mounting for data persistence
- [ ] Know why Docker is critical for ML infrastructure
- [ ] Spent approximately 90 minutes on focused learning

---

### Day 2 (Tue Dec 2): FastAPI in Docker + PostgreSQL Basics

#### Primary Video Resources

**Video 1: "Dockerize FastAPI Application"**
- Link: https://www.youtube.com/watch?v=0H2miBK_gAk
- Duration: 15:00
- Practical FastAPI containerization walkthrough

**Video 2: "PostgreSQL Crash Course"**
- Link: https://www.youtube.com/watch?v=qw--VYLpxG4
- Duration: 1:16:00
- Watch: First 20 minutes (basics, installation, SQL fundamentals)

#### Reading Materials

**Dockerfile Best Practices:**
- Link: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- Duration: 15 min
- Critical for production-ready images

**PostgreSQL Official Tutorial:**
- Link: https://www.postgresql.org/docs/current/tutorial.html
- Sections 1-3: Getting Started, SQL Language, Advanced Features intro
- Duration: 25 min

#### Day 2 Schedule (90 minutes total)

**Part 1: Create Dockerfile for FastAPI (35 min)**

**Requirements:**
- Start with python:3.11-slim base image for smaller image size
- Copy requirements.txt file first before application code
- Install all Python dependencies from requirements file
- Copy application code after dependencies installed
- Expose port 8000 for external access
- Set command to run uvicorn server

**What to figure out:**
- Dockerfile syntax (FROM, COPY, RUN, EXPOSE, CMD instructions)
- Layer caching optimization strategy
- Why copying requirements before code enables faster rebuilds
- Difference between CMD and ENTRYPOINT instructions
- How to minimize image size
- Security best practices for base images

**Test:**
- Build Docker image with meaningful tag name
- Run container with port mapping to host
- Access API documentation at localhost:8000/docs
- Verify all endpoints function correctly inside container
- Test stopping and restarting container

**Success criteria:**
- Image builds without errors or warnings
- Container runs and API is accessible from host browser
- All FastAPI functionality works identically to local
- Can stop and restart container without data loss issues
- Understand build process and layers

---

**Part 2: PostgreSQL Basics (35 min)**

**Requirements:**

**1. Install PostgreSQL Locally (10 min)**
- Install PostgreSQL version 15 or 16
- Set up initial admin password securely
- Verify psql command-line tool works
- Start PostgreSQL service

**2. Create First Database (10 min)**
- Create new database for transactions
- Connect to newly created database
- Create test table with appropriate columns:
  - Auto-incrementing primary key
  - Decimal column for monetary amounts
  - Variable character column for merchant names
  - Timestamp column with default current time
- Understand table structure and constraints

**3. Basic SQL Operations (15 min)**
- INSERT: Add 5 test transaction records with varied data
- SELECT: Retrieve all records, then filter by amount threshold
- UPDATE: Modify merchant name for specific transaction
- DELETE: Remove one transaction based on ID
- Understand CRUD operations and their purposes

**What to figure out:**
- How to connect to PostgreSQL using psql
- Command to switch between databases
- Command to list all tables in database
- Command to describe table structure
- How to exit psql interface
- Transaction concepts (BEGIN, COMMIT, ROLLBACK)

---

**Part 3: Reflection (20 min)**

**Document:**
1. Why Dockerfile layers matter for build performance
2. How FastAPI runs in Docker compared to local environment
3. Basic SQL commands learned and their business purposes
4. How PostgreSQL will store paper metadata in your system
5. Questions to explore tomorrow about integration

#### Key Concepts to Master

**Dockerfile Layer Optimization:**
- Each Dockerfile instruction creates new layer
- Layers are cached to speed up subsequent builds
- If layer unchanged, Docker reuses cached version
- Order instructions from least to most frequently changing
- Copying requirements before code means dependency layer cached
- Only code layer rebuilt when application code changes

**Layer Caching Benefits:**
- Faster development iteration
- Reduced CI/CD build times
- Efficient disk space usage
- Predictable build performance

**PostgreSQL Fundamentals:**
- **Database:** Container for related tables and data
- **Table:** Structured data storage with rows and columns
- **Primary Key:** Unique identifier ensuring row uniqueness
- **Foreign Key:** Reference establishing relationship between tables
- **Data Types:** INTEGER, SERIAL, VARCHAR, TEXT, DECIMAL, TIMESTAMP, BOOLEAN
- **Constraints:** NOT NULL, UNIQUE, CHECK, DEFAULT

**SQL Transaction Concepts:**
- BEGIN: Start transaction block
- Multiple operations within transaction
- COMMIT: Save all changes permanently
- ROLLBACK: Undo all changes if error occurs
- Ensures data consistency (all succeed or all fail)

#### Practice Requirements

**Exercise 1: Multi-Stage Docker Build (Advanced)**
- Create Dockerfile with separate builder and runtime stages
- Install build dependencies only in builder stage
- Copy only necessary artifacts to slim runtime stage
- Compare final image sizes between single and multi-stage
- Understand production optimization strategy

**Exercise 2: Environment Variables in Docker**
- Create .env file with configuration variables
- Use ENV instruction in Dockerfile
- Pass environment variables at runtime with -e flag
- Access environment variables in FastAPI application code
- Understand configuration management

**Exercise 3: SQL Transactions Practice**
- Start transaction block
- Insert multiple related records
- Simulate error condition
- Observe rollback behavior
- Understand atomicity concept

**Exercise 4: SQL Relationships**
- Create second table (e.g., merchants)
- Establish foreign key relationship to transactions
- Query data across both tables using JOIN
- Understand relational database concepts

#### End of Day 2 Checklist

- [ ] Created Dockerfile for FastAPI application
- [ ] Built Docker image successfully without errors
- [ ] Ran containerized FastAPI with port mapping
- [ ] API accessible and functional from host browser
- [ ] PostgreSQL installed and running locally
- [ ] Created test database and table with proper schema
- [ ] Performed all CRUD operations successfully in SQL
- [ ] Understand Dockerfile layer caching optimization
- [ ] Know basic SQL commands for database operations
- [ ] Can explain benefits of containerization
- [ ] Spent approximately 90 minutes on learning

---

### Day 3 (Wed Dec 3): PostgreSQL Deep Dive + OpenSearch Intro

#### Primary Video Resources

**Video 1: "PostgreSQL Advanced Features"**
- Link: https://www.youtube.com/watch?v=qw--VYLpxG4
- Duration: Continue from 20:00 to 45:00
- Topics: Indexes, relationships, transactions, performance

**Video 2: "What is Elasticsearch/OpenSearch"**
- Link: https://www.youtube.com/watch?v=gS_nHTWZEJ8
- Duration: 10:00
- Search engine fundamentals and architecture

**Video 3: "OpenSearch Tutorial"**
- Link: https://www.youtube.com/watch?v=hDC_QkfYPLU
- Duration: 20:00
- Hands-on introduction to OpenSearch

#### Reading Materials

**psycopg3 Documentation:**
- Link: https://www.psycopg.org/psycopg3/docs/
- Basic usage section and connection handling
- Duration: 20 min
- Python PostgreSQL connector library

**OpenSearch Getting Started:**
- Link: https://opensearch.org/docs/latest/getting-started/
- Quickstart section and core concepts
- Duration: 15 min

#### Day 3 Schedule (90 minutes total)

**Part 1: Python + PostgreSQL Integration (40 min)**

**Requirements:**

**1. Install psycopg3 library**
- Install psycopg with binary compilation option
- Verify installation successful

**2. Create database connection module**
- Database connection string configuration
- Connection pooling setup for efficient resource usage
- Connection context manager for automatic cleanup
- Error handling for connection failures and timeouts
- Retry logic for transient network issues

**3. Implement paper metadata storage**

**Table Schema Design:**
- Primary key: paper_id as unique identifier
- Unique constraint: arxiv_id (prevent duplicates)
- Required fields: title, abstract, categories, published date
- Array fields: authors list, category tags
- Optional fields: PDF path, parsing status
- Timestamp fields: downloaded_at, parsed_at, created_at, updated_at
- Status field: parsing_status with enumerated values
- Indexes: On published_date for date queries
- Indexes: On parsing_status for filtering
- Indexes: On categories array using GIN index

**4. Create CRUD operations module**
- Insert new paper metadata with data validation
- Get paper by arxiv_id with error handling
- Update parsing status with timestamp tracking
- Query papers by date range with efficient indexes
- Query papers by category with array filtering
- Handle duplicate inserts gracefully (upsert logic)
- Batch operations for efficient bulk inserts

**What to figure out:**
- Connection string format with all parameters
- Using context managers (with statement) for safety
- Parameterized queries to prevent SQL injection attacks
- Handling PostgreSQL array data types in Python
- Date and time handling with timezone awareness
- Error handling patterns (connection errors, constraint violations)
- Transaction management for multiple operations
- Connection pool configuration for optimal performance

**Test:**
- Insert 5 complete paper records with all fields
- Query paper by exact arxiv_id match
- Update parsing status and verify timestamp updates
- Query papers published in last 7 days
- Handle duplicate arxiv_id insertion attempt gracefully
- Test with missing optional fields
- Verify data integrity across operations

---

**Part 2: OpenSearch Introduction (35 min)**

**Requirements:**

**1. Understanding OpenSearch (15 min)**
- What is full-text search and how it differs from SQL
- Inverted index concept and how it enables fast search
- Why PostgreSQL LIKE queries insufficient for document search
- OpenSearch vs Elasticsearch relationship (they're forks)
- When to use OpenSearch vs vector databases vs SQL databases
- Relevance scoring and ranking concepts
- Search performance characteristics

**2. Install OpenSearch with Docker (10 min)**
- Pull OpenSearch Docker image
- Run container in single-node mode for development
- Set discovery type for standalone operation
- Configure initial admin password
- Map ports 9200 (HTTP API) and 9600 (Performance Analyzer)
- Set environment variables for configuration
- Verify OpenSearch running and accessible

**3. Basic OpenSearch operations (10 min)**
- Access OpenSearch cluster health endpoint
- Create first index with default settings
- Index a sample document with fields
- Search documents using match query
- Understand JSON request and response format
- Examine search relevance scores

**What to figure out:**
- Index concept (equivalent to database in SQL terms)
- Document concept (equivalent to row in SQL terms)
- Mapping concept (equivalent to schema in SQL terms)
- Query DSL (Domain Specific Language) structure
- Relevance scoring algorithm (BM25)
- How full-text search tokenizes and matches text
- Difference between analyzed and keyword fields

---

**Part 3: Reflection (15 min)**

**Document:**
1. When to use PostgreSQL structured data vs OpenSearch for search
2. Why arrays in PostgreSQL vs separate tables trade-offs
3. How database indexes improve query performance
4. How full-text search works differently than SQL LIKE patterns
5. Integration plan: Using PostgreSQL and OpenSearch together
6. Data synchronization strategy between databases

#### Key Concepts to Master

**PostgreSQL Connection Management:**
- Connection pooling reduces overhead of creating connections
- Context managers ensure connections always closed properly
- Automatic transaction management within context
- Error handling prevents resource leaks
- Connection parameters: host, port, database, user, password, timeout

**Parameterized Queries (Security):**
- Never concatenate user input directly into SQL strings
- SQL injection vulnerability allows malicious code execution
- Parameterized queries safely handle user input
- Database driver properly escapes special characters
- Always use placeholders for dynamic values

**PostgreSQL Arrays:**
- Native array data type for lists
- Store multiple values in single field
- Query with array operators (ANY, ALL, @>)
- Useful for tags, categories, authors
- GIN indexes enable efficient array queries
- Avoids need for junction tables in many cases

**OpenSearch Core Concepts:**
- **Index:** Named container for documents of similar type
- **Document:** JSON object stored in index
- **Mapping:** Schema defining field types and analysis
- **Shard:** Subdivision of index for scalability
- **Replica:** Copy of shard for availability
- **Node:** Single OpenSearch server instance
- **Cluster:** Collection of nodes working together

**Full-Text Search vs SQL:**
- SQL LIKE: Pattern matching, no relevance scoring
- Full-text search: Tokenization, stemming, relevance ranking
- Inverted index: Maps terms to documents for fast lookup
- BM25 algorithm: Industry standard relevance scoring
- Analyzers: Process text (lowercase, remove stop words, stem)

**Why Both Databases?**
- PostgreSQL: Source of truth for structured metadata
- PostgreSQL: Relationships, transactions, strong consistency
- OpenSearch: Fast full-text search with relevance ranking
- OpenSearch: Complex filters, aggregations, analytics
- Keep synchronized: Update both when data changes

#### Practice Requirements

**Exercise 1: Database Connection Pool**
- Configure connection pool with min and max connections
- Handle max connections limit gracefully
- Implement retry logic for failed connection attempts
- Test concurrent access from multiple threads
- Monitor connection usage and performance

**Exercise 2: Transaction Management**
- Use context manager for automatic transaction handling
- Insert record into papers table
- Insert related records into sections table
- If any operation fails, all operations rolled back
- Understand atomicity principle

**Exercise 3: Complex SQL Queries**
- Get papers published in last 7 days filtered by category
- Count papers grouped by category with aggregation
- Find papers where specific author in authors array
- Update batch of papers' parsing status efficiently
- Combine multiple conditions with AND/OR logic

**Exercise 4: OpenSearch Index Mapping**
- Create papers index with explicit mapping
- Define title field as analyzed text for full-text search
- Define abstract field as analyzed text
- Define arxiv_id field as keyword for exact matching
- Define published_date field as date type
- Understand analyzed vs keyword field types

**Exercise 5: OpenSearch Search Queries**
- Index 10 sample paper documents
- Search for papers containing specific keyword
- Filter results by date range
- Filter results by category
- Combine filters with boolean must/should/must_not
- Paginate results with from and size parameters

#### End of Day 3 Checklist

- [ ] Installed psycopg3 Python library successfully
- [ ] Created database connection module with pooling
- [ ] Implemented papers table with proper schema
- [ ] Created all CRUD operations for papers
- [ ] Tested with sample data insertion and retrieval
- [ ] Understand parameterized queries prevent SQL injection
- [ ] Know how to work with PostgreSQL array fields
- [ ] OpenSearch running in Docker container
- [ ] Created first OpenSearch index successfully
- [ ] Indexed sample documents and performed searches
- [ ] Performed basic searches with keyword queries
- [ ] Understand when to use PostgreSQL vs OpenSearch
- [ ] Know benefits and trade-offs of each database
- [ ] Spent approximately 90 minutes on focused learning

---

### Day 4 (Thu Dec 4): OpenSearch Implementation + Airflow Basics

#### Primary Video Resources

**Video 1: "OpenSearch Python Client"**
- Link: https://opensearch.org/docs/latest/clients/python/
- Read documentation with examples
- Duration: 20 min

**Video 2: "Apache Airflow Tutorial"**
- Link: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Duration: 51:00
- Watch: First 25 minutes (what is Airflow, DAGs, operators)

**Video 3: "Airflow in 100 Seconds"**
- Link: https://www.youtube.com/watch?v=AHMm1wfGuHE
- Quick overview before detailed dive

#### Reading Materials

**OpenSearch Python Client Guide:**
- Link: https://opensearch.org/docs/latest/clients/python/
- All basic examples and patterns
- Duration: 25 min

**Airflow Fundamental Concepts:**
- Link: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
- Core concepts and architecture
- Duration: 20 min

#### Day 4 Schedule (90 minutes total)

**Part 1: OpenSearch Python Integration (45 min)**

**Requirements:**

**1. Install OpenSearch Python client library**
- Install opensearch-py package
- Verify installation successful

**2. Create OpenSearch connection module**
- Connect to OpenSearch cluster with authentication
- Handle connection configuration (host, port, credentials)
- Error handling for connection failures and timeouts
- Connection pooling configuration for performance
- SSL/TLS configuration for security

**3. Implement paper search functionality**

**Index Mapping for Papers:**
- arxiv_id: keyword field for exact matching and filtering
- title: text field with English analyzer for full-text search
- abstract: text field with English analyzer
- full_text: text field for complete paper content search
- authors: text field for author name searching
- categories: keyword field for category filtering
- published_date: date field for temporal filtering
- citation_count: integer field for ranking

**Analyzers:**
- English analyzer: Removes stop words, stems words, lowercase
- Improves search relevance for English text
- Standard analyzer for other languages

**4. Implement search operations**
- Index new paper document in OpenSearch
- Bulk index multiple papers efficiently
- Search by keywords with relevance ranking
- Filter by date range using range queries
- Filter by multiple categories with terms queries
- Sort results by relevance score or date
- Pagination for large result sets (from and size parameters)
- Return highlighted snippets showing matches

**What to figure out:**
- OpenSearch Python client initialization with all parameters
- Document indexing (single document vs bulk operations)
- Query DSL structure and syntax
- Difference between match queries (full-text) and term queries (exact)
- Boolean queries combining must, should, filter, must_not
- Pagination implementation (from, size parameters)
- Aggregations for statistics and faceted search
- Highlighting search terms in results
- Handling missing fields gracefully

**Test:**
- Index 10 sample papers with complete metadata
- Search for "transformer architecture" with relevance ranking
- Filter results to only cs.AI category papers
- Get papers published in last 30 days
- Sort results by publication date (newest first)
- Paginate through results showing 5 per page
- Verify relevance scores make sense

---

**Part 2: Apache Airflow Fundamentals (30 min)**

**Requirements:**

**1. Understanding Airflow Concepts (15 min)**

**What to learn:**
- What is workflow orchestration and why needed
- Limitations of cron jobs for complex pipelines
- DAG (Directed Acyclic Graph) concept and structure
- Operators and Tasks relationship
- Task dependencies and execution order
- Scheduling with cron expressions
- Execution dates and backfilling

**Core Concepts:**
- **DAG:** Complete workflow definition with tasks
- **Task:** Single unit of work in workflow
- **Operator:** Template defining what task does (Python, Bash, SQL, etc.)
- **Dependency:** Execution order between tasks (A before B)
- **Schedule:** When DAG runs automatically (cron syntax)
- **Execution Date:** Logical date for DAG run
- **Task Instance:** Single execution of task

**Airflow vs Cron Jobs:**
- Cron: Simple scheduling, no dependencies, no monitoring
- Airflow: Complex dependencies, monitoring, retries, UI, logging

**2. Install Airflow with Docker Compose (15 min)**

**Using official Docker Compose configuration:**
- Download official Airflow docker-compose.yaml file
- Create required directories (dags, logs, plugins, config)
- Set Airflow UID in environment file
- Start all Airflow services with docker-compose
- Wait for initialization to complete

**Services Created:**
- Airflow webserver: Web UI for monitoring and management
- Airflow scheduler: Monitors DAGs and triggers tasks
- PostgreSQL: Stores Airflow metadata (not your papers)
- Redis: Task queue for Celery executor
- Airflow worker: Executes tasks in parallel

**Access:**
- Web UI available at localhost:8080
- Default credentials: airflow/airflow
- Browse example DAGs included

---

**Part 3: Reflection (15 min)**

**Document:**
1. How OpenSearch complements PostgreSQL capabilities
2. BM25 relevance scoring concept and importance
3. What problems Airflow solves vs manual scripts
4. How you'll use Airflow for paper ingestion pipeline
5. Sketch DAG structure you'll build next week

#### Key Concepts to Master

**OpenSearch Client Usage:**
- Initialize client with host, port, authentication
- Connection configuration for security
- Index document with index name and document ID
- Document body as Python dictionary (converts to JSON)
- Response includes success status and metadata

**Bulk Indexing for Efficiency:**
- Index many documents in single request
- Significantly faster than individual requests
- Less network overhead
- Use helpers module for convenient bulk operations
- Specify actions list with index and document data
- Handle partial failures in bulk operations

**Search with Filters:**
- Boolean query combines multiple conditions
- must clause: All conditions required (AND logic)
- should clause: At least one condition (OR logic)
- filter clause: Must match but doesn't affect score
- must_not clause: Must not match (NOT logic)
- Range queries for dates and numbers
- Term queries for exact matches on keywords
- Match queries for full-text search with relevance

**Pagination:**
- from: Starting position (0-based)
- size: Number of results per page
- Total results in hits.total.value
- Calculate total pages for UI

**Airflow DAG Structure:**
- DAG definition with unique ID and schedule
- Default arguments for all tasks (retries, timeout, etc.)
- Tasks created with operators
- Task dependencies defined with bitshift operators
- Tasks can run sequentially or in parallel

**Task Dependencies:**
- task1 >> task2: task1 runs before task2
- task1 >> [task2, task3]: task1 before both (parallel after)
- [task1, task2] >> task3: Both before task3 (parallel then join)
- Dependencies create execution graph

**Airflow Architecture:**
1. **Scheduler:** Monitors DAGs, triggers tasks when scheduled
2. **Executor:** Determines how tasks run (sequential, parallel, distributed)
3. **Worker:** Executes task logic (can have multiple workers)
4. **Metadata DB:** Stores DAG runs, task status, configuration
5. **Web UI:** Monitor, trigger, debug workflows visually

#### Practice Requirements

**Exercise 1: Complex Search Query**
- Search papers containing "attention mechanism"
- Filter to only cs.AI category papers
- Published after January 1, 2020
- Sort by published date (newest first)
- Return top 20 results with pagination
- Include highlighted snippets

**Exercise 2: Aggregations for Analytics**
- Count papers per category (faceted search)
- Count papers per month (date histogram)
- Average citation count per category
- Top 10 most common author names
- Understand aggregation structure

**Exercise 3: First Airflow DAG**
- Create simple DAG with meaningful ID
- Two tasks: First prints current date, second prints success message
- Second task depends on first task
- Schedule to run daily
- Test triggering manually in UI

**Exercise 4: Search Performance**
- Index 100 papers in bulk
- Measure bulk indexing time
- Perform 10 different searches
- Measure average search response time
- Compare to PostgreSQL LIKE query performance

#### End of Day 4 Checklist

- [ ] OpenSearch Python client installed successfully
- [ ] Created OpenSearch connection module with error handling
- [ ] Implemented paper search functionality with full features
- [ ] Tested keyword search with relevance ranking
- [ ] Tested filtering by category and date range
- [ ] Understand query DSL structure and syntax
- [ ] Know difference between match and term queries
- [ ] Airflow running via Docker Compose successfully
- [ ] Accessed Airflow web UI at localhost:8080
- [ ] Explored example DAGs in interface
- [ ] Understand DAG, Task, Operator concepts clearly
- [ ] Know Airflow use cases and benefits
- [ ] Spent approximately 90 minutes on focused learning

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
- Watch: First 20 minutes on multi-container applications

#### Reading Materials

**Airflow Best Practices:**
- Link: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
- Duration: 20 min

**Docker Compose Documentation:**
- Link: https://docs.docker.com/compose/
- Getting Started section and Compose file reference
- Duration: 15 min

#### Day 5 Schedule (90 minutes total)

**Part 1: Advanced Airflow Concepts (35 min)**

**Requirements:**

**1. Task Dependencies Patterns (15 min)**

**What to learn:**
- Linear dependencies: Task A then B then C (sequential pipeline)
- Fan-out pattern: A runs first, then B/C/D run in parallel
- Fan-in pattern: A/B/C run in parallel, then all feed into D
- Conditional execution: BranchOperator for if/else logic
- Task groups: Organize related tasks into logical units
- Dynamic task generation: Create tasks programmatically

**Linear Example:**
- Download paper → Parse paper → Index in OpenSearch
- Each task depends on previous completion

**Fan-out Example:**
- Fetch papers → [Download PDF 1, Download PDF 2, Download PDF 3]
- One task triggers multiple parallel downloads
- Efficient for I/O-bound operations

**Fan-in Example:**
- [Parse Introduction, Parse Methods, Parse Results] → Index Complete Paper
- Parallel processing of paper sections
- Combine results after all complete

**Conditional Example:**
- Check file size → [Process Large File, Process Small File]
- Different handling based on conditions

**2. Airflow Operators (20 min)**

**What to learn:**
- PythonOperator: Execute Python function with parameters
- BashOperator: Execute bash command or script
- PostgresOperator: Execute SQL query on PostgreSQL
- HttpOperator: Make REST API calls with retries
- CustomOperator: Create your own reusable operator

**When to use each:**
- PythonOperator: Complex Python logic, API calls, data processing
- BashOperator: System commands, file operations, CLI tools
- PostgresOperator: Database operations, data validation queries
- HttpOperator: REST API calls with built-in retry logic
- CustomOperator: Reusable logic across multiple DAGs

**Practice:**
- Create DAG with PythonOperator executing function
- Create DAG with BashOperator running system command
- Create DAG combining Python and Bash operators
- Implement error handling with on_failure_callback
- Implement retry logic with retries and retry_delay
- Implement success callbacks for notifications

---

**Part 2: Docker Compose for Full Stack (40 min)**

**Requirements:**

**1. Create complete docker-compose.yml for entire system**

**Services to define:**
- FastAPI application: Your REST API service
- PostgreSQL database: Relational data storage
- OpenSearch cluster: Full-text search engine
- Airflow webserver: UI for monitoring
- Airflow scheduler: DAG execution controller
- Airflow worker: Task executor
- Redis: Task queue for Airflow

**For each service specify:**
- Base image or build context directory
- Container name for easy reference
- Port mappings (host:container) for external access
- Environment variables for configuration
- Volume mounts for data persistence
- Network assignment for inter-service communication
- Health check commands and intervals
- Restart policy for resilience
- Dependency order (depends_on relationships)
- Resource limits (CPU, memory) optional

**What to figure out:**
- Service definition syntax in YAML
- Port mapping to avoid conflicts
- Volume mount paths for each service
- Environment variable format for each service
- Network configuration for service discovery
- Health check commands for each service
- Startup order to prevent failures
- Volume driver configuration

**2. Environment variable management**
- Create .env file for sensitive data (passwords, keys)
- Database credentials and connection strings
- API keys for external services
- OpenSearch admin password
- Airflow secret keys and passwords
- Never commit .env to version control (add to .gitignore)

**3. Data persistence configuration**
- PostgreSQL data volume: Persist database files
- OpenSearch data volume: Persist search indexes
- Airflow logs volume: Persist execution logs
- Downloaded PDFs volume: Persist paper files
- Volume driver selection (local, NFS, etc.)

**Test:**
- Start all services: docker-compose up -d
- Verify each service healthy: docker-compose ps
- FastAPI accessible at localhost:8000
- PostgreSQL accepting connections at localhost:5432
- OpenSearch responding at localhost:9200
- Airflow UI accessible at localhost:8080
- Check logs for all services: docker-compose logs
- Stop all services: docker-compose down
- Restart and verify data persists

---

**Part 3: Reflection (15 min)**

**Document:**
1. Task dependency patterns you'll use in pipeline
2. Which operators appropriate for which tasks
3. Why Docker Compose better than managing containers manually
4. Data persistence strategy for production
5. Network configuration understanding and importance

#### Key Concepts to Master

**Docker Compose Service Structure:**
- Version specification at top
- Services section lists all containers
- Each service has configuration block
- Networks section defines connectivity
- Volumes section defines persistent storage
- Top-level volumes are named and shared

**Service Configuration:**
- image: Pre-built image from registry
- build: Directory with Dockerfile to build
- container_name: Friendly name for reference
- ports: Map host:container for external access
- environment: Configuration via environment variables
- env_file: Load environment from file
- volumes: Mount host directories or named volumes
- networks: Assign to network for connectivity
- depends_on: Start order dependencies
- restart: Restart policy (always, on-failure, unless-stopped)

**Service Communication:**
- Services on same network discover each other by name
- FastAPI connects to postgres:5432 not localhost:5432
- Service name acts as hostname (DNS resolution)
- Internal ports used for inter-service communication
- External ports only needed for host access
- Isolated network for security

**Environment Variables:**
- Define in docker-compose.yml inline
- Or reference from .env file
- Or use env_file directive for multiple files
- Interpolation syntax: ${VARIABLE_NAME}
- Default values: ${VARIABLE_NAME:-default}

**Health Checks:**
- Command to test if service ready
- Interval: Time between health checks
- Timeout: Maximum time for check to complete
- Retries: Number of failures before unhealthy
- Start period: Initial grace period for startup
- depends_on with condition: service_healthy

**Startup Order:**
- depends_on: Start services in order
- But doesn't wait for service ready
- Use health checks for true readiness
- Implement retry logic in application code
- Can use wait-for-it script for complex dependencies

**Airflow DAG Best Practices:**
- Keep DAGs simple and readable
- Use meaningful task_id names
- Set appropriate retries and retry_delay
- Use execution_date for idempotency
- Don't process data in DAG file itself
- Only define structure in DAG file
- Use XCom for small data between tasks
- Use external storage for large data transfers

**Task Dependencies Methods:**
- Bitshift operators: task1 >> task2 >> task3
- set_downstream/set_upstream methods
- List syntax: task1 >> [task2, task3] >> task4
- chain function for linear dependencies
- Multiple dependencies create execution graph

#### Practice Requirements

**Exercise 1: Complete docker-compose.yml**
- Define all 7 services (API, PostgreSQL, OpenSearch, Airflow x3, Redis)
- Configure networking between all services
- Set up persistent volumes for data
- Add health checks for critical services
- Test: Bring up full stack, verify all healthy

**Exercise 2: Multi-Stage DAG**
- Stage 1: Check arXiv API for new papers
- Stage 2: Download PDFs (3 parallel tasks)
- Stage 3: Combine download results
- Stage 4: Update database with metadata
- Implement with proper task dependencies

**Exercise 3: Error Handling Callbacks**
- Add on_failure_callback for error notification
- Add on_retry_callback for retry logging
- Add on_success_callback for success confirmation
- Test by forcing task to fail
- Verify callbacks execute correctly

**Exercise 4: Environment Configuration**
- Create .env.example template file
- Document each variable purpose
- Set up .env file for local development
- Test services read environment correctly
- Verify sensitive data not in git

#### End of Day 5 Checklist

- [ ] Understand all Airflow operator types
- [ ] Know task dependency patterns (linear, fan-out, fan-in)
- [ ] Can create DAGs with multiple tasks and dependencies
- [ ] Implemented error handling callbacks in DAG
- [ ] Created complete docker-compose.yml with all services
- [ ] Defined all required services with proper configuration
- [ ] Configured networking for inter-service communication
- [ ] Set up data persistence with named volumes
- [ ] Services discover each other via service names
- [ ] Understand depends_on and health check relationship
- [ ] Tested starting and stopping full stack
- [ ] All services communicate correctly
- [ ] Spent approximately 90 minutes on focused learning

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

**Complete Stack Service Definitions**

**Services needed:**
1. FastAPI application for REST API
2. PostgreSQL database for metadata
3. OpenSearch cluster for full-text search
4. Airflow webserver for UI
5. Airflow scheduler for orchestration
6. Airflow worker for task execution
7. Redis for Airflow task queue

**For EACH service, define:**
- Base image or build context path
- Unique container name
- Port mappings from host to container
- Environment variables for configuration
- Volume mounts for persistence
- Network assignment (single bridge network)
- Health check configuration
- Restart policy for reliability
- Service dependencies (depends_on)
- Resource limits (optional but recommended)

**Networking requirements:**
- Create single bridge network: paper-network
- All services must be on same network
- Services access each other by service name
- Only expose necessary ports to host
- Internal communication via service names

**Volume requirements:**
- postgres-data: PostgreSQL database persistence
- opensearch-data: OpenSearch indexes persistence
- airflow-logs: Airflow execution logs
- airflow-dags: DAG files (bind mount to local directory)
- pdfs-storage: Downloaded PDFs persistence
- All volumes must survive container restarts

**Environment variables:**
- PostgreSQL: Database name, username, password
- OpenSearch: Admin password, memory limits
- Airflow: Executor type, database connection string
- FastAPI: Database URL, OpenSearch URL, environment mode
- Redis: No authentication required for development
- Use environment file for sensitive data

**What to figure out:**
- Correct image versions for stability
- Port mapping without host conflicts
- Volume mount paths inside each container
- Environment variable formats for each service
- Proper health check commands
- Startup order to prevent failures
- Memory and CPU limits if needed

**Success criteria:**
- All 7 services defined correctly
- No port conflicts between services
- Proper network configuration
- All volumes declared
- Environment variables parameterized not hardcoded
- Health checks for critical services
- Clear, readable YAML structure with comments
- Passes yaml lint validation

---

### HOUR 2: Service Integration & Testing

**Task 1: Verify Service Communication (30 min)**

**Requirements:**

**Test PostgreSQL connectivity:**
- FastAPI can connect to postgres:5432
- Airflow can connect for metadata storage
- Run test query from FastAPI container
- Run test query from Airflow scheduler
- Verify connection pooling works correctly
- Test connection retry logic

**Test OpenSearch connectivity:**
- FastAPI can reach opensearch:9200
- Can create index from FastAPI container
- Can index document successfully
- Can search documents successfully
- Verify authentication works
- Test error handling for connection failures

**Test Redis connectivity:**
- Airflow scheduler can connect to redis:6379
- Airflow worker can connect for task queue
- Verify Celery executor working
- Test task queuing mechanism

**What to verify:**
- Service name DNS resolution working
- Each service can reach required dependencies
- Authentication credentials working
- Connection timeouts configured properly
- Retry logic functioning correctly

---

**Task 2: End-to-End Workflow Test (30 min)**

**Requirements:**

**Create test workflow:**
1. Insert test paper metadata via FastAPI POST endpoint
2. Verify paper stored in PostgreSQL database
3. Index same paper in OpenSearch via API endpoint
4. Search for paper in OpenSearch by keyword
5. Retrieve paper metadata from PostgreSQL by ID
6. Verify data consistency between both databases

**Test scenarios:**
- Happy path: All services working perfectly
- PostgreSQL down: FastAPI handles gracefully with error
- OpenSearch down: Search returns error but app doesn't crash
- Restart individual services: Others continue working
- Restart all services: Data persists correctly

**What to verify:**
- Data persists after container restarts
- Error handling for service failures
- Connection retry logic working
- Timeout handling prevents hanging
- Logging provides useful debugging information

---

### HOUR 3: Health Checks & Monitoring

**Task 1: Implement Comprehensive Health Checks (30 min)**

**Requirements:**

**For each service implement:**

**PostgreSQL:**
- Test command: Check PostgreSQL ready to accept connections
- Interval: Every 10 seconds
- Timeout: 5 seconds
- Retries: 5 attempts
- Start period: 10 seconds for initialization

**OpenSearch:**
- Test command: Check cluster health endpoint returns success
- Interval: Every 30 seconds
- Timeout: 10 seconds
- Retries: 5 attempts
- Start period: 60 seconds (needs time to initialize)

**FastAPI:**
- Test command: Check health endpoint returns 200 status
- Interval: Every 30 seconds
- Timeout: 10 seconds
- Retries: 3 attempts
- Start period: 40 seconds

**Airflow Webserver:**
- Test command: Check health endpoint returns success
- Interval: Every 30 seconds
- Timeout: 10 seconds
- Retries: 3 attempts
- Start period: 60 seconds

**What to figure out:**
- Appropriate check intervals for each service
- Correct health check endpoints
- Sufficient startup periods for initialization
- Reasonable retry counts
- Appropriate timeout values
- Commands that work inside containers

---

**Task 2: Create Monitoring Endpoints (30 min)**

**Requirements:**

**Add to FastAPI application:**

**GET /health endpoint:**
- Returns 200 status if service healthy
- Checks PostgreSQL connection status
- Checks OpenSearch connection status
- Returns JSON with detailed service status
- Includes timestamp of check
- Used by Docker health checks

**GET /metrics endpoint:**
- Total papers in PostgreSQL database
- Total papers in OpenSearch index
- Last successful ingestion timestamp
- Storage usage statistics
- Service uptime duration
- Response times for last operations

**Implement in each service:**
- Graceful shutdown handlers
- Log rotation configuration
- Error logging to persistent files
- Service startup logged clearly
- Performance metrics collection

**Test procedures:**
- Verify health endpoint returns 200 when healthy
- Verify metrics endpoint returns valid data
- Check log files being written correctly
- Test health check during service restart
- Verify unhealthy status detected properly

---

### HOUR 4: Polish & Documentation

**Task 1: Create Comprehensive README (30 min)**

**Requirements:**

**Document complete structure:**

**1. System Architecture Section**
- Architecture diagram (ASCII art or link to image)
- Description of each service role
- Port mappings reference table
- Network diagram showing connectivity
- Data flow explanation step by step

**2. Prerequisites Section**
- Docker Desktop/Engine minimum version
- Docker Compose minimum version
- System requirements (RAM, disk space)
- Operating system compatibility notes

**3. Installation Section**
- Clone repository instructions
- Create environment file from template
- Edit environment file instructions
- Build and start services command
- Verify all services running
- Check logs command
- Access each service URLs

**4. Configuration Section**
- Environment variables detailed explanation
- Each variable's purpose
- Default values provided
- Required vs optional variables
- Security considerations for production

**5. Usage Section**
- Accessing FastAPI: URL and documentation
- Accessing Airflow: URL and credentials
- Accessing OpenSearch: URL and authentication
- Accessing PostgreSQL: Connection details
- Example API calls

**6. Troubleshooting Section**
- Common issues and solutions
- Service unhealthy: Check logs and endpoints
- Port already in use: Change port mappings
- Can't connect to PostgreSQL: Check connection string
- View logs command for each service
- Restart individual service command
- Reset entire stack commands

**7. Maintenance Section**
- Backup procedures for data
- Update procedures for services
- Scaling considerations
- Data cleanup procedures
- Monitoring recommendations

---

**Task 2: Create Environment Template (10 min)**

**Requirements:**

**Create .env.example file with:**
- PostgreSQL configuration variables
- OpenSearch configuration variables
- FastAPI configuration variables
- Airflow configuration variables
- arXiv API configuration (for Week 4)
- Storage configuration variables

**Document:**
- How to generate Fernet key for Airflow
- Security warning about default passwords
- Which values must be changed for production
- Format requirements for each variable

---

**Task 3: Final Testing & Validation (20 min)**

**Requirements:**

**Complete test checklist:**
- docker-compose up -d succeeds without errors
- All services show "healthy" in docker-compose ps
- FastAPI /health endpoint returns 200 status
- Airflow UI accessible at localhost:8080
- PostgreSQL accepting connections
- OpenSearch responding to queries
- Can create test paper via API
- Paper stored in PostgreSQL correctly
- Paper indexed in OpenSearch
- Can retrieve paper via both databases
- docker-compose down cleans up properly
- docker-compose up -d again, data persists
- Logs accessible via docker-compose logs

**Test failure scenarios:**
- Stop PostgreSQL: FastAPI handles error gracefully
- Stop OpenSearch: Search fails but app doesn't crash
- Restart one service: Others continue working
- Kill container: Docker restarts automatically
- Simulate network issues: Retry logic works

---

### Day 6 Deliverables

**Working Infrastructure:**
- [ ] Complete docker-compose.yml with 7 services
- [ ] All services running and healthy
- [ ] Service-to-service communication working
- [ ] Data persistence configured correctly
- [ ] Health checks implemented for all services
- [ ] Monitoring endpoints functional

**Documentation:**
- [ ] README.md with comprehensive instructions
- [ ] .env.example with all variables documented
- [ ] Architecture diagram or description
- [ ] Troubleshooting guide with solutions
- [ ] Usage instructions clear and complete

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
- [ ] Restart capability tested
- [ ] All health checks passing

### Common Issues & Solutions

**Issue: "Port 5432 already in use"**
- Solution: Change host port in docker-compose.yml to 5433:5432
- Or stop local PostgreSQL service
- Identify what's using port: lsof -i :5432

**Issue: "OpenSearch won't start - vm.max_map_count too low"**
- Solution: Increase virtual memory limit on host
- Linux command: sysctl -w vm.max_map_count=262144
- Make permanent: Add to /etc/sysctl.conf

**Issue: "Airflow webserver healthy but can't access UI"**
- Solution: Check firewall rules
- Verify port mapping correct
- Check webserver logs for errors
- Verify on correct host IP address

**Issue: "Services can't communicate"**
- Solution: Verify all on same network
- Use service names not localhost
- Check network created: docker network ls
- Inspect network: docker network inspect

**Issue: "Out of disk space"**
- Solution: Prune unused Docker data
- Remove unused images: docker image prune
- Remove unused volumes: docker volume prune
- Remove everything: docker system prune -a --volumes

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
- PostgreSQL accessible from host machine
- OpenSearch accessible from host machine
- FastAPI accessible from host machine
- Airflow UI accessible from host machine
- All services see each other on internal network

**Test Suite 2: Data Flow**
- Create paper via FastAPI POST endpoint
- Verify paper in PostgreSQL using query
- Index same paper in OpenSearch via API
- Search via OpenSearch API successfully
- Retrieve via FastAPI GET endpoint
- Verify data consistency across systems

**Test Suite 3: Persistence**
- Create test data in all systems
- Stop all services: docker-compose down
- Start services: docker-compose up -d
- Verify all data still exists
- Confirm volumes working correctly

**Test Suite 4: Error Handling**
- Stop PostgreSQL, verify FastAPI error handling
- Stop OpenSearch, verify search returns proper error
- Send invalid data to API, verify proper error response
- Attempt duplicate paper insertion, verify conflict handling

**Test Suite 5: Performance**
- Bulk insert 100 papers into PostgreSQL
- Measure total insert time
- Bulk index 100 papers in OpenSearch
- Perform 50 search queries
- Measure average search response time
- Verify no memory leaks during operations

**What to document:**
- Test results for each suite (pass/fail)
- Any failures discovered and fixes applied
- Performance baseline metrics established
- Known issues or limitations identified
- Recommendations for improvements

---

**Task 2: Create Test Scripts (30 min)**

**Requirements:**

**Create test_infrastructure.py script:**
- Test PostgreSQL connection successful
- Test OpenSearch connection successful
- Test FastAPI endpoints responding
- Test Airflow API accessible
- Run all tests with pytest framework
- Generate test report with results

**Create test_data_flow.py script:**
- Insert test paper into system
- Verify in PostgreSQL database
- Index in OpenSearch
- Search for paper successfully
- Delete paper from both systems
- Verify cleanup successful

**Create load_test.py script:**
- Insert 1000 test papers
- Measure throughput (papers per second)
- Calculate error rate percentage
- Monitor system stability
- Verify no service crashes

**Run all tests:**
- Execute infrastructure tests verbosely
- Execute data flow tests verbosely
- Execute load tests with monitoring
- Collect results and metrics

**Success criteria:**
- All tests pass successfully
- Clear error messages for any failures
- Tests are repeatable without manual intervention
- Tests clean up after themselves
- Performance metrics collected

---

### HOUR 2: Documentation & Examples

**Task 1: Create API Examples Document (30 min)**

**Requirements:**

**Create EXAMPLES.md file with:**

**Example 1: Create Paper**
- HTTP method and endpoint
- Required headers
- Request body with complete paper data
- Expected response with status code
- Error scenarios and responses

**Example 2: Search Papers**
- HTTP GET request with query parameters
- Multiple search parameter examples
- Expected response format
- Pagination example
- Filter combination examples

**Example 3: Get Paper by ID**
- HTTP GET request with path parameter
- Expected successful response
- 404 error scenario
- Response time expectations

**Example 4: Update Paper Status**
- HTTP PATCH request details
- Request body for status update
- Success response format
- Validation error scenarios

**Example 5: Direct PostgreSQL Query**
- Command to execute query in container
- Sample queries for common tasks
- How to export query results

**Example 6: Direct OpenSearch Query**
- Command to query via REST API
- Sample search queries
- Aggregation query examples
- How to analyze results

---

**Task 2: Create Architecture Documentation (30 min)**

**Requirements:**

**Create ARCHITECTURE.md document:**

**Section 1: System Overview**
- High-level architecture diagram or description
- Component descriptions and responsibilities
- Technology stack with versions
- Design decisions and rationale

**Section 2: Service Details**

**For each service document:**
- Purpose and responsibility in system
- Technology and version used
- Port mappings (internal and external)
- Environment variables required
- Data storage location
- Dependencies on other services
- Scaling considerations

**Section 3: Data Flow**
- Paper ingestion flow (Week 4 preview)
- Search request flow
- API request flow
- Database interaction patterns

**Section 4: Database Schemas**

**PostgreSQL tables:**
- Complete table definition
- All columns with types
- Constraints and indexes
- Relationships between tables

**OpenSearch mappings:**
- Index structure
- Field definitions with types
- Analyzer configurations
- Search optimization settings

**Section 5: Network Architecture**
- Bridge network configuration
- Service discovery mechanism
- Port mapping strategy
- Security considerations

**Section 6: Volume Architecture**
- Data persistence strategy
- Backup considerations
- Volume locations and purposes
- Cleanup procedures

---

### HOUR 3: Week 3 Reflection & Week 4 Prep

**Task 1: Week 3 Reflection (30 min)**

**Requirements:**

**Create WEEK3_REFLECTION.md document:**

**What you learned:**
- Docker containerization concepts and benefits
- Docker Compose orchestration capabilities
- PostgreSQL relational database design
- OpenSearch full-text search implementation
- Apache Airflow workflow orchestration
- Service networking and communication
- Data persistence strategies
- Health checks and monitoring

**What was challenging:**
- Most difficult concepts encountered
- Bugs and issues faced
- Time management across topics
- Balance between depth and breadth

**What clicked:**
- "Aha!" moments during learning
- Concepts that suddenly made sense
- Connections between technologies

**How it connects to ML/AI:**
- Why these tools matter for ML pipelines
- Production ML infrastructure requirements
- Scalability considerations
- Real-world applications in fintech

**Skills assessment:**
- Docker proficiency: Rate 1-10 with justification
- PostgreSQL proficiency: Rate 1-10 with justification
- OpenSearch proficiency: Rate 1-10 with justification
- Airflow proficiency: Rate 1-10 with justification
- Overall confidence: Rate 1-10 with justification

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
- Understand query parameter syntax
- Examine example XML responses
- Identify fields to extract from responses
- Plan data validation strategy

**Prepare for PDF processing:**
- Research GROBID (academic PDF parser tool)
- Understand challenges of PDF parsing
- Review Docling as fallback option
- Plan storage organization strategy

**Prepare for Airflow DAG:**
- Sketch pipeline task flow on paper
- Identify all steps in complete pipeline
- Plan error handling for each step
- Consider scheduling (daily at 2 AM?)

**Set up accounts/access:**
- No API key needed for arXiv (public API)
- GROBID runs locally via Docker
- Docling is open source library

**Mental preparation:**
- Week 4 is implementation-heavy
- All infrastructure now ready
- Focus on data pipeline business logic
- Debugging will be important skill
- Stay organized with incremental testing

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
- ✅ Python database integration with psycopg3
- ✅ OpenSearch indexing and searching
- ✅ Airflow DAG creation and task dependencies
- ✅ Service networking and communication

**Deliverables:**
- ✅ Working Docker Compose infrastructure
- ✅ All services communicating successfully
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
- Practical examples with API

**Video 2: "XML Parsing in Python"**
- Link: https://www.youtube.com/watch?v=j0xr0-IAqyk
- Duration: 15:00
- ElementTree basics for XML handling

#### Reading Materials

**arXiv API User Manual:**
- Link: https://arxiv.org/help/api/user-manual
- Duration: 45 min
- Complete guide to API features

**Article: "Building Data Pipelines"**
- Link: https://realpython.com/python-data-pipeline/
- Duration: 20 min
- Pipeline architecture patterns

#### Day 8 Schedule (90 minutes total)

**Part 1: Understanding arXiv API (30 min)**

**Requirements:**

**1. Read API documentation thoroughly (15 min)**

**What to understand:**
- Base URL structure for API requests
- Query parameters (search_query, max_results, start, sortBy, sortOrder)
- Response format (Atom XML standard)
- Rate limits (3 seconds between requests mandatory)
- Search field codes: ti (title), au (author), cat (category), abs (abstract)
- Boolean operators: AND, OR, ANDNOT
- Date range filtering syntax
- Pagination with start parameter

**2. Test API manually with various queries (15 min)**

**Test different query types:**
- Get latest papers from cs.AI category
- Search by keyword across all fields
- Multiple categories with OR operator
- Date range filtering
- Pagination through results
- Author-specific queries
- Title-specific queries

**Examine XML response structure:**
- Entry structure and elements
- Available fields in each entry
- PDF link location in response
- Author format and handling
- Category format and handling
- Date formats used

---

**Part 2: Create arXiv Client Module (45 min)**

**Requirements:**

**Create arxiv_client.py module with ArxivClient class:**

**Method 1: Initialize client**
- Accept base URL parameter
- Accept rate limit seconds parameter (default 3)
- Track last request timestamp
- Initialize logging for debugging

**Method 2: Search papers**
- Build query URL with parameters
- Respect rate limits (sleep if needed)
- Make GET request with timeout
- Handle HTTP errors gracefully
- Return XML response text
- Log all request details

**Method 3: Parse XML entry**
- Extract arxiv_id from entry ID element
- Extract title and clean whitespace
- Extract authors list from author elements
- Extract abstract/summary text
- Extract category tags
- Extract published date in ISO format
- Extract PDF URL
- Extract last updated date
- Return structured dictionary
- Handle missing elements

**Method 4: Fetch papers from category**
- Call search method with parameters
- Parse XML response using ElementTree
- Handle XML namespaces correctly
- Loop through all entry elements
- Parse each entry to dictionary
- Collect papers into list
- Handle parsing errors gracefully
- Return list of paper dictionaries

**Method 5: Fetch recent papers**
- Calculate date range (today minus N days)
- For each category in list
- Build date-filtered query string
- Fetch papers from category
- Collect all results
- Remove duplicates by arxiv_id
- Sort by published date descending
- Return combined list

**Error handling requirements:**
- HTTP errors (network issues, API unavailable)
- XML parsing errors (malformed response)
- Missing required fields in entries
- Rate limit errors (429 status code)
- Timeout errors (slow network)
- Invalid category queries

**What to figure out:**
- XML namespace handling in Atom feeds
- Proper date parsing from ISO 8601 format
- Rate limiting implementation with timestamps
- Logging best practices for debugging
- Request retries with exponential backoff
- Data cleaning (strip whitespace, handle None values)
- Efficient XML parsing with ElementTree

---

**Part 3: Testing & Validation (15 min)**

**Requirements:**

**Create test_arxiv_client.py script:**

**Test case 1: Single category fetch**
- Fetch 5 papers from cs.AI category
- Verify exactly 5 papers returned
- Verify all required fields present in each
- Print sample paper to inspect

**Test case 2: Multiple categories**
- Fetch from cs.AI and cs.LG categories
- Verify papers from both categories present
- Verify no duplicate papers in results

**Test case 3: Recent papers with date filtering**
- Fetch papers from last 7 days
- Verify all papers within date range
- Verify sorted by date correctly

**Test case 4: Error handling**
- Invalid category (expect empty results)
- Network timeout (expect retry and recovery)
- Malformed response (expect logging and graceful handling)

**Test case 5: Rate limiting**
- Make 3 requests rapidly
- Verify 3 second gaps between requests
- Check logs confirm rate limit enforcement

**Success criteria:**
- All tests pass successfully
- No crashes on errors
- Rate limits respected consistently
- Clean data extraction working
- Logging provides useful information

#### Key Concepts to Master

**arXiv API Query Structure:**
- Base URL with query parameters
- search_query parameter with field codes
- Pagination with start and max_results
- Sorting options (submittedDate, lastUpdatedDate, relevance)
- Sort order (ascending or descending)

**XML Parsing with ElementTree:**
- Parse XML string to tree structure
- Navigate tree with find and findall
- Handle XML namespaces properly (Atom namespace)
- Extract text from elements safely
- Extract attributes from elements
- Iterate through child elements

**Rate Limiting Pattern:**
- Track timestamp of last request
- Calculate time elapsed since last request
- Sleep for remaining time if needed
- Update timestamp after each request
- Prevents API rate limit violations

**Retry Logic with Backoff:**
- Attempt request with error handling
- If fails, wait and retry
- Increase wait time exponentially (backoff)
- Maximum retry attempts limit
- Log each attempt for debugging

**Data Validation:**
- Check required fields present
- Validate data formats correct
- Handle missing optional fields
- Validate arxiv_id format
- Clean whitespace from text fields

#### Practice Requirements

**Exercise 1: Build Query String Function**
- Function accepts multiple parameters
- Returns properly formatted query URL
- Handles special characters in queries
- Supports all query field types
- Handles date range formatting

**Exercise 2: Parse Authors Array**
- arXiv returns multiple author elements
- Extract all author names into list
- Handle single author case
- Handle many authors (20+) case
- Clean author name formatting

**Exercise 3: Extract Clean arXiv ID**
- From full URL: http://arxiv.org/abs/1706.03762v2
- Extract paper ID: 1706.03762
- Remove version suffix (v2, v1, etc.)
- Handle different ID formats (old and new)
- Validate ID format

**Exercise 4: Date Range Query**
- Fetch papers between two specific dates
- Use submittedDate filter in query
- Parse dates correctly
- Format dates for API correctly
- Handle timezone issues

#### End of Day 8 Checklist

- [ ] Thoroughly understand arXiv API structure
- [ ] Know all query parameters and formats
- [ ] Created ArxivClient class with all methods
- [ ] Implemented search method with rate limiting
- [ ] Implemented XML parsing successfully
- [ ] Implemented data extraction for all fields
- [ ] Error handling works for all scenarios
- [ ] Created comprehensive test script
- [ ] All tests passing consistently
- [ ] Can fetch papers from arXiv reliably
- [ ] Data validation prevents bad data
- [ ] Rate limiting prevents API violations
- [ ] Spent approximately 90 minutes focused

---

### Day 9 (Tue Dec 9): PDF Download Logic + Storage

#### Primary Video Resources

**Video 1: "Downloading Files with Python"**
- Link: https://www.youtube.com/watch?v=_Zr1z_FVpHs
- Duration: 15:00
- Using requests library for file downloads

**Video 2: "File Management in Python"**
- Link: https://realpython.com/working-with-files-in-python/
- Duration: 20 min reading
- File I/O, paths, organization strategies

#### Reading Materials

**Article: "Downloading Large Files"**
- Link: https://www.geeksforgeeks.org/downloading-files-web-using-python/
- Duration: 10 min
- Streaming downloads for large files

**Article: "Python Path Management"**
- Link: https://realpython.com/python-pathlib/
- Duration: 15 min
- Modern path handling with pathlib

#### Day 9 Schedule (90 minutes total)

**Part 1: PDF Download Manager (45 min)**

**Requirements:**

**Create pdf_downloader.py module with PDFDownloader class:**

**Method 1: Initialize downloader**
- Accept storage base directory path
- Accept rate limit seconds between downloads
- Track last download timestamp
- Create storage directories if needed
- Initialize logging for operations

**Method 2: Generate organized filepath**
- Accept arxiv_id as parameter
- Extract year and month from arxiv_id
- Create directory structure: /storage/YYYY/MM/
- Generate filename: arxiv_id.pdf
- Create subdirectories if not exist
- Return complete Path object

**Method 3: Download single PDF**
- Check if already downloaded (skip if exists)
- Respect rate limits before downloading
- Stream download (don't load entire file to memory)
- Save to generated filepath atomically
- Verify download successful (file size > 0)
- Handle download errors gracefully
- Return filepath if success, None if failure
- Log all operations

**Method 4: Batch download multiple PDFs**
- Accept list of papers with PDF URLs
- Loop through papers list
- Extract PDF URL for each paper
- Download with rate limiting between
- Track successes, failures, skips
- Return statistics dictionary
- Log progress throughout

**Method 5: Verify PDF validity**
- Accept filepath as parameter
- Check file exists at path
- Check file size reasonable (> 1KB, < 50MB)
- Try to open with PDF library
- Verify it's valid PDF format
- Return True if valid, False otherwise

**What to figure out:**
- Streaming downloads for memory efficiency
- File organization strategy by date
- Handling partial or corrupted downloads
- Checking existing files before re-downloading
- Progress tracking for batch operations
- Error handling (network errors, disk full, corrupted files)
- Logging download statistics and errors
- Atomic file writes to prevent corruption

---

**Part 2: Storage Organization System (25 min)**

**Requirements:**

**1. Design directory structure**

**Proposed organization:**
- Base directory: /data/pdfs/
- Year subdirectories: 2024/, 2023/, etc.
- Month subdirectories within year: 01/, 02/, etc.
- PDF files: arxiv_id.pdf
- Failed downloads directory: /failed/ for retry tracking

**Benefits of this structure:**
- Easy navigation by date
- Reasonable file count per directory
- Can process by time period
- Easy cleanup of old data
- Clear organization

**2. Implement storage manager class**

**StorageManager class methods:**
- get_storage_stats(): Return total files, total size, breakdown by year/month
- find_pdf(arxiv_id): Locate PDF file by arxiv_id efficiently
- cleanup_failed(): Remove failed download attempts
- get_pdfs_by_date_range(start, end): Get all PDFs in date range
- verify_all_pdfs(): Check all PDFs are valid and not corrupted

**3. Database integration**

**Update papers table with new columns:**
- pdf_path: Full path to PDF file
- pdf_size_bytes: File size for monitoring
- download_attempts: Number of download tries
- download_error: Last error message if failed

**After successful download:**
- Update pdf_path in database record
- Update pdf_size_bytes from file
- Update downloaded_at timestamp
- Set parsing_status to 'downloaded'

**After failed download:**
- Increment download_attempts counter
- Store download_error message
- Set parsing_status to 'failed' if max attempts reached
- Schedule retry if under max attempts

---

**Part 3: Testing & Integration (20 min)**

**Requirements:**

**Create test_pdf_download.py script:**

**Test case 1: Single PDF download**
- Select one paper's PDF URL
- Download using PDFDownloader
- Verify file exists at expected path
- Verify file is valid PDF
- Verify database updated correctly

**Test case 2: Batch download**
- Download 5 papers in batch
- Track statistics (success, failed, skipped)
- Verify all 5 downloaded successfully
- Verify directory organization correct

**Test case 3: Resume capability**
- Download 5 papers successfully
- Attempt downloading same 5 again
- Should skip existing (fast operation)
- Verify skip count correct in statistics

**Test case 4: Error handling**
- Invalid PDF URL (404 error expected)
- Network timeout simulation
- Disk space simulation (if feasible)
- Corrupted PDF handling

**Test case 5: Storage statistics**
- Download 10 papers
- Get storage statistics
- Verify counts and sizes accurate
- Verify grouping by year/month correct

**Success criteria:**
- Downloads work reliably
- Rate limiting enforced consistently
- Database updated correctly for all outcomes
- Error handling robust and informative
- Can resume interrupted batch downloads
- Storage organized properly by date
- Performance acceptable for batch operations

#### Key Concepts to Master

**Streaming Downloads:**
- Don't load entire file into memory
- Download in chunks (8KB typical)
- Write each chunk to disk immediately
- Memory-efficient for large files
- Can show progress for large downloads

**Path Management with pathlib:**
- Modern path handling in Python
- Platform-independent path operations
- Easy directory creation with parents
- Simple path joining with / operator
- Convenient file existence checking
- File size and metadata access

**PDF Validation:**
- Verify file can be opened as PDF
- Check number of pages > 0
- Validates file not corrupted
- Prevents processing invalid files
- Early detection of download problems

**Database Update After Download:**
- Connect to database
- Update record with download information
- Include filepath, size, timestamp
- Update status for processing pipeline
- Handle update errors

**Batch Processing with Progress:**
- Iterate through items with progress indication
- Track statistics throughout process
- Report progress to user
- Handle errors without stopping batch
- Summary statistics at end

#### Practice Requirements

**Exercise 1: Extract Year/Month from arXiv ID**
- New format: YYMM.NNNNN (e.g., 2401.00123 = January 2024)
- Old format: category/YYMMNNN
- Extract year and month accurately
- Use for directory organization
- Handle both old and new formats

**Exercise 2: Implement Retry Logic**
- Maximum 3 download attempts per PDF
- Exponential backoff (wait 2s, 4s, 8s)
- Log each attempt clearly
- Update database with attempt count
- Give up after max attempts

**Exercise 3: Storage Cleanup**
- Find PDFs with 'failed' status in database
- Check if files exist on disk
- Delete orphaned files (file exists but record deleted)
- Update database if files missing
- Clean up empty directories

**Exercise 4: Parallel Downloads (Optional Advanced)**
- Use ThreadPoolExecutor for concurrency
- Download 10 PDFs in parallel
- Maintain rate limiting globally
- Handle thread-safe file writes
- Aggregate statistics from threads

#### End of Day 9 Checklist

- [ ] Created PDFDownloader class completely
- [ ] Implemented download method with streaming
- [ ] Streaming downloads working efficiently
- [ ] Rate limiting implemented and enforced
- [ ] File organization by year/month working
- [ ] Database updates after successful downloads
- [ ] Database updates after failed downloads
- [ ] Created StorageManager class
- [ ] Implemented storage statistics calculation
- [ ] Error handling for all download failure scenarios
- [ ] Can resume interrupted batch downloads
- [ ] PDF validation working correctly
- [ ] Test script with all test cases written
- [ ] All tests passing consistently
- [ ] Spent approximately 90 minutes focused

---

### Remaining Days (Wed-Sun) Preview

**Day 10 (Wed): GROBID Setup + XML Parsing**
- Install GROBID via Docker for PDF parsing
- Understand GROBID TEI XML output format
- Parse sections, citations, figures metadata
- Extract structured content from papers
- Store parsed data in PostgreSQL

**Day 11 (Thu): Docling Fallback Parser**
- Install Docling library
- Implement fallback logic (GROBID first, Docling if fails)
- Compare output quality between parsers
- Store parsed content with metadata
- Handle parsing errors gracefully

**Day 12 (Fri): Airflow DAG Creation**
- Design complete pipeline DAG architecture
- Task 1: Fetch new papers from arXiv API
- Task 2: Download PDFs (parallel tasks)
- Task 3: Parse with GROBID/Docling
- Task 4: Index in OpenSearch
- Task dependencies and error handling
- Scheduling and monitoring

**Day 13 (Sat): Automated Daily Pipeline (4h)**
- Complete DAG implementation with all tasks
- Schedule for daily 2 AM execution
- Implement monitoring and alerting
- Test complete end-to-end pipeline
- Handle failures and retries
- Performance optimization

**Day 14 (Sun): Testing, Monitoring & Documentation (3h)**
- Comprehensive integration testing
- Create monitoring dashboard
- Document complete system
- Week 4 comprehensive reflection
- Prepare for Week 5 (LLM Fundamentals)

---

## Additional Resources

### Tools

**Postman or Insomnia:**
- API testing graphical interfaces

**DBeaver:**
- Database GUI for PostgreSQL visualization
- Download: https://dbeaver.io/

**OpenSearch Dashboards:**
- Visualization and monitoring UI
- Bundled with OpenSearch

### Supplementary Learning

**Docker Documentation:**
- https://docs.docker.com/
- Reference for all Docker commands and features

**PostgreSQL Tutorial:**
- https://www.postgresqltutorial.com/
- Comprehensive SQL learning guide

**Airflow Best Practices:**
- https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
- Production-ready DAG development

### Community Resources

**Docker Community Forum:**
- https://forums.docker.com/
- Help with Docker issues

**Airflow Slack Channel:**
- https://apache-airflow-slack.herokuapp.com/
- Active community support

**Stack Overflow:**
- Search for specific error messages
- Active PostgreSQL and OpenSearch communities

---

## Success Metrics

### By End of Week 3-4

You should be able to:

**Infrastructure Skills:**
- ✅ Run multi-container applications with Docker Compose
- ✅ Design and implement database schemas
- ✅ Implement full-text search with OpenSearch
- ✅ Create workflow orchestration with Airflow

**Data Engineering Skills:**
- ✅ Integrate with external REST APIs
- ✅ Download and store large files efficiently
- ✅ Parse and extract structured data
- ✅ Build automated data pipelines

**Production Engineering Skills:**
- ✅ Implement health checks and monitoring
- ✅ Implement error handling and retry logic
- ✅ Set up logging and debugging
- ✅ Write comprehensive documentation
- ✅ Create thorough test suites

### You do NOT need to:

- ❌ Master every Docker feature (focus on essentials)
- ❌ Become PostgreSQL DBA expert (basic operations sufficient)
- ❌ Optimize for 100k papers initially (start small, iterate)
- ❌ Perfect the system immediately (continuous improvement mindset)

---

## Looking Ahead: Week 5

### You're Ready Because:

- ✅ Infrastructure is production-ready and tested
- ✅ Data pipeline is automated and reliable
- ✅ You understand orchestration patterns
- ✅ Error handling is comprehensive and robust

### Week 5 Preview: LLM Fundamentals

- Monday: Andrej Karpathy LLM foundation lectures
- Tuesday: Transformer architecture conceptual overview
- Wednesday: Embeddings deep-dive and applications
- Thursday: OpenAI API basics and authentication
- Weekend: Prompt engineering for paper search and categorization

**You've built the infrastructure foundation. Now we add AI intelligence! 🚀**

---

## Tips for Success

### General Advice

1. **Start Simple**: Get basic version working before adding complexity
2. **Test Frequently**: Don't build everything then test at end
3. **Document as You Go**: Don't wait until end of week
4. **Ask for Help**: When stuck > 30 min, seek assistance
5. **Take Breaks**: Complex systems need fresh perspective

### If You Get Stuck

**Docker issues:**
- Check logs: docker-compose logs service_name
- Restart specific service: docker-compose restart service_name
- Rebuild: docker-compose up -d --build
- Remove all and start fresh: docker-compose down -v

**Database connection issues:**
- Connect directly: docker exec -it postgres psql -U postgres
- Check if accepting connections: docker exec postgres pg_isready
- View tables: psql command \dt
- Check connection string format

**Network connectivity issues:**
- Verify network exists: docker network ls
- Inspect network: docker network inspect paper-network
- Check service names resolve correctly
- Verify services on same network

**Airflow workflow issues:**
- Check scheduler logs: docker-compose logs airflow-scheduler
- Test Python function independently first
- Use print statements, check task logs
- Trigger DAG manually in UI for testing
- Check task dependencies are correct

---

## License

This learning plan is for personal educational use.

---

**Last Updated:** November 2025
**Plan Version:** Final 8.5-Month Career Transition Plan
**Current Status:** Week 3-4 Infrastructure & Data Pipeline
**Next:** Week 5 LLM Fundamentals begins December 15, 2025