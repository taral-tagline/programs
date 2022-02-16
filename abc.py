import csv

header = ['name,ok', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF']


with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)