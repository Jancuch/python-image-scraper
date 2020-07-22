import requests
from bs4 import BeautifulSoup


req = requests

response = req.get('https://www.reddit.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text , 'html.parser')
images = soup.findAll('img')
for image in images:
    print( image['src'])

    