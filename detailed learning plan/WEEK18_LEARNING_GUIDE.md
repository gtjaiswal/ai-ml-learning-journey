# WEEK 18 LEARNING GUIDE: Multimodal Agents + Table Extraction

**Timeline:** March 16-22, 2026  
**Total Time:** ~11-12 hours  
**Focus:** Vision models (GPT-4V, Claude 3.5 Sonnet), financial table extraction, multimodal agents

---

## 📋 WEEK OVERVIEW

**What You'll Build:**
- Vision-enabled agent (GPT-4V/Claude Vision)
- Financial table extraction system
- PDF → CSV pipeline for balance sheets
- Multimodal fraud detection (text + images)
- Chart/graph analysis agent

**What You'll Learn:**
- GPT-4V and Claude 3.5 Sonnet Vision capabilities
- Image preprocessing for LLMs
- Table extraction from PDFs
- OCR vs Vision models
- Structured output from images
- Why vision models for financial documents

**Fintech Application:**
**CRITICAL:** Balance sheets, financial statements, and invoices are in PDFs with tables.
Traditional parsing fails because:
- Tables span multiple pages
- Formatting varies
- Numbers misalign with headers
- OCR gets confused by layouts

**Vision models see images like humans → extract tables accurately → critical for financial analysis.**

**Time Allocation:**
- Mon-Fri: 1-1.5 hours/day (7-7.5h total)
- Weekend: 4-4.5 hours (2-2.5h Sat, 2h Sun)
- Total: 11-12 hours

---

## DAY 1 (MONDAY): Vision Model Fundamentals

**Time:** 1.5 hours

---

### SESSION 1: Understanding Vision Models (45 min)

**Video: "GPT-4V Explained"** - OpenAI  
- URL: https://www.youtube.com/watch?v=outcGtbnMuQ
- Duration: 8:45
- What you'll learn: GPT-4 Vision capabilities

**Video: "Claude 3.5 Sonnet Vision"** - Anthropic  
- URL: https://www.youtube.com/watch?v=vSk6KHLlYRQ
- Duration: 6:30
- What you'll learn: Claude Vision features

**Reading:**
📖 **GPT-4V Technical Report**  
- URL: https://openai.com/research/gpt-4v-system-card
- Duration: 20 min read
- Focus: Capabilities, Limitations, Safety

**What you need to understand:**

**What Vision Models Can Do:**

**1. Describe Images:**
```
Input: Photo of balance sheet
Output: "This is a financial balance sheet showing assets and liabilities. 
         The layout has two columns with monetary values aligned right..."
```

**2. Extract Text (OCR-like):**
```
Input: Invoice image
Output: "Invoice #12345, Date: 2026-03-01, Amount: $1,234.56, 
         Vendor: ABC Corp..."
```

**3. Understand Structure:**
```
Input: Table image
Output: Recognizes rows, columns, headers, data cells
         Can convert to CSV format
```

**4. Analyze Charts:**
```
Input: Bar chart image
Output: "Sales increased from $1M in Q1 to $1.5M in Q2, 
         a 50% growth..."
```

**5. Answer Questions:**
```
Input: Image + "What's the total revenue?"
Output: "The total revenue is $15.2M (sum of all revenue line items)"
```

**What Vision Models Can't Do (Yet):**
- ❌ Perfect OCR on handwriting
- ❌ Very small text (<10pt reliably)
- ❌ Complex mathematical equations
- ❌ Real-time video analysis
- ❌ 3D depth perception

**Key Limitations:**
- Token limits include image tokens
- Images consume ~765 tokens (high detail mode)
- Expensive ($0.01 per image in GPT-4V)
- Slower than text-only
- Some hallucination on ambiguous images

---

### SESSION 2: Vision Model Comparison (45 min)

**Hands-On Exercise: Model Comparison**

**Requirements:**
Create `VISION_MODELS_COMPARISON.md`:

**GPT-4V (OpenAI):**

**Strengths:**
- Excellent at structured data extraction
- Good with tables and forms
- Strong OCR capabilities
- Detailed image descriptions
- Function calling support

**Weaknesses:**
- Expensive ($0.01/image)
- Slower than text-only
- Image size limits (20MB)
- Rate limits

**Best For:**
- Financial documents
- Forms and invoices
- Structured tables
- High-accuracy OCR

**Pricing:**
- $0.01 per image (1024x1024, high detail)
- Plus text tokens ($0.01/1K input, $0.03/1K output)

**Claude 3.5 Sonnet Vision:**

**Strengths:**
- Best-in-class vision understanding
- Better at complex layouts
- More nuanced image analysis
- Larger context window (200K tokens)
- Better reasoning about images

**Weaknesses:**
- Slightly more expensive
- Also slower
- Fewer examples/documentation than GPT-4V

**Best For:**
- Complex documents
- Nuanced analysis
- Long documents (more context)
- Charts and graphs

**Pricing:**
- Similar to GPT-4V
- Check latest Anthropic pricing

**Gemini 1.5 Pro Vision:**

**Strengths:**
- Fastest
- Cheapest
- Long context (1M tokens)
- Good for bulk processing

**Weaknesses:**
- Lower accuracy than GPT-4V/Claude
- Less structured output
- Fewer features

**Best For:**
- High-volume processing
- Cost-sensitive applications
- Speed critical

