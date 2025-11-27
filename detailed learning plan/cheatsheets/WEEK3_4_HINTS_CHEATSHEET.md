# Week 3-4 Hints & Cheat Sheet

## Purpose

Quick reference guide when you get stuck. Contains hints, patterns, and key reminders - **NOT full solutions**. Try to solve problems yourself first, then use these hints if needed.

---

## WEEK 3: INFRASTRUCTURE SETUP

### Day 1: Docker Fundamentals

**Docker Commands Pattern:**
```
docker [command] [options] [image/container]
```

**Common Commands Structure:**
- Pull: `docker pull [image:tag]`
- Run: `docker run [options] [image]`
- List running: `docker ps`
- List all: `docker ps -a`
- Stop: `docker stop [container-id]`
- Remove: `docker rm [container-id]`

**Port Mapping Hint:**
- Format: `-p [host-port]:[container-port]`
- Example: Map container port 8000 to host port 8080

**Volume Mounting Hint:**
- Format: `-v [host-path]:[container-path]`
- Use absolute paths for host
- Container path depends on where app expects data

**Interactive Mode Hint:**
- Use `-it` flags together
- `-i` keeps STDIN open
- `-t` allocates pseudo-TTY
- Combine with `bash` or `sh` for shell access

---

### Day 2: FastAPI in Docker + PostgreSQL

**Dockerfile Structure Pattern:**
```
Base image → Working directory → Copy dependencies → 
Install dependencies → Copy code → Expose port → Command
```

**Layer Caching Key:**
- Order matters - least changing first
- Requirements before code
- Each instruction = new layer
- Unchanged layers use cache

**PostgreSQL Connection String Pattern:**
```
postgresql://[user]:[password]@[host]:[port]/[database]
```

**psql Command Pattern:**
```
psql -U [username] -d [database]
```

**SQL Command Structure:**
- CREATE TABLE: Define structure first
- INSERT INTO: Specify table and values
- SELECT: Choose columns, use WHERE for filtering
- UPDATE: Set new values, use WHERE for targeting
- DELETE: Use WHERE or delete all rows

**Key psql Commands:**
- `\c [database]` - Switch database
- `\dt` - List all tables
- `\d [table]` - Describe table structure
- `\q` - Quit psql

---

### Day 3: PostgreSQL + OpenSearch

**psycopg3 Connection Pattern:**
- Use context manager (with statement)
- Connection string with all parameters
- Always close connections (context manager does this)

**Parameterized Query Hint:**
- Never use string formatting with user input
- Use `%s` placeholder in query
- Pass values as tuple in second parameter
- Library handles escaping

**PostgreSQL Array Column:**
- Column type: `TEXT[]` or `VARCHAR(50)[]`
- Insert: Pass Python list
- Query: Use `ANY()` operator for contains check

**OpenSearch Index Mapping Fields:**
- `text` type: Analyzed for full-text search
- `keyword` type: Exact match only
- `date` type: For temporal filtering
- `integer` type: For numeric operations

**OpenSearch Query Structure:**
- Wrap in `query` object
- `match` for full-text search
- `term` for exact keyword match
- `range` for numeric/date filtering

---

### Day 4: OpenSearch + Airflow

**OpenSearch Client Connection:**
- Needs host, port
- Authentication (user, password)
- SSL settings (can disable for local)

**OpenSearch Index Document:**
- Specify index name
- Optional document ID
- Document body as dictionary

**OpenSearch Search Query Pattern:**
```
{
  "query": {
    "bool": {
      "must": [...],      # All required (AND)
      "should": [...],    # At least one (OR)
      "filter": [...]     # Must match, no score
    }
  }
}
```

**OpenSearch Pagination:**
- `from`: Starting position (0-based)
- `size`: Number of results
- Calculate: `from = (page - 1) * size`

**Airflow DAG Structure Pattern:**
```
Import DAG and operators →
Define default_args →
Create DAG instance →
Define tasks with operators →
Set task dependencies
```

**Task Dependency Operators:**
- `>>` means "then" (A >> B: A before B)
- `[A, B] >> C`: Both A and B before C
- `A >> [B, C]`: A before both B and C

---

### Day 5: Airflow + Docker Compose

**Docker Compose File Structure:**
```
version →
services →
  service1:
    configuration
  service2:
    configuration
volumes →
networks →
```

**Service Configuration Elements:**
- `image` or `build`
- `container_name`
- `ports` as list
- `environment` as key-value
- `volumes` as list
- `networks` as list
- `depends_on` as list

**Service Communication Hint:**
- Use service name as hostname
- Example: `postgres:5432` not `localhost:5432`
- Only works on same network

