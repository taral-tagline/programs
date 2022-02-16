'''
Fetch all images from this site: http://rizzyhome.com/Images/Full_Img/ and put them into a text file as well as JSON File.
Note:- Put only the image file name in the text file. 
        Full path put into the JSON file.
'''

import re
import requests
from bs4 import BeautifulSoup
import json
import csv


URL = "http://rizzyhome.com/Images/Full_Img/"
#headers = {'user-agent': 'my-app/0.0.1'}
page = requests.get(URL)
#print(page)
soup = BeautifulSoup(page.content,'html.parser')
table = soup.find('pre')
#print(table.prettify())
data = []
#data = page.find('a')
#print(data)

for row in table.findAll('a'):
    #details = {}
    text = row.text
    link = row['href']
    #data.append(details)
    #print(json.dumps(link))
    with open('img_urls.json','a') as f :
      json.dumps(link,f)

    #with open("img_name.txt",'a') as d :
      #d.write(text)
      #d.write('\n')
#print(data)