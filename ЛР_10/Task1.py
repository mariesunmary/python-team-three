# Костян О. 1-ий студент
try:
    # Відкриття файлу для запису
    with open('questions1.txt', 'w', encoding='utf-8') as file:
        # Запис прізвища та питання першого студента
        file.write("Прізвище першого студента: Костян\n")
        file.write("Питання від першого студента: Як створити список у Python?\n")
    print("Файл успішно створено та заповнено.")
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except Exception as e:
    print("Сталася помилка:", e)

# Коноплянченко Д. 2-ий студент
try:
    # відкриття файлу в режимі дозапису
    with open('questions1.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write('Прізвище другого студента: Коноплянченко\n')
        file.write('Відповідь на питання першого студента:\n')
        file.write('Для створення списку можна використати два підходи:\n')
        file.write('1. Використання квадратних дужок: a = [1, 2, 3]\n')
        file.write('2. Використання методу list(obj), в якості obj приймається будь-який ітерабельний об\'єкт: a = list("test")\n')
        file.write('Питання для другого студента: Обрати 3 функції роботи з рядком і коротко їх описати\n')
    print("Файл дозаповнено рядками 2-го студента.")
except Exception as e:
    print(f"Виникла помилка ({type(e)}): {e}")

