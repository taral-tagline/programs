'''
Fetch all images from this site: http://rizzyhome.com/Images/Full_Img/ and put them into a text file as well as JSON File.
Note:- Put only the image file name in the text file. 
        Full path put into the JSON file.

class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj))
obj1 = check()
print("Address of class object = ",id(obj1))
'''

import re
from wsgiref import headers
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
#from google.colab import files

original_url = "https://taglineinfotech.com/"
headers = {'user-agent': 'my-app/0.0.1'}

unscraped = deque([original_url])  

scraped = set()  

emails = set()  

while len(unscraped):
    url = unscraped.popleft()  
    scraped.add(url)

    parts = urlsplit(url)
        
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if '/' in parts.path:
      path = url[:url.rfind('/')+1]
    else:
      path = url

    print("Crawling URL %s" % url)
    try:
        response = requests.get(url,headers=headers)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
    emails.update(new_emails) 

    soup = BeautifulSoup(response.text, 'html.parser')

    for anchor in soup.find_all("a"):
      if "href" in anchor.attrs:
        link = anchor.attrs["href"]
      else:
        link = ''

        if link.startswith('/'):
            link = base_url + link
        
        elif not link.startswith('http'):
            link = path + link

        if not link.endswith(".gz"):
          if not link in unscraped and not link in scraped:
              unscraped.append(link)

print(pd.DataFrame(emails, columns=["Email"]))
#df.to_csv('email.csv', index=False)

#files.download("email.csv")