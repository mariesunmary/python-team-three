try:
    # Відкриття файлу для запису
    with open('questions1.txt', 'w') as file:
        # Запис прізвища та питання першого студента
        file.write("Прізвище першого студента: Костян\n")
        file.write("Питання від першого студента: Як створити список у Python?\n")
    print("Файл успішно створено та заповнено.")
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except Exception as e:
    print("Сталася помилка:", e)
