import csv

'''
with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Taral', 'last_name': 'Patel'})
    writer.writerow({'first_name': 'Nirav', 'last_name': 'Tandel'})
'''
#print(csv.list_dialects())
#with open('students.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile, dialect='unix')

#with open('names.csv') as csvfile:
#    dialect = csv.Sniffer().sniff(csvfile.read(1024))
#    csvfile.seek(0)
#    reader = csv.reader(csvfile, dialect)

with open('file.csv') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)