import asyncio
import ollama
from pydantic import BaseModel, ValidationError, Field
from typing import Dict, Any

# --- Configuration ---
DEFAULT_MODEL = "llama3.2:3b"
FALLBACK_MODEL = "phi3:mini"
TIMEOUT_SECONDS = 5.0

# --- 1. Response Validation Schema ---
class TransactionCategory(BaseModel):
    category: str = Field(..., description="The main category of the transaction")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score between 0 and 1")
    is_subscription: bool = Field(False, description="Whether this looks like a recurring subscription")

# --- 2. The Robust Async Function ---
async def categorize_transaction(transaction_text: str, model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    """
    Categorizes a transaction using the official ollama library with asyncio for timeouts.
    """
    
    system_prompt = """
    You are a financial classifier. 
    Analyze the transaction and return a JSON object with:
    - category (e.g., Transport, Food, Utilities, Shopping)
    - confidence (0.0 to 1.0)
    - is_subscription (true/false)
    
    Return ONLY valid JSON.
    """

    print(f"🤖 Asking {model} to categorize: '{transaction_text}'...")

    try:
        # --- Timeout Implementation using asyncio.wait_for ---
        # We use the AsyncClient to make the call
        client = ollama.AsyncClient()
        
        response = await asyncio.wait_for(
            client.chat(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Transaction: {transaction_text}"}
                ],
                format="json", # Force JSON mode
                stream=False
            ),
            timeout=TIMEOUT_SECONDS
        )
        
        content = response['message']['content']
        
        # --- Response Validation ---
        validated_data = TransactionCategory.model_validate_json(content)
        print(f"✅ Success: {validated_data.model_dump()}")
        return validated_data.model_dump()

    except asyncio.TimeoutError:
        print(f"⏱️ Timeout! Model {model} took longer than {TIMEOUT_SECONDS}s.")
        return await handle_fallback(transaction_text, "Timeout")
        
    except (ValidationError, KeyError) as e:
        print(f"⚠️ Validation Error: {e}")
        return await handle_fallback(transaction_text, "Validation Failed")
        
    except Exception as e:
        print(f"💥 Unexpected Error: {e}")
        return await handle_fallback(transaction_text, str(e))

# --- 3. Fallback Logic ---
async def handle_fallback(transaction_text: str, original_error: str) -> Dict[str, Any]:
    print("🔄 Attempting fallback strategy...")
    
    if DEFAULT_MODEL != FALLBACK_MODEL:
        try:
            print(f"   -> Trying fallback model: {FALLBACK_MODEL}")
            client = ollama.AsyncClient()
            # Simpler prompt for fallback
            response = await asyncio.wait_for(
                client.chat(
                    model=FALLBACK_MODEL,
                    messages=[{"role": "user", "content": f"Categorize this transaction: {transaction_text}. Return just the category name."}]
                ),
                timeout=3.0
            )
            
            return {
                "category": response['message']['content'].strip(),
                "confidence": 0.5,
                "is_subscription": False,
                "note": "Fallback model used"
            }
        except Exception as e:
            print(f"   -> Fallback failed: {e}")

    return {
        "category": "Uncategorized",
        "confidence": 0.0,
        "is_subscription": False,
        "error_log": original_error
    }

# --- Main Execution ---
async def main():
    # Test 1: Normal
    await categorize_transaction("UBER RIDE $45.00")
    print("-" * 50)
    
    # Test 2: Simulate Timeout (by setting global timeout to near zero temporarily)
    print("🧪 Simulating Timeout...")
    global TIMEOUT_SECONDS
    TIMEOUT_SECONDS = 0.001 
    await categorize_transaction("NETFLIX.COM")

if __name__ == "__main__":
    asyncio.run(main())
