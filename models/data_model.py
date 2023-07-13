import csv


def load_data():
    data = []
    with open('./data/persons.csv', 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            # Convert the 'id' column to integer
            row['ID'] = int(row['ID'])
            data.append(row)
    return data
