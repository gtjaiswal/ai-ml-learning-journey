# 📚 WEEK 7 LEARNING GUIDE (Transition Plan)

**Your Timeline:** Weekend before Steps 9-12 implementation  
**Corresponds to:** Steps 9-12, MOAI Week 3  
**Focus:** OpenSearch + BM25 Full-Text Search

---

## 🎯 WEEK 7 OVERVIEW

**What You'll Learn:**
- OpenSearch fundamentals
- Inverted indexes
- BM25 ranking algorithm
- Index mapping (text vs keyword fields)
- Query DSL (match, multi_match, bool queries)
- Field boosting and highlighting
- opensearch-py Python client

**Why These Matter:**
- Full-text search across large text collections
- Relevance ranking (best matches first)
- Fast search at scale (millions of documents)
- Production search patterns

**Time Investment:** 4-5 hours (weekend)

---

## 📖 PREREQUISITE KNOWLEDGE

**You should know:**
✅ Python basics (dictionaries, JSON)
✅ HTTP requests and REST APIs
✅ Database basics (tables, indexes, queries)
✅ Docker fundamentals

**New concepts you'll learn:**
- Search engines vs databases
- Inverted index data structure
- TF-IDF and BM25 scoring
- Text analysis and tokenization
- Query DSL (JSON-based queries)

---

## 🗓️ LEARNING SCHEDULE

### **Saturday Morning (2.5-3 hours)**

**9:00-10:00 AM** - Module 1: OpenSearch Fundamentals  
**10:15-11:00 AM** - Module 2: Inverted Indexes  
**11:15-12:15 PM** - Module 3: BM25 Algorithm

**Break for lunch**

### **Sunday Morning (2 hours)**

**9:00-9:45 AM** - Module 4: Index Mapping  
**10:00-11:00 AM** - Module 5: Query DSL  
**11:15-12:00 PM** - Module 6: Python Client

**Afternoon (optional):** Hands-on exercises with OpenSearch Dashboards

---

## 📚 CORE LEARNING MODULES

### **MODULE 1: OpenSearch Fundamentals** ⏱️ 1 hour

#### **1.1 What is OpenSearch?** (20 min)

**Video:**
📺 **"What is Elasticsearch"** - Elastic  
URL: https://www.youtube.com/watch?v=C3tlMqaNSaI  
Watch: First 15 minutes  
Note: OpenSearch is an Elasticsearch fork, 95% of concepts are identical
https://www.youtube.com/watch?v=6k6-OeWZTYY
https://www.youtube.com/watch?v=LqXj1oC1FH0
**Key Points:**

**Search Engine vs Database:**

```
Traditional Database (e.g., PostgreSQL):
- Optimized for: Exact matches, transactions, JOINs
- Query language: SQL
- Use case: "Find user with email = 'john@example.com'"
- Consistency: ACID (immediate)

Search Engine (e.g., OpenSearch):
- Optimized for: Text search, relevance ranking
- Query language: Query DSL (JSON)
- Use case: "Find documents about 'climate change'"
- Consistency: Eventually consistent
```

**Example Use Cases:**

**E-commerce Product Search:**
- User searches: "wireless headphones"
- Finds products with "bluetooth headphones", "cordless earbuds"
- Ranks by relevance, popularity, price

**Documentation Search:**
- Developer searches: "authentication tutorial"
- Finds docs with "auth", "login", "security guide"
- Highlights matching sections

**Log Analysis:**
- Search logs: "ERROR database connection"
- Finds all error logs about DB connections
- Aggregates by timestamp, server

**Core Concepts:**

**Index** = Collection of documents (like a database table)
- Example: "products" index, "blog_posts" index

**Document** = Single entry (like a database row)
- JSON object
- Example: `{"title": "iPhone 15", "price": 999, "category": "phones"}`

**Field** = Property of document (like a column)
- Has a type: text, keyword, integer, date
- Example: title (text), price (integer)

**Mapping** = Schema definition
- Defines field types
- Defines how to analyze text
- Example: title is searchable text, SKU is exact-match keyword

**Analyzer** = Text processing pipeline
- Tokenizes: "Wireless Headphones" → ["wireless", "headphones"]
- Normalizes: ["Wireless", "Headphones"] → ["wireless", "headphones"]
- Stems: ["headphones"] → ["headphone"]

#### **1.2 Architecture Overview** (15 min)

**Reading:**
📖 **OpenSearch Documentation - Overview**  
URL: https://opensearch.org/docs/latest/  
Read: "What is OpenSearch?" section

