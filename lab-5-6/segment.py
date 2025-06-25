import math

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_len(self):
        dx = self.point1.x - self.point2.x
        dy = self.point1.y - self.point2.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"{self.point1.name}{self.point2.name}({self.point1.x},{self.point1.y}; {self.point2.x},{self.point2.y})"

    def __add__(self, other):
        if isinstance(other, Segment):
            from broken_line import BrokenLine
            return BrokenLine([self.point1, self.point2, other.point2])
        raise TypeError("Можно складывать только с другим объектом Segment")
