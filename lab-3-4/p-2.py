class Human:
    def __init__(self, fio, age=0, gender="М"):
        self.last_name, self.name, self.father_name = fio.split()
        self.age = age
        self.gender = gender

    def get_fio(self):
        return f"{self.last_name} {self.name[0]}. {self.father_name[0]}."

    def get_full_info(self):
        return f"Фамилия: {self.last_name}\nИмя: {self.name}\nОтчество: {self.father_name}\nПол: {self.gender}\nВозраст: {self.age}"


class Student(Human):
    def __init__(self, fio, group, age=0, gender="М"):
        super().__init__(fio, age, gender)
        self.group = group

    def get_full_info(self, comma=False):
        info = super().get_full_info()
        info += f"\nГруппа: {self.group}"
        if comma:
            return info.replace("\n", ", ")
        return info


