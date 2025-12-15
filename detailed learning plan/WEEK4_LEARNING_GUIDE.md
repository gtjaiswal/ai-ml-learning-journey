# 📚 WEEK 4 LEARNING GUIDE (Transition Plan)

**Your Timeline:** December 09-22, 2025  
**Corresponds to:** Steps 5-8 + Addendums, MOAI Week 2  
**Focus:** Automated Data Ingestion Pipeline

---

## 🎯 WEEK 4 OVERVIEW

**What You'll Build:**
- Step 5: arXiv API client (fetch papers, rate limiting)
- Step 6: SKIP (PDF download in ArxivClient)
- Step 7: PDF parser with Docling (extract text/sections)
- Step 7 Addendum: Add 7 PDF fields to database
- Step 8: Airflow DAG (automated daily pipeline)
- Step 8 Addendum: Add GET /papers/ list endpoint

**What You'll Learn:**
- Async HTTP clients (httpx)
- XML parsing
- Rate limiting strategies
- PDF processing with Docling
- Apache Airflow orchestration
- DAG development
- XCom data passing

**Time Investment:** ~13-14 hours total
- Learning: 3-4 hours
- Implementation: 10-11 hours

---

## 📖 WHAT YOU ALREADY KNOW (from Week 3)

✅ **Week 3 (Steps 1-4):**
- Docker and PostgreSQL
- SQLAlchemy ORM
- FastAPI basics
- Async Python fundamentals
- Pydantic schemas
- Repository pattern

**You now have:**
- Working database
- Basic API with 3 endpoints
- Foundation for automation

---

## 📚 CORE LEARNING MODULES

### **MODULE 1: Async HTTP with httpx** ⏱️ 30 minutes

#### **1.1 Why httpx?** (10 min)

**Reading:**
📖 **httpx Documentation - Overview**  
URL: https://www.python-httpx.org/  
Read: Home page

**Key Points:**

**requests vs httpx:**
```python
# requests (sync, no async support)
import requests
response = requests.get("https://api.example.com")

# httpx (async + sync)
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com")
```

**Why httpx for your project:**
- ✅ Async support (non-blocking)
- ✅ HTTP/2 support
- ✅ Connection pooling
- ✅ Timeout handling
- ✅ Better error handling

#### **1.2 httpx Async Patterns** (20 min)

**Video:**
📺 **"Async HTTP Requests in Python"**  
URL: https://www.youtube.com/watch?v=qAh5dDODJ5k  
Watch: First 15 minutes

**Key Patterns:**

**Basic GET:**
```python
async with httpx.AsyncClient() as client:
    response = await client.get(url)
    data = response.text
```

**With Parameters:**
```python
params = {"search_query": "cat:cs.AI", "max_results": 10}
response = await client.get(url, params=params)
```

**With Timeout:**
```python
async with httpx.AsyncClient(timeout=30.0) as client:
    response = await client.get(url)
```

**Error Handling:**
```python
try:
    response = await client.get(url)
    response.raise_for_status()  # Raises for 4xx/5xx
except httpx.TimeoutException:
    print("Request timed out")
except httpx.HTTPStatusError as e:
    print(f"HTTP error: {e.response.status_code}")
```

---

### **MODULE 2: XML Parsing** ⏱️ 30 minutes

#### **2.1 XML Basics** (15 min)

**Video:**
📺 **"XML in 100 Seconds"** - Fireship  
URL: https://www.youtube.com/watch?v=1JblVElt5K0  
Watch: Full video (2 min)

**Reading:**
📖 **XML Tutorial**  
URL: https://www.w3schools.com/xml/  
Read: "XML Introduction" and "XML Syntax"

**Key Concepts:**

**XML Structure:**
```xml
<feed>
  <entry>
    <id>http://arxiv.org/abs/2401.12345</id>
    <title>Sample Paper</title>
    <author>
      <name>John Doe</name>
    </author>
    <summary>Abstract text...</summary>
  </entry>
</feed>
```

