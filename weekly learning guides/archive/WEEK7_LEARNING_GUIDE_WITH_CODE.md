# 📚 WEEK 7 LEARNING GUIDE: OpenSearch & BM25 Search

**Pre-learning for Steps 9-12 (OpenSearch Implementation)**

**Your Timeline:** Weekend before implementing Steps 9-12  
**Time Investment:** 4-5 hours  
**Format:** Self-paced learning modules

---

## 🎯 LEARNING OBJECTIVES

By the end of this guide, you should understand:

1. **What is OpenSearch** and how it differs from traditional databases
2. **How search engines work** - inverted indexes, analyzers, tokenization
3. **BM25 algorithm** - the ranking function behind keyword search
4. **Index mapping** - defining document structure
5. **Query DSL** - how to build search queries
6. **Python OpenSearch client** - interacting with OpenSearch from code

**Goal:** Confident enough to implement Steps 9-12 without confusion

---

## 📖 MODULE 1: OpenSearch Fundamentals (1 hour)

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

## 📖 MODULE 2: Inverted Indexes (45 min)

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

## 📖 MODULE 3: BM25 Algorithm (1 hour)

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
- Play with BM25 calculator: http://www.bm25.org/ (if available)

---

## 📖 MODULE 4: Index Mapping (45 min)

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
2. Lowercase: ["machine", "learning"]
3. Remove stopwords: (none in this case)

**Custom analyzers** can:
- Remove stopwords ("the", "a", "is")
- Stem words ("running" → "run")
- Handle synonyms ("ML" → "machine learning")

### **Resources:**

**Read (30 min):**
- OpenSearch "Mappings" docs: https://opensearch.org/docs/latest/field-types/
- OpenSearch "Analyzers" docs: https://opensearch.org/docs/latest/analyzers/

**Practice (15 min):**
- Try defining mapping for a book index
- Fields: title, author, description, isbn, published_year

---

## 📖 MODULE 5: Query DSL (1 hour)

### **What is Query DSL?**

DSL = Domain Specific Language

Query DSL is JSON-based query language for OpenSearch.

### **Basic Query Types:**

**1. match** - Full-text search (uses BM25)
```json
{
  "query": {
    "match": {
      "title": "machine learning"
    }
  }
}
```

**2. multi_match** - Search across multiple fields
```json
{
  "query": {
    "multi_match": {
      "query": "neural networks",
      "fields": ["title", "abstract"]
    }
  }
}
```

**3. term** - Exact match (for keyword fields)
```json
{
  "query": {
    "term": {
      "categories": "cs.AI"
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
        {"term": {"categories": "cs.AI"}}
      ]
    }
  }
}
```

### **Query Components:**

**1. must** - Document MUST match (affects score)
```json
"must": [
  {"match": {"title": "AI"}}
]
```

