import requests

api_key = 'd2992057f3b14c4ba469d54a25726661'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2023-02-28&sortBy=publishedAt&apiKey=' \
      'd2992057f3b14c4ba469d54a25726661'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
      print(article['title'])
      print(article['description'])



