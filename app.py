from flask import Flask, jsonify
import csv

print("Main app, Hello")


# loads the data from the CSV file
def load_data(path):
    csv_data = []
    with open(path, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            csv_data.append(row)
    return csv_data


#data = load_data('./data/persons.csv')

#print(data)

# sets up the server
app = Flask(__name__)


@app.route('/api/data', methods=['GET'])
def get_data():
    data = load_data('./data/persons.csv')
    return jsonify(data)


if __name__ == '__main__':
    app.run()