**2. filter** - Document MUST match (doesn't affect score)
```json
"filter": [
  {"term": {"category": "cs.AI"}}
]
```

**3. should** - Document SHOULD match (boosts score)
```json
"should": [
  {"match": {"abstract": "neural"}}
]
```

**4. must_not** - Document MUST NOT match
```json
"must_not": [
  {"term": {"category": "math.CO"}}
]
```

### **Boosting Fields:**

Give more weight to title matches:
```json
{
  "query": {
    "multi_match": {
      "query": "machine learning",
      "fields": ["title^3", "abstract^2", "authors^1"]
    }
  }
}
```

- title^3 = 3x weight
- abstract^2 = 2x weight
- authors^1 = 1x weight

### **Pagination:**

```json
{
  "query": {...},
  "from": 0,
  "size": 10
}
```

### **Highlighting:**

Show matching parts:
```json
{
  "query": {...},
  "highlight": {
    "fields": {
      "abstract": {}
    }
  }
}
```

### **Resources:**

**Read (45 min):**
- OpenSearch "Query DSL" docs: https://opensearch.org/docs/latest/query-dsl/
- Focus on: match, multi_match, bool queries

**Practice (15 min):**
- Write queries for:
  - Search papers by title
  - Search across title and abstract
  - Search + filter by category
  - Search with field boosting

---

## 📖 MODULE 6: Python OpenSearch Client (45 min)

### **opensearch-py Library**

Official Python client for OpenSearch.

### **Installation:**

```bash
pip install opensearch-py
```

### **Basic Usage:**

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
- opensearch-py docs: https://opensearch.org/docs/latest/clients/python/
- GitHub examples: https://github.com/opensearch-project/opensearch-py

**Practice (15 min):**
- Install opensearch-py
- Connect to OpenSearch (from Step 9)
- Try creating test index
- Index a document
- Search for it

---

## 🎯 HANDS-ON EXERCISES

### **Exercise 1: Analyze Text (15 min)**

Use OpenSearch Dashboards (http://localhost:5601):

```json
POST /_analyze
{
  "analyzer": "standard",
  "text": "Machine Learning Algorithms"
}
```

**Observe:** How text is tokenized

### **Exercise 2: Create Test Index (20 min)**

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

### **Exercise 3: Compare text vs keyword (15 min)**

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

## 📋 WEEK 7 READINESS CHECKLIST

**Before starting Steps 9-12, you should be able to:**

- [ ] Explain difference between PostgreSQL and OpenSearch
- [ ] Describe how inverted indexes work
- [ ] Explain BM25 in simple terms
- [ ] Define index mapping with field types
- [ ] Write basic match and multi_match queries
- [ ] Write bool queries with must/filter
- [ ] Use Python OpenSearch client to:
  - [ ] Create index
  - [ ] Index documents
  - [ ] Search documents
- [ ] Understand text vs keyword fields
- [ ] Know what analyzers do

**If you can do all above:** ✅ Ready for Steps 9-12!

---

## 🎓 LEARNING SCHEDULE

**Weekend Before Week 7:**

**Saturday (2-3 hours):**
- Module 1: OpenSearch Fundamentals (1h)
- Module 2: Inverted Indexes (45min)
- Module 3: BM25 Algorithm (1h)

**Sunday (2 hours):**
- Module 4: Index Mapping (45min)
- Module 5: Query DSL (1h)
- Module 6: Python Client (45min)
- Hands-on Exercises (45min)

**Total:** 4-5 hours

---

## 📚 OPTIONAL DEEP DIVES

**If you want to go deeper:**

**Advanced BM25:**
- Tune k1 and b parameters
- Custom similarity algorithms

**Advanced Analyzers:**
- Custom analyzers with filters
- Synonym handling
- N-grams for autocomplete

**Advanced Queries:**
- Function score queries
- Script queries
- Aggregations

**But for Steps 9-12:** Basic understanding is enough!

---

## 🎯 KEY TAKEAWAYS

**Remember these 5 things:**

1. **OpenSearch = Search engine, not database**
   - Use for full-text search
   - PostgreSQL is still source of truth

2. **Inverted index = Fast lookups**
   - Term → Document IDs
   - O(1) instead of O(n)

3. **BM25 = Ranking algorithm**
   - Term frequency + rarity + length
   - Automatic in OpenSearch

4. **Mapping = Schema**
   - text = full-text search
   - keyword = exact match

5. **Query DSL = JSON queries**
   - match = full-text
   - term = exact
   - bool = combine

**If you understand these 5:** You're 80% ready! ✅

---

## 🚀 NEXT STEPS

After completing this guide:

1. **Take a break** (let it sink in)
2. **Review key concepts** (5 takeaways)
3. **Start Step 9** (OpenSearch setup)
4. **Reference this guide** as needed during Steps 10-12

**Remember:** You don't need to memorize everything. Understanding concepts > memorizing syntax.

---

## 💡 CONNECTION TO YOUR PROJECT

**In your arXiv RAG system:**

**PostgreSQL:**
- Stores complete paper metadata
- Source of truth for all data
- Handles transactional operations

**OpenSearch:**
- Indexes paper content for search
- Enables fast full-text search
- Ranks results by relevance
- Provides highlighting

**The Flow:**
1. Papers stored in PostgreSQL (Steps 1-8)
2. Papers indexed in OpenSearch (Step 10)
3. Users search via API (Step 12)
4. OpenSearch finds relevant papers (BM25)
5. Results returned with highlights

---

## 📖 ADDITIONAL RESOURCES

**Official Documentation:**
- OpenSearch: https://opensearch.org/docs/latest/
- opensearch-py: https://opensearch.org/docs/latest/clients/python/

**Video Tutorials:**
- OpenSearch Basics Playlist (Elastic content applies)
- BM25 Algorithm Explained

**Interactive Learning:**
- OpenSearch Dashboards Dev Tools
- Try queries in real-time

---

**Document Generated:** December 23, 2025  
**Purpose:** Pre-learning for Week 7 (Steps 9-12)  
**Time Required:** 4-5 hours  
**Format:** Self-paced learning modules  
**Part of:** 8.5-Month AI/ML Career Transition Plan
