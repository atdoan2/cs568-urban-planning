from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

client.files.create(
  file=open("Metra_Ridership.jsonl", "rb"),
  purpose="fine-tune"
)
