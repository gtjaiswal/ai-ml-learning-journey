import ollama
import csv
import datetime

# --- Helper Function to Extract Verdict ---
def extract_verdict(text):
    """
    Simple heuristic to extract a verdict from the response text.
    Looks for common keywords in the first few lines.
    """
    text_upper = text.upper()
    if "SUSPICIOUS" in text_upper[:100]:
        return "SUSPICIOUS"
    elif "LEGITIMATE" in text_upper[:100]:
        return "LEGITIMATE"
    elif "FRAUD" in text_upper[:100]:
        return "FRAUD"
    elif "UNCLEAR" in text_upper[:100]:
        return "UNCLEAR"
    else:
        return "Not Found / Unclear"

# --- Method 1: Call the Model ---
def generate_response(model_name, messages, options=None):
    print(f"\nModel '{model_name}' is evaluating...")
    """
    Calls the Ollama model with the given messages and options.
    Returns a dictionary containing the response content, timestamp, and metadata.
    """
    try:
        # Get the response from Ollama
        response = ollama.chat(
            model=model_name, 
            stream=False, 
            messages=messages, 
            options=options
        )
        
        # Extract the content
        assistant_msg = response['message']['content']
        print(f"\nResponse from model '{model_name}' is {assistant_msg}")
        timestamp = datetime.datetime.now().isoformat()
        
        return {
            "success": True,
            "response_text": assistant_msg,
            "timestamp": timestamp,
            "verdict": extract_verdict(assistant_msg),
            "length": len(assistant_msg)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
        }

# --- Method 2: Review and Create Evaluation Table ---
def create_evaluation_table(results_data, output_csv=None):
    """
    Takes a list of result dictionaries and prints a formatted report.
    Optionally saves the data to a CSV file.
    """
    # 1. Print to Console
    print("\n" + "="*90)
    print(f"{'FINAL EVALUATION REPORT':^90}")
    print("="*90)
    print(f"{'Option':<15} {'Temp':<6} {'Run':<5} {'Extracted Verdict':<25} {'Response Length'}")
    print("-" * 90)

    for row in results_data:
        # Handle potential error rows gracefully
        if not row.get("success", True):
            print(f"{row.get('Option', 'N/A'):<15} {row.get('Temp', 'N/A'):<6} {row.get('Run', 'N/A'):<5} {'ERROR':<25} 0 chars")
            continue

        print(f"{row['Option']:<15} {row['Temp']:<6} {row['Run']:<5} {row['Verdict']:<25} {row['Length']} chars")

    print("="*90 + "\n")

    # 2. Save to CSV (if filename provided)
    if output_csv:
        try:
            with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                # Header
                header = ["Option_Name", "Run", "Temperature", "Top_P", "Verdict", "Length", "Response", "Timestamp"]
                csv_writer.writerow(header)
                
                for row in results_data:
                    if row.get("success", True):
                        csv_writer.writerow([
                            row['Option'],
                            row['Run'],
                            row['Temp'],
                            row['Top_P'],
                            row['Verdict'],
                            row['Length'],
                            row['Response'],
                            row['timestamp']  # Fixed: Use lowercase 'timestamp' to match generate_response
                        ])
                    else:
                        csv_writer.writerow([
                            row.get('Option'),
                            row.get('Run'),
                            row.get('Temp'),
                            row.get('Top_P'),
                            "ERROR",
                            0,
                            row.get('error'),
                            row.get('timestamp')
                        ])
            print(f"✅ Detailed results saved to {output_csv}")
        except Exception as e:
            print(f"❌ Failed to save CSV: {e}")


def enrich_result(result: dict, option_name: str, option_values: dict, run=1)->dict:
    """
    Enriches the result with metadata and appends it to the results list.
    """
    if result["success"]:
        print(" Done.")
        # Enrich result with metadata for the report
        result["Option"] = option_name
        result["Run"] = run
        result["Temp"] = option_values["temperature"]
        result["Top_P"] = option_values["top_p"]
        result["Verdict"] = result["verdict"]  # Map for table
        result["Length"] = result["length"]  # Map for table
        result["Response"] = result["response_text"]  # Map for CSV
        # Note: 'timestamp' is already in result from generate_response
    else:
        print(f" Failed: {result['error']}")
        result["Option"] = option_name
        result["Run"] = run
        result["Temp"] = option_values["temperature"]
        result["Top_P"] = option_values["top_p"]
    return result


# --- Main Execution Block (Example Usage) ---
if __name__ == "__main__":
    # Configuration

    model = "llama3.1:latest"
    runs_per_option = 1
    
    options_map = {
        "deterministic": {"temperature": 0.1, "top_p": 0.95},
        "balanced": {"temperature": 0.5, "top_p": 0.9},
        "creative": {"temperature": 0.9, "top_p": 0.85}
    }

    message_payload = [
        {
            "role": "user",
            "content": """Analyze this transaction for fraud: 
                      Amount: $7,500
                      Merchant: Electronics Store XYZ  
                      Time: 2:30 AM
                      Location: 500 miles from cardholder home
                      Cardholder pattern: Average $150, mostly groceries.
                      
                      Start your response with a single word verdict: SUSPICIOUS, LEGITIMATE, or UNCLEAR. Then explain."""
        }
    ]

    # Collector for all results
    all_results = []

    print(f"🚀 Starting experiment with model: {model}")

    # Loop through options and runs
    for option_name, option_values in options_map.items():
        print(f"\n--- Testing Option: '{option_name}' ---")
        for run in range(1, runs_per_option + 1):
            print(f"  Running iteration {run}...", end="", flush=True)
            # CALL METHOD 1
            result = generate_response(model_name=model, messages=message_payload, options=option_values)
            # CALL METHOD 2 (Helper)
            all_results.append(
            enrich_result(
                result=result, 
                option_name=option_name, 
                option_values=option_values,
                run=run
            ))
            print(f"all results length : {len(all_results)}")

    # CALL METHOD 2 (Final Report)
    create_evaluation_table(all_results, output_csv="sampling_results.csv")
