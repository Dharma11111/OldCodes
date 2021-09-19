###################################################################


# from __future__ import print_function
# from PIL import ImageGrab
# import os
# import datetime
# import time

# import win32api, win32con

# from PIL import ImageOps
# from numpy import *

# import keyboard
# from pynput.keyboard import Key, Controller
# keyboard = Controller()

# from more_itertools import locate

# ###################################################################
# from BasicCommands import *
# from ZZZcollectData import *
# from ZZZvariablesDataSDAupgrade import *
# ###################################################################


#Web Scraping
from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

###################################################################
# url1 = 'https://ts2.x1.international.travian.com/karte.php?x=70&y=93'
url2 = 'https://ts2.x1.international.travian.com/statistics/wonderoftheworld'
url3 = 'https://ts2.x1.international.travian.com/logout.php'

#Login Stage
login_url = 'https://ts2.x1.international.travian.com/logout.php'
payload = {
    "name"      : "Teddybro",
    "password"  : "asdzxc",
}

# Start the session
# session = requests.Session()

# Create the payload


# Post the payload to the site to log in
# s = driver.post(url3, data=payload)

# Navigate to the next page and scrape the data
s = driver.get(url2)

soup = BeautifulSoup(s.text, 'html.parser')
# soup.find('img')['src']
body = soup.find("body")    # id_ ="map_details")
title = body.text
###################################################################


# html_text = requests.get(url3).text
# soup = BeautifulSoup(html_text, 'lxml')
# body = soup.find("body")    # id_ ="map_details")
# title = body.text


# print(soup)
# print(jobs)
print(title)



# if __name__ == '__main__':
#     main()



#end

