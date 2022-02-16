import csv

with open("my_file.txt") as data :
    red = csv.reader(data , delimiter = ',')
    count = 0
    for row in red :
        if count == 0 :
            print(f'Column name is {", ".join(row)}')
            count+= 1
        else:
            print(f'name is {row[0]} last name is {row[1]}')
            count += 1
