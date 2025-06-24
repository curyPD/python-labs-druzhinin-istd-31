class Animal:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class Cat(Animal):
    def get_sound(self):
        print("мяю")


class Dog(Animal):
    def get_sound(self):
        print("гав-гав")


class Chicken(Animal):
    def get_sound(self):
        print("чик-чик")


Animals = [
    Cat("Мурка"), Cat("Бааааарсик"), Cat("Тайлунг"),
    Dog("Пятачок"), Dog("Бобик"), Dog("Шарик"),
    Chicken("Цыпа"), Chicken("Хей-Хей"), Chicken("Клювик")
]

for animal in Animals:
    print(f"Имя: {animal.name}")
    animal.get_sound()

Animals[0].add_friend(Animals[3])  
Animals[0].add_friend(Animals[1]) 

