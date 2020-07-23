import requests
from bs4 import BeautifulSoup
import urllib.request
import os

req = requests
def scrape(link):
    response = req.get(link , headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text , 'html.parser' )
    images = soup.findAll('img' , attrs={"alt":"Post image"})
    number = 0 

    for image in images:
        number += 1
        bnumber =  "./data/images/{0}.png".format(number)
        download = image['src']
        urllib.request.urlretrieve(download, str(bnumber))
        
scrape('https://www.reddit.com/r/tf2memes/')
    
    

    

    