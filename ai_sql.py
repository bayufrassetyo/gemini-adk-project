import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_sql(user_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""
    Convert this natural language into SQL query.

    Table name: issues
    Columns: id, title, category, priority

    Only return SQL query, no explanation.

    Input: {user_input}
    """

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    text_output = result["candidates"][0]["content"]["parts"][0]["text"]
    return text_output.strip().replace("```sql", "").replace("```", "")