**Key Architecture Components:**

**Cluster:**
- Collection of nodes working together
- Distributes data and queries
- Provides redundancy

**Node:**
- Single server in cluster
- Stores data and executes queries
- Can have different roles (data, master, etc.)

**Shard:**
- Subset of an index
- Allows horizontal scaling
- Example: 1 million documents split into 5 shards

**Replica:**
- Copy of a shard
- Provides fault tolerance
- Improves read throughput

#### **1.3 When to Use OpenSearch** (15 min)

**Reading:**
📖 **Search Engine vs Database**  
URL: https://www.elastic.co/blog/found-uses-of-elasticsearch  
Read: First 3 sections

**✅ Use OpenSearch for:**

- **Full-text search:** Find documents containing "neural network" (matches "neural networks", "NN", related terms)
- **Fuzzy matching:** User types "machne learing" → finds "machine learning"
- **Faceted search:** E-commerce filters (category, price range, brand) + search
- **Log aggregation:** Analyze logs, create dashboards
- **Autocomplete:** Type "pyth" → suggest "python", "python tutorial"

**❌ Don't use OpenSearch for:**

- **Source of truth:** Use relational database (PostgreSQL, MySQL)
- **Transactions:** Banking, orders (need ACID guarantees)
- **Complex JOINs:** Multi-table relationships
- **Frequently updated data:** Real-time inventory, stock prices

**Best Practice Pattern:**

```
Application Data Flow:
  
1. Write to PostgreSQL (source of truth)
   ├─ User creates blog post
   └─ Stored in "posts" table
  
2. Index to OpenSearch (search layer)
   ├─ Copy post to OpenSearch
   └─ Now searchable
  
3. Search via OpenSearch
   ├─ User searches "docker tutorial"
   └─ Returns ranked results
  
4. Display results (from database)
   ├─ Get post IDs from search
   └─ Fetch full data from PostgreSQL
```

#### **1.4 Simple Example** (10 min)

**Scenario:** Blog search

**PostgreSQL stores:**
```sql
posts
- id
- title
- content
- author_id
- created_at
```

**OpenSearch indexes:**
```json
{
  "post_id": 123,
  "title": "Getting Started with Docker",
  "content": "Docker is a containerization platform...",
  "author": "John Doe",
  "tags": ["docker", "devops", "containers"],
  "published_date": "2024-01-15"
}
```

**User searches:** "container tutorial"

**OpenSearch returns:**
- Post 123 (score: 8.5) - mentions "container" in title and content
- Post 456 (score: 6.2) - mentions "container" in content
- Post 789 (score: 4.1) - mentions "tutorial" only

**Application fetches:** Posts 123, 456, 789 from PostgreSQL for display

---

### **MODULE 2: Inverted Indexes** ⏱️ 45 minutes

#### **2.1 The Problem with Traditional Search** (15 min)

**Database Table Scan:**

```
blog_posts table:
ID | Title                        | Content
1  | Introduction to Python       | Python is a programming language...
2  | Python Web Development       | Building web apps with Python...
3  | JavaScript Tutorial          | Learn JavaScript fundamentals...
```

**Query:** Find posts containing "Python"

**SQL approach:**
```sql
SELECT * FROM blog_posts 
WHERE title LIKE '%Python%' 
   OR content LIKE '%Python%';
```

**Process:**
1. Scan row 1: Check title and content for "Python" → MATCH
2. Scan row 2: Check title and content for "Python" → MATCH
3. Scan row 3: Check title and content for "Python" → NO MATCH

**Problem:** O(n) complexity - must scan every row

With 1 million posts = 1 million scans = SLOW!

#### **2.2 The Inverted Index Solution** (20 min)

**Video:**
📺 **"How do search engines work?"** - Fireship  
URL: https://www.youtube.com/watch?v=0LTXCcVRQi0  
Watch: Full video (12 min)

**Concept: Reverse the relationship**

**Traditional:** Document → Words it contains  
**Inverted:** Word → Documents containing it

**Building an Inverted Index:**

**Documents:**
```
Doc 1: "Introduction to Python"
Doc 2: "Python Web Development"
Doc 3: "JavaScript Tutorial"
```

**Inverted Index:**
```
Term            → Document IDs
"introduction"  → [1]
"python"        → [1, 2]
"web"           → [2]
"development"   → [2]
"javascript"    → [3]
"tutorial"      → [3]
```

