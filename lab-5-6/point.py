class Point:
    def __init__(self, x: int, y: int, name: str):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f"{self.name}({self.x},{self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y and self.name == other.name

    def __hash__(self):
        return hash((self.x, self.y, self.name))

    def __add__(self, other):
        if isinstance(other, Point):
            from segment import Segment
            return Segment(self, other)
        raise TypeError("Можно складывать только с другим объектом Point")

