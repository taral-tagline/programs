import requests
from bs4 import BeautifulSoup
import re


URL = "https://www.flipkart.com/search?q=mi+10+pro&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_8_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_8_5_na_na_na&as-pos=8&as-type=RECENT&suggestionId=mi+10+pro&requestId=d08660aa-236d-4a99-81f5-9d5213370aad&as-backfill=on"
headers = {'user-agent': 'my-app/0.0.1'}
page = requests.get(URL,headers=headers)
#print(page)
soup = BeautifulSoup(page.content,'html5lib')
#print(soup.prettify())
table = soup.find('div',attrs={'class' : '_1YokD2 _3Mn1Gg'})
#name = soup.find_all('div',attrs={'class' : '_4rR01T'})[0].get_text()
#print(name)
#print(table.prettify())
data=[]

for row in table :
    #print(type(row))
    #bs4.element.Tag
    details = {}
    details['mobile name'] = [text.get_text() for text in row.find_all('div',attrs={'class' : '_4rR01T'})]
    #print(mob_name)
    details['rating'] = [text.get_text() for text in row.find_all('div',attrs={'class' : '_3LWZlK'})]
    #print(rating)
    details['total rating'] = [text.get_text() for text in row.find_all('span',attrs={'class' : '_2_R_DZ'})]
    #print(total_rating)
    details['price'] = [text.get_text() for text in row.find_all('div',attrs={'class' : '_30jeq3 _1_WHN1'})]
    #print(price)
    #quote['mobile name'] = row.find_all('div',attrs={'class' : '_4rR01T'})[0].get_text()
    #quote['rating'] = row.find_all('div',attrs={'class' : '_3LWZlK'})[0].get_text()
    #quote['total rating'] = row.find_all('span',attrs={'class' : '_2_R_DZ'})[0].get_text()
    #quote['price'] = row.find_all('div',attrs={'class' : '_30jeq3 _1_WHN1'})[0].get_text()
    if details['mobile name'] == [] :
        pass
    else :
        data.append(details)
print(data)


# for row in table.find_all('div',attrs={'class' : '_4rR01T'}):
#     quote = {}
#     quote['mobile name'] = row.get_text()
#     data.append(quote)
# print(data)

# for row in table.find_all('div',attrs={'class' : '_3LWZlK'}):
#     quote = {}
#     quote['rating'] = row.get_text()
#     data.append(quote)
# print(data)

# for row in table.find_all('span',attrs={'class' : '_2_R_DZ'}):
#     quote = {}
#     quote['total rating'] = row.find('span').contents[0].get_text()
#     data.append(quote)
# print(data)

# for row in table.find_all('div',attrs={'class' : '_30jeq3 _1_WHN1'}):
#     quote = {}
#     quote['price'] = row.get_text()
#     data.append(quote)
# print(data)

#_4rR01T mobile name
#class="_3LWZlK" rating
#class="_30jeq3 _1_WHN1" price