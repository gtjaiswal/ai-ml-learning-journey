# 📚 WEEK 7 LEARNING GUIDE: Redis, OpenSearch & BM25 Search

**Pre-learning for Steps 9-12 (Search Infrastructure + Caching)**

**Time Investment:** 5-6 hours over the weekend before Week 7

---

## 🎯 LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **What is Redis** and how caching improves performance
2. **What is OpenSearch** and how it differs from traditional databases
3. **How search engines work** - inverted indexes, analyzers, tokenization
4. **BM25 algorithm** - the ranking function behind keyword search
5. **Index mapping** - defining document structure
6. **Query DSL** - how to build search queries
7. **Python clients** - Redis and OpenSearch from code

**Goal:** Confident enough to implement Steps 9-12 without confusion

---

## 📖 MODULE 1: Redis Fundamentals (45 minutes)

### **What is Redis?**

Redis = **RE**mote **DI**ctionary **S**erver

It's an **in-memory data structure store** - think of it as:
- Ultra-fast key-value database
- All data stored in RAM (microsecond latency)
- Perfect for caching
- Optional persistence to disk

**Speed comparison:**

| Storage | Latency | Use Case |
|---------|---------|----------|
| Redis (RAM) | ~0.1ms | Caching, sessions |
| PostgreSQL (Disk) | ~10ms | Persistent data |
| OpenSearch (Disk) | ~50ms | Full-text search |

### **When to use Redis?**