**Search for "Python":**
```
Traditional approach: Scan 3 documents → O(n)
Inverted index:      Lookup "python" → [1, 2] → O(1)
```

**Result:** Instant lookup regardless of dataset size!

#### **2.3 Building the Index** (10 min)

**Reading:**
📖 **Inverted Index Explained**  
URL: https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html  
Read: Sections 1.1 and 1.2

**Processing Pipeline:**

**Step 1: Tokenization**
```
"Introduction to Python"
→ ["Introduction", "to", "Python"]
```

**Step 2: Normalization**
```
["Introduction", "to", "Python"]
→ lowercase → ["introduction", "to", "python"]
```

**Step 3: Filtering** (optional)
```
["introduction", "to", "python"]
→ remove stopwords ("to") → ["introduction", "python"]
```

**Step 4: Stemming** (optional)
```
["programming", "programs", "programmer"]
→ stem → ["program", "program", "program"]
```

**Step 5: Index**
```
"introduction" → {doc1: [position 0]}
"python"       → {doc1: [position 2], doc2: [position 0]}
```

**Why store positions?**
- Enable phrase search: "to Python" (must be adjacent)
- Enable highlighting: Show WHERE the term appears
- Enable proximity queries: Terms within N words

**Trade-offs:**

**Advantages:**
✅ O(1) lookup time
✅ Scales to billions of documents
✅ Supports fuzzy matching
✅ Enables relevance scoring

**Disadvantages:**
❌ Extra storage (10-30% of original data)
❌ Slower writes (must update index)
❌ Eventually consistent (not immediate)

---

### **MODULE 3: BM25 Algorithm** ⏱️ 1 hour

#### **3.1 The Relevance Problem** (15 min)

**Scenario:** Search for "Python tutorial"

**Results without ranking:**
```
Doc A: "Python" appears 1 time
Doc B: "Python" appears 1 time  
Doc C: "Python" appears 1 time
```

**Problem:** All 3 have same score! Which to show first?

**Better ranking considers:**
1. **Term frequency:** How often does "Python" appear?
2. **Document rarity:** Is "Python" common or rare across all docs?
3. **Document length:** Long doc might have more words naturally

**BM25 = Best Match 25**
- Ranking function that solves this
- Used by Google, Bing, OpenSearch, Elasticsearch
- Standard for text search

#### **3.2 BM25 Components** (25 min)

**Video:**
📺 **"BM25 Explained"** - Elastic  
URL: https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables  
Watch: Read article (15 min)

**Component 1: Term Frequency (TF)**

**Question:** How many times does the search term appear in this document?

**Example: Search for "docker"**

```
Blog Post A: "Docker basics. Docker is great. Docker tutorial."
- "docker" appears 3 times
- High TF

Blog Post B: "Docker is a containerization tool."
- "docker" appears 1 time
- Low TF
```

**Intuition:** More mentions = more relevant

**But with diminishing returns:**
```
1 → 2 mentions: Big increase in relevance
2 → 3 mentions: Medium increase
10 → 11 mentions: Tiny increase (saturation)
```

**Why?** Prevents keyword stuffing from dominating results.

**Component 2: Inverse Document Frequency (IDF)**

**Question:** How rare is this term across ALL documents?

**Example:**

```
Term "the"
- Appears in 95% of documents
- Very common
- IDF = 0.1 (low)
- Low impact on score

Term "kubernetes"
- Appears in 2% of documents
- Rare, specific
- IDF = 4.5 (high)
- High impact on score
```

**Intuition:** Rare terms are more meaningful for relevance.

**Why?** "the" tells you nothing about what doc is about, but "kubernetes" is very specific.

**Component 3: Document Length Normalization**

**Question:** Should doc length affect the score?

**Example:**

```
Short doc (100 words) with "docker" once
- 1/100 = 1% of document is about docker
- High density

Long doc (10,000 words) with "docker" once  
- 1/10000 = 0.01% of document about docker
- Low density
```

**Intuition:** Shorter docs with term are more focused on that topic.

**Normalization:** Adjusts score based on doc length vs average doc length.

#### **3.3 The Formula** (10 min)

**Reading:**
📖 **BM25 on Wikipedia**  
URL: https://en.wikipedia.org/wiki/Okapi_BM25  
Read: "The ranking function" section

