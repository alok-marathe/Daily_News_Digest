import requests

api_key = "22c84d954a7748e78ae7fd07f814e55c"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-08-28&sortBy=publishedAt&"
       "apiKey=22c84d954a7748e78ae7fd07f814e55c")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
