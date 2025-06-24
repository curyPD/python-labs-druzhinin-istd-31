# Задача 9. 
# Написать функцию, которая возвращает случайную дату в следующем 
# формате «дд-мм-гггг».
import random
from datetime import datetime, timedelta

def random_date():
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2030, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    result_date = start_date + timedelta(days=random_days)
    return result_date.strftime("%d-%m-%Y")

print(random_date())
