import requests # pip install requests
from datetime import datetime, timedelta
from urllib.parse import quote

query = input("What type of news are you interested in today? ")
api = "98d34345c5f64a0894d746f91607ba47"

date_from = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
encoded_query = quote(query)
url = f"https://newsapi.org/v2/everything?q={encoded_query}&from={date_from}&sortBy=publishedAt&language=en&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()

# Handle API errors gracefully
if data.get("status") != "ok":
    print("API Error:", data.get("message", "Unknown error"))
    print("Full Response:", data)
    exit()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
