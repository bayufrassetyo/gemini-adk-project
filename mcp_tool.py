import requests

def get_wikipedia_summary(query):
    try:
        query = query.replace(" ", "_")

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

        headers = {
            "User-Agent": "ai-agent/1.0 (your-email@example.com)"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary available")
        else:
            return f"No data found ({response.status_code})"

    except Exception as e:
        return f"Error fetching data: {str(e)}"