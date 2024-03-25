import json
from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key="INSERT KEY HERE")

# Load the input-output pairs from the JSON file
with open("input_output_pairs.json", "r") as file:
    data = json.load(file)[:10]  # Select only the first 2000 entries

# Prepare the data for fine-tuning
training_data = ""
counter = 0  # Initialize counter
for entry in data:
    if "input" in entry and "output" in entry:  # Check if keys exist
        input_text = entry["input"].split("?")[0]  # Cut off everything after the question mark
        output_text = entry["output"]
        training_data += f"{input_text}\n-> {output_text}\n"  # Corrected arrow here
        counter += 1
        if counter % 1 == 0:  # Print status every 200 lines
            print(f"Processed {counter} lines...")

# Fine-tune the model
response = client.fine_tuning.jobs.create(
    training_file=training_data,
    model="davinci-002",
    hyperparameters={
        "n_epochs": 15,
        "batch_size": 3,
        "learning_rate_multiplier": 0.3
    }
)

# Print the job ID and status
job_id = response.id
print(f'Fine-tuning model with job ID: {job_id}.')
print(f"Training Response: {response}")
print(f"Training Status: {response.status}")
