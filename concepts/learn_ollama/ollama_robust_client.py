import requests
import json
from pydantic import BaseModel, ValidationError, Field
from typing import Optional, Dict, Any
import time

# --- Configuration ---
OLLAMA_API_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "llama3.2:3b"
FALLBACK_MODEL = "phi3:mini" # Or another small model you have
TIMEOUT_SECONDS = 100.0 # Strict timeout

# --- 1. Response Validation Schema ---
class TransactionCategory(BaseModel):
    category: str = Field(..., description="The main category of the transaction")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0 and 1")
    is_subscription: bool = Field(False, description="Whether this looks like a recurring subscription")

# --- 2. The Robust Client Function ---
def categorize_transaction(transaction_text: str, model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    """
    Categorizes a transaction with timeout, validation, and fallback logic.
    """
    
    # Construct the prompt to force JSON output
    system_prompt = """
    You are a financial classifier. 
    Analyze the transaction and return a JSON object with:
    - category (e.g., Transport, Food, Utilities, Shopping)
    - confidence (0.0 to 1.0)
    - is_subscription (true/false)
    
    Return ONLY valid JSON. Do not write explanations.
    """
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Transaction: {transaction_text}"}
        ],
        "stream": False,
        "format": "json" # Ollama specific: forces JSON mode
    }

    print(f"🤖 Asking {model} to categorize: '{transaction_text}'...")
    start_time = time.time()

    try:
        # --- Timeout Implementation ---
        response = requests.post(
            OLLAMA_API_URL, 
            json=payload, 
            timeout=TIMEOUT_SECONDS
        )
        response.raise_for_status()
        
        result_json = response.json()
        content = result_json.get("message", {}).get("content", "")
        
        # --- Response Validation ---
        # Parse the raw string into our Pydantic model
        validated_data = TransactionCategory.model_validate_json(content)
        
        duration = time.time() - start_time
        print(f"✅ Success ({duration:.2f}s): {validated_data.model_dump()}")
        return validated_data.model_dump()

    except requests.Timeout:
        print(f"⏱️ Timeout! Model {model} took longer than {TIMEOUT_SECONDS}s.")
        return handle_fallback(transaction_text, original_error="Timeout")
        
    except (ValidationError, json.JSONDecodeError) as e:
        print(f"⚠️ Validation Error: Model output was not valid JSON or missing fields.\nOutput: {content}")
        return handle_fallback(transaction_text, original_error="Validation Failed")
        
    except requests.RequestException as e:
        print(f"💥 Network/API Error: {e}")
        return handle_fallback(transaction_text, original_error=str(e))

# --- 3. Fallback Logic ---
def handle_fallback(transaction_text: str, original_error: str) -> Dict[str, Any]:
    """
    Decides what to do when the primary attempt fails.
    Could try a different model, or return a safe default.
    """
    print("🔄 Attempting fallback strategy...")
    
    # Strategy A: Try a faster/different model (if not already using it)
    # Note: In a real app, prevent infinite recursion if fallback is same as default
    if DEFAULT_MODEL != FALLBACK_MODEL:
        try:
            print(f"   -> Trying fallback model: {FALLBACK_MODEL}")
            # Simple retry logic (simplified for demo)
            # In production, you'd refactor to avoid code duplication
            payload = {
                "model": FALLBACK_MODEL,
                "messages": [{"role": "user", "content": f"Category for: {transaction_text}. Respond with just the category name."}],
                "stream": False
            }
            resp = requests.post(OLLAMA_API_URL, json=payload)
            if resp.status_code == 200:
                # Fallback might return simple text, not structured JSON
                category = resp.json()["message"]["content"].strip()
                return {
                        "category": category,
                        "confidence": 0.5, # Low confidence for fallback
                        "is_subscription": False,
                        "note": "Fallback model used"
                    }
        except Exception as e:
            print(f"   -> Fallback model also failed: {e}")
    # Strategy B: Return Safe Default
    print("   -> Returning default 'Uncategorized' response.")
    return {
        "category": "Uncategorized",
        "confidence": 0.0,
        "is_subscription": False,
        "error_log": original_error
    }

# --- Test Run ---
if __name__ == "__main__":
    # Test 1: Simple Transaction
    categorize_transaction("UBER RIDE $45.00")
    print("-" * 50)
    
    # Test 2: Ambiguous/Complex (might take longer or confuse model)
    categorize_transaction("AMZN MKTP US*1A2B3C")
    print("-" * 50)
    
    # Test 3: Simulate Timeout (by setting a tiny timeout)
    print("🧪 Simulating Timeout...")
    TIMEOUT_SECONDS = 0.001 # Impossible timeout
    categorize_transaction("NETFLIX.COM")
