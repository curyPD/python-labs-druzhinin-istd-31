# Задача 13. 
# Программа генерирует случайное целое число от 0 до 10. Пользователь 
# должен угадать с 3х попыток это число. В случае успеха должно вывестись на 
# экран поздравление с победой. В случае проигрыша – верный вариант ответа. 
import random

secret = random.randint(0, 10)
attempts = 3

for i in range(attempts):
    guess = input(f"Попытка {i+1}. Угадайте число от 0 до 10: ")
    if guess.isdigit() and int(guess) == secret:
        print("My man!")
        break
else:
    print(f"Вы проиграли. Загаданное число было: {secret}")
