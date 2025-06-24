class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, value):
        if value < self.__b + self.__c:
            self.__a = value
        else:
            print("Ошибка: сторона a не может быть больше или равна сумме двух других сторон.")

    def set_b(self, value):
        if value < self.__a + self.__c:
            self.__b = value
        else:
            print("Ошибка: сторона b не может быть больше или равна сумме двух других сторон.")

    def set_c(self, value):
        if value < self.__a + self.__b:
            self.__c = value
        else:
            print("Ошибка: сторона c не может быть больше или равна сумме двух других сторон.")

    def get_perimetr(self):
        return self.__a + self.__b + self.__c
