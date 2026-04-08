import os
import requests
from dotenv import load_dotenv
import json
from mcp_tool import get_wikipedia_summary

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("GEMINI_API_KEY")

def classify_issue(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""
    Classify this user issue into:
    category: bug / feature / question
    priority: low / medium / high

    Return STRICT JSON:
    {{
      "category": "...",
      "priority": "...",
      "confidence": 0-1
    }}

    Text: {text}
    """

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # 🔍 DEBUG
        print("RAW:", result)

        text_output = result["candidates"][0]["content"]["parts"][0]["text"]

        # bersihkan json
        text_output = text_output.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(text_output)

        # 🔥 MCP TOOL CALL (Wikipedia dengan mapping yang lebih akurat)
        category = parsed.get("category", "bug")

        if category == "bug":
            keyword = "software bug"
        elif category == "feature":
            keyword = "software feature"
        elif category == "question":
            keyword = "technical support"
        else:
            keyword = category

        wiki_info = get_wikipedia_summary(keyword)

        # 🔥 tambahkan ke response
        parsed["additional_info"] = wiki_info

        return parsed

    except Exception as e:
        return {
            "error": "Failed",
            "details": str(e)
        }