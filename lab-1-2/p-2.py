# Задача 2. 
# Написать программу, которая должна поочередно запросить у 
# пользователя его ФИО и вывести результат в формате «Фамилия И. О.»
full_name = input("Введите ФИО: ").split()
if len(full_name) == 3:
    last, first, father_name = full_name
    print(f"{last} {first[0]}. {father_name[0]}.")
else:
    print("Введите ФИО в формате: Фамилия Имя Отчество")