**Elements:** `<entry>`, `<title>`, etc.  
**Attributes:** `<link type="pdf">`  
**Namespaces:** `xmlns:atom="http://..."`

#### **2.2 Python XML Parsing** (15 min)

**Reading:**
📖 **ElementTree Documentation**  
URL: https://docs.python.org/3/library/xml.etree.elementtree.html  
Read: "Tutorial" section

**Basic Parsing:**
```python
import xml.etree.ElementTree as ET

# Parse XML string
root = ET.fromstring(xml_data)

# Find elements
entries = root.findall("entry")

# Get text
title = entry.find("title").text

# Get attribute
pdf_url = link.get("href")
```

**With Namespaces:**
```python
namespaces = {"atom": "http://www.w3.org/2005/Atom"}
entries = root.findall("atom:entry", namespaces)
title = entry.find("atom:title", namespaces).text
```

---

### **MODULE 3: Rate Limiting** ⏱️ 20 minutes

#### **3.1 Why Rate Limiting?** (10 min)

**Reading:**
📖 **"Rate Limiting Explained"**  
URL: https://www.cloudflare.com/learning/bots/what-is-rate-limiting/  
Read: Full article

**Key Concepts:**

**The Problem:**
```python
# Without rate limiting
for i in range(1000):
    fetch_paper()  # Too fast! API blocks you
```

**With Rate Limiting:**
```python
# Wait between requests
for i in range(1000):
    fetch_paper()
    await asyncio.sleep(3)  # 3 seconds between requests
```

**Why APIs require it:**
- Prevent abuse
- Ensure fair usage
- Protect server resources

**arXiv API:**
- Recommends 3 seconds between requests
- Max 2000 results per query

#### **3.2 Implementation Patterns** (10 min)

**Example:**
```python
class RateLimiter:
    def __init__(self, delay: float = 3.0):
        self.delay = delay
        self.last_request_time = None
    
    async def wait_if_needed(self):
        if self.last_request_time:
            elapsed = time.time() - self.last_request_time
            if elapsed < self.delay:
                await asyncio.sleep(self.delay - elapsed)
        
        self.last_request_time = time.time()
```

**Retry with Exponential Backoff:**
```python
for attempt in range(max_retries):
    try:
        response = await client.get(url)
        return response
    except httpx.TimeoutException:
        if attempt < max_retries - 1:
            wait_time = 5 * (2 ** attempt)  # 5s, 10s, 20s...
            await asyncio.sleep(wait_time)
        else:
            raise
```

---

### **MODULE 4: PDF Processing** ⏱️ 45 minutes

#### **4.1 PDF Structure Basics** (15 min)

**Video:**
📺 **"How PDFs Work"**  
URL: https://www.youtube.com/watch?v=Qvh0gN5A8V4  
Watch: First 10 minutes

**Key Concepts:**

**PDF Contains:**
- Text (sometimes!)
- Images
- Fonts
- Layout information
- Metadata

**Challenges:**
- Text might be images (scanned PDFs)
- Complex layouts
- Tables and figures
- Multi-column text
- Mathematical symbols

#### **4.2 Docling Overview** (20 min)

**Reading:**
📖 **Docling Documentation**  
URL: https://github.com/DS4SD/docling  
Read: README and "Getting Started"

**What is Docling?**
- Modern PDF parsing library
- Extracts text, sections, tables
- Better than pypdf2/pdfplumber
- Uses ML models for layout

**Basic Usage:**
```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("paper.pdf")
text = result.document.export_to_text()
```

**Key Features:**
- Automatic section detection
- Table extraction
- Figure detection
- Preserves document structure

**Limitations:**
- Slower than simple parsers
- Requires model loading
- Memory intensive for large PDFs

#### **4.3 Chunking Strategy** (10 min)

**Reading:**
📖 **"Document Chunking for RAG"**  
URL: https://www.pinecone.io/learn/chunking-strategies/  
Read: "Why chunk?" section

