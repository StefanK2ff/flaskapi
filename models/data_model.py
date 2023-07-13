import csv

def load_data():
    data = []
    with open('./data/persons.csv', 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
    return data

