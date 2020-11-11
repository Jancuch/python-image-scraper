import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from datetime import date
def prepare_data():
    today = date.today()
    now =   today.strftime("%d.%m.%Y")
    now = str(now)
    number = 0
    try:
        path = "./images/" + now
        os.mkdir(path)
        config = open("./config.txt", "r")
        safe = 0
        for ln in config:
        
            lines = ln.split()
            if lines[0] == "images_count":
            
                safe = 1
    
        if safe == 1:
            config = open("./config.txt", "w")
            config.write("images_count 0")
        print("Directory " , path ,  " Created ") 
    except FileExistsError:
        config = open("./config.txt", "r")
        safe = 0
        for ln in config:
        
            lines = ln.split()
            if lines[0] == "images_count":
                number = lines[1]
            
        print("Directory " , path ,  " already exists")
    return number



def scrape(link , number):
    today = date.today()
    now =   today.strftime("%d.%m.%Y")
    now = str(now)
    req = requests
    response = req.get(link , headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text , 'html.parser' )
    images = soup.findAll('img' , attrs={"alt":"Post image"})
    

    for image in images:
        number += 1
        bnumber =  "{0}/{1}.png".format("./images/" + now ,number)
        download = image['src']
        urllib.request.urlretrieve(download, str(bnumber))
    config = open("./config.txt", "w")
    config.write("images_count " + str(number))

#scrape('https://www.reddit.com/r/dankmemes/', int(number))
    
    

    

    
