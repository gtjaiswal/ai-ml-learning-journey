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