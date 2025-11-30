# Week 2 Learning Schedule - APIs & Advanced Math

## Overview

A comprehensive 7-day learning plan covering gradient descent, loss functions, REST APIs, Python requests library, and FastAPI development. Total commitment: ~11 hours.

---

## Week Schedule

| Day | Date | Topic | Time |
|-----|------|-------|------|
| Mon | Nov 24 | Calculus concepts - Derivatives & Gradients | 1h |
| Tue | Nov 25 | Gradient Descent Deep Dive | 1h |
| Wed | Nov 26 | Loss Functions & Optimization | 1h |
| Thu | Nov 27 | REST API Basics | 1h |
| Fri | Nov 28 | Python Requests Library | 1h |
| Sat | Nov 29 | **FastAPI Basics & Build API** | 3h |
| Sun | Nov 30 | Polish Transaction Stats API | 3h |

**Total Week 2:** ~11 hours

---

   ## Day 1: Calculus Concepts - Derivatives & Gradients

   ### Primary Video Resources

   #### 3Blue1Brown - Essence of Calculus

   **Video 1: "Essence of Calculus" - Chapter 1**
   - Link: https://www.youtube.com/watch?v=WUvTyaaNkzM
   - Duration: 10:26
   - What you'll learn: What IS a derivative? (brilliant visual explanation)

   **Video 2: "The paradox of the derivative"**
   - Link: https://www.youtube.com/watch?v=9vKqVkMQHKk
   - Duration: 10:14
   - What you'll learn: Derivative paradox, deeper intuition

   **Video 3 (Optional): "Derivative formulas through geometry"**
   - Link: https://www.youtube.com/watch?v=S0_qX4VJhMQ
   - Duration: 10:11
   - Watch if you have extra time

   ### Reading Materials

   **Article: "A Gentle Introduction to Gradient in Machine Learning"**
   - Link: https://machinelearningmastery.com/gradient-in-machine-learning/
   - Duration: 10 min read
   - Focus: What gradients mean for ML

   **Khan Academy: Introduction to Derivatives**
   - Link: https://www.khanacademy.org/math/calculus-1/cs1-derivatives-definition-and-basic-rules/cs1-derivatives-intro/v/calculus-derivatives-1-new-hd-version
   - Duration: 10 min
   - Quick overview if 3Blue1Brown isn't enough

   ### Day1's Schedule (60 minutes total)

   **Recommended Order:**

   1. **Watch: 3Blue1Brown Chapter 1** (10 min)
      - Focus on understanding, not memorization

   2. **Watch: 3Blue1Brown "Paradox of derivative"** (10 min)
      - Let it sink in

   3. **Read: ML Mastery article on gradients** (10 min)
      - Connect calculus to ML

   4. **Visualize and Draw** (15 min)
      - Draw a curve on paper
      - Pick a point, draw tangent line (derivative)
      - Label: steep slope = large derivative
      - Flat area = small derivative

   5. **Reflection Questions** (15 min)

   ### Reflection Questions

   Write answers to:
   - What does a derivative tell you?
   - What is a gradient in ML terms?
   - Why do we "follow the gradient" when training models?
   - How does gradient descent help models learn?

   ### Key Concepts to Master

   **Derivative = Rate of Change**
   - How fast is y changing as x changes?
   - Slope of the tangent line

   **Gradient = Direction of Steepest Ascent**
   - In ML: direction that increases loss most
   - Gradient descent: go opposite direction (downhill)

   **Why It Matters:**
   - Neural networks learn by following gradients
   - Backpropagation computes gradients
   - Learning rate controls how big steps we take

   ### End of Day1 Checklist

   - [ ] Watched both 3Blue1Brown videos
   - [ ] Read ML Mastery article
   - [ ] Drew curves and tangent lines on paper
   - [ ] Wrote notes answering reflection questions
   - [ ] Understand derivatives conceptually (not calculations)
   - [ ] Can explain "gradient descent" in simple terms
   - [ ] Spent approximately 60 minutes

   ---

   ## Day 2: Gradient Descent Deep Dive

   ### Primary Video Resources

   **Video 1: StatQuest "Gradient Descent, Step-by-Step"**
   - Link: https://www.youtube.com/watch?v=sDv4f4s2SB8
   - Duration: 21:59
   - **WATCH THIS COMPLETELY** - best gradient descent explanation

   **Video 2: 3Blue1Brown "Gradient descent, how neural networks learn"**
   - Link: https://www.youtube.com/watch?v=IHZwWFHWa-w
   - Duration: 21:01
   - From Neural Networks series, Chapter 2
   - Visual, intuitive explanation

   **Video 3 (Optional): "Stochastic vs Batch Gradient Descent"**
   - Link: https://www.youtube.com/watch?v=TW7W1M-H-YM
   - Duration: 8:54
   - If you have extra time

   ### Reading Materials

   **Article: "Gradient Descent For Machine Learning"**
   - Link: https://machinelearningmastery.com/gradient-descent-for-machine-learning/
   - Duration: 15 min read
   - Comprehensive explanation with examples

   **Interactive: Gradient Descent Visualization**
   - Link: https://www.benfrederickson.com/numerical-optimization/
   - Play with learning rate slider
   - See how different rates affect convergence

   ### Day2's Schedule (60 minutes total)

   **Option A: Watch Both Long Videos (Recommended if you have 90 min)**
   - StatQuest (22 min)
   - 3Blue1Brown (21 min)
   - Quick reflection (10 min)
   - Total: ~50 min of video + 10 min notes

   **Option B: One Video + Article + Interactive (60 min)**
   - StatQuest video (22 min)
   - Read ML Mastery article (15 min)
   - Play with interactive visualization (15 min)
   - Reflection questions (8 min)

   ### Key Concepts to Master

   **Gradient Descent Algorithm:**
   1. Start with random parameters
   2. Calculate loss (how wrong are we?)
   3. Calculate gradient (which direction increases loss?)
   4. Move opposite to gradient (decrease loss)
   5. Repeat until loss stops decreasing

   **Learning Rate:**
   - Too small: slow learning, might never finish
   - Too large: miss minimum, unstable
   - Just right: efficient convergence

   **Local vs Global Minima:**
   - Gradient descent can get stuck in local minima
   - Modern techniques help avoid this (momentum, Adam optimizer)

   **Why It Matters:**
   - This is HOW all neural networks learn
   - LLMs are trained with gradient descent (scaled up massively)
   - Understanding this helps debug training issues

   ### Practice Problems

   **Problem 1: Conceptual**
   You have loss function that's high. Gradient points "east."
   - Which direction should you move parameters? (West - opposite)
   - Why? (To decrease loss)

   **Problem 2: Learning Rate**
   Starting at loss = 100:
   - Learning rate = 0.01: After update, loss = 99
   - Learning rate = 0.1: After update, loss = 90
   - Learning rate = 2.0: After update, loss = 150

   Which learning rate is:
   a) Too small?
   b) Good?
   c) Too large?

   **Problem 3: Plateau**
   Your model trains for 100 epochs:
   - Epochs 1-50: Loss decreases steadily
   - Epochs 51-100: Loss stays at 0.5

   What happened?
   - Reached local minimum? Global minimum?
   - What could you try? (Lower learning rate, different optimizer)

   ### End of Day2 Checklist

   - [ ] Watched StatQuest video (minimum)
   - [ ] Watched 3Blue1Brown video (if time)
   - [ ] Read article OR played with interactive
   - [ ] Worked through practice problems
   - [ ] Can explain gradient descent algorithm
   - [ ] Understand impact of learning rate
   - [ ] Spent approximately 60 minutes

   ---

   ## Day 3: Loss Functions & Optimization

   ### Primary Video Resources

   **Video 1: StatQuest "Cross Entropy"**
   - Link: https://www.youtube.com/watch?v=6ArSys5qHAU
   - Duration: 11:49
   - Critical for classification (fraud detection, LLMs)

   **Video 2: StatQuest "Maximum Likelihood"**
   - Link: https://www.youtube.com/watch?v=XepXtl9YKwc
   - Duration: 12:23
   - Why we use certain loss functions

   **Video 3: "Loss Functions Explained"**
   - Link: https://www.youtube.com/watch?v=QBbC3Cjsnjg
   - Duration: 8:29
   - Quick overview of different losses

   ### Reading Materials

   **Article: "Loss Functions in Machine Learning"**
   - Link: https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/
   - Duration: 15 min read

   **Article: "Understanding Cross-Entropy Loss"**
   - Link: https://towardsdatascience.com/understanding-binary-cross-entropy-log-loss-a-visual-explanation-a3ac6025181a
   - Duration: 10 min read
   - Visual explanation

   ### Day3's Schedule (60 minutes total)

   1. **Watch: StatQuest "Cross Entropy"** (12 min)
      - Most important loss for classification

   2. **Watch: StatQuest "Maximum Likelihood"** (12 min)
      - Understand the theory behind losses

   3. **Read: ML Mastery article** (15 min)
      - Overview of different loss functions

   4. **Practice Problems** (15 min)
      - Calculate simple losses by hand

   5. **Reflection** (6 min)
      - Write: When to use which loss function?

   ### Practice Problems

   **Problem 1: Mean Squared Error (MSE)**
   Predictions: [2, 4, 6]
   Actual values: [3, 5, 5]

   Calculate MSE:
   - Errors: (2-3)², (4-5)², (6-5)² = 1, 1, 1
   - MSE = (1+1+1)/3 = 1.0

   **Problem 2: Binary Cross-Entropy**
   Model predicts fraud probability = 0.8
   Actual: fraud = 1 (yes fraud)

   Which is better?
   a) Prediction = 0.8, Actual = 1
   b) Prediction = 0.3, Actual = 1

   (Answer: a - higher probability for correct class)

   **Problem 3: Use Cases**
   Which loss function for:
   - Predicting transaction amount? (MSE - regression)
   - Predicting fraud yes/no? (Binary cross-entropy - classification)
   - Predicting next word in LLM? (Cross-entropy - multi-class)
   - Predicting customer satisfaction (1-5)? (MSE or ordinal loss)

   ### Key Concepts to Master

   **Loss Function = How Wrong Are We?**
   - Measures difference between prediction and actual
   - Training tries to minimize this

   **Common Loss Functions:**

   **1. Mean Squared Error (MSE)**
   - For regression (predicting numbers)
   - Formula: average of (prediction - actual)²
   - Use: predicting transaction amounts, prices

   **2. Binary Cross-Entropy**
   - For binary classification (yes/no)
   - Penalizes confident wrong predictions heavily
   - Use: fraud detection, spam detection

   **3. Categorical Cross-Entropy**
   - For multi-class classification
   - Use: LLM next token prediction, transaction categorization

   **Why It Matters:**
   - Right loss function = better model
   - LLMs use cross-entropy loss
   - Understanding loss helps interpret training metrics

   ### End of Day3 Checklist

   - [ ] Watched StatQuest videos on cross-entropy and maximum likelihood
   - [ ] Read ML Mastery article
   - [ ] Worked through practice problems
   - [ ] Can explain what loss functions measure
   - [ ] Know when to use MSE vs Cross-Entropy
   - [ ] Calculated simple losses by hand
   - [ ] Spent approximately 60 minutes

   ---

   ## Day 4: REST API Basics

   ### Primary Video Resources

   **Video 1: "What is a REST API?"**
   - Link: https://www.youtube.com/watch?v=lsMQRaeKNDk
   - Duration: 6:04
   - Clear, simple explanation

   **Video 2: "REST API concepts and examples"**
   - Link: https://www.youtube.com/watch?v=7YcW25PHnAA
   - Duration: 8:41
   - Good examples

   **Video 3: "HTTP Status Codes Explained"**
   - Link: https://www.youtube.com/watch?v=wJa5CTIFj7U
   - Duration: 5:52
   - Understand 200, 404, 500, etc.

   ### Reading Materials

   **Article: "What is a REST API?"**
   - Link: https://www.redhat.com/en/topics/api/what-is-a-rest-api
   - Duration: 10 min read

   **Mozilla MDN: HTTP Overview**
   - Link: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
   - Duration: 15 min read
   - More technical but comprehensive

   **JSON Introduction:**
   - Link: https://www.json.org/json-en.html
   - Duration: 5 min
   - Understand JSON structure

   ### Day4's Schedule (60 minutes total)

   1. **Watch: "What is REST API"** (6 min)
      - Get foundation

   2. **Watch: "REST API concepts"** (9 min)
      - See examples

   3. **Watch: "HTTP Status Codes"** (6 min)
      - Know common codes

   4. **Read: Red Hat article** (10 min)
      - Reinforce concepts

   5. **Hands-on: Test APIs** (20 min)
      - Install Postman or use curl
      - Make requests to public APIs

   6. **Reflection** (9 min)
      - Document what you learned

   ### Hands-On Practice

   **Install Postman:**
   - Link: https://www.postman.com/downloads/
   - Or use online version: https://web.postman.com/

   **Test These Public APIs:**

   1. **JSONPlaceholder (fake blog):**
   ```
      GET https://jsonplaceholder.typicode.com/posts
      GET https://jsonplaceholder.typicode.com/posts/1
      POST https://jsonplaceholder.typicode.com/posts
   ```

   2. **CoinDesk (Bitcoin price):**
   ```
      GET https://api.coindesk.com/v1/bpi/currentprice.json
   ```

   3. **Exchange Rate:**
   ```
      GET https://api.exchangerate-api.com/v4/latest/USD
   ```

   **For each API:**
   - What HTTP method? (GET, POST)
   - What's the status code? (200, 404)
   - What's in the response? (JSON format)
   - What headers are sent?

   ### Key Concepts to Master

   **REST API Fundamentals:**

   **HTTP Methods:**
   - GET: Retrieve data (read-only)
   - POST: Create new data
   - PUT: Update existing data
   - DELETE: Remove data

   **Status Codes:**
   - 200: Success
   - 201: Created
   - 400: Bad request (client error)
   - 404: Not found
   - 500: Server error

   **JSON Format:**
   ```json
   {
   "transaction_id": "123",
   "amount": 50.00,
   "merchant": "Starbucks",
   "status": "approved"
   }
   ```

   **Why It Matters:**
   - OpenAI API is a REST API
   - You'll build APIs for your AI models
   - All web services communicate via APIs

   ### Practice Exercises

   **Exercise 1: Design an API**
   Design a REST API for transaction management:
   - What endpoint to get all transactions?
   - What endpoint to get one transaction?
   - What endpoint to create a transaction?
   - What HTTP method for each?

   **Exercise 2: Status Codes**
   What status code for:
   - Successfully retrieved transaction? (200)
   - Transaction not found? (404)
   - Invalid transaction format? (400)
   - Server crashed? (500)
   - Transaction created? (201)

   **Exercise 3: JSON Design**
   Design JSON for a fraud alert:
   ```json
   {
   "alert_id": "...",
   "transaction_id": "...",
   "risk_score": 0.85,
   "reason": "...",
   "timestamp": "..."
   }
   ```

   ### End of Day4 Checklist

   - [ ] Watched all 3 videos
   - [ ] Read Red Hat article
   - [ ] Installed Postman
   - [ ] Made API calls to 3 public APIs
   - [ ] Understand REST API concepts
   - [ ] Know HTTP methods and status codes
   - [ ] Comfortable with JSON format
   - [ ] Spent approximately 60 minutes

   ---

   ## Day 5: Python Requests Library

   ### Primary Video Resources

   **Video: "Python Requests Library Tutorial"**
   - Link: https://www.youtube.com/watch?v=tb8gHvYlCFs
   - Duration: 30:00
   - Comprehensive tutorial covering GET, POST, headers, error handling

   **Video: "Working with APIs in Python"**
   - Link: https://www.youtube.com/watch?v=9NKvVyro4y4
   - Duration: 15:25
   - Practical examples with real APIs

   ### Reading Materials

   **Requests Documentation:**
   - Link: https://requests.readthedocs.io/en/latest/user/quickstart/
   - Duration: 15 min read
   - Official quick start guide

   **Real Python Tutorial:**
   - Link: https://realpython.com/python-requests/
   - Duration: 20 min read
   - Comprehensive with practical examples

   ### Day5's Schedule (60 minutes total)

   1. **Setup** (5 min)
      - Install requests library
      - Install python-dotenv
      - Create new Jupyter notebook

   2. **Watch: Requests tutorial** (30 min)
      - Watch at comfortable speed
      - Take notes on key functions
      - Note examples to try

   3. **Hands-on Practice** (20 min)
      - Complete 5 exercises below
      - Code in Jupyter notebook
      - Test each before moving to next

   4. **Reflection** (5 min)
      - Document what you learned
      - Note any confusions

   ### Hands-On Exercises

  **Exercise 1: Basic GET Request**