**BM25 Formula:**
```
score(D, Q) = Σ IDF(qi) × (TF(qi,D) × (k1 + 1)) / (TF(qi,D) + k1 × (1 - b + b × |D| / avgdl))

Where:
- D = document being scored
- Q = query
- qi = individual query term
- TF(qi, D) = frequency of term qi in document D
- IDF(qi) = inverse document frequency of term qi
- |D| = length of document D (word count)
- avgdl = average document length in collection
- k1 = TF saturation parameter (typically 1.2)
- b = length normalization parameter (typically 0.75)
```

**Don't memorize the formula!**

**Understand the intuition:**
- More term occurrences → higher score (but saturates)
- Rarer terms → higher score
- Shorter docs → slightly higher score

#### **3.4 BM25 Example** (10 min)

**Search query:** "docker container"

**Document A:**
```
Title: "Docker Tutorial"
Content: "Docker is a container platform. Docker containers are lightweight. 
          Use Docker for development."
- "docker" appears 3 times
- "container" appears 2 times
- Length: 50 words
```

**Document B:**
```
Title: "Kubernetes Guide"  
Content: "Kubernetes orchestrates containers. It manages Docker and other 
          container runtimes across clusters."
- "docker" appears 1 time
- "container" appears 2 times
- Length: 48 words
```

**Document C:**
```
Title: "Cloud Computing Overview"
Content: "Cloud computing includes many technologies. Virtual machines, 
          serverless, and container platforms like Docker exist."
- "docker" appears 1 time
- "container" appears 1 time
- Length: 200 words
```

**BM25 Scoring:**

```
Document A:
- High TF for "docker" (3 times)
- Medium TF for "container" (2 times)
- Short doc (50 words)
→ BM25 Score: 12.5

Document B:
- Low TF for "docker" (1 time)
- Medium TF for "container" (2 times)  
- Short doc (48 words)
→ BM25 Score: 8.3

Document C:
- Low TF for "docker" (1 time)
- Low TF for "container" (1 time)
- Long doc (200 words) - penalty
→ BM25 Score: 3.2
```

**Results (sorted):**
1. Document A (12.5)
2. Document B (8.3)
3. Document C (3.2)

**Good news:** OpenSearch calculates BM25 automatically - you just write simple queries!

---

### **MODULE 4: Index Mapping** ⏱️ 45 minutes

#### **4.1 What is Mapping?** (10 min)

**Mapping = Schema for your index**

Like CREATE TABLE in SQL, but for search.

**It defines:**
- What fields exist in documents
- Type of each field
- How to analyze text fields
- Whether field is searchable, sortable, aggregatable

**Reading:**
📖 **OpenSearch Mapping**  
URL: https://opensearch.org/docs/latest/field-types/  
Read: "Supported field types" section

#### **4.2 Field Types** (25 min)

**1. text - For full-text search**

**Use for:** Product descriptions, blog content, reviews

**Characteristics:**
- Analyzed (tokenized, lowercased, stemmed)
- Searchable but not sortable
- Not for exact matches

**Example:**
```json
{
  "description": {
    "type": "text",
    "analyzer": "english"
  }
}
```

**Input:** "Running Shoes for Marathon Runners"  
**Stored as tokens:** ["run", "shoe", "marathon", "runner"]  
**Search "running"** → MATCHES (stemmed to "run")

**2. keyword - For exact matching**

**Use for:** SKUs, emails, tags, categories, IDs, URLs

**Characteristics:**
- NOT analyzed (stored exactly as-is)
- Sortable and aggregatable
- Exact match only

**Example:**
```json
{
  "product_sku": {
    "type": "keyword"
  }
}
```

**Input:** "SKU-12345-A"  
**Stored as:** "SKU-12345-A" (exact)  
**Search "SKU-12345"** → NO MATCH (not exact)  
**Search "SKU-12345-A"** → MATCH

**3. date - For timestamps**

**Use for:** created_at, published_date, updated_at

**Example:**
```json
{
  "published": {
    "type": "date",
    "format": "strict_date_optional_time||epoch_millis"
  }
}
```

**Input:** "2024-01-15T10:30:00Z"  
**Supports:** Range queries, date math

**4. integer, float - For numbers**

**Use for:** Prices, quantities, ratings, scores

**Example:**
```json
{
  "price": {
    "type": "float"
  },
  "stock_quantity": {
    "type": "integer"
  }
}
```

**Supports:** Range queries, sorting, aggregations

**5. boolean - For true/false**

**Use for:** Flags (is_active, in_stock, featured)

**Example:**
```json
{
  "in_stock": {
    "type": "boolean"
  }
}
```

#### **4.3 Analyzers** (10 min)

