# Задача 15. 
# Написать функцию, которая примет произвольную строку. Функция 
# должна вернуть словарь, который содержит себе следующие ключи и 
# значения: 
# 1) length — длина строки 
# 2) words_count — количество слов 
# 3) digit_count — количество цифровых символов
def analyze_string(s):
    return {
        "length": len(s),
        "words_count": len(s.split()),
        "digit_count": sum(c.isdigit() for c in s)
    }
