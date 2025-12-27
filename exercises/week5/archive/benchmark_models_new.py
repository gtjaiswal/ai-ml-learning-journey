"""**Requirements:**
Create `benchmark_models.py` that:
- Pulls all 3 models via Ollama
- Tests each model on all 20 transactions
- Measures: accuracy, speed, consistency
- Outputs results to CSV

**Models to test:**
1. **llama3.2** (3B params - Meta's latest)
2. **mistral** (7B params - Mistral AI)
3. **phi3** (3.8B params - Microsoft)

**Metrics to capture:**
- **Accuracy**: % matching ground truth
- **Speed**: Average ms per transaction
- **Consistency**: Agreement across repeat runs
- **Output quality**: Follows format?

**What you need to figure out:**
- How to install multiple Ollama models
- How to measure response time accurately
- How to calculate accuracy programmatically
- How to test "consistency" (run same transaction 3 times?)"""

import ollama
import json
import os

import execute_and_evaluate_model

# def enrich_result(result: dict, option_name: str, option_values: dict, run=1)->dict:
#     """
#     Enriches the result with metadata and appends it to the results list.
#     """
#     if result["success"]:
#         print(" Done.")
#         # Enrich result with metadata for the report
#         result["Option"] = option_name
#         result["Run"] = run
#         result["Temp"] = option_values["temperature"]
#         result["Top_P"] = option_values["top_p"]
#         result["Verdict"] = result["category"]  # Map for table
#         result["Reasoning"] = result["reasoning"]  # Map for CSV
#         result["Length"] = result["length"]  # Map for table
#         result["Response"] = result["response_text"]  # Map for CSV
#         # Note: 'timestamp' is already in result from generate_response
#     else:
#         print(f" Failed: {result['error']}")
#         result["Option"] = option_name
#         result["Run"] = run
#         result["Temp"] = option_values["temperature"]
#         result["Top_P"] = option_values["top_p"]
#     return result

# --- 2. Load Payload from JSON ---
json_file_name = "../transactions_feed.json"
if os.path.exists(json_file_name):
    with open(json_file_name, "r") as f:
     sample_transactions = json.dumps(json.load(f), indent=2)

# --- 1. Setup Models ---
models_to_evaluate = ['llama3.2:latest', 'mistral:7b', 'phi3:mini']
print("Checking available models...")
available_models = [mod['model'] for mod in ollama.list()['models']]

system_prompt = "You are a Financial Fraud Investigator. Analyse the transactions submitted and categorize as Legitimate or Suspicious. As output give Category and Reasoning in JSON"
payload=[
    {"role" :"system",
     "content":system_prompt},
    {"role" :"user",
     "content":sample_transactions}
]

options_map = {
    "deterministic": {"temperature": 0.1, "top_p": 0.95},
    # "balanced": {"temperature": 0.5, "top_p": 0.9},
    # "creative": {"temperature": 0.9, "top_p": 0.85}
}
all_results = []

for model in models_to_evaluate:
    if model not in available_models:
        print(f"\nModel '{model}' is missing. Pulling now...")
        response = ollama.pull(model, stream=True)
        for progress in response:
            print(f"  {progress.get('status')}", end='\r')
        print(f"\nFinished pulling {model}")
    else:
        print(f"Model '{model}' is ready.")
        # Loop through options and runs
    for option_name, option_values in options_map.items():
        print(f"\n--- Testing Option: '{option_name}' ---")
        result_dict = execute_and_evaluate_model.generate_response(model_name=model, messages=payload,options=option_values)
        # CALL METHOD 2 (Helper)
        all_results.append(enrich_result(
            result=result_dict,
            option_name=option_name,
            option_values=option_values,
            run=1
        ))
# CALL METHOD 2 (Final Report)
execute_and_evaluate_model.create_evaluation_table(all_results, output_csv="sampling_results.csv")



























# json_file_path = "transactions.json"
#
# if os.path.exists(json_file_path):
#     with open(json_file_path, 'r') as f:
#         transactions = json.load(f)
#
#     print(f"\nSuccessfully loaded {len(transactions)} transactions from {json_file_path}")
#
#     # Print first one to verify
#     print("First transaction sample:")
#     print(json.dumps(transactions[0], indent=2))
# else:
#     print(f"\nError: File {json_file_path} not found!")
#     transactions = []

# --- Next Steps: Loop through models and transactions ---
