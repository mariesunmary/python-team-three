text = "Колишня розпродажна виручка виявилася мрією. Все було продано, навіть ті товари, що лежали на полицях занадто довго. Щасливий вигляд покупців свідчив про успіх події. Але задоволення від такого результату затмарила пізніша звістка про пожежу в складському приміщенні."

# 1. Перетворення тексту у нижній регістр
lower_text = text.lower()

# 2. Розділення тексту на окремі слова
words = lower_text.split()

# 3. Підрахунок кількості слів у тексті
word_count = len(words)

print("Текст у нижньому регістрі:", lower_text)
print("Слова у тексті:", words)
print("Кількість слів у тексті:", word_count)