**Comparison Matrix:**

| Feature | GPT-4V | Claude 3.5 Sonnet | Gemini 1.5 Pro |
|---------|--------|-------------------|----------------|
| OCR Accuracy | ★★★★★ | ★★★★★ | ★★★★☆ |
| Table Extraction | ★★★★★ | ★★★★★ | ★★★★☆ |
| Chart Analysis | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Speed | ★★★☆☆ | ★★★☆☆ | ★★★★★ |
| Cost | ★★★☆☆ | ★★☆☆☆ | ★★★★★ |
| Context Window | 128K | 200K | 1M |

**Recommendation for Fintech:**
- **Financial tables:** GPT-4V or Claude 3.5 Sonnet (accuracy critical)
- **High volume:** Gemini 1.5 Pro
- **Complex analysis:** Claude 3.5 Sonnet
- **Forms/Invoices:** GPT-4V

**What to figure out:**
- Which model for balance sheet extraction?
- When to use which model?
- How to handle model failures?
- Cost optimization strategies?

**Success criteria:**
✅ All 3 models compared  
✅ Strengths/weaknesses documented  
✅ Use cases mapped  
✅ Recommendation made  
✅ Understand trade-offs

---

## DAY 2 (TUESDAY): Image Preprocessing & API Integration

**Time:** 1.5 hours

---

### SESSION 1: Image Preprocessing (45 min)

**Reading:**
📖 **Image Preprocessing for Vision Models**  
- URL: https://platform.openai.com/docs/guides/vision
- Duration: 20 min read
- Focus: Image requirements, Best practices

**What you need to understand:**

**Why Preprocess Images?**

**Problem 1: File Size**
```
Original PDF page: 8MB
→ Too large, slow upload, high cost

Solution: Resize, compress
→ Reduced to 500KB
```

**Problem 2: Resolution**
```
Original: 4000x3000px (12MP)
→ Overkill, wasted tokens

Solution: Resize to 1024x1024
→ Optimal for GPT-4V
```

**Problem 3: Format**
```
PDF pages as images
→ Need to convert to PNG/JPEG

Solution: PDF → Image conversion
→ One image per page
```

**Problem 4: Quality**
```
Blurry, skewed, low contrast
→ Model can't read text

Solution: Enhance, deskew, sharpen
→ Readable text
```

**Preprocessing Pipeline:**

**Step 1: PDF to Images**
```python
# Convert PDF pages to images
# Library: pdf2image, PyMuPDF
# Output: One PNG per page
```

**Step 2: Resize**
```python
# Resize to optimal dimensions
# Target: 1024x1024 or 2048x2048
# Maintain aspect ratio
```

**Step 3: Enhance (if needed)**
```python
# Increase contrast
# Sharpen text
# Remove noise
# Deskew if rotated
```

**Step 4: Compress**
```python
# Optimize file size
# JPEG quality: 85-95%
# PNG optimization
```

**Step 5: Validate**
```python
# Check file size < 20MB
# Check dimensions
# Check format (PNG/JPEG/WebP)
```

---

### SESSION 2: GPT-4V API Integration (45 min)

**Hands-On Exercise: Vision API Client**

**Requirements:**
Build GPT-4V API integration.

**1. Image Upload Methods:**

**Method A: Base64 Encoding**
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Usage
base64_image = encode_image("balance_sheet.png")
```

**Method B: URL (if image hosted)**
```python
image_url = "https://example.com/balance_sheet.png"
```

**2. API Call Structure:**
```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",  # or "gpt-4-turbo" for latest
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Extract all data from this balance sheet table."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}",
                        "detail": "high"  # or "low" for faster/cheaper
                    }
                }
            ]
        }
    ],
    max_tokens=1000
)
```

**3. Detail Levels:**

**Low Detail:**
- Faster, cheaper
- Lower resolution analysis
- Good for: Simple images, rough descriptions

**High Detail:**
- Slower, more expensive
- Higher resolution analysis
- Good for: Tables, detailed text, small fonts

**Auto (default):**
- Model decides based on image size

**4. Response Parsing:**
```python
# Extract text from response
extracted_text = response.choices[0].message.content

# If requesting structured output
# Parse JSON from response
```

**What to figure out:**
- Base64 vs URL for your use case?
- When to use low vs high detail?
- How to handle large PDFs (multiple pages)?
- How to structure prompts for best extraction?
- How to validate extracted data?

**Requirements to Implement:**

**Create `vision_client.py`:**

**Function 1: `preprocess_image(pdf_path, page_num)`**
- Convert PDF page to image
- Resize to optimal dimensions
- Enhance if needed
- Return image path

**Function 2: `encode_image_base64(image_path)`**
- Read image file
- Encode to base64
- Return base64 string

**Function 3: `extract_with_vision(image_path, prompt, detail="high")`**
- Encode image
- Call GPT-4V API
- Parse response
- Return extracted text

**Function 4: `extract_table_from_pdf(pdf_path, page_num, prompt)`**
- Preprocess PDF page
- Extract with vision
- Return structured data

**Error Handling:**
- File not found
- API errors (rate limit, timeout)
- Invalid image format
- Response parsing errors

**Success criteria:**
✅ PDF to image conversion working  
✅ Base64 encoding working  
✅ GPT-4V API calls successful  
✅ Extracted text returned  
✅ Errors handled gracefully  
✅ Can extract from sample PDF

---

## DAY 3 (WEDNESDAY): Financial Table Extraction

**Time:** 1.5 hours

---

### SESSION 1: Table Extraction Challenges (45 min)

**Reading:**
📖 **Why Financial Tables Are Hard**  
- URL: https://arxiv.org/abs/2303.00716 (Table extraction survey paper)
- Duration: 15 min read (Introduction + Challenges section)

**What you need to understand:**

**Challenge 1: Complex Layouts**

**Problem:**
```
Traditional Table:
┌─────────────┬──────────┬──────────┐
│ Account     │ 2025     │ 2024     │
├─────────────┼──────────┼──────────┤
│ Revenue     │ $10.5M   │ $8.2M    │
└─────────────┴──────────┴──────────┘