**Video:**
📺 **"Text Analysis in Elasticsearch"**  
URL: https://www.youtube.com/watch?v=F08cqvhVbHI  
Watch: First 10 minutes

**Analyzer = Text processing pipeline**

**Standard Analyzer** (default):
```
Input: "The Quick Brown Fox!"

1. Character filter: (none by default)
2. Tokenize: ["The", "Quick", "Brown", "Fox", "!"]
3. Token filter - lowercase: ["the", "quick", "brown", "fox", "!"]
4. Token filter - remove punctuation: ["the", "quick", "brown", "fox"]

Output: ["the", "quick", "brown", "fox"]
```

**English Analyzer** (with stemming):
```
Input: "Running quickly through forests"

1. Tokenize: ["Running", "quickly", "through", "forests"]
2. Lowercase: ["running", "quickly", "through", "forests"]
3. Stop words: ["running", "quickly", "forests"] (removed "through")
4. Stem: ["run", "quick", "forest"]

Output: ["run", "quick", "forest"]

Now "run" matches "running", "runs", "ran"
```

**Keyword Analyzer** (no analysis):
```
Input: "SKU-12345-A"
Output: "SKU-12345-A" (unchanged)
```

**Choosing Analyzer:**
- English text → english analyzer
- Multi-language → standard analyzer
- Exact match → keyword (no analyzer)
- Code, URLs, IDs → keyword

---

### **MODULE 5: Query DSL** ⏱️ 1 hour

#### **5.1 What is Query DSL?** (10 min)

**DSL = Domain Specific Language**

**Query DSL = JSON-based language for searching**

**Reading:**
📖 **OpenSearch Query DSL**  
URL: https://opensearch.org/docs/latest/query-dsl/  
Read: "Query DSL" intro

**Think of it as:** SQL for search engines (but in JSON)

```
SQL:
SELECT * FROM products WHERE title LIKE '%laptop%';

Query DSL:
{
  "query": {
    "match": {
      "title": "laptop"
    }
  }
}
```

#### **5.2 Basic Query Types** (30 min)

**Video:**
📺 **"Elasticsearch Queries Tutorial"**  
URL: https://www.youtube.com/watch?v=oPObRc8tHgQ  
Watch: First 20 minutes

**1. match - Full-text search**

**Use for:** Searching text fields

```json
{
  "query": {
    "match": {
      "description": "wireless headphones"
    }
  }
}
```

**What it does:**
- Tokenizes query: ["wireless", "headphones"]
- Searches for documents with these terms
- Ranks by BM25
- Supports fuzzy matching

**2. multi_match - Search multiple fields**

**Use for:** Searching across title, description, etc.

```json
{
  "query": {
    "multi_match": {
      "query": "laptop gaming",
      "fields": ["title", "description", "brand"]
    }
  }
}
```

**What it does:**
- Searches all specified fields
- Combines scores from each field
- Returns best overall matches

**3. term - Exact match**

**Use for:** Keyword fields (categories, SKUs, tags)

```json
{
  "query": {
    "term": {
      "category": "electronics"
    }
  }
}
```

**What it does:**
- Exact match only (case-sensitive)
- No analysis
- Use for keyword fields

**4. range - Numeric/date ranges**

**Use for:** Prices, dates, quantities

```json
{
  "query": {
    "range": {
      "price": {
        "gte": 500,
        "lte": 1000
      }
    }
  }
}
```

**What it does:**
- Filters by range
- gte: greater than or equal
- lte: less than or equal

**5. bool - Combine queries**

**Use for:** Complex searches with multiple conditions

```json
{
  "query": {
    "bool": {
      "must": [
        {"match": {"description": "laptop"}}
      ],
      "filter": [
        {"term": {"category": "electronics"}},
        {"range": {"price": {"lte": 1500}}}
      ],
      "must_not": [
        {"term": {"brand": "BrandX"}}
      ]
    }
  }
}
```

**Components:**
- **must**: MUST match (affects score, slower)
- **filter**: MUST match (no score, faster)
- **should**: SHOULD match (boosts score if matched)
- **must_not**: MUST NOT match

**When to use what:**
- **must**: For search terms that affect relevance
- **filter**: For exact conditions (category, price, availability)
- **should**: For optional boosting (brand preference)
- **must_not**: For exclusions

#### **5.3 Advanced Features** (20 min)

**Reading:**
📖 **Bool Query Documentation**  
URL: https://opensearch.org/docs/latest/query-dsl/compound/bool/  
Read: Full page

