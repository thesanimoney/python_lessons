from abc import ABC, abstractmethod
#class Circle:
#         def __init__(self, r):
#             self.w = r
#
#         def getArea(self):
#             return 3.14 * self.w**2
#
#         def __str__(self):
#             return  f"Your area for Circle is {self.getArea()}"
# class Square:
#         def __init__(self, a):
#             self.a = a
#
#         def getArea(self):
#             return self.a**2
#
#         def __str__(self):
#             return  f"Your area for Square is {self.getArea()}"
#
#
# s1 = Square(4)
# c1 = Circle(2)
# s2 = Square(6)
# c2 = Circle(5)
# c3 = Circle(1)
#
# print(c1.getArea())

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
# class TextBox(UIControl):
#     def draw(self):
#         print('TextxBox')
# class DropDownList(UIControl):
#     def draw(self):
#         print('Dropdownlist')
#
# def draw1(controlsObject):
#     for control in controlsObject:
#         control.draw()
#
# object1 = TextBox()
# object2 = DropDownList()
#
# draw1([object2, object1])

# class Text(str):
#     def duplicate(self):
#
#         return self + ' ' + self
#
#
# class TrackebleList(list):
#     def append(self, object):
#         print('Append')
#         super().append(object)
#
# list = TrackebleList()
# list.append('1')

# --namedtuple--
# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
# p1 = Point(x=1, y=2)
# p2 = Point(x=1, y=2)
# print(p1 == p2)

from Eccommerce.Login.LoginForm import Login


