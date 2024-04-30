# Костян О.В. Студент №1
import csv
import json

# Дані для запису
data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "Los Angeles"},
    {"name": "Peter", "age": 34, "city": "Chicago"}
]

# Шлях до .csv файлу
csv_file_path = 'data.csv'
# Шлях до .json файлу
json_file_path = 'data.json'

# Запис у .csv файл
try:
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())  # Записуємо заголовки стовпців
        for row in data:
            writer.writerow(row.values())
except IOError as e:
    print(f"An error occurred while writing to the CSV file: {e}")

# Читання з .csv і запис у .json
try:
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

    with open(json_file_path, mode='w') as file:
        json.dump(rows, file, indent=4)
except IOError as e:
    print(f"An error occurred during file handling: {e}")
