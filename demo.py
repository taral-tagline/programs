'''cars = ["audi","bmw","hundai","honda","toyota","suzuki"]

#print all item
for item in cars:
    print(item)

#print list
print(cars)

#print start with 2 position
print(cars[2::])

#print end with 2 position
print(cars[:2:])

#reverse list
print(cars[::-1])

#append item
cars.append("kia")
print(cars)

#mearge to list
extra = ["lamborghini","rolls royels"]
new_cars = cars + extra
print(new_cars)

#mearge list and tuple
data = ("dodge","nissan")
new_cars.extend(data)
print(new_cars)

#remove item
new_cars.remove("rolls royels")
print(new_cars)

#define new list which car name have A in name
new_list = []
for i in new_cars :
    if "a" in i :
        new_list.append(i)
print(new_list)

#list cmoprihension
[print(x) for x in new_list]

#define new list which car name have u  in name
new_list1 = [ item for item in cars if "u" in item ]
print(new_list1)

#list in upper case
new_list2 = [ item.upper() for item in cars]
print(new_list2)

#list range
new_list3 = [item for item in range(5)]
print(new_list3)

#sort
cars.sort()
print(cars)

cars.append("CHEVROLET")
print(cars)

cars.sort()
print(cars)

cars.sort(key = str.lower)
print(cars)'''

'''#tuple
tup = ("abc","pqr","xyz")
print(tup)
for item in tup:
    print(item)'''

'''
#set
set_data = {"taral","nirav","jigar","mayur"}
for item in set_data :
    print(item)

print("taral" in set_data)
'''


'''
#dictionary
dic = { "id" : 101 , "name" : "taral" , "age" : 23 , "subject" : ["python","java","C Programming"]}
print(dic["subject"])
print(type(dic["subject"]))

#access the item
name = dic.get("name")
print(name)

key_name = dic.keys()
print(key_name)

print(dic) #before change
dic["bg"] = "O+"

print(dic) #After change

if "age" in dic :
    print("age is avilable as a key in dictionary")

dic.update({"age" : 24 })
print(dic)

del dic["subject"][0]
print(dic)

[print(item) for item in dic.values()]
[print(key,item) for key,item in dic.items()]

copy_dic = dict(dic)
print(copy_dic)

'''

'''
def myfun(num):
    if num >= 5 :
        return num
    else :
        print("num less then 5")

no = myfun(4)
print(no)
'''
'''
def demo(*arg):
    print("big number " + arg[1])
demo('1','3','2')
'''

'''
import re

txt = "my name is taral"
x = re.findall("^m.*l$",txt)
print(x)

x = re.split("\s",txt)
print(x)
'''
'''
txt = "hello"

if not type(txt) is int :
    raise TypeError("only integer are allowd")
'''


def demo(n):
    for row in range(0,n):
        for space in range(n,row,-1):
            print(end=" ")
        for column in range(0,row):
            print("*",end=" ")
        print("\r")

    for row in range(n-1,0,-1):
        for space in range(n+1,row,-1):
            print(end=" ")
        for column in range(0,row-1):
            print("*",end=" ")
        print("\r")

n= input("enter the number:- ")
demo(int(n)+1)