### Requirements

-   Make GET request to CoinGecko API:\
    `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd`
-   Parse JSON response
-   Extract Bitcoin price in USD
-   Print formatted message: **"Current Bitcoin Price: \$X,XXX.XX"**

### What to Figure Out

-   Import `requests`
-   Make GET request
-   Parse JSON
-   Navigate dictionaries
-   Format output

### Success Criteria

-   Status 200
-   JSON parsed
-   Correct path
-   No errors
-   Clean output

## Exercise 2: Error Handling

### Requirements

-   Invalid URL test\
    `https://api.coingecko.com/v3/invalid-endpoint`
-   Handle:
    -   Connection errors\
    -   HTTP errors\
    -   JSON errors\
    -   Timeout errors
-   Graceful user-friendly errors

### What to Figure Out

-   try/except
-   `.raise_for_status()`
-   Catch:
    -   HTTPError
    -   ConnectionError
    -   Timeout
    -   RequestException

### Testing

-   Invalid URL → connection error\
-   Missing endpoint → 404\
-   No internet\
-   Timeout test

## Exercise 3: POST Request

### Requirements

POST → `https://jsonplaceholder.typicode.com/posts`

Send:

``` json
{
  "title": "Learning Python APIs",
  "body": "Understanding how to make POST requests",
  "userId": 1
}
```

