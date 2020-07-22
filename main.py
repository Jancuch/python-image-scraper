import requests
from bs4 import BeautifulSoup
import urllib.request
import os

req = requests

response = req.get('https://www.reddit.com/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text , 'html.parser' )
images = soup.findAll('img' , attrs={"alt":"Post image"})
number = 0 
bnumber =  "{0}.png".format(number)
for image in images:
    number += 1
    download = image['src']
    urllib.request.urlretrieve(download, str(bnumber))
    

    

    