**Volume Types:**
- Named volume: Just volume name
- Bind mount: `./local/path:/container/path`
- Named volumes persist, bind mounts sync

**Environment Variable Reference:**
- In compose file: `${VARIABLE_NAME}`
- Must be in .env file or shell environment
- No spaces around `=` in .env

**Docker Compose Commands Pattern:**
```
docker-compose [command] [options]
```
- `up -d`: Start in background
- `down`: Stop and remove
- `ps`: List containers
- `logs [service]`: View logs
- `restart [service]`: Restart one service

---

### Day 6: Complete Docker Compose Stack

**All Services Needed:**
1. api (FastAPI)
2. postgres
3. opensearch
4. airflow-webserver
5. airflow-scheduler
6. airflow-worker
7. redis

**Health Check Pattern:**
```
healthcheck:
  test: [command to test service]
  interval: [how often to check]
  timeout: [max time for check]
  retries: [failures before unhealthy]
  start_period: [grace period]
```

**PostgreSQL Health Check:**
- Command: Check if ready to accept connections
- Tool: `pg_isready`

**HTTP Service Health Check:**
- Command: curl to health endpoint
- Check status code 200

**Network Setup:**
- Create one bridge network
- All services join same network
- Services discover by name

**Volume Naming:**
- Descriptive names
- Separate volume per data type
- Declare at top level
- Reference in services

---

### Day 7: Testing & Documentation

**README Sections to Include:**
1. Architecture overview
2. Prerequisites
3. Installation steps
4. Configuration explanation
5. Usage instructions
6. Troubleshooting
7. Maintenance

**Testing Approach:**
- Test connectivity first
- Then test data flow
- Then test persistence
- Then test errors
- Document all results

**Common Docker Troubleshooting:**
- Port conflicts: Change host port
- Can't connect: Check service names
- Not starting: Check logs
- No data persistence: Check volumes

---

## WEEK 4: DATA PIPELINE

### Day 8: arXiv API Integration

**arXiv API URL Pattern:**
```
http://export.arxiv.org/api/query?search_query=[query]&max_results=[N]
```

**Query Field Codes:**
- `cat:` Category
- `ti:` Title
- `au:` Author
- `abs:` Abstract
- `all:` All fields

**Query Operators:**
- `AND` - Both conditions
- `OR` - Either condition
- `ANDNOT` - Exclude

**Rate Limiting Pattern:**
```
Before request:
  Check time since last request
  If less than minimum, sleep
  Record current time
  Make request
```

**XML Parsing with ElementTree:**
- Parse string: `ET.fromstring(xml_string)`
- Define namespace: `{'atom': 'http://www.w3.org/2005/Atom'}`
- Find element: `root.find('atom:entry', namespaces)`
- Get text: `.text` attribute
- Handle None: Check if element exists first

**Extracting arXiv ID:**
- Full URL format: `http://arxiv.org/abs/[ID]v[version]`
- Need to extract just the ID part
- Remove version suffix
- Handle both old and new format

---

### Day 9: PDF Download

**Streaming Download Pattern:**
```
Make request with stream=True
Open file in write-binary mode
Loop through response chunks
Write each chunk to file
```

**File Path Organization:**
- Extract year and month from arXiv ID
- Format: YYMM.NNNNN (first 4 digits)
- Create directories if needed
- Use Path for platform independence

**arXiv ID Date Extraction:**
- New format: First 2 digits = year, next 2 = month
- Example: 2401.12345 = January 2024
- Handle 20XX and 19XX papers

**Checking File Exists:**
- Use Path.exists() method
- Skip download if already present
- Verify size > 0 bytes
- Can add PDF validation check

**PDF Validation Hint:**
- Try opening with PyPDF2 or pypdf
- Check number of pages > 0
- Catch exceptions for invalid PDFs

**Database Update After Download:**
- UPDATE statement with WHERE arxiv_id
- Set pdf_path, pdf_size_bytes, downloaded_at
- Set parsing_status to next stage
- Use parameterized query

**Retry Logic Pattern:**
```
For attempt 1 to max_attempts:
  Try operation
  If success: return result
  If fail and not last attempt:
    Wait (exponential: 2^attempt seconds)
  If fail and last attempt:
    Log failure and return None
```

---

### Day 10: GROBID Setup (Preview)

**GROBID Docker Command:**
- Pull from Docker Hub
- Run with port mapping
- Default port: 8070
- Keep running in background

**GROBID API Endpoint:**
- POST to `/api/processFulltextDocument`
- Send PDF file in request body
- Receive TEI XML response

**TEI XML Structure:**
- Header: Metadata (title, authors, abstract)
- Body: Sections with paragraphs
- Back: References, citations

