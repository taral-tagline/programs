import re

#txt = "This is 1 String 123 1221 hello"
'''
data = re.findall("[a-j]",txt)
print(data)

#data = re.findall("[T..s]",txt)
#print(data)

data = re.findall("^This",txt)
print(data)

data = re.findall("..3$",txt)
print(data)

data = re.findall("..3$",txt)
print(data)

data = re.findall("T..s|.s",txt)
print(data)

data = re.findall("T.*s",txt)
print(data)

data = re.findall("T*?s",txt)
print(data)

data = re.findall("T.+s",txt)
print(data)

data = re.findall("T..s",txt)
print(data)

data = re.findall(".s",txt)
print(data)

data = re.findall("he.{2}o",txt)
print(data)

data = re.findall("he.{2}o",txt)
print(data)
'''
'''
txt = "This is 1 String 123 1221 hello"
print(re.findall("\AT",txt)) #return a match if the specified character is begining of string
print(re.findall(r"\bThis",txt)) #begining or end of words
print(re.findall(r"hello\b",txt))
print(re.findall(r"\Bng",txt)) #match but not begining or end of word
print(re.findall(r"h\B",txt))
print(re.findall("\d",txt))
print(re.findall("\D",txt))
print(re.findall("\s",txt))
print(re.findall("\S",txt)) 
print(re.findall("\w",txt)) #return only character
print(re.findall("\W",txt)) #return digit and number not character
print(re.findall("hello\Z",txt))
'''

with open('file.csv', "r") as f:
    data = f.read()
    print(data)
    #print(type(data))
    #print(re.sub(",","#",data))
    print(re.findall("^Name",data))
    print(re.findall(r"\W",data))