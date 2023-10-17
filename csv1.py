import csv

with open('Python Standard Library/data.csv') as file:
    reader = csv.reader(file)
    print(list(reader))