Expect: - 201 Created\
- Extract ID

## Exercise 4: Query Parameters

GET → `https://api.coinbase.com/v2/exchange-rates?currency=USD`

Goals: - Extract EUR, GBP, JPY - Convert \$100 USD - Format results

## Exercise 5: Reusable API Function

Create: `fetch_api(url, method="GET", timeout=10)`

Must: - Support GET/POST\
- Handle all errors\
- Return JSON or None\
- Never crash

Test with: - CoinGecko\
- Coinbase\
- JSONPlaceholder

## Exercise 6: Payment Monitoring (Bonus)

GET:
`https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true`

Extract: - Price\
- 24h change\
- Volume

Logic: - If \> ±5% → volatility alert\
- Add timestamp

## Checklist

-   GET works\
-   JSON parsed\
-   Error handling\
-   POST works\
-   Query params\
-   Reusable function\
-   Clean code

## Verified APIs (Nov 2025)

-   CoinGecko price\
-   Coinbase rates\
-   JSONPlaceholder POST\
-   CoinGecko extended


   ### Key Concepts to Master

   **HTTP Request Flow:**
   1. Send request to server
   2. Server processes
   3. Server sends response
   4. Parse response
   5. Use data

   **Error Types:**
   - ConnectionError
   - Timeout
   - HTTPError
   - JSONDecodeError
   - KeyError

   **Best Practices:**
   - Check status codes
   - Handle errors
   - Use timeouts
   - Don't hardcode API keys
   - Log errors

   ### Common Issues

   **Connection Error:** Check internet, verify URL

   **JSON Decode Error:** Print raw response, check format

   **Key Error:** Print JSON structure, check key names

   **403/401 Error:** Check authentication requirements

   ### End of Day5 Checklist

   - [ ] Installed requests and python-dotenv
   - [ ] Watched tutorial video
   - [ ] Completed Exercise 1 (Basic GET)
   - [ ] Completed Exercise 2 (Error Handling)
   - [ ] Completed Exercise 3 (POST Request)
   - [ ] Completed Exercise 4 (Query Parameters)
   - [ ] Completed Exercise 5 (Reusable Function)
   - [ ] Jupyter notebook with all 5 exercises
   - [ ] Can make GET and POST requests
   - [ ] Error handling implemented
   - [ ] Spent approximately 60 minutes

   ---

   ## Day 6: FastAPI Basics

   ### Primary Video Resources

   **Video 1: "FastAPI Tutorial for Beginners"**
   - Link: https://www.youtube.com/watch?v=7t2alSnE2-I
   - Duration: 23:00
   - Comprehensive introduction with examples

   **Video 2: "FastAPI - Quick Start"**
   - Link: https://www.youtube.com/watch?v=-ykeT6kk4bk
   - Duration: 15:00
   - Practical walkthrough

   ### Reading Materials

   **FastAPI Official Tutorial:**
   - Link: https://fastapi.tiangolo.com/tutorial/
   - Read these sections (in order):
   1. First Steps
   2. Path Parameters
   3. Query Parameters
   4. Request Body
   5. Query Parameters and String Validations
   - Total reading time: ~45 min
   - Best documentation you'll find for any framework

   **Pydantic Documentation:**
   - Link: https://docs.pydantic.dev/latest/
   - Quick start section only
   - Duration: 10 min
   - Understand validation models

   ### Day6's Schedule (3 hours total)

   **Hour 1:** Setup & Basic Routes (60 min)
   - Install FastAPI and dependencies
   - Create first API with simple endpoints
   - Learn routing basics
   - Test with browser and Swagger UI

   **Hour 2:** Path & Query Parameters (60 min)
   - Add dynamic routes with parameters
   - Implement query parameters
   - Add request body with Pydantic validation
   - Test various parameter combinations

   **Hour 3:** Mini-Project - Transaction API (60 min)
   - Build complete CRUD API for transactions
   - Implement in-memory storage
   - Add validation rules
   - Test all endpoints thoroughly

   ---

   ### HOUR 1: Setup & Basic Routes

   **Cretae directory structure (10 min)**

    week2_fastapi_project/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── main.py              # FastAPI app (START HERE)
    │   ├── models.py            # Pydantic models
    │   ├── database.py          # Database connection (Week 3)
    │   └── routers/             # Organize endpoints (later)
    │       ├── __init__.py
    │       └── transactions.py
    │
    ├── tests/
    │   ├── __init__.py
    │   └── test_api.py          # API tests
    │
    ├── notebooks/               # Optional: for exploration
    │   └── test_endpoints.ipynb

   **Task 1: Installation & Setup (10 min)**

   **Requirements:**
   - Install FastAPI framework
   - Install uvicorn (ASGI server)
   - Install pydantic (validation)
   - Create main.py
   - Verify imports work

   **Success criteria:**
   - No import errors
   - Can create FastAPI app instance
   - Ready to write code

   ---

   **Task 2: Your First Endpoint (15 min)**

   **Requirements:**
   - Path: `/`
   - Method: GET
   - Response: JSON with welcome message
   - Include: API name, version, message

   **What to figure out:**
   - Create FastAPI app
   - Define route decorator
   - Create handler function
   - Return JSON
   - Allowed return types

   **Test:**
   - Run with uvicorn
   - Visit http://localhost:8000
   - Check http://localhost:8000/docs

   **Success:**
   - Server runs without errors
   - Endpoint accessible
   - Valid JSON returned
   - Swagger docs accessible

   ---

   **Task 3: Additional Simple Endpoints (15 min)**

   **Requirements:**

   **Health Check:**
   - Path: `/health`
   - Return: status message

   **Current Time:**
   - Path: `/time`
   - Return: ISO 8601 timestamp

   **API Info:**
   - Path: `/info`
   - Return: name, version, description, endpoints

   **What to figure out:**
   - Multiple route decorators
   - DateTime handling
   - JSON structure
   - Endpoint organization

   ---

   **Task 4: Understanding Swagger UI (10 min)**

   **Explore:**
   - Visit `/docs`
   - Expand endpoints
   - "Try it out"
   - Execute requests
   - See request/response details

   **Understand:**
   - What is Swagger/OpenAPI?
   - Why auto-documentation?
   - How FastAPI generates it?
   - What info is shown?

   ---

   **Task 5: Testing & Reflection (10 min)**

   **Test:**
   - All endpoints in browser
   - All in Swagger UI
   - Verify JSON format
   - Multiple requests

   **Reflection:**
   - How does routing work?
   - What are decorators?
   - What types can return?
   - Why is Swagger useful?

   ---

   ### HOUR 2: Parameters & Validation

   **Task 1: Path Parameters (20 min)**

   **Requirements:**

   **User Endpoint:**
   - Path: `/user/{user_id}`
   - Extract user_id
   - Return: user info (fake data)

   **Transaction Endpoint:**
   - Path: `/transaction/{transaction_id}`
   - Extract transaction_id
   - Return: transaction details

   **Category Endpoint:**
   - Path: `/category/{category_name}/transactions`
   - Extract category_name
   - Return: transactions list

   **Validation:**
   - user_id: integer
   - transaction_id: string
   - category_name: lowercase

   **Test:**
   - `/user/123`
   - `/user/abc` (should fail)
   - `/transaction/txn_001`
   - `/category/food/transactions`

   ---

   **Task 2: Query Parameters (15 min)**

   **Requirements:**

   **Search Endpoint:**
   - Path: `/transactions`
   - Query params:
   - min_amount (optional, float)
   - max_amount (optional, float)
   - category (optional, string)
   - merchant (optional, string)
   - limit (optional, int, default=10)

   **Behavior:**
   - No params: all transactions
   - min_amount: filter >=
   - max_amount: filter <=
   - Multiple filters: AND logic

   **What to figure out:**
   - Define query parameters
   - Make optional
   - Set defaults
   - Combine filters
   - Validate types

   **Test scenarios:**
   - `/transactions`
   - `/transactions?min_amount=50`
   - `/transactions?category=food&max_amount=100`
   - `/transactions?limit=5`
   - `/transactions?min_amount=abc` (should error)

   ---

   **Task 3: Request Body with Pydantic (25 min)**

   **Requirements:**

   **Create Transaction:**
   - Path: `/transaction`
   - Method: POST
   - Accept JSON body
   - Validate with Pydantic
   - Return with generated ID

   **Pydantic Model Fields:**
   - amount: float, required, > 0
   - merchant: string, required, 1-100 chars
   - category: string, optional, from allowed list
   - notes: string, optional, max 500 chars
   - date: datetime, optional, default now

   **Allowed categories:**
   food, transport, entertainment, shopping, bills, utilities, healthcare, other

   **Validation rules:**
   - Amount > 0, max 2 decimals
   - Merchant not empty/whitespace
   - Category case-insensitive, in list
   - Notes max 500 chars

   **What to figure out:**
   - Create Pydantic BaseModel
   - Use Field validators
   - Required vs optional
   - Default values
   - Use in endpoint
   - Generate UUID
   - Return 201 status

   **Test cases:**
   1. Valid transaction
   2. Negative amount (fail)
   3. Empty merchant (fail)
   4. Invalid category (fail)
   5. Missing required (fail)
   6. Valid without optionals

   ---

   ### HOUR 3: Transaction API Mini-Project

   **Project Overview:**
   Build complete in-memory transaction API

   **Data Storage:**
   - Python list for transactions
   - Each transaction as dictionary
   - Data lost on restart (OK for now)

   ---

   **Task 1: Create Transaction (15 min)**

   **POST /transactions**

   **Requirements:**
   - Accept transaction data
   - Validate with Pydantic
   - Generate UUID
   - Add timestamp
   - Store in list
   - Return with 201

   **Additional:**
   - Check duplicates (same merchant/amount within 5 sec)
   - Return 409 if duplicate

   **Handle:**
   - Empty body
   - Invalid JSON
   - Missing fields
   - Invalid types
   - Duplicates

   ---

   **Task 2: Get All Transactions (15 min)**

   **GET /transactions**

   **Requirements:**
   - Return all transactions
   - Support filters:
   - category (exact)
   - merchant (partial, case-insensitive)
   - min_amount, max_amount
   - date_from, date_to
   - All optional
   - Combine with AND

   **Response:**
   ```json
   {
   "count": 5,
   "transactions": [...]
   }
   ```

   **Handle:**
   - Empty database
   - No matches
   - Invalid filters

   ---

   **Task 3: Get Single Transaction (10 min)**

   **GET /transactions/{id}**

   **Requirements:**
   - Accept ID as path param
   - Search in list
   - Return if found
   - 404 if not found

   **What to figure out:**
   - Search list
   - Return 404
   - Error response format

   **Test:**
   - Valid ID
   - Non-existent ID
   - Invalid format

   ---

   **Task 4: Statistics (15 min)**

   **GET /stats**

   **Requirements:**

   Calculate:
   - Total transactions
   - Total amount
   - Average amount
   - Min/max amounts
   - Count by category
   - Top 5 merchants

   **Response:**
   ```json
   {
   "total_transactions": 10,
   "total_amount": 1234.56,
   "average_amount": 123.46,
   "min_amount": 5.00,
   "max_amount": 500.00,
   "by_category": {...},
   "top_merchants": [...]
   }
   ```

   **What to figure out:**
   - Calculate statistics
   - Group by category
   - Count occurrences
   - Sort and limit
   - Handle empty database

   ---

   **Task 5: Delete Transaction (5 min)**

   **DELETE /transactions/{id}**

   **Requirements:**
   - Accept ID
   - Find and remove
   - Return confirmation
   - 404 if not found

   **Response:**
   ```json
   {
   "message": "Transaction deleted",
   "transaction_id": "..."
   }
   ```

   ---

   **Testing Complete API (10 min)**

   **Workflow:**
   1. GET all (empty)
   2. CREATE 5 transactions
   3. GET all (5 returned)
   4. Filter by category
   5. GET statistics
   6. GET one by ID
   7. DELETE one
   8. GET all (4 returned)
   9. Try GET deleted (404)

   **Test with:**
   - Swagger UI (`/docs`)
   - Postman
   - curl
   - Python requests

   ### Day6 Deliverables

   **Working API:**
   - [ ] POST /transactions
   - [ ] GET /transactions
   - [ ] GET /transactions/{id}
   - [ ] GET /stats
   - [ ] DELETE /transactions/{id}

   **Understanding:**
   - [ ] FastAPI routing
   - [ ] Path vs query params
   - [ ] Pydantic validation
   - [ ] Request/response
   - [ ] Status codes
   - [ ] In-memory storage
   - [ ] Swagger UI

   **Code Quality:**
   - [ ] Clean function names
   - [ ] Proper validation
   - [ ] Error handling
   - [ ] Organized structure
   - [ ] No crashes

   ### Common Issues & Solutions

   **Issue: "Uvicorn not found"**
   - Solution: `pip install uvicorn[standard]`

   **Issue: "Pydantic validation not working"**
   - Solution: Check BaseModel usage, verify field types

   **Issue: "404 on valid endpoint"**
   - Solution: Check route path, typos, slashes

   **Issue: "Can't find transaction in list"**
   - Solution: Print list, check ID comparison

   **Issue: "Statistics calculations wrong"**
   - Solution: Print intermediate values, test small dataset

   ---

   ## Day 7: Polish Transaction API

   ### Day7's Schedule (3 hours total)

   **Hour 1:** Error Handling & Validation (60 min)
   **Hour 2:** Enhanced Features (60 min)
   **Hour 3:** Documentation, Testing & GitHub (60 min)

   ---

   ### HOUR 1: Error Handling & Validation

   **Task 1: Comprehensive Error Handling (20 min)**

   **Requirements:**

   **1. Transaction Not Found (404)**
   - GET/transactions/{id} for non-existent
   - Return 404 status
   - JSON: `{"detail": "Transaction not found"}`
   - Test with random UUID

   **2. Invalid Transaction Data (400)**
   - Amount = 0 or negative
   - Amount > $10,000 (flag suspicious)
   - Merchant empty/whitespace
   - Merchant > 100 chars
   - Return 400 with clear message
   - Test: amount = -50

   **3. Invalid Query Parameters (422)**
   - min_amount > max_amount
   - Both non-negative
   - Valid numbers not text
   - Return 422 with details
   - Test: min=100, max=50

   **4. Duplicate Prevention (409)**
   - Check same merchant/amount/time (5 sec)
   - Return 409 Conflict
   - Suggest: "Possible duplicate"

   **5. Empty Results**
   - GET /transactions returns []
   - Status 200 (not error)
   - Include metadata: `{"count": 0, "transactions": []}`

   ---

   **Task 2: Enhanced Validation (20 min)**

   **Requirements:**

   **Category Validation:**
   - Allowed: food, transport, entertainment, shopping, bills, utilities, healthcare, other
   - Reject others
   - Case-insensitive (convert lowercase)
   - Default "other" if not provided

   **Merchant Cleaning:**
   - Strip whitespace
   - Capitalize first letter each word
   - Example: "  starbucks  " → "Starbucks"
   - Reject if empty result

   **Amount Validation:**
   - Must be positive
   - Max 2 decimals
   - Auto-round if more
   - Example: 50.12345 → 50.12

   **ID Validation:**
   - Must be valid UUID
   - Reject if not
   - Error: "Invalid transaction ID format"

   ---

   **Task 3: Test Error Cases (20 min)**

   **Test scenarios:**
   1. amount = -100
   2. merchant = ""
   3. category = "xyz"
   4. invalid UUID
   5. non-existent UUID
   6. min=500, max=100
   7. delete non-existent
   8. create duplicate

   **Document:** Error code and message for each

   ---

   ### HOUR 2: Enhanced Features

   **Task 1: Timestamps (15 min)**

   **Requirements:**
   - Every transaction gets `created_at`
   - Format: ISO 8601 "2025-11-30T14:30:00Z"
   - Auto-generated (user can't set)
   - UTC timezone
   - Include in responses

   **Test:**
   - Create transaction
   - Verify timestamp exists
   - Check current time
   - Verify ISO 8601 format

   ---

   **Task 2: Sorting (15 min)**

   **Requirements:**

   **GET /transactions with sorting:**
   - `?sort_by=amount` - by amount
   - `?sort_by=created_at` - by timestamp
   - `?sort_by=merchant` - alphabetically
   - `?order=asc` - ascending (default)
   - `?order=desc` - descending

   **Examples:**
   - `?sort_by=amount&order=desc` - highest first
   - `?sort_by=created_at&order=asc` - oldest first

   **Validation:**
   - Reject invalid sort_by
   - Reject invalid order
   - Return 400

   **Test:**
   - Create 5 different amounts
   - Sort ascending
   - Sort descending
   - Verify order

   ---

   **Task 3: Pagination (15 min)**

   **Requirements:**

   **GET /transactions with pagination:**
   - `?page=1` - page number (starts 1)
   - `?page_size=10` - items per page (default 10, max 100)

   **Response:**
   ```json
   {
   "page": 1,
   "page_size": 10,
   "total_count": 45,
   "total_pages": 5,
   "transactions": [...]
   }
   ```

   **Logic:**
   - total_pages = ceil(total_count / page_size)
   - Return only requested page items
   - If page > total_pages: empty array
   - Validate: page >= 1, page_size 1-100

   **Test:**
   - Create 25 transactions
   - Get page 1, size 10 (returns 10)
   - Get page 3, size 10 (returns 5)
   - Get page 10, size 10 (returns empty)

   ---

   **Task 4: Enhanced Statistics (15 min)**

   **Requirements:**

   **GET /stats returns:**

   **Basic:**
   - Total transactions
   - Sum of amounts
   - Average (2 decimals)
   - Min/max amounts

   **By Category:**
   For each category:
   - Count
   - Total amount
   - Average amount
   - Percentage of total

   **Merchants:**
   - Top 5 by count
   - Top 5 by amount
   - Each: name, count, total

   **Time:**
   - First transaction timestamp
   - Last transaction timestamp
   - Count today
   - Count this week

   **Response Structure:**
   ```json
   {
   "summary": {...},
   "by_category": {...},
   "top_merchants": {...},
   "time_range": {...}
   }
   ```

   **Test:**
   - Create transactions across categories
   - Verify calculations
   - Check percentages sum to 100%

   ---

   ### HOUR 3: Documentation, Testing & GitHub

   **Task 1: Create README.md (25 min)**

   **Requirements:**

   **Section 1: Overview**
   - Project name, description
   - Purpose
   - Key features
   - Technologies

   **Section 2: Installation**
   - Prerequisites
   - Installation commands
   - Run instructions
   - Access documentation

   **Section 3: API Endpoints**

   For EACH endpoint document:
   - HTTP Method & Path
   - Description
   - Path Parameters
   - Query Parameters
   - Request Body
   - Response Format
   - Error Codes

   **Document:**
   1. POST /transactions
   2. GET /transactions
   3. GET /transactions/{id}
   4. GET /stats
   5. DELETE /transactions/{id}

   **Section 4: Example Usage**

   Complete workflow:
   1. Create transaction
   2. Get all
   3. Filter by category
   4. Get statistics
   5. Delete transaction

   **Section 5: Data Models**

   Transaction model:
   - Field names
   - Data types
   - Validation rules
   - Required vs optional

   **Section 6: Error Handling**

   Error code table:
   | Code | Meaning | Scenario |
   |------|---------|----------|
   | 200 | Success | GET returns data |
   | 201 | Created | POST succeeds |
   | 400 | Bad Request | Invalid data |
   | 404 | Not Found | Transaction doesn't exist |
   | 409 | Conflict | Duplicate transaction |
   | 422 | Validation Error | Pydantic validation fails |

   **Section 7: Future Enhancements**

   List potential improvements:
   - Database integration (PostgreSQL)
   - User authentication
   - Rate limiting
   - Caching
   - Export to CSV/Excel
   - Notification system
   - Fraud detection scoring

   ---

   **Task 2: Complete Testing (20 min)**

   **Testing Checklist:**

   **Happy Path:**
   - [ ] Create valid transaction
   - [ ] Get all transactions
   - [ ] Get specific transaction
   - [ ] Get statistics
   - [ ] Delete transaction
   - [ ] Filter by category
   - [ ] Sort by amount
   - [ ] Paginate results

   **Edge Cases:**
   - [ ] Minimum valid amount
   - [ ] Maximum valid amount
   - [ ] Empty database
   - [ ] Page beyond total
   - [ ] Invalid sort field
   - [ ] No transactions stats

   **Error Handling:**
   - [ ] Negative amount → 400
   - [ ] Empty merchant → 400
   - [ ] Invalid category → 400
   - [ ] Invalid UUID → 400
   - [ ] Non-existent UUID → 404
   - [ ] Delete non-existent → 404
   - [ ] min > max → 422
   - [ ] Duplicate → 409

   **Document test results:**
   - Create table or list
   - For each: PASS/FAIL
   - If FAIL: note issue and fix

   ---

   **Task 3: GitHub Repository (15 min)**

   **Repository Structure:**
   ```
   transaction-api/
   ├── README.md
   ├── requirements.txt
   ├── .gitignore
   ├── main.py
   └── tests/ (optional)
   ```

   **requirements.txt:**
   ```
   fastapi
   uvicorn
   pydantic
   python-dotenv
   ```

   **.gitignore:**
   ```
   __pycache__/
   *.pyc
   .env
   venv/
   .DS_Store
   ```

   **Commit Messages:**
   - "Initial FastAPI setup with basic endpoints"
   - "Add transaction filtering and sorting"
   - "Fix validation for negative amounts"
   - "Add comprehensive README with examples"
   - "Week 2 complete - Transaction Stats API v1.0"

   ---

   ### Day7 Deliverables

   **Code Quality:**
   - [ ] All endpoints working
   - [ ] Comprehensive error handling
   - [ ] Input validation
   - [ ] Clean code structure
   - [ ] Meaningful names

   **Features:**
   - [ ] CRUD operations
   - [ ] Filtering
   - [ ] Sorting
   - [ ] Pagination
   - [ ] Enhanced statistics
   - [ ] Timestamps
   - [ ] Duplicate detection

   **Documentation:**
   - [ ] Complete README.md
   - [ ] All endpoints documented
   - [ ] Example usage
   - [ ] Error codes explained
   - [ ] Setup instructions

   **Testing:**
   - [ ] All paths tested
   - [ ] Edge cases tested
   - [ ] Errors tested
   - [ ] Results documented

   **GitHub:**
   - [ ] Code committed
   - [ ] README visible
   - [ ] .gitignore configured
   - [ ] requirements.txt complete

   **Reflection:**
   Create LEARNING.md and answer:
   1. What did you learn this week?
   2. What was hardest?
   3. What would you do differently?
   4. How does this connect to LLMs?
   5. Ready for Week 3?

   ---

## Week 2 Summary

### What You've Completed

**Math Foundations:**
- ✅ Derivatives, gradients, gradient descent
- ✅ Loss functions and optimization
- ✅ Conceptual understanding of how models learn

**API Skills:**
- ✅ REST API design principles
- ✅ Python requests library
- ✅ FastAPI framework
- ✅ Pydantic validation
- ✅ Error handling in APIs
- ✅ API documentation

**Practical Projects:**
- ✅ 5 exercises with requests library
- ✅ Complete Transaction Statistics API
- ✅ CRUD operations implementation
- ✅ Production-ready code

**Total Time:** ~11 hours
- Weekdays: 5 hours (1h/day)
- Weekend: 6 hours (3h Sat, 3h Sun)

**Outcome:** Production-quality API, ready for Week 3 (LLMs)

---

## Additional Resources

### Tools

**Postman:**
- Link: https://www.postman.com/downloads/
- For testing APIs

**Public APIs for Practice:**
- Link: https://github.com/public-apis/public-apis
- Collection of free APIs

### Supplementary Learning

**FastAPI Full Course:**
- Link: https://fastapi.tiangolo.com/tutorial/
- Comprehensive documentation

**StatQuest Playlists:**
- Gradient Descent and Neural Networks
- Machine Learning Fundamentals

**3Blue1Brown Neural Networks:**
- Link: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
- Visual explanations

---

## Success Metrics

### By End of Week 2

You should be able to:

- ✅ Explain how neural networks learn (gradient descent)
- ✅ Choose appropriate loss functions
- ✅ Build REST APIs with FastAPI
- ✅ Make API calls with Python requests
- ✅ Implement Pydantic validation
- ✅ Handle errors gracefully
- ✅ Document APIs professionally
- ✅ Test APIs thoroughly

### You do NOT need to:

- ❌ Derive gradient descent mathematically
- ❌ Build production database integration
- ❌ Implement authentication systems
- ❌ Master all HTTP specifications

---

## Looking Ahead: Week 3

### You're Ready Because:

- ✅ Can build APIs (will wrap LLM calls)
- ✅ Understand JSON/HTTP (OpenAI uses these)
- ✅ Know validation (crucial for LLM inputs)
- ✅ Can handle errors (LLM calls can fail)
- ✅ Understand how models learn (gradient descent)

### Week 3 Preview:

- Monday: Andrej Karpathy LLM lecture
- Tuesday: OpenAI API setup
- Wednesday: Tokenization deep dive
- Weekend: Build transaction categorizer with GPT-4

**You've built the foundation. Now we add AI! 🚀**

---

## Tips for Success

### General Advice

1. **Build, Don't Copy**: Type everything yourself
2. **Test Frequently**: Don't write all code then test
3. **Read Errors**: Error messages tell you what's wrong
4. **Use Swagger**: FastAPI's `/docs` is your friend
5. **Commit Often**: Git commit after each working feature

### If You Get Stuck

**Videos too technical:**
- Watch multiple explanations
- StatQuest for intuition, then deeper content
- Pause and take notes

**API not working:**
- Check server is running
- Verify endpoint path (typos!)
- Look at Swagger UI for hints
- Print variables to debug

**Validation failing:**
- Print the data you're sending
- Check Pydantic model carefully
- Read error messages in response

---

## License

This learning plan is for personal educational use.

---

**Last Updated:** November 2025