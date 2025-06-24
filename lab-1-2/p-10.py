# Задача 10. 
# Написать функцию, которая принимает:  
# 1) 1 обязательный аргумент дату в формате строки (можно использовать 
# функцию из задачи №9) 
# 2) 1 необязательный аргумент объект даты, по умолчанию должна быть 
# текущая дата
# Функция должна вернуть число секунд между двумя этими датами.
from datetime import datetime

def seconds_between(date_str, another_date=datetime.now()):
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    return abs(int((another_date - date_obj).total_seconds()))


