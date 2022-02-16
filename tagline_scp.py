
import re
import requests


URL = "https://taglineinfotech.com/"
headers = {'user-agent': 'my-app/0.0.1'}
page = requests.get(URL,headers=headers).text
email = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", page))
print(email)

#print(page.status_code)
#soup = BeautifulSoup(page.text,'html.parser')
#print(soup.prettify())
#emails = []
#page = soup.find('html')
#print(table)
#print(type(table))
#table_data = page.text
#print(type(table_data))
#new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", soup))
#print(new_emails)
#print(table)

#for row in table.findAll('a'):
    #quote = {}
    #quote['text'] = row.text
    #new_emails = list[re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", row.text)]
    #emails.append(new_emails)
    #quote['url'] = row['href']
    #data.append(quote)
    #print(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com"))
#print(emails)

#with open('urls.json','w') as f:
#		json.dump(data , f , indent=1)