**Parsing TEI XML:**
- Different namespace than Atom
- Use same ElementTree approach
- Navigate by section structure

---

### Day 11: Docling Fallback (Preview)

**Fallback Logic Pattern:**
```
Try GROBID first:
  If success: return GROBID result
  If fail: log error
  
Try Docling:
  If success: return Docling result
  If fail: log error
  
Mark as failed in database
```

**Storing Parsed Content:**
- New table or JSON column
- Store sections separately
- Link to paper via foreign key
- Update parsing_status

---

### Day 12: Airflow DAG (Preview)

**DAG Definition Pattern:**
```
Define default_args with retries
Create DAG with schedule
Define tasks with operators
Set dependencies
```

**PythonOperator Hint:**
- python_callable: Function name (no parentheses)
- op_args: Tuple of arguments
- op_kwargs: Dictionary of keyword arguments

**Task Dependencies for Pipeline:**
```
fetch → download → parse → index
```

**Parallel Downloads Pattern:**
```
fetch → [download1, download2, download3] → combine → parse
```

---

### Day 13: Automated Pipeline (Preview)

**Cron Schedule Format:**
```
minute hour day month day_of_week
```
- Daily at 2 AM: `0 2 * * *`
- Every 6 hours: `0 */6 * * *`
- Weekdays at 3 AM: `0 3 * * 1-5`

**Monitoring Approach:**
- Check DAG run status in UI
- Set up failure callbacks
- Log important metrics
- Alert on failures

---

## GENERAL DEBUGGING HINTS

### Docker Issues

**Container Won't Start:**
1. Check logs: `docker logs [container]`
2. Check Dockerfile syntax
3. Check image exists
4. Check port conflicts

**Can't Connect to Service:**
1. Is container running?
2. Using correct port mapping?
3. Using service name (not localhost)?
4. On same network?

**Data Not Persisting:**
1. Volume declared in compose?
2. Volume mounted in service?
3. Correct path in container?
4. Check `docker volume ls`

### Python Debugging

**Import Errors:**
1. Is package installed?
2. Correct package name?
3. Virtual environment activated?
4. Check requirements.txt

**Connection Errors:**
1. Is service running?
2. Correct host/port?
3. Firewall blocking?
4. Credentials correct?

**File Not Found:**
1. Check absolute vs relative path
2. Check working directory
3. Check file permissions
4. Print path to verify

### SQL Debugging

**Query Errors:**
1. Check syntax (semicolon at end?)
2. Table exists? (`\dt`)
3. Column names correct? (`\d table`)
4. Using parameterized queries?

**Connection Failed:**
1. PostgreSQL running?
2. Connection string correct?
3. User has permissions?
4. Database exists?

### API Debugging

**Request Fails:**
1. Check URL (typos?)
2. Check HTTP method
3. Check request body format
4. Check authentication
5. Print full error response

**Rate Limited:**
1. Respect rate limits
2. Add delays between requests
3. Check API documentation
4. Implement exponential backoff

---

## QUICK REFERENCE TABLES

### Docker Compose Commands

| Command | Purpose |
|---------|---------|
| `up -d` | Start services background |
| `down` | Stop and remove |
| `ps` | List containers status |
| `logs [service]` | View service logs |
| `logs -f [service]` | Follow logs live |
| `restart [service]` | Restart one service |
| `exec [service] [cmd]` | Run command in container |
| `build` | Rebuild images |

### Docker Commands

| Command | Purpose |
|---------|---------|
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker images` | List images |
| `docker logs [id]` | View container logs |
| `docker exec -it [id] bash` | Enter container |
| `docker stop [id]` | Stop container |
| `docker rm [id]` | Remove container |
| `docker volume ls` | List volumes |
| `docker network ls` | List networks |

### PostgreSQL psql Commands

| Command | Purpose |
|---------|---------|
| `\l` | List databases |
| `\c [db]` | Connect to database |
| `\dt` | List tables |
| `\d [table]` | Describe table |
| `\du` | List users |
| `\q` | Quit psql |

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 500 | Server Error |

---

## COMMON PATTERNS

### Error Handling Pattern

```
Try:
    Operation that might fail
Except SpecificError as e:
    Log error with details
    Handle gracefully (return None, retry, etc.)
    Don't crash the program
