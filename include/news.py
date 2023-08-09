import requests
import json

from include.api_key import api_key_news

def get_news(category="general", country="fr", api_key=api_key_news):
    BASE_URL = "https://newsapi.org/v2/top-headlines"

    url = (BASE_URL + "?country=" + country + "&category=" + category + "&apiKey=" + api_key)

    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()

        articles = data['articles']

        i = 5

        articles_info = []

        for article in articles:
            articles_info.append({
                "title": article['title'],
                "description": article['description'],
                "publishedAt": article['publishedAt'],
                "content": article['content']
            })
            i -= 1
            if i == 0:
                break

        return json.dumps(articles_info)
    else:
        return None