**Field Boosting:**

**Concept:** Some fields are more important than others

```json
{
  "query": {
    "multi_match": {
      "query": "laptop",
      "fields": [
        "title^3",        // 3x weight
        "description^2",  // 2x weight
        "brand^1"         // 1x weight
      ]
    }
  }
}
```

**Result:**
- Match in title: score × 3
- Match in description: score × 2
- Match in brand: score × 1

**Use case:** Product title more important than description.

**Pagination:**

```json
{
  "query": {...},
  "from": 0,      // Skip first N results
  "size": 10      // Return max N results
}
```

**Pages:**
```
Page 1: from=0,  size=10  (results 1-10)
Page 2: from=10, size=10  (results 11-20)
Page 3: from=20, size=10  (results 21-30)
```

**Highlighting:**

**Show where matches occurred:**

```json
{
  "query": {
    "match": {"description": "wireless"}
  },
  "highlight": {
    "fields": {
      "description": {}
    }
  }
}
```

**Response includes:**
```json
{
  "hits": [{
    "_source": {
      "description": "These wireless headphones are great"
    },
    "highlight": {
      "description": [
        "These <em>wireless</em> headphones are great"
      ]
    }
  }]
}
```

**Sorting:**

```json
{
  "query": {...},
  "sort": [
    {"price": {"order": "asc"}},
    "_score"
  ]
}
```

**Sorts by:** Price ascending, then relevance score

---

### **MODULE 6: Python OpenSearch Client** ⏱️ 45 minutes

#### **6.1 opensearch-py Basics** (25 min)

**Reading:**
📖 **opensearch-py Documentation**  
URL: https://opensearch.org/docs/latest/clients/python/  
Read: "Getting started" section

**Installation:**
```bash
pip install opensearch-py
```

**Basic Operations:**

**1. Connect to cluster:**
```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False
)

# Test connection
if client.ping():
    print("Connected to OpenSearch!")
```

**2. Create index with mapping:**
```python
index_name = "products"

mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "sku": {"type": "keyword"},
            "price": {"type": "float"},
            "description": {"type": "text"},
            "category": {"type": "keyword"},
            "in_stock": {"type": "boolean"}
        }
    }
}

response = client.indices.create(index=index_name, body=mapping)
print(f"Index created: {response['acknowledged']}")
```

**3. Index a document:**
```python
product = {
    "title": "Wireless Headphones",
    "sku": "WH-1000XM4",
    "price": 349.99,
    "description": "Premium noise-canceling headphones",
    "category": "electronics",
    "in_stock": True
}

response = client.index(
    index="products",
    id="1",
    body=product
)

print(f"Document indexed: {response['result']}")
```

**4. Search documents:**
```python
query = {
    "query": {
        "match": {
            "description": "headphones"
        }
    }
}

response = client.search(
    index="products",
    body=query
)

print(f"Found {response['hits']['total']['value']} products")

for hit in response['hits']['hits']:
    print(f"Title: {hit['_source']['title']}")
    print(f"Score: {hit['_score']}")
    print()
```

**5. Check cluster health:**
```python
health = client.cluster.health()
print(f"Cluster status: {health['status']}")
print(f"Number of nodes: {health['number_of_nodes']}")
```

#### **6.2 Common Operations** (20 min)

**Video:**
📺 **"Python Elasticsearch Tutorial"** - Tech With Tim  
URL: https://www.youtube.com/watch?v=p23JJ2hIFB4  
Watch: First 15 minutes

**Check if index exists:**
```python
if client.indices.exists(index="products"):
    print("Index exists")
else:
    print("Index does not exist")
```

**Delete index:**
```python
client.indices.delete(index="products")
print("Index deleted")
```

**Update document:**
```python
update_body = {
    "doc": {
        "price": 299.99,
        "in_stock": False
    }
}

client.update(
    index="products",
    id="1",
    body=update_body
)
```

**Delete document:**
```python
client.delete(index="products", id="1")
```

**Bulk indexing:**
```python
from opensearchpy import helpers

products = [
    {
        "_index": "products",
        "_id": "1",
        "_source": {"title": "Product 1", "price": 10.99}
    },
    {
        "_index": "products",
        "_id": "2",
        "_source": {"title": "Product 2", "price": 20.99}
    }
]

helpers.bulk(client, products)
print("Bulk indexing complete")
```