✅ **Perfect for:**
- Caching search results (← what we're doing!)
- Session storage
- Rate limiting
- Real-time counters
- Pub/sub messaging
- Temporary data that can be regenerated

❌ **Not for:**
- Primary data storage (use PostgreSQL)
- Complex queries (use PostgreSQL/OpenSearch)
- Large datasets that don't fit in RAM

**In your project:**
- **PostgreSQL** = Source of truth (all papers permanently stored)
- **OpenSearch** = Search index (fast text search)
- **Redis** = Cache layer (frequently accessed searches)

### **Core Concepts:**

**1. Key-Value Store:**
```
Key:   "search:abc123"
Value: '{"query": "ML", "total": 42, "hits": [...]}'
```

Simple as a Python dictionary, but:
- Shared across application instances
- Persists between restarts (with AOF)
- Automatic expiration (TTL)

**2. TTL (Time To Live):**
```python
# Set key with 300-second expiration
redis.setex("search:123", 300, '{"results": [...]}')

# After 300 seconds: key automatically deleted
```

**Why TTL?**
- Search results become stale over time
- Free up memory automatically
- Balance freshness vs performance

**3. Eviction Policies:**

What happens when Redis runs out of memory?

**LRU (Least Recently Used)** - We use this:
- Tracks when each key was last accessed
- Removes oldest-accessed keys first
- Keeps frequently used data in cache
- Example: Popular search "machine learning" stays, rare search "quantum cheese" gets evicted

**Other policies:**
- LFU (Least Frequently Used): Remove least-used keys
- Random: Remove random keys
- No eviction: Reject new writes when full

**4. Persistence:**

**AOF (Append-Only File)** - We use this:
- Logs every write operation
- Can replay log to rebuild data
- Slower but safer
- Good for: Cache you don't want to lose

**RDB (Snapshot):**
- Periodic full dumps
- Faster but can lose recent data
- Good for: Truly temporary cache

### **Real-World Example:**

**Without Redis:**
```
User searches "machine learning"
  ↓
Query OpenSearch (~100ms)
  ↓
Return results

User searches "machine learning" again
  ↓
Query OpenSearch again (~100ms)  ← Wasted work!
```

**With Redis:**
```
User searches "machine learning"
  ↓
Check Redis cache (MISS)
  ↓
Query OpenSearch (~100ms)
  ↓
Cache result in Redis (TTL: 5 min)
  ↓
Return results

User searches "machine learning" again
  ↓
Check Redis cache (HIT) (~1ms) ← 100x faster!
  ↓
Return cached results
```

### **Resources:**

**Watch (15 min):**
- "Redis in 100 Seconds" by Fireship: https://www.youtube.com/watch?v=G1rOthIU-uo
- "What is Redis?" by Redis University: https://university.redis.com/courses/ru101/

**Read (30 min):**
- Redis official docs: https://redis.io/docs/about/
- Focus on: "Introduction to Redis" and "Data types tutorial"
- Redis persistence: https://redis.io/docs/management/persistence/

**Key Takeaways:**
- Redis stores everything in RAM → ultra fast (< 1ms)
- Use for temporary data that can be regenerated
- TTL automatically expires old data
- LRU eviction keeps frequently accessed items
- AOF persistence protects against crashes

---

## 📖 MODULE 2: OpenSearch Fundamentals (1 hour)

### **What is OpenSearch?**

OpenSearch is a **search and analytics engine** - think of it as:
- Google search for your data
- Optimized for text search (not SQL queries)
- Built on inverted indexes (not tables)
- Real-time search and aggregations

**Key difference from PostgreSQL:**

| PostgreSQL | OpenSearch |
|------------|------------|
| Relational database | Search engine |
| Tables with rows | Indexes with documents |
| SQL queries | Query DSL (JSON) |
| ACID transactions | Eventually consistent |
| Exact matches | Fuzzy matches, relevance scoring |
| `WHERE title = 'AI'` | `"Machine Learning" → finds "ML", "machine learning", "AI"` |

### **When to use OpenSearch?**

✅ **Good for:**
- Full-text search (searching papers, articles, documents)
- Fuzzy matching ("machne lerning" finds "machine learning")
- Relevance ranking (best matches first)
- Faceted search (filter by category, date, author)
- Analytics and aggregations

❌ **Not for:**
- Transactional data (use PostgreSQL)
- Complex joins (use PostgreSQL)
- Source of truth (use PostgreSQL)

**In your project:**
- **PostgreSQL** = Source of truth (stores all papers)
- **OpenSearch** = Search layer (fast text search)
- **Redis** = Cache layer (frequently accessed searches)

### **Core Concepts:**

**1. Index** = Like a database table
- Contains documents
- Has a mapping (schema)

**2. Document** = Like a row
- JSON object
- Example: A paper with title, abstract, authors

**3. Field** = Like a column
- Part of document
- Can be text, keyword, date, etc.

**4. Mapping** = Schema definition
- Defines field types
- Defines analyzers

**5. Analyzer** = Text processing pipeline
- Breaks text into tokens
- Lowercases, removes stopwords, stems words
- "Machine Learning Papers" → ["machine", "learn", "paper"]

### **Resources:**

**Watch (30 min):**
- "What is Elasticsearch" by Elastic (OpenSearch is a fork): https://www.youtube.com/watch?v=C3tlMqaNSaI
- Note: OpenSearch = Elasticsearch fork, 95% same concepts

**Read (30 min):**
- OpenSearch official docs: https://opensearch.org/docs/latest/
- Focus on: "What is OpenSearch?" section
- Browse: Getting Started tutorial

---

## 📖 MODULE 3: Inverted Indexes (45 min)

### **How Search Engines Work**

Traditional database:
```
Papers table:
ID | Title
1  | Machine Learning Basics
2  | Deep Learning Tutorial
```

To find "Learning", you scan every row. Slow!

**Inverted Index:**
```
Term → Document IDs
"machine"  → [1]
"learning" → [1, 2]
"basics"   → [1]
"deep"     → [2]
"tutorial" → [2]
```

To find "Learning", lookup once in index. Fast!

### **How it's built:**

**Step 1: Tokenization**
```
"Machine Learning Basics" 
→ ["Machine", "Learning", "Basics"]
```

**Step 2: Normalization (lowercase, stem)**
```
["Machine", "Learning", "Basics"]
→ ["machine", "learn", "basic"]
```

**Step 3: Build index**
```
"machine" → doc1
"learn"   → doc1
"basic"   → doc1
```

### **Why it's fast:**

- Lookup in hash map: O(1)
- No scanning rows: O(n) → O(1)
- Scales to billions of documents

### **Resources:**

**Watch (20 min):**
- "How do search engines work?" by Fireship: https://www.youtube.com/watch?v=0LTXCcVRQi0

**Read (25 min):**
- OpenSearch "Inverted Index" concept: https://opensearch.org/docs/latest/field-types/
- Focus on: text vs keyword fields

---

## 📖 MODULE 4: BM25 Algorithm (1 hour)

### **What is BM25?**

BM25 = **Best Match 25** (25th iteration of the algorithm)

It's a **ranking function** that scores how relevant a document is to a query.

**Simple version:**
```
Score = How often term appears in document 
        × How rare the term is across all documents
        × Document length normalization
```

### **Example:**

**Query:** "machine learning"

**Document 1:** "Machine learning is a subset of AI. Machine learning uses algorithms."
- "machine" appears 2 times
- "learning" appears 2 times
- Term frequency: HIGH
- **Score: HIGH**

**Document 2:** "This paper mentions machine learning once."
- "machine" appears 1 time
- "learning" appears 1 time
- Term frequency: LOW
- **Score: LOWER**

### **BM25 Components:**

**1. Term Frequency (TF)**
- How many times does term appear in document?
- But with diminishing returns (2→3 occurrences matters less than 0→1)

**2. Inverse Document Frequency (IDF)**
- How rare is the term across all documents?
- "the" appears everywhere → LOW score
- "quantum" appears rarely → HIGH score

**3. Document Length Normalization**
- Short documents with term → HIGHER score
- Long documents with term → LOWER score
- Prevents long documents from dominating

### **Formula (simplified):**

```
BM25(D, Q) = Σ IDF(qi) × (f(qi, D) × (k1 + 1)) / (f(qi, D) + k1 × (1 - b + b × |D| / avgdl))

Where:
- D = document
- Q = query
- qi = query term i
- f(qi, D) = frequency of qi in D
- |D| = document length
- avgdl = average document length
- k1 = term frequency saturation (usually 1.2)
- b = length normalization (usually 0.75)
```

**Don't memorize this!** Just understand:
- More term occurrences = higher score (but diminishing returns)
- Rarer terms = higher score
- Shorter documents = slightly higher score

### **In Practice:**

OpenSearch does this automatically!

```json
{
  "query": {
    "match": {
      "title": "machine learning"
    }
  }
}
```

BM25 calculates scores for all documents, returns best matches first.

### **Resources:**

**Watch (15 min):**
- "BM25 Explained" by Elastic: https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables

**Read (30 min):**
- Wikipedia BM25: https://en.wikipedia.org/wiki/Okapi_BM25
- OpenSearch "Similarity" docs: https://opensearch.org/docs/latest/query-dsl/

**Interactive (15 min):**
- Play with search in OpenSearch Dashboards (Step 9)

---

## 📖 MODULE 5: Index Mapping (45 min)

### **What is Mapping?**

Mapping = Schema definition for your index

It tells OpenSearch:
- What fields exist
- What type each field is (text, keyword, date, etc.)
- How to analyze text fields

### **Field Types:**

**1. text** - For full-text search
- Analyzed (tokenized, lowercased, stemmed)
- Searchable with match queries
- Example: Abstract, content

**2. keyword** - For exact matches
- NOT analyzed (stored as-is)
- Searchable with term queries
- Example: arXiv ID, category tags

**3. date** - For dates
- Stored as timestamp
- Searchable with range queries

**4. integer, float** - For numbers

### **Example Mapping:**

```json
{
  "mappings": {
    "properties": {
      "arxiv_id": {
        "type": "keyword"
      },
      "title": {
        "type": "text",
        "analyzer": "standard"
      },
      "abstract": {
        "type": "text",
        "analyzer": "standard"
      },
      "categories": {
        "type": "keyword"
      },
      "published_date": {
        "type": "date"
      }
    }
  }
}
```

### **Analyzers:**

**Standard analyzer** (default):
1. Tokenize: "Machine Learning" → ["Machine", "Learning"]
2. Lowercase: ["Machine", "Learning"] → ["machine", "learning"]
3. Remove stopwords: ["the", "machine", "learning"] → ["machine", "learning"]

**Custom analyzers:**
- English analyzer: Stems words ("running" → "run")
- Keyword analyzer: No analysis (keeps exact text)

### **Why Mapping Matters:**

Wrong mapping:
```json
"arxiv_id": {"type": "text"}  ← WRONG!
```

Searching for `"2401.00001"` might find `"2401.00002"` (partial match)

Right mapping:
```json
"arxiv_id": {"type": "keyword"}  ← CORRECT!
```

Searching for `"2401.00001"` only finds exact match.

### **Resources:**

**Read (30 min):**
- OpenSearch field types: https://opensearch.org/docs/latest/field-types/
- Analyzers: https://opensearch.org/docs/latest/analyzers/

**Practice (15 min):**
- Experiment with analyzers in OpenSearch Dashboards

---

## 📖 MODULE 6: Query DSL (1 hour)

### **What is Query DSL?**

DSL = **Domain Specific Language**

It's JSON-based query syntax for OpenSearch:

```json
{
  "query": {
    "match": {
      "title": "machine learning"
    }
  }
}
```

### **Common Query Types:**

**1. match** - Full-text search
```json
{
  "query": {
    "match": {
      "abstract": "neural networks"
    }
  }
}
```

Finds: "neural networks", "network neurology", "neuronal net"

**2. multi_match** - Search across multiple fields
```json
{
  "query": {
    "multi_match": {
      "query": "transformers",
      "fields": ["title^3", "abstract^2", "authors^1"]
    }
  }
}
```

`^3` = 3x boost (title matches score 3x higher)

**3. term** - Exact match (for keyword fields)
```json
{
  "query": {
    "term": {
      "arxiv_id": "2401.00001"
    }
  }
}
```

**4. bool** - Combine queries
```json
{
  "query": {
    "bool": {
      "must": [
        {"match": {"title": "machine learning"}}
      ],
      "filter": [
        {"terms": {"categories": ["cs.AI", "cs.LG"]}}
      ]
    }
  }
}
```

- `must`: Affects score (BM25)
- `filter`: Doesn't affect score (faster)
- `should`: Optional (boosts score if matched)
- `must_not`: Excludes documents

### **Pagination:**

```json
{
  "query": {...},
  "from": 0,
  "size": 10
}
```

- `from`: Offset (0-indexed)
- `size`: Results per page

### **Highlighting:**

```json
{
  "query": {...},
  "highlight": {
    "fields": {
      "title": {},
      "abstract": {}
    }
  }
}
```

Returns: `"This is <mark>machine learning</mark>"`

### **Resources:**

**Read (45 min):**
- Query DSL overview: https://opensearch.org/docs/latest/query-dsl/
- Match query: https://opensearch.org/docs/latest/query-dsl/full-text/match/
- Bool query: https://opensearch.org/docs/latest/query-dsl/compound/bool/

**Practice (15 min):**
- Try queries in OpenSearch Dashboards Dev Tools

---

## 📖 MODULE 7: Python Clients (45 min)

### **Redis Client (redis-py):**

**Installation:**

```bash
pip install redis
```

**Basic Usage:**

**Connect:**
```python
import redis

client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True  # Return strings, not bytes
)
```

**Set with TTL:**
```python
client.setex(
    name='search:abc123',
    time=300,  # 5 minutes
    value='{"results": [...]}'
)
```

**Get:**
```python
value = client.get('search:abc123')
# Returns: '{"results": [...]}' or None
```

**Check existence:**
```python
exists = client.exists('search:abc123')
# Returns: 1 (exists) or 0 (doesn't exist)
```

### **OpenSearch Client (opensearch-py):**

**Installation:**

```bash
pip install opensearch-py
```

**Basic Usage:**

**Connect:**
```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False
)
```

**Create Index:**
```python
index_name = "papers"
mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "abstract": {"type": "text"}
        }
    }
}

client.indices.create(index=index_name, body=mapping)
```

**Index Document:**
```python
document = {
    "title": "Machine Learning Paper",
    "abstract": "This paper explores..."
}

client.index(
    index="papers",
    id="paper1",
    body=document
)
```

**Search:**
```python
query = {
    "query": {
        "match": {
            "title": "machine learning"
        }
    }
}

response = client.search(
    index="papers",
    body=query
)

for hit in response['hits']['hits']:
    print(hit['_source']['title'])
    print(f"Score: {hit['_score']}")
```

### **Resources:**

**Read (30 min):**
- redis-py docs: https://redis-py.readthedocs.io/
- opensearch-py docs: https://opensearch.org/docs/latest/clients/python/
- GitHub examples: https://github.com/opensearch-project/opensearch-py

**Practice (15 min):**
- Install both libraries
- Connect to both services (from Step 9)
- Try basic operations

---

## 🎯 HANDS-ON EXERCISES

### **Exercise 1: Test Redis (15 min)**

**Using redis-cli:**
```bash
# Connect
redis-cli

# Set key with 60-second expiration
SETEX test:key 60 "Hello Redis"

# Get value
GET test:key

# Check TTL
TTL test:key

# Wait 60 seconds, try GET again
GET test:key  # Returns (nil)
```

**Observe:** Automatic expiration

### **Exercise 2: Analyze Text (15 min)**

Use OpenSearch Dashboards (http://localhost:5601):

```json
POST /_analyze
{
  "analyzer": "standard",
  "text": "Machine Learning Algorithms"
}
```

**Observe:** How text is tokenized

### **Exercise 3: Create Test Index (20 min)**

```json
PUT /test-papers
{
  "mappings": {
    "properties": {
      "title": {"type": "text"},
      "category": {"type": "keyword"}
    }
  }
}
```

Index 3 documents, search them.

### **Exercise 4: Compare text vs keyword (15 min)**

Create index with both types:
```json
{
  "title_text": {"type": "text"},
  "title_keyword": {"type": "keyword"}
}
```

Index: "Machine Learning"

Search:
- `{"match": {"title_text": "machine"}}` → FOUND
- `{"term": {"title_keyword": "machine"}}` → NOT FOUND
- `{"term": {"title_keyword": "Machine Learning"}}` → FOUND

**Understand:** text is analyzed, keyword is not

---

## 🎓 LEARNING SCHEDULE

**Weekend Before Week 7:**

**Saturday (3 hours):**
- Module 1: Redis Fundamentals (45min)
- Module 2: OpenSearch Fundamentals (1h)
- Module 3: Inverted Indexes (45min)
- Module 4: BM25 Algorithm (30min)

**Sunday (2.5 hours):**
- Module 5: Index Mapping (45min)
- Module 6: Query DSL (1h)
- Module 7: Python Clients (45min)

**Total:** 5.5 hours

---

## 📋 WEEK 7 READINESS CHECKLIST

**Before starting Steps 9-12, you should be able to:**

**Redis:**
- [ ] Explain what Redis is and why it's fast
- [ ] Understand TTL concept
- [ ] Know what LRU eviction means
- [ ] Differentiate AOF vs RDB persistence

**OpenSearch:**
- [ ] Explain difference between PostgreSQL and OpenSearch
- [ ] Describe how inverted indexes work
- [ ] Explain BM25 in simple terms
- [ ] Define index mapping with field types
- [ ] Understand text vs keyword fields
- [ ] Know what analyzers do

**Query DSL:**
- [ ] Write basic match and multi_match queries
- [ ] Write bool queries with must/filter
- [ ] Understand field boosting (^3, ^2)

**Python Clients:**
- [ ] Use redis-py to get/set with TTL
- [ ] Use opensearch-py to:
  - [ ] Create index
  - [ ] Index documents
  - [ ] Search documents

**If you can do all above:** ✅ Ready for Steps 9-12!

---

## 🎯 KEY TAKEAWAYS

**Remember these 7 things:**

1. **Redis = Ultra-fast cache in RAM**
   - Use for temporary data
   - TTL for automatic expiration
   - < 1ms latency

2. **OpenSearch = Search engine, not database**
   - Use for full-text search
   - PostgreSQL is still source of truth

3. **Inverted index = Fast lookups**
   - Term → Document IDs
   - O(1) instead of O(n)

4. **BM25 = Ranking algorithm**
   - Term frequency + rarity + length
   - Automatic in OpenSearch

5. **Mapping = Schema**
   - text = full-text search
   - keyword = exact match

6. **Query DSL = JSON queries**
   - match = full-text
   - term = exact
   - bool = combine

7. **Three-layer architecture:**
   - PostgreSQL (persistent storage)
   - OpenSearch (search index)
   - Redis (cache layer)

**If you understand these 7:** You're 90% ready! ✅

---

## 🚀 NEXT STEPS

After completing this guide:

1. **Take a break** (let it sink in)
2. **Review key concepts** (7 takeaways)
3. **Start Step 9** (Redis + OpenSearch setup)
4. **Reference this guide** as needed during Steps 9-12

**Remember:** You don't need to memorize everything. Understanding concepts > memorizing syntax.

---

**Document Generated:** December 26, 2025  
**Purpose:** Pre-learning for Week 7 (Steps 9-12)  
**Time Required:** 5-6 hours  
**Format:** Self-paced learning modules with Redis integration