**Why chunk documents:**
- PDF is 12,000 words
- LLM context limit: ~8,000 words
- Solution: Split into chunks

**Your Strategy:**
- Use natural sections (Introduction, Methods, etc.)
- Limit chunk size: ~600 words
- Preserve document structure

---

### **MODULE 5: Apache Airflow** ⏱️ 90 minutes

#### **5.1 What is Airflow?** (20 min)

**Video:**
📺 **"Apache Airflow in 5 Minutes"** - Astronomer  
URL: https://www.youtube.com/watch?v=-tRZasCSuS0
Watch: Full video

📺 **"What is Airflow?"** - Marc Lamberti  
URL: https://www.youtube.com/watch?v=K9AnJ9_ZAXE  
Watch: First 10 minutes

**Key Concepts:**

**What Airflow Does:**
- Orchestrates tasks
- Schedules workflows
- Monitors execution
- Handles failures

**Without Airflow:**
```bash
# Cron jobs
0 2 * * * python fetch_papers.py
0 3 * * * python parse_pdfs.py
0 4 * * * python store_data.py

# Problems:
# - No dependencies (what if fetch fails?)
# - No retries
# - No monitoring
# - Hard to debug
```

**With Airflow:**
```python
# DAG: One workflow
fetch → parse → store
  ↓       ↓       ↓
 retry   retry   retry
```

#### **5.2 Core Concepts** (30 min)

**Video:**
📺 **"Airflow Tutorial for Beginners"** - Marc Lamberti  
URL: https://www.youtube.com/watch?v=K9AnJ9_ZAXE  
Watch: Minutes 10-40 (DAGs, Tasks, Operators)

**Key Concepts:**

