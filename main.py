from abc import ABC, abstractmethod
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def zero(cls):
#        return cls(2, 3)
#
#     def draw(self):
#         return f'Cordinate x: {self.x} \nCoordinate y: {self.y}'
#
#     def __str__(self):
#         return f'{self.x} {self.y}'
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#
# point = Point(9,11)
# point1 = Point(10,12)
# print(point1 + point)


# --Magic Methods in a Class--
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}
#
#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
#
#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)
#
#     def __setitem__(self, tag, value):
#        self.__tags[tag.lower()] = value
#
#     def __len__(self):
#         return len(self.__tags)
#
#     def __iter__(self):
#        return iter(self.__tags.items())
#
#
# cloud = TagCloud()


# --Properties--
# class Product:
#     def __init__(self, price):
#         self.price = price
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, value):
#         if value <= 0:
#             raise ValueError('Price cannot be negative')
#
#         self.__price = value
#
#
#
# product = Product(10)
# product.price = -1
# print(product.price)

# --Inheretence--
# class Animal:
#     def __init__(self):
#         print("Animal Constructur")
#         self.age = 1
#
#     def eat(self):
#         print('eat')
#
#
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print('Mammal Constructur')
#         self.weight = 2
#
#     def walk(self):
#         print('walk')
#
#
# class Fish(Animal):
#     def swim(self):
#         print('swim')
#
#
# m = Mammal()
# print(m.age)

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        self.opened = False
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print('Reading data from a file')

class NetworkStream(Stream):
    def read(self):
        print('Reading data from a network')

class MemoryStream(Stream):
    def read(self):
        print('Reading data from memory stream')

mstream = MemoryStream()


















































