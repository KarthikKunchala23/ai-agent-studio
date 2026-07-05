import os
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set.")

if OPENAI_API_KEY.strip() != OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY contains leading or trailing whitespace.")

print("✅ OPENAI_API_KEY loaded successfully")