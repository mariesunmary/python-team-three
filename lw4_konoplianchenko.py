text = "Колишня розпродажна виручка виявилася мрією. Все було продано, навіть ті товари, що лежали на полицях занадто довго. Щасливий вигляд покупців свідчив про успіх події. Але задоволення від такого результату затмарила пізніша звістка про пожежу в складському приміщенні."

# 1. Видалення '.' з початку та кінця рядка в text
text_strip_dot: str = text.strip('.')

# 2. Заміна '.' на '!' в text
text_replace_dot = text.replace('.', '!')

# 3. Кількість 'а' в text
text_count_a = text.count('а')

print(f'Text strip dot: {text_strip_dot}\n')
print(f'Text replace dot: {text_replace_dot}\n')
print(f'Count of "а" in text: {text_count_a}\n')
