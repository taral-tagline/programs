'''
Scrape any Website, then find all anchor tags and Store them in the JSON file where the key is URL and the value is anchor text.
'''
'''
from bs4 import BeautifulSoup
import html5lib
import requests

URL = "https://www.geeksforgeeks.org/data-structures/"
req = requests.get(URL)
print(req.content)

soup = BeautifulSoup(req.content , 'html5lib' )
print(soup.prettify())
'''

#Python program to scrape website
#and save quotes from website
# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# #print(soup.prettify())

# quotes=[] # a list to store quotes

# table = soup.find('div', attrs = {'id':'all_quotes'})
# #print(table)

# for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
# 	quote = {}
# 	quote['url'] = row.a['href']
# 	quote['text'] = row.h5.a.text
# 	#quote['text'] = row.find('a').contents[0]
# 	#quote['text'] = row.a.text
# 	#quote['img'] = row.img['src']
# 	#quote['lines'] = row.img['alt'].split(" #")[0]
# 	#quote['author'] = row.img['alt'].split(" #")[1]
# 	quotes.append(quote)
# 	#print(row.find('a').contents[0])
# #print(quotes)

# filename = 'Anchor_tag_file.csv'
# with open(filename, 'w', newline='') as f:
# 	w = csv.DictWriter(f,['url','text'])
# 	w.writeheader()
# 	for quote in quotes:
# 		w.writerow(quote)


import html5lib
import requests
from bs4 import BeautifulSoup
import json


# URL = "https://www.w3schools.com/python/python_json.asp"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content)
# data=[]
# table = soup.find('div', attrs = {'id':'sidenav'})
# #print(table)

# for row in table.findAll('a'):
#     quote = {}
#     quote['text'] = row.text
#     quote['url'] = row['href']
#     data.append(quote)
	
# #print(data)

# with open('urls.json','w') as f:
# 		json.dump(data , f , indent=1)

URL = "https://www.w3schools.com/python/python_json.asp"
page = requests.get(URL).content
#print(page)
#soup = BeautifulSoup(page.content)
#data=[]
data = page.find('a')
print(data)

# for row in table.findAll('a'):
#     quote = {}
#     quote['text'] = row.text
#     quote['url'] = row['href']
#     data.append(quote)
	
#print(data)