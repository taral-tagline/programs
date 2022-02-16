'''
str = "Name,Surname Taral,Patel Chirag,Dobariya"
item = str.split(" ")

#print (type(item))
print (item)

f = open("my_file.txt","w")

for element in item:
   f.write(element + "\n")
'''


'''
str ="ABcDef123gh67JK"
#print(str.lower())
#print(str.upper())
print(str)
sum = 0
alpha = ''
for item in range(len(str)) :
   if ord(str[item]) >= 65 and ord(str[item]) <= 90 or ord(str[item]) >= 97 and ord(str[item]) <= 122 :
     alpha += str[item].swapcase()
   else :
      sum += int(str[item])
print(alpha)
print(sum)
'''


'''
str ="ABcDef123gh67JK"
#print(str.lower())
#print(str.upper())
print(str)
sum = 0
alpha = ''
for item in str :
   if item.isalpha():
     alpha += item.swapcase()
   else :
      sum += int(item)
print(alpha)
print(sum)
'''

s = "03/02/2022"
s=s.split("/")
print(s)
new_s = "-".join(s)
print(new_s)
new_s = new_s.split("-")[-1:]
print(new_s)
print("-".join(new_s))