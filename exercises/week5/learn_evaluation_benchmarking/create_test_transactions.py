import ollama
import csv
import datetime

# --- Configuration ---
deterministic_options = {"temperature": 0.1, "top_p": 0.95}
balanced_option = {"temperature": 0.5, "top_p": 0.9}
creative_options = {"temperature": 0.9, "top_p": 0.85}

# Use a dictionary to give names to your option sets
options_map = {
    "deterministic": deterministic_options,
    "balanced": balanced_option,
    "creative": creative_options
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

model = "llama3.1:latest"
output_filename = "sampling_results.csv"
runs_per_option = 10

# List to store data for the final report
report_data = []

def extract_verdict(text):
    """
    Simple heuristic to extract a verdict from the response text.
    Looks for common keywords in the first few lines.
    """
    text_upper = text.upper()
    if "SUSPICIOUS" in text_upper[:100]: # Check start of message
        return "SUSPICIOUS"
    elif "LEGITIMATE" in text_upper[:100]:
        return "LEGITIMATE"
    elif "FRAUD" in text_upper[:100]:
        return "FRAUD"
    elif "UNCLEAR" in text_upper[:100]:
        return "UNCLEAR"
    else:
        return "Not Found / Unclear"

# --- Main Execution ---
# Open the CSV file for writing
with open(output_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    header = ["Option_Name", "Run", "Temperature", "Top_P", "Response", "Timestamp"]
    csv_writer.writerow(header)
    
    print(f"Starting experiment... Results will be saved to {output_filename}")

    # Loop through the named options first
    for option_name, option_values in options_map.items():
        print(f"\n--- Testing Option: '{option_name}' for {runs_per_option} runs ---")
        
        # Loop through the runs for each option
        for run in range(1, runs_per_option + 1):
            print(f"  Starting Run: {run}...")
            
            try:
                # Get the response from Ollama
                response = ollama.chat(
                    model=model, 
                    stream=False, 
                    messages=message_payload, 
                    options=option_values
                )
                
                # Extract the content
                assistant_msg = response['message']['content']
                
                # Get current timestamp
                timestamp = datetime.datetime.now().isoformat()
                
                # Analyze for report
                verdict = extract_verdict(assistant_msg)
                length = len(assistant_msg)
                
                # Store for final report
                report_data.append({
                    "Option": option_name,
                    "Temp": option_values["temperature"],
                    "Run": run,
                    "Verdict": verdict,
                    "Length": length
                })

                # Prepare data row for CSV
                data_row = [
                    option_name,
                    run,
                    option_values["temperature"],
                    option_values["top_p"],
                    assistant_msg,
                    timestamp
                ]
                
                # Write the row to the CSV file
                csv_writer.writerow(data_row)
                
                print(f"    -> Success. Verdict: {verdict}")

            except Exception as e:
                print(f"    -> ERROR: An error occurred: {e}")
                error_row = [option_name, run, option_values["temperature"], option_values["top_p"], f"ERROR: {e}", datetime.datetime.now().isoformat()]
                csv_writer.writerow(error_row)
                
                report_data.append({
                    "Option": option_name,
                    "Temp": option_values["temperature"],
                    "Run": run,
                    "Verdict": "ERROR",
                    "Length": 0
                })

print("\n--- Experiment Finished ---")

# --- Print Final Report ---
print("\n" + "="*80)
print(f"{'FINAL REPORT':^80}")
print("="*80)
print(f"{'Option':<15} {'Temp':<6} {'Run':<5} {'Extracted Verdict':<25} {'Response Length'}")
print("-" * 80)

for row in report_data:
    print(f"{row['Option']:<15} {row['Temp']:<6} {row['Run']:<5} {row['Verdict']:<25} {row['Length']} chars")

print("="*80 + "\n")