Easy to parse!

Financial Statement:
Assets
  Current Assets
    Cash                      $500,000
    Accounts Receivable       $300,000
      Less: Allowance          ($15,000)
    Net Accounts Receivable   $285,000
  Total Current Assets        $785,000
  
  Long-term Assets
    ...

Nested, indented, complex hierarchy!
```

**Challenge 2: Spanning Headers**

**Problem:**
```
┌────────────────────────────────────────────┐
│           Financial Position              │
├───────────────┬──────────┬─────────┬──────┤
│               │   2025   │   2024  │Change│
├───────────────┼──────────┼─────────┼──────┤
│ Assets        │          │         │      │
│  Current      │  $100M   │  $80M   │ +25% │

Headers span columns!
Model must understand which column is which.
```

**Challenge 3: Multi-page Tables**

**Problem:**
```
Page 1:
Balance Sheet
Assets...
(continued on next page)

Page 2:
Balance Sheet (continued)
Liabilities...

Model needs context across pages!
```

**Challenge 4: Formatting Variations**

**Problem:**
```
Document A:
Revenue    $10,500,000

Document B:
Revenue    10.5M

Document C:
Revenue    $10.5 million

Same value, different formats!
Model must normalize.
```

**Challenge 5: Alignment Issues**

**Problem:**
```
When PDF is scanned:
Account     Amount
Cash        $5 00,000  ← Space in wrong place
Revenue     $1,234 56  ← Decimal misaligned

OCR gets confused!
Vision models can see alignment.
```

**Why Vision Models Solve This:**

**Vision models:**
- See layout like humans
- Understand visual structure
- Can handle complex formatting
- Work with scanned documents
- No need for perfect OCR

**Traditional parsing:**
- Breaks on complex layouts
- Confused by spanning headers
- Fails on scanned documents
- Requires perfect structure

---

### SESSION 2: Table Extraction Prompts (45 min)

**Hands-On Exercise: Prompt Engineering for Tables**

**Requirements:**
Create `TABLE_EXTRACTION_PROMPTS.md`:

**Prompt 1: Basic Table Extraction**
```
You are a financial data extraction specialist.

Extract ALL data from the balance sheet table in this image.

Output format: CSV with proper headers

