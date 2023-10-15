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

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
       self.tags[tag.lower()] = value

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
       return iter(self.tags.items())


cloud = TagCloud()

cloud.add('Python')
cloud.add('Python')
cloud['python'] = 12
cloud['Jython'] = 12
cloud.add('Java')
cloud.add('JavaScript')

for tag, values in cloud:
    print(values)