**Error handling:**
```python
from opensearchpy import NotFoundError, RequestError

try:
    result = client.get(index="products", id="999")
except NotFoundError:
    print("Document not found")
except RequestError as e:
    print(f"Request error: {e.info}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 🎯 HANDS-ON EXERCISES

### **EXERCISE 1: Text Analysis** ⏱️ 15 minutes

**Prerequisites:** OpenSearch running on localhost:9200

**Tool:** OpenSearch Dashboards (http://localhost:5601)  
**Location:** Dev Tools → Console

#### **Requirements:**

Test how different analyzers process text.

#### **Tasks:**

**Task 1: Test standard analyzer**

**Input text:** "Running Through The Forest Quickly"

**What to figure out:**
- POST /_analyze endpoint syntax
- How to specify analyzer
- How to interpret results

**Deliverables:**
- List of tokens produced
- Observe: lowercase, tokenization

**Hints:**
```json
POST /_analyze
{
  "analyzer": "standard",
  "text": "..."
}
```

**Task 2: Compare analyzers**

Test with same input text:
- standard analyzer
- english analyzer
- keyword analyzer

**Deliverables:**
- Document differences
- Note: stemming in english analyzer
- Note: no analysis in keyword

**Verification:**
```
standard: ["running", "through", "the", "forest", "quickly"]
english:  ["run", "forest", "quick"] (stemmed, stopwords removed)
keyword:  "Running Through The Forest Quickly" (unchanged)
```

---

### **EXERCISE 2: Create Product Index** ⏱️ 20 minutes

**Tool:** OpenSearch Dashboards Console

#### **Requirements:**

Create an index for e-commerce products with proper field types.

#### **Tasks:**

**Task 1: Define mapping**

**Fields:**
- title: searchable text
- sku: exact match (keyword)
- price: numeric
- category: exact match (keyword)
- description: searchable text
- in_stock: boolean

**What to figure out:**
- PUT endpoint for index creation
- Mapping structure
- Choosing correct field types

**Deliverables:**
- Index created successfully
- Appropriate types for each field

**Hints:**
```json
PUT /products
{
  "mappings": {
    "properties": {
      "field_name": {"type": "..."},
      ...
    }
  }
}
```

**Task 2: Index 3 products**

**Products:**
1. Laptop, SKU: LAP-001, $899, electronics, "High-performance laptop", in_stock
2. Mouse, SKU: MSE-002, $25, electronics, "Wireless mouse", in_stock
3. Keyboard, SKU: KEY-003, $75, electronics, "Mechanical keyboard", out_of_stock

**What to figure out:**
- POST endpoint for document indexing
- Document structure
- How to set document ID

**Task 3: Search products**

**Search:** "wireless"

**Expected results:**
- Returns Mouse (has "wireless" in description)
- Does NOT return Laptop or Keyboard

**What to figure out:**
- GET _search endpoint
- Match query structure
- How to read results

**Verification:**
```bash
GET /products/_search
{
  "query": {
    "match": {"description": "wireless"}
  }
}

