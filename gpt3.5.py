from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

client.fine_tuning.jobs.create(
  training_file="Average_Daily_Traffic_Counts_20240324.jsonl",
  model="gpt-3.5-turbo-0125"
)