```

### Logging Pattern

```
At start of function: Log what you're doing
During operation: Log important steps
On success: Log success with details
On error: Log error with context
```

### Configuration Pattern

```
Load from environment variables
Provide sensible defaults
Validate configuration
Fail fast if required config missing
```

### Testing Pattern

```
1. Setup test data
2. Execute operation
3. Assert expected results
4. Cleanup test data
```

---

## WHEN TO USE WHAT

### PostgreSQL vs OpenSearch

**Use PostgreSQL when:**
- Need transactions
- Need relationships
- Need strong consistency
- Structured metadata

**Use OpenSearch when:**
- Full-text search
- Relevance ranking
- Complex filters
- Aggregations

### Operators in Airflow

**PythonOperator:**
- Custom Python logic
- API calls
- Data processing

**BashOperator:**
- System commands
- Shell scripts
- CLI tools

**PostgresOperator:**
- SQL queries
- Database operations

### Docker vs Docker Compose

**Docker (single container):**
- Development
- Testing one service
- Simple applications

**Docker Compose (multi-container):**
- Full stack applications
- Service dependencies
- Production-like environment

---

## TROUBLESHOOTING CHECKLIST

### Service Won't Start
- [ ] Check logs for errors
- [ ] Verify port not in use
- [ ] Check dependencies started
- [ ] Verify configuration correct
- [ ] Check disk space
- [ ] Check memory available

### Can't Connect to Database
- [ ] Database container running
- [ ] Using correct credentials
- [ ] Using correct host (service name)
- [ ] Using correct port
- [ ] Database exists
- [ ] User has permissions

### Can't Access API
- [ ] API container running
- [ ] Port mapped correctly
- [ ] Using correct URL
- [ ] Firewall not blocking
- [ ] API started successfully

### Data Not Saved
- [ ] Volume configured
- [ ] Volume mounted correctly
- [ ] Write permissions ok
- [ ] Disk space available
- [ ] Transaction committed

---

## REMINDER: BEST PRACTICES

### Docker
- One process per container
- Use official images
- Don't run as root
- Use .dockerignore
- Small base images
- Multi-stage builds for production

### PostgreSQL
- Use indexes on filtered columns
- Use parameterized queries
- Close connections
- Use connection pooling
- Back up data regularly

### OpenSearch
- Appropriate shard count
- Proper mapping types
- Efficient queries
- Monitor cluster health
- Regular index cleanup

### Airflow
- Idempotent tasks
- Don't process in DAG file
- Use XCom sparingly
- Set appropriate retries
- Monitor task duration

### Python
- Use virtual environments
- Handle exceptions
- Log appropriately
- Write tests
- Use type hints

---

## GETTING UNSTUCK

### When Stuck > 15 Minutes

1. **Read error message carefully**
   - What's the actual error?
   - What line/file?
   - What was it trying to do?

2. **Check basics**
   - Is service running?
   - Are credentials correct?
   - Is syntax correct?
   - Are imports available?

3. **Isolate the problem**
   - Does simpler version work?
   - Which part specifically fails?
   - Can you reproduce consistently?

4. **Search strategically**
   - Copy exact error message
   - Include technology name
   - Check official docs first
   - Look for recent solutions

5. **Ask for help**
   - Describe what you're trying
   - Show what you tried
   - Include error messages
   - Share relevant config

### Before Asking for Help

- [ ] I read the error message
- [ ] I checked the logs
- [ ] I verified basic configuration
- [ ] I tried simplest possible case
- [ ] I searched for the error
- [ ] I can explain what I'm trying to do
- [ ] I can show what I've tried

---

## REMEMBER

- **Start simple** - Get basic version working first
- **Test frequently** - Don't build everything then test
- **Read errors** - They usually tell you what's wrong
- **Check logs** - First place to look for problems
- **Use print/log statements** - See what's actually happening
- **Google exact errors** - Someone likely had same issue
- **Take breaks** - Fresh eyes find solutions faster

---

## KEYBOARD SHORTCUTS

### Terminal
- `Ctrl + C` - Stop running process
- `Ctrl + D` - Exit shell/psql
- `Ctrl + L` - Clear screen
- `Ctrl + R` - Search command history

### VS Code
- `Ctrl + ~` - Toggle terminal
- `Ctrl + B` - Toggle sidebar
- `Ctrl + P` - Quick file open
- `Ctrl + Shift + P` - Command palette

---

## USEFUL COMMANDS

### Check What's Using a Port
```
lsof -i :[port]
netstat -an | grep [port]
```

### Check Docker Disk Usage
```
docker system df
```

### Clean Up Docker
```
docker system prune -a
docker volume prune
```

### View Environment Variables
```
printenv
echo $VARIABLE_NAME
```

### Find Files
```
find . -name "*.py"
find . -type f -size +10M
```

---

**Remember: These are HINTS, not solutions. Try to figure things out yourself first. That's where real learning happens!**

**Last Updated:** November 2025