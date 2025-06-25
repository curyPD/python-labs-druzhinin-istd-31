from point import Point

p1 = Point(0, 0, "A")
p2 = Point(3, 4, "B")
p3 = Point(0, 0, "A")  
p4 = Point(1, 2, "C")
p5 = Point(2, 1, "D")

print(str(p1))  
print(p1 == p3)  
print(len({p1, p2, p3, p4, p5})) 

seg = p1 + p2
print(str(seg))
print(seg.get_len())  

seg2 = p2 + p4
bl = seg + seg2
print(str(bl)) 
print(bl.get_len())

bl2 = bl + p5
print(str(bl2))
print(bl2.get_len())
