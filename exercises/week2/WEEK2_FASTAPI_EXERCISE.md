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
