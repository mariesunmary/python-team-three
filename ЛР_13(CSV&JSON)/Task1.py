import csv
import json

# Костян О.В. Студент №1
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

# Коноплянчено Д. Студент №2
# Нові записи
new_data_2 = [
    {"name": "Michael", "age": 45, "city": "San Francisco"},
    {"name": "Oleksiy", "age": 19, "city": "Seattle"},
    {"name": "David", "age": 25, "city": "Boston"}
]

# Читання з .json файлу
try:
    with open(json_file_path, mode='r') as file:
        json_data = json.load(file)

    # Об'єднуємо з новими записами
    json_data.extend(new_data_2)

    # Запис у .json файл
    with open(json_file_path, mode='w') as file:
        json.dump(json_data, file, indent=4)

    # Запис у .csv файл
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)

except IOError as e:
    print(f"An error occurred during file handling: {e}")
except json.JSONDecodeError as e:
    print(f"An error occurred while decoding the JSON file: {e}")

# Вощенко Д. Студент №3
# Нові записи
new_data_3 = [
    {"name": "Sam", "age": 25, "city": "London"},
    {"name": "Solid", "age": 59, "city": "Milan"},
    {"name": "David", "age": 25, "city": "Boston"}
]

# Читання з .csv файлу і додавання нових даних
try:
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

    # Об'єднуємо з новими записами
    rows.extend(new_data_3)

    # Запис у .csv файл
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    # Запис у .json файл
    with open(json_file_path, mode='w') as file:
        json.dump(rows, file, indent=4)

except IOError as e:
    print(f"An error occurred during file handling: {e}")
except json.JSONDecodeError as e:
    print(f"An error occurred while decoding the JSON file: {e}")
