from segment import Segment
from point import Point

class BrokenLine:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Ломаная должна состоять минимум из 3-х точек")
        self.points = points

    def get_len(self):
        total = 0
        for i in range(len(self.points) - 1):
            seg = Segment(self.points[i], self.points[i + 1])
            total += seg.get_len()
        return total

    def __str__(self):
        return ",".join(p.name for p in self.points)

    def __add__(self, other):
        if isinstance(other, Point):
            return BrokenLine(self.points + [other])
        raise TypeError("К ломаной можно прибавить только точку")