Requirements:
1. Preserve exact numbers (don't round)
2. Include currency symbols
3. Maintain account hierarchy (indent with spaces or use parent columns)
4. Handle negative numbers correctly (e.g., -$500 or ($500))
5. Extract ALL rows, even if many

Example output:
Account,Amount_2025,Amount_2024
Assets,,
  Current Assets,,
    Cash,$500000,$450000
    Accounts Receivable,$300000,$275000
Total Current Assets,$800000,$725000
...

Extract the data now:
```

**What this prompt achieves:**
- Clear role definition
- Specific output format
- Handles hierarchy
- Preserves formatting
- Requests completeness

**Prompt 2: Structured JSON Extraction**
```
Extract the balance sheet data from this image as a structured JSON object.

JSON structure:
{
  "document_type": "balance_sheet",
  "date": "2025-12-31",
  "currency": "USD",
  "sections": [
    {
      "section_name": "Assets",
      "subsections": [
        {
          "subsection_name": "Current Assets",
          "line_items": [
            {"account": "Cash", "amount": 500000},
            {"account": "Accounts Receivable", "amount": 300000}
          ],
          "subtotal": 800000
        }
      ],
      "total": 1500000
    }
  ]
}

Extract the data maintaining this exact structure.
Only include data you can clearly read.
If unsure about a value, use null.
```

**What this prompt achieves:**
- Structured output
- Clear schema
- Handles uncertainty
- Nested structure

**Prompt 3: Table with Validation**
```
Extract the balance sheet table and validate the totals.

Process:
1. Extract all line items
2. Calculate subtotals
3. Verify totals match
4. Flag any discrepancies

Output format:
{
  "data": {
    "assets": [...],
    "liabilities": [...],
    "equity": [...]
  },
  "validation": {
    "assets_total_calculated": 1500000,
    "assets_total_stated": 1500000,
    "match": true
  },
  "discrepancies": []
}

If totals don't match, explain why in "discrepancies".
```

**What this prompt achieves:**
- Self-validation
- Error detection
- Explainability
- Quality assurance

**Prompt 4: Multi-Column Comparison**
```
This balance sheet has multiple date columns (2025, 2024).

Extract data for BOTH years and calculate changes.

Output CSV format:
Account,Amount_2025,Amount_2024,Change_Amount,Change_Percent
Cash,$500000,$450000,$50000,11.1%
...

Requirements:
1. Calculate absolute change (2025 - 2024)
2. Calculate percentage change ((2025-2024)/2024 * 100)
3. Use CALCULATOR for all arithmetic (don't calculate yourself)
4. Format percentages with 1 decimal place
5. Handle negative changes correctly

Extract and calculate now:
```

**What this prompt achieves:**
- Multi-column extraction
- Calculated fields
- Forces calculator use (critical!)
- Proper formatting

**What to figure out:**
- Which prompt for which use case?
- How to handle prompt variations?
- How to test prompt quality?
- When to use CSV vs JSON?
- How to enforce calculator usage?

**Success criteria:**
✅ 4 table extraction prompts created  
✅ Each optimized for specific use case  
✅ Output formats clearly defined  
✅ Validation included  
✅ Calculator usage enforced

---

## DAY 4 (THURSDAY): PDF → CSV Pipeline

**Time:** 1.5 hours

---

### SESSION 1: Pipeline Architecture (45 min)

**Hands-On Exercise: Pipeline Design**

**Requirements:**
Create `PDF_TO_CSV_PIPELINE.md`:

**Pipeline Overview:**
```
Input: balance_sheet.pdf (10 pages)
  ↓
Step 1: PDF Page Detection
  → Identify pages with tables
  → Filter out text-only pages
  ↓
Step 2: Page Preprocessing
  → Convert PDF pages to images
  → Enhance quality
  → Resize optimally
  ↓
Step 3: Vision Extraction
  → Send to GPT-4V/Claude
  → Extract table data
  → Parse response
  ↓
Step 4: Data Validation
  → Verify totals
  → Check completeness
  → Flag errors
  ↓
Step 5: Data Merging
  → Combine multi-page tables
  → Resolve duplicates
  → Create unified dataset
  ↓
Step 6: CSV Export
  → Format data
  → Write CSV file
  → Validate CSV structure
  ↓
Output: balance_sheet_data.csv
```

**Step 1: Page Detection**

**Goal:** Identify which PDF pages contain tables.

**Approach A: Heuristic**
```python
def has_table(pdf_page):
    # Check for:
    # - Grid lines
    # - Aligned numbers
    # - Column structure
    # - Table keywords ("Total", "Amount", etc.)
    return True/False
```

**Approach B: Vision Pre-screening**
```python
def has_table_vision(pdf_page):
    # Quick low-detail vision check
    prompt = "Does this page contain a financial table? Yes or No only."
    response = gpt4v_quick(page, prompt)
    return "yes" in response.lower()
```

**Step 2: Preprocessing**

**Requirements:**
```python
def preprocess_page(pdf_path, page_num):
    # 1. Extract page as image
    image = pdf_to_image(pdf_path, page_num)
    
    # 2. Enhance
    image = enhance_contrast(image)
    image = sharpen(image)
    
    # 3. Resize
    image = resize_to_optimal(image, target=1024)
    
    # 4. Save temporary file
    temp_path = save_temp_image(image)
    
    return temp_path
```

**Step 3: Vision Extraction**

**Requirements:**
```python
def extract_table_data(image_path, table_type="balance_sheet"):
    # 1. Select appropriate prompt
    prompt = get_prompt_for_table_type(table_type)
    
    # 2. Call vision model
    response = gpt4v_extract(image_path, prompt, detail="high")
    
    # 3. Parse response (CSV or JSON)
    data = parse_response(response)
    
    # 4. Validate structure
    validate_table_structure(data)
    
    return data
```

**Step 4: Validation**

**Requirements:**
```python
def validate_table_data(data):
    # 1. Check required fields present
    assert "Account" in data.columns
    assert "Amount" in data.columns
    
    # 2. Verify totals (if applicable)
    calculated_total = sum(data["Amount"])
    stated_total = data[data["Account"] == "Total"]["Amount"].values[0]
    assert abs(calculated_total - stated_total) < 0.01
    
    # 3. Check for missing data
    assert data.isnull().sum().sum() == 0
    
    # 4. Validate data types
    assert data["Amount"].dtype in [int, float]
    
    return True
```

**Step 5: Merging**

**Requirements:**
```python
def merge_multi_page_tables(page_data_list):
    # 1. Detect continuation
    # If page N ends with "(continued)" or partial table
    
    # 2. Combine dataframes
    combined = pd.concat(page_data_list, ignore_index=True)
    
    # 3. Remove duplicate headers
    # If header row repeated on each page
    
    # 4. Recalculate totals if needed
    
    return combined
```

**Step 6: CSV Export**

**Requirements:**
```python
def export_to_csv(data, output_path):
    # 1. Format columns
    # Ensure consistent column names
    
    # 2. Format numbers
    # Remove currency symbols if needed
    # Standardize decimal places
    
    # 3. Write CSV
    data.to_csv(output_path, index=False)
    
    # 4. Validate CSV
    # Re-read and verify
    
    return output_path
```

**What to figure out:**
- Which steps can be parallelized?
- How to handle errors at each step?
- How to make pipeline resumable?
- How to optimize for speed vs accuracy?
- How to log progress?

**Success criteria:**
✅ Complete pipeline designed  
✅ All steps defined  
✅ Error handling planned  
✅ Validation included  
✅ Understand data flow

---

### SESSION 2: Pipeline Implementation (45 min)

**Requirements:**
Implement skeleton of PDF → CSV pipeline.

**Create `pdf_to_csv_pipeline.py`:**

**Core Functions:**

**Function 1: `process_pdf(pdf_path, output_csv_path)`**
- Main entry point
- Orchestrates all steps
- Returns success/failure

**Function 2: `detect_table_pages(pdf_path)`**
- Identifies pages with tables
- Returns list of page numbers

**Function 3: `process_page(pdf_path, page_num)`**
- Preprocesses page
- Extracts data
- Returns structured data

**Function 4: `validate_and_merge(page_data_list)`**
- Validates each page's data
- Merges into single dataset
- Returns combined data

**Function 5: `export_csv(data, output_path)`**
- Formats data
- Writes CSV
- Returns file path

**Error Handling:**

**Handle these scenarios:**
- PDF file not found
- Page has no table
- Vision API error
- Extraction fails
- Validation fails
- CSV write fails

**For each:**
- Log error clearly
- Retry if transient (API)
- Skip page if unrecoverable
- Don't crash entire pipeline

**Testing:**

**Test with:**
1. Single-page balance sheet
2. Multi-page balance sheet
3. PDF with no tables (should skip)
4. PDF with mixed pages (text + tables)
5. Low-quality scanned PDF

**What to figure out:**
- How to make pipeline robust?
- How to handle partial failures?
- How to resume from checkpoint?
- How to track progress?
- How to optimize costs?

**Success criteria:**
✅ Pipeline skeleton implemented  
✅ All core functions defined  
✅ Error handling comprehensive  
✅ Tested with sample PDF  
✅ Produces valid CSV output

---

## DAY 5 (FRIDAY): Multimodal Fraud Detection

**Time:** 1 hour

---

### SESSION 1: Image-Based Fraud Detection (30 min)

**Reading:**
📖 **Visual Fraud Detection**  
- URL: https://arxiv.org/abs/2209.09452
- Duration: 15 min read (Abstract, Introduction)

**Hands-On Exercise: Fraud Scenarios**

**Requirements:**
Create `VISUAL_FRAUD_DETECTION.md`:

**Scenario 1: Receipt Verification**

**Use Case:**
Customer claims transaction but receipt looks suspicious.

**What Vision Model Can Detect:**
- Photo editing artifacts
- Inconsistent fonts/formatting
- Misaligned text
- Wrong merchant logos
- Tampered amounts

**Prompt:**
```
Analyze this receipt image for signs of tampering or fraud.

Check for:
1. Font consistency (all text same font?)
2. Alignment (is text properly aligned?)
3. Logos (does logo look authentic?)
4. Amounts (any signs of editing?)
5. Date/time (does it match transaction?)

Output:
{
  "authentic": true/false,
  "confidence": 0-1,
  "red_flags": ["..."],
  "explanation": "..."
}
```

**Scenario 2: Document Verification**

**Use Case:**
ID verification for account opening.

**What Vision Model Can Detect:**
- Photo of a photo (not original ID)
- Photoshopped ID
- Expired documents
- Mismatched information
- Low-quality forgeries

**Prompt:**
```
Verify this ID document is authentic and not tampered.

Check for:
1. Photo quality (is this a photo of a photo?)
2. Text clarity (blurry or sharp?)
3. Holograms/security features visible?
4. Information consistency
5. Signs of digital manipulation

CRITICAL: Do NOT extract PII. Only verify authenticity.

Output:
{
  "appears_authentic": true/false,
  "confidence": 0-1,
  "concerns": ["..."]
}
```

**Scenario 3: Check Verification**

**Use Case:**
Verify check is real, not forged.

**What Vision Model Can Detect:**
- Bank logo authenticity
- MICR line presence
- Signature consistency
- Amount tampering
- Check stock quality

**Scenario 4: Invoice Fraud**

**Use Case:**
Detect fake invoices submitted for payment.

**What Vision Model Can Detect:**
- Inconsistent company branding
- Generic invoice templates (not company-specific)
- Mismatched addresses
- Unusual formatting
- Low-quality logos

**What to figure out:**
- Which fraud types detectable with vision?
- What accuracy can be expected?
- When to escalate to human?
- How to avoid false positives?
- Privacy concerns with image data?

**Success criteria:**
✅ 4 fraud scenarios documented  
✅ Detection capabilities identified  
✅ Prompts created  
✅ Limitations understood  
✅ Privacy considerations noted

---

### SESSION 2: Multimodal Agent Design (30 min)

**Hands-On Exercise: Multimodal Agent Architecture**

**Requirements:**
Create `MULTIMODAL_AGENT_DESIGN.md`:

**Agent: Fraud Investigation Agent**

**Capabilities:**
- Analyze transaction data (text)
- Verify receipts (vision)
- Check documents (vision)
- Cross-reference information
- Generate investigation report

**Tools:**

**Text Tools:**
- database_query (get transaction history)
- calculate (risk scoring)
- pattern_matcher (fraud patterns)

**Vision Tools:**
- verify_receipt (image analysis)
- verify_document (ID/check verification)
- extract_invoice_data (table extraction)

**Workflow:**

**Investigation Request:**
```
User: "Investigate transaction TX123 - customer claims receipt is valid"

Agent process:
1. Query transaction: database_query(TX123)
   → Amount: $500, Merchant: ABC Store
   
2. Request receipt image from user
   → User uploads receipt.jpg
   
3. Verify receipt: verify_receipt(receipt.jpg)
   → Authentic: Yes, Amount: $500, Merchant: ABC Store
   
4. Cross-check:
   → Receipt amount matches transaction ✓
   → Receipt merchant matches transaction ✓
   → Receipt date matches transaction date ✓
   
5. Decision: LEGITIMATE
   
6. Generate report with evidence
```

**Agent State:**
```python
class FraudInvestigationState(TypedDict):
    transaction_id: str
    transaction_data: Dict
    receipt_image: Optional[str]
    receipt_analysis: Optional[Dict]
    document_images: List[str]
    document_analyses: List[Dict]
    cross_checks: List[Dict]
    final_decision: Optional[str]
    evidence: List[str]
```

**Decision Logic:**
```python
def make_decision(state):
    # If all cross-checks pass → LEGITIMATE
    # If any major red flag → FRAUDULENT
    # If minor concerns → MANUAL_REVIEW
    # If missing critical evidence → REQUEST_MORE_INFO
```

**What to figure out:**
- When to request images from user?
- How to handle missing images?
- How to weight visual evidence vs data?
- What constitutes "sufficient evidence"?
- How to explain decision to user?

**Success criteria:**
✅ Multimodal agent designed  
✅ Text and vision tools integrated  
✅ Workflow defined  
✅ Decision logic specified  
✅ Understand capabilities and limitations

---

## DAY 6 (SATURDAY): Build Table Extraction System

**Time:** 2.5 hours

---

### SESSION 1: Implement Complete Pipeline (90 min)

**Requirements:**
Build end-to-end balance sheet extraction system.

**System Requirements:**

**Input:** 
- PDF file (balance sheet, 1-10 pages)

**Output:**
- CSV file with extracted data
- Validation report
- Extraction metadata

**Implementation:**

**1. Create `balance_sheet_extractor.py`:**

**Main function:**
```python
def extract_balance_sheet(pdf_path, output_csv_path):
    """
    Extract balance sheet from PDF to CSV.
    
    Returns:
        {
            "success": bool,
            "csv_path": str,
            "pages_processed": int,
            "total_rows": int,
            "validation": {...},
            "errors": [...]
        }
    """
```

**2. Implement all pipeline steps:**

From Day 4 design:
- PDF page detection
- Image preprocessing
- Vision extraction
- Data validation
- Multi-page merging
- CSV export

**3. Add logging:**
```python
import logging

logger = logging.getLogger(__name__)

# Log at each step:
logger.info(f"Processing PDF: {pdf_path}")
logger.info(f"Detected {num_pages} pages with tables")
logger.info(f"Extracting page {page_num}...")
logger.info(f"Validation passed: {validation_result}")
logger.info(f"CSV exported: {output_path}")
```

**4. Add progress tracking:**
```python
from tqdm import tqdm

for page_num in tqdm(table_pages, desc="Extracting pages"):
    # Process page
```

**5. Implement caching:**
```python
import json
from pathlib import Path

def get_cache_path(pdf_path, page_num):
    cache_dir = Path(".cache")
    cache_dir.mkdir(exist_ok=True)
    return cache_dir / f"{Path(pdf_path).stem}_page{page_num}.json"

def extract_with_cache(pdf_path, page_num):
    cache_path = get_cache_path(pdf_path, page_num)
    
    # Check cache
    if cache_path.exists():
        logger.info(f"Using cached data for page {page_num}")
        return json.loads(cache_path.read_text())
    
    # Extract
    data = extract_page(pdf_path, page_num)
    
    # Cache
    cache_path.write_text(json.dumps(data))
    
    return data
```

**Why caching:**
- Vision API calls are slow (~5-10s each)
- Expensive ($0.01 per image)
- Re-running should be instant
- Resume from failures

**Testing:**

**Test Files:**
1. `simple_balance_sheet.pdf` (1 page, clean)
2. `multi_page_balance_sheet.pdf` (3 pages)
3. `scanned_balance_sheet.pdf` (low quality)
4. `complex_balance_sheet.pdf` (nested accounts)

**For Each Test:**
- Run extraction
- Verify CSV created
- Check row count
- Validate totals
- Review any errors

**Success Metrics:**
- Extraction accuracy: >95%
- Processing time: <30s per page
- Validation pass rate: >90%
- Error handling: 100% (no crashes)

**What to figure out:**
- How to optimize for speed?
- How to improve accuracy?
- How to handle edge cases?
- When to use cache vs re-extract?

**Success criteria:**
✅ Complete pipeline implemented  
✅ All test PDFs processed  
✅ CSV outputs validated  
✅ Caching working  
✅ Logging comprehensive  
✅ Error handling robust

---

### SESSION 2: Quality Assurance (60 min)

**Requirements:**
Validate extraction quality and create QA process.

**1. Manual Validation:**

**Process:**
- Take sample balance sheet PDF
- Extract with your system
- Manually verify each row
- Document accuracy

**Accuracy Calculation:**
```
Accuracy = (Correct Rows / Total Rows) × 100

Example:
Total rows: 50
Correct: 48
Wrong: 2

Accuracy: 96%
```

**Error Analysis:**
For each error:
- What was wrong?
- Why did it fail?
- How to fix?

**2. Automated Validation:**

**Create `validate_extraction.py`:**
```python
def validate_extraction(csv_path, ground_truth_path):
    """
    Compare extracted CSV against ground truth.
    
    Returns:
        {
            "accuracy": 0.96,
            "errors": [
                {"row": 15, "expected": "$1,000", "actual": "$1,00"},
                ...
            ]
        }
    """
```

**Validation Checks:**
1. Row count matches
2. Column headers correct
3. Numbers formatted properly
4. Totals calculated correctly
5. No missing data

**3. Quality Metrics:**

**Define acceptable thresholds:**
```
Minimum accuracy: 95%
Maximum errors per page: 2
Validation pass rate: 90%
Processing time: <1 min per page
```

**Track metrics:**
```python
metrics = {
    "total_pages": 10,
    "successful_pages": 9,
    "average_accuracy": 0.97,
    "average_time_per_page": 45.2,
    "total_cost": 0.10,  # $0.01 per image
    "cache_hit_rate": 0.30
}
```

**4. Improvement Iteration:**

**If accuracy < 95%:**
1. Analyze failure cases
2. Improve prompts
3. Adjust preprocessing
4. Try different detail level
5. Re-test

**Common Issues & Fixes:**

**Issue: Numbers misaligned**
- Fix: Use high detail mode
- Fix: Improve image resolution

**Issue: Headers confused**
- Fix: Clearer prompt about headers
- Fix: Explicitly request column names

**Issue: Totals wrong**
- Fix: Add validation step in prompt
- Fix: Use calculator tool for verification

**What to figure out:**
- What accuracy is good enough?
- Which errors are acceptable vs critical?
- How to continuously improve?
- When to use human review?

**Success criteria:**
✅ Manual validation completed  
✅ Accuracy measured  
✅ Automated validation implemented  
✅ Quality metrics tracked  
✅ Improvement plan documented  
✅ System meets quality thresholds

---

## DAY 7 (SUNDAY): Documentation & Week Summary

**Time:** 2 hours

---

### SESSION 1: System Documentation (60 min)

**Requirements:**
Create comprehensive documentation.

**1. USER_GUIDE.md:**

**Purpose:** Help users use the system.

**Contents:**

**Installation:**
```bash
pip install -r requirements.txt
# Requirements: openai, pdf2image, Pillow, pandas
```

**Basic Usage:**
```python
from balance_sheet_extractor import extract_balance_sheet

result = extract_balance_sheet(
    pdf_path="balance_sheet.pdf",
    output_csv_path="output.csv"
)

print(f"Extracted {result['total_rows']} rows")
print(f"Accuracy: {result['validation']['accuracy']}")
```

**Advanced Options:**
```python
result = extract_balance_sheet(
    pdf_path="balance_sheet.pdf",
    output_csv_path="output.csv",
    model="gpt-4-vision-preview",  # or "claude-3-sonnet"
    detail_level="high",            # or "low"
    use_cache=True,
    validate=True
)
```

**2. TECHNICAL_DOCS.md:**

**Purpose:** Help developers understand system.

**Contents:**

**Architecture:**
- Pipeline diagram
- Component descriptions
- Data flow

**API Reference:**
- All functions documented
- Parameters explained
- Return values specified
- Examples provided

**Error Handling:**
- All error types
- Recovery strategies
- Logging approach

**Performance:**
- Benchmarks
- Optimization tips
- Cost analysis

**3. TROUBLESHOOTING.md:**

**Common Issues:**

**Issue 1: "File not found"**
- Check PDF path correct
- Check file permissions
- Check file format (must be PDF)

**Issue 2: "API error"**
- Check API key set
- Check internet connection
- Check rate limits
- Check model availability

**Issue 3: "Poor extraction quality"**
- Try high detail mode
- Check image quality
- Try different preprocessing
- Review prompt

**Issue 4: "Slow performance"**
- Enable caching
- Use low detail for simple images
- Process pages in parallel
- Consider batch processing

**What to figure out:**
- What do users need to know?
- What will developers need?
- What problems will arise?
- How to make docs helpful?

**Success criteria:**
✅ User guide complete  
✅ Technical docs thorough  
✅ Troubleshooting comprehensive  
✅ All functions documented  
✅ Examples provided

---

### SESSION 2: Week 18 Summary (60 min)

**Requirements:**
Create `WEEK18_SUMMARY.md`:

**1. What You Built:**

**Systems:**
- Vision API client (GPT-4V/Claude)
- PDF → CSV extraction pipeline
- Balance sheet extractor
- Multimodal fraud detection agent

**Capabilities:**
- Extract tables from PDFs
- Verify receipts/documents
- Analyze financial statements
- Convert images to structured data

**2. Key Learnings:**

**Technical:**
- Vision model capabilities and limitations
- Image preprocessing techniques
- Prompt engineering for vision tasks
- Table extraction challenges
- Validation strategies
- Pipeline architecture

**Fintech-Specific:**
- Why vision models critical for financial docs
- Balance sheets in PDFs are messy
- Tables != databases
- Visual fraud detection use cases
- Compliance considerations with image data

**3. Challenges & Solutions:**

**Challenge: Complex table layouts**
- Solution: High detail mode + specific prompts

**Challenge: Multi-page tables**
- Solution: Merge strategy with continuation detection

**Challenge: Accuracy validation**
- Solution: Automated validation + manual spot checks

**Challenge: API costs**
- Solution: Caching + selective high-detail usage

**4. Portfolio Preparation:**

**Demo Script:**
Show:
1. Simple balance sheet extraction (quick win)
2. Complex multi-page extraction (capability)
3. Quality validation (rigor)
4. Receipt verification (fraud application)

**Interview Talking Points:**
- "I built a vision-based table extraction system..."
- "Financial data lives in PDFs with messy tables - traditional parsing fails..."
- "Vision models see structure like humans, achieving 97% accuracy..."
- "I optimized with caching, reducing costs 70% on re-runs..."
- "The system extracts balance sheets to CSV for downstream analysis..."

**Metrics to Highlight:**
- 97% extraction accuracy
- <1 min per page
- $0.01 per page cost
- Handles multi-page documents
- Validates totals automatically

**5. Fintech Impact:**

**Why This Matters:**
```
Traditional Approach:
- Manual data entry from PDFs
- Error-prone (typos, misalignments)
- Slow (minutes per page)
- Expensive (human time)

Vision-Based Approach:
- Automated extraction
- 97% accurate
- Fast (<1 min per page)
- Cheap ($0.01 per page)

Impact:
- 50x faster than manual
- 10x cheaper
- Higher accuracy
- Scalable to thousands of documents
```

**Real-World Applications:**
- Loan underwriting (analyze financial statements)
- Due diligence (extract data from many PDFs)
- Compliance reporting (structured data from documents)
- Fraud detection (verify receipts, checks, IDs)

**6. Next Steps:**

**Week 19 Preview:**
- Structured outputs with Pydantic
- Guaranteed JSON responses
- Integration with Java backends
- Type safety across systems

**What to figure out:**
- What's most impressive about what you built?
- How to explain impact clearly?
- What questions might interviewers ask?
- What would you improve given more time?

**Success criteria:**
✅ Week summary comprehensive  
✅ Portfolio materials ready  
✅ Demo script polished  
✅ Interview stories prepared  
✅ Metrics documented  
✅ Fintech impact clear  
✅ Ready for Week 19

---

## 📚 ADDITIONAL RESOURCES

**Vision Models:**
- GPT-4V System Card: https://openai.com/research/gpt-4v-system-card
- Claude 3.5 Sonnet: https://www.anthropic.com/claude/sonnet
- Gemini Vision: https://deepmind.google/technologies/gemini/

**Table Extraction:**
- Table Detection Survey: https://arxiv.org/abs/2303.00716
- Document AI: https://cloud.google.com/document-ai

**Image Processing:**
- Pillow (PIL): https://pillow.readthedocs.io/
- pdf2image: https://github.com/Belval/pdf2image
- OpenCV: https://opencv.org/

---

## ✅ WEEK 18 DELIVERABLES

**Documentation:**
- [ ] VISION_MODELS_COMPARISON.md - Model comparison
- [ ] TABLE_EXTRACTION_PROMPTS.md - Extraction prompts
- [ ] PDF_TO_CSV_PIPELINE.md - Pipeline design
- [ ] VISUAL_FRAUD_DETECTION.md - Fraud scenarios
- [ ] MULTIMODAL_AGENT_DESIGN.md - Agent architecture
- [ ] USER_GUIDE.md - User documentation
- [ ] TECHNICAL_DOCS.md - Developer docs
- [ ] TROUBLESHOOTING.md - Common issues
- [ ] WEEK18_SUMMARY.md - Week summary

**Working System:**
- [ ] Vision API client
- [ ] PDF → CSV pipeline
- [ ] Balance sheet extractor
- [ ] Quality validation system
- [ ] Caching mechanism

**Understanding:**
- [ ] Vision model capabilities
- [ ] Table extraction challenges
- [ ] Prompt engineering for vision
- [ ] Multimodal agent design
- [ ] Quality assurance processes

---

## 🎯 SUCCESS CRITERIA

**By end of Week 18, you should be able to:**

**Conceptual:**
- Explain vision model capabilities
- Understand table extraction challenges
- Know when to use vision vs OCR
- Understand multimodal agents

**Practical:**
- Use GPT-4V/Claude Vision APIs
- Extract tables from PDFs
- Build PDF → CSV pipelines
- Validate extraction quality
- Optimize for cost and speed
- Design multimodal agents

**Portfolio Impact:**
This week adds:
- ✅ Table extraction system (FINTECH CRITICAL)
- ✅ Vision model expertise
- ✅ PDF processing pipeline
- ✅ Multimodal agent capability
- ✅ Real fintech application
- ✅ Measurable business impact

---

**Total Learning Time:** 11-12 hours  
**Fintech Impact:** CRITICAL - Financial data in PDFs, vision extraction essential  
**Next Week:** Structured outputs + Pydantic (type safety for Java integration)

---

**Document Generated:** December 27, 2025  
**For:** Week 18 - Multimodal Agents + Table Extraction  
**Part of:** Phase 2 Cohort (Weeks 15-21)