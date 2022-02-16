import csv

str = "Name:Surname Taral:Patel Sanket:Dobariya"

li = str.split(" ")
print(li)
for item in li :
        print(item.split(","))
for item in li :
        print(item.split(":"))

with open("file.csv" , "w") as file :
    for item in li :
        writer = csv.writer(file)
        writer.writerow(item.split(","))
with open("file.csv" , "a") as file :
    for item in li :
        writer = csv.writer(file)
        writer.writerow(item.split(":"))