**DAG (Directed Acyclic Graph):**
- Workflow definition
- Collection of tasks
- No cycles (can't loop back)

**Task:**
- Single unit of work
- Python function or command
- Can succeed or fail

**Operator:**
- Template for tasks
- PythonOperator (run Python function)
- BashOperator (run shell command)

**Dependencies:**
```python
task1 >> task2 >> task3  # Sequential
task1 >> [task2, task3] >> task4  # Parallel then join
```

**Scheduling:**
```python
# Every day at 6 AM
schedule="0 6 * * *"

# Weekdays only at 6 AM
schedule="0 6 * * 1-5"
```

#### **5.3 XCom (Cross-Communication)** (20 min)

**Reading:**
📖 **Airflow XCom Documentation**  
URL: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html  
Read: "Concepts" section

**What is XCom?**
- Pass data between tasks
- Small messages only
- Stored in Airflow database

**Example:**
```python
# Task 1: Push data
def fetch_papers(**context):
    papers = fetch_from_arxiv()
    context['ti'].xcom_push(key='paper_count', value=len(papers))

# Task 2: Pull data
def process_papers(**context):
    count = context['ti'].xcom_pull(
        task_ids='fetch_papers',
        key='paper_count'
    )
    print(f"Processing {count} papers")
```

**Use Cases:**
- Pass counts between tasks
- Share IDs or references
- Coordinate task behavior

**Limitations:**
- Small data only (<1 MB)
- Don't pass large datasets

#### **5.4 Practical Patterns** (20 min)

**Video:**
📺 **"Airflow Best Practices"** - Marc Lamberti  
URL: https://www.youtube.com/watch?v=XXy6lHvqG8g  
Watch: First 20 minutes

**Key Patterns:**

**Idempotent Tasks:**
```python
# BAD (not idempotent)
def append_data():
    file.write(data)  # Duplicates on retry!

# GOOD (idempotent)
def store_data():
    if not exists(data):
        file.write(data)  # Safe to retry
```

**Error Handling:**
```python
dag = DAG(
    'my_dag',
    default_args={
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    }
)
```

**Task Context:**
```python
def my_task(**context):
    # Access execution date
    ds = context['ds']  # Date string
    
    # Access task instance
    ti = context['ti']
    
    # Push/pull XCom
    ti.xcom_push(key='result', value=123)
```

---

## 🎯 WHAT TO FOCUS ON

### **CRITICAL (Must understand):**
- ✅ httpx async client usage
- ✅ XML parsing with ElementTree
- ✅ Rate limiting concept and implementation
- ✅ Docling basic usage
- ✅ Airflow DAG structure
- ✅ Task dependencies
- ✅ XCom data passing

### **IMPORTANT (Very helpful):**
- ✅ Retry strategies (exponential backoff)
- ✅ PDF structure challenges
- ✅ Airflow scheduling syntax
- ✅ Error handling patterns

### **NICE TO HAVE (Can learn while building):**
- Advanced XML namespaces
- Docling advanced features
- Airflow advanced patterns
- Performance optimization

---

## ✅ READINESS CHECKLIST

Before starting Steps 5-8 implementation, you should be able to answer:

**Conceptual:**
- [ ] Why use httpx instead of requests?
- [ ] What is rate limiting and why is it needed?
- [ ] What challenges exist in PDF parsing?
- [ ] What is a DAG?
- [ ] What is XCom used for?
- [ ] When should tasks retry?

**Practical:**
- [ ] How to make async HTTP request with httpx?
- [ ] How to parse XML with ElementTree?
- [ ] How to implement rate limiting?
- [ ] How to use Docling to parse PDF?
- [ ] How to define a DAG?
- [ ] How to pass data between Airflow tasks?

---

## 📚 ADDITIONAL RESOURCES (Optional)

**httpx:**
- Documentation: https://www.python-httpx.org/
- Async Guide: https://www.python-httpx.org/async/

**XML:**
- ElementTree: https://docs.python.org/3/library/xml.etree.elementtree.html
- XML Tutorial: https://www.w3schools.com/xml/

**Docling:**
- GitHub: https://github.com/DS4SD/docling
- Examples: Check repository examples/

**Airflow:**
- Official Docs: https://airflow.apache.org/docs/
- Tutorials: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/
- Best Practices: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html

---

## 🚀 AFTER LEARNING

**You're ready to build Steps 5-8 when you can:**
1. Make async HTTP requests with httpx
2. Parse XML responses
3. Implement rate limiting
4. Use Docling to extract PDF text
5. Define an Airflow DAG
6. Create task dependencies
7. Pass data between tasks with XCom

**Then proceed to:**
- [STEP5_COMPLETE.md](computer:///mnt/user-data/outputs/STEP5_COMPLETE.md) - arXiv API Client
- [STEP7_COMPLETE.md](computer:///mnt/user-data/outputs/STEP7_COMPLETE.md) - PDF Parser
- [STEP8_COMPLETE.md](computer:///mnt/user-data/outputs/STEP8_COMPLETE.md) - Airflow DAG
- [STEP7_ADDENDUM_DATABASE.md](computer:///mnt/user-data/outputs/STEP7_ADDENDUM_DATABASE.md) - Add PDF fields
- [STEP8_ADDENDUM_ENDPOINT.md](computer:///mnt/user-data/outputs/STEP8_ADDENDUM_ENDPOINT.md) - Add list endpoint

---

## 🎯 WEEK 4 GOALS

**By end of week, you'll have:**
- ✅ arXiv API client working
- ✅ PDFs downloaded and cached
- ✅ PDFs parsed with Docling
- ✅ Full text stored in database
- ✅ Airflow DAG running daily
- ✅ Automated paper ingestion
- ✅ List endpoint to view papers

**This sets you up for:**
- Week 7 (Transition): Add OpenSearch + BM25 search
- Search your automatically collected papers!

---

**Time estimate:** 3-4 hours of focused learning  
**Best approach:** Learn over weekend, implement Mon-Fri  
**Note:** Week 4 is denser (13-14h) - plan accordingly!

---

**Document Generated:** December 8, 2025  
**For:** Transition Week 4 (Steps 5-8, MOAI Week 2)