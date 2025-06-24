# Задача 14. 
# Написать функцию, которая принимает список строк. Функция должна 
# вернуть случайный элемент списка в верхнем регистре.
import random

def random_uppercase(l):
    if l:
        return random.choice(l).upper()
    return None

