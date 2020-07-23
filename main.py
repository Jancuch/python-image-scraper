import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from datetime import date

today = date.today()
now =   today.strftime("%d.%m.%Y")
now = str(now)
try:
    now = "./data/images/" + now
    os.mkdir(now)
    print("Directory " , now ,  " Created ") 
except FileExistsError:
    print("Directory " , now ,  " already exists")

req = requests
def scrape(link):
    response = req.get(link , headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text , 'html.parser' )
    images = soup.findAll('img' , attrs={"alt":"Post image"})
    number = 0 

    for image in images:
        number += 1
        bnumber =  "{0}/{1}.png".format(now ,number)
        download = image['src']
        urllib.request.urlretrieve(download, str(bnumber))
        
scrape('https://www.reddit.com/r/tf2memes/')
    
    

    

    