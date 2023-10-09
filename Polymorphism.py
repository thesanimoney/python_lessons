class Circle:
        def __init__(self, r):
            self.w = r

        def getArea(self):
            return 3.14 * self.w**2

        def __str__(self):
            return  f"Your area for Circle is {self.getArea()}"
class Square:
        def __init__(self, a):
            self.a = a

        def getArea(self):
            return self.a**2

        def __str__(self):
            return  f"Your area for Square is {self.getArea()}"


s1 = Square(4)
c1 = Circle(2)
s2 = Square(6)
c2 = Circle(5)
c3 = Circle(1)

list = [s1, c1, s2, c2, c3]

for i in  list:
    print(i)