# Should return 1 hit (Mouse)
```

**Task 4: Filter by category**

**Filter:** category = "electronics" AND in_stock = true

**Expected results:**
- Returns Laptop and Mouse
- Does NOT return Keyboard (out of stock)

**What to figure out:**
- Bool query structure
- Filter clause (not must)
- Term queries for exact match

---

### **EXERCISE 3: Text vs Keyword Field Types** ⏱️ 15 minutes

**Tool:** OpenSearch Dashboards Console

#### **Requirements:**

Understand the difference between text and keyword field types through experimentation.

#### **Tasks:**

**Task 1: Create index with both types**

**Index:** "field_comparison"

**Fields:**
- title_text: type text
- title_keyword: type keyword

**Both fields:** Store same value

**Task 2: Index test document**

**Document:**
```json
{
  "title_text": "Wireless Headphones",
  "title_keyword": "Wireless Headphones"
}
```

**Task 3: Run comparison searches**

**Search A:** Search title_text for "wireless"
```json
{"query": {"match": {"title_text": "wireless"}}}
```
**Expected:** ✅ FOUND (text analyzed, partial match works)

**Search B:** Search title_keyword for "wireless"
```json
{"query": {"term": {"title_keyword": "wireless"}}}
```
**Expected:** ❌ NOT FOUND (keyword not analyzed, case matters)

**Search C:** Search title_keyword for "Wireless Headphones"
```json
{"query": {"term": {"title_keyword": "Wireless Headphones"}}}
```
**Expected:** ✅ FOUND (exact match)

**Search D:** Search title_keyword for "wireless headphones"
```json
{"query": {"term": {"title_keyword": "wireless headphones"}}}
```
**Expected:** ❌ NOT FOUND (case doesn't match)

**Deliverables:**
- Document which searches match
- Explain why each behaves differently

**What to figure out:**
- match vs term queries
- When to use each field type
- Case sensitivity in keyword fields

**Verification:**

After tests, you should understand:
- **text fields:** Analyzed → lowercase, tokenized → partial matches work
- **keyword fields:** Not analyzed → exact string → case-sensitive

**Use cases:**
- text: Product descriptions, blog content, reviews
- keyword: SKUs, email addresses, categories, URLs

---

## ✅ READINESS CHECKLIST

Before implementing Steps 9-12, verify you can:

### **Conceptual Understanding:**

- [ ] Explain: Search engine vs database - when to use each?
- [ ] Explain: How does inverted index enable O(1) lookups?
- [ ] List: What are the 3 components of BM25?
- [ ] Decide: When to use text vs keyword field type?
- [ ] Describe: What does an analyzer do?
- [ ] Explain: Difference between must and filter in bool query?

### **Practical Skills:**

- [ ] Connect to OpenSearch from Python
- [ ] Create an index with mapping
- [ ] Index a document
- [ ] Write a match query
- [ ] Write a multi_match query with field boosting
- [ ] Add pagination (from, size)
- [ ] Enable highlighting
- [ ] Write a bool query combining must + filter

### **Real-World Scenarios:**

- [ ] Design mapping for e-commerce product search
- [ ] Build query: Search + filter by category + price range
- [ ] Explain: Why use both PostgreSQL AND OpenSearch?

**If you answered YES to all:** ✅ Ready to implement Steps 9-12!

---

## 🎯 WHAT TO FOCUS ON

### **CRITICAL (Must understand):**
- ✅ OpenSearch vs database (different use cases)
- ✅ Inverted index concept (word → documents)
- ✅ BM25 scoring basics (TF × IDF × length)
- ✅ text vs keyword field types
- ✅ match vs term queries
- ✅ bool query structure (must, filter, should, must_not)

### **IMPORTANT (Very helpful):**
- ✅ Analyzer selection (standard vs english)
- ✅ Field boosting (title^3)
- ✅ Pagination patterns (from, size)
- ✅ Error handling in Python client

### **NICE TO HAVE (Learn as needed):**
- Advanced analyzers (custom token filters)
- BM25 parameter tuning (k1, b)
- Shard allocation strategies
- Performance optimization

---

## 📚 ADDITIONAL RESOURCES (Optional)

**OpenSearch:**
- Official Docs: https://opensearch.org/docs/latest/
- Getting Started: https://opensearch.org/docs/latest/getting-started/
- Field Types: https://opensearch.org/docs/latest/field-types/

**Query DSL:**
- Query Reference: https://opensearch.org/docs/latest/query-dsl/
- Bool Query: https://opensearch.org/docs/latest/query-dsl/compound/bool/
- Match Query: https://opensearch.org/docs/latest/query-dsl/full-text/match/

**Python Client:**
- opensearch-py: https://opensearch.org/docs/latest/clients/python/
- GitHub: https://github.com/opensearch-project/opensearch-py
- Examples: https://github.com/opensearch-project/opensearch-py/tree/main/samples

**Books (Optional):**
- "Relevant Search" by Doug Turnbull & John Berryman
- "Elasticsearch: The Definitive Guide" (concepts apply to OpenSearch)

**Community:**
- OpenSearch Forums: https://forum.opensearch.org/
- Stack Overflow: Tag `opensearch`

---

## 🚀 AFTER LEARNING

**You're ready to implement Steps 9-12 when you can:**

1. Explain why inverted indexes are faster than database LIKE queries
2. Describe how BM25 ranks search results
3. Choose text vs keyword for any given field
4. Write a multi_match query with field boosting
5. Connect to OpenSearch from Python
6. Create index, index documents, search documents

**Next Steps:**
- Apply these concepts to your specific project
- Implement Steps 9-12 using requirements guides
- Reference this guide when stuck on concepts

---

**Time estimate:** 4-5 hours focused learning  
**Best approach:** Learn over weekend, implement during week  
**Remember:** Concepts first, then application!

---

**Document Generated:** December 24, 2025  
**Purpose:** OpenSearch & BM25 conceptual learning  
**Approach:** Generic examples, technology-agnostic
