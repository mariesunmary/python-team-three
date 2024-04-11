def display_students(dictionary):
    """Функція виводить на екран словник з даними студентів."""
    print("Дані про студентів:")
    for group, students in dictionary.items():
        print(f"Група: {group}")
        for student in students:
            print(f"Прізвище: {student['прізвище']}")
            print(f"Ім'я: {student['ім\'я']}")
            print(f"По батькові: {student['по батькові']}")
            print(f"Курс: {student['курс']}")
            print("Предмети та оцінки:")
            for subject, grade in student['предмети'].items():
                print(f"\t{subject}: {grade}")
            print("------------")
def add_entry(dictionary, group, last_name, first_name, middle_name, course, subjects_grades):
    """Функція додає новий запис про студента до словника."""
    # Перевірка наявності групи в словнику
    if group not in dictionary:
        dictionary[group] = []

    # Створення словника для нового студента
    new_student = {
        'прізвище': last_name,
        'ім\'я': first_name,
        'по батькові': middle_name,
        'курс': course,
        'предмети': subjects_grades
    }

    # Додавання нового студента до групи
    dictionary[group].append(new_student)
    print("Студент доданий успішно.")


def remove_entry(dictionary, group, last_name):
    """Функція видаляє запис про студента зі словника за вказаним прізвищем."""
    if group in dictionary:
        students = dictionary[group]
        for student in students:
            if student['прізвище'] == last_name:
                students.remove(student)
                print("Студент з прізвищем", last_name, "видалений.")
                return
        print("Учня з прізвищем", last_name, "не знайдено.")
    else:
        print("Групу", group, "не знайдено.")


def exit_program():
    """Функція виводить повідомлення та завершує програму."""
    print("Програма завершена.")
def main():
    """Головна функція програми."""
    students_performance = {}  # Словник для зберігання інформації про успішність студентів групи
    while True:
        print("\nМеню:")
        print("1. Додати інформацію про студента")
        print("2. Видалити інформацію про студента")
        print("3. Вивести інформацію про всіх студентів")
        print("0. Вийти з програми")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            group = input("Введіть номер групи: ")
            last_name = input("Введіть прізвище студента: ")
            first_name = input("Введіть ім'я студента: ")
            middle_name = input("Введіть по батькові студента: ")
            course = int(input("Введіть курс студента: "))

            subjects_grades = {}
            subjects = input("Введіть предмети студента (через кому): ").split(',')
            for subject in subjects:
                mark = int(input(f"Введіть оцінку за предмет {subject.strip()}: "))
                subjects_grades[subject.strip()] = mark

            add_entry(students_performance, group, last_name, first_name, middle_name, course, subjects_grades)
            pass

        elif choice == '2':
            group = input("Введіть номер групи: ")
            last_name = input("Введіть прізвище студента для видалення: ")
            remove_entry(students_performance, group, last_name)
            pass

        elif choice == '3':
            display_students(students_performance)

        elif choice == '0':
            exit_program()
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
