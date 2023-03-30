import requests
import os
from send_email import send_email

topic = 'tesla'

api_key = os.getenv('NEWSAPIPASSWORD')

url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      'from=2023-02-28&sortBy=publishedAt&apiKey=' \
      f'{api_key}&' \
      'language=en'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


body = 'Subject: Today\'s news' + '\n'

# Access the article titles and description
for article in content['articles'][:20]:
      if article['title'] is not None:
            body = body + article['title'] + '\n' \
                   + article['description'] \
                   + '\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)






