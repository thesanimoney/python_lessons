import re
from collections import deque
from array import array
from pprint import pprint
from timeit import timeit

#
# def replacement(mystring, letter, new_letter):
#     string = print(re.sub(f'{letter}', f'{new_letter}', mystring))
#     return string
#
# replacement('Dima Dima', 'D', "Z")

# items = [
#     ('Product1', 11.65),
#     ('Product2', 12.25),
#     ('Product3', 10.15),
#     ('Product5', 15.15),
# ]
#
# prices1 = list(filter(lambda item: item[1] > 12, items))
# prices = [item for item in items if item[1] > 12]
# print(prices)
# print(prices1)

# for item in x:
#     print(item)

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(browsing_session)
# last = browsing_session.pop()
# print(browsing_session)
# last = browsing_session.pop()
# print(browsing_session)
#
# if browsing_session == False:
#     print('browsing session is ended')

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print('Empty')
# code1 = """
# sentence = 'this is a common interview question'
#
#
# letter_list = []
#
# for letter in sentence:
#     x = int(sentence.count(letter))
#     letter_list.append(x)
#
# max_value = max(letter_list)
# index_max_value = letter_list.index(max_value)
#
#
# """
#
# code2 = """
# sentence2 = 'this is a common interview question'
# char_values = {}
# for char in sentence2:
#     if char in char_values:
#        char_values[char] += 1
#     else:
#         char_values[char] = 1
#
# sort = sorted(char_values.items(), key=lambda kv: kv[1], reverse=True)
#
# """
# print('first code', timeit(code1, number=10000))
# print('second code', timeit(code2, number=10000))
#



# code3 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise (ValueError('Age cannot be 0'))
#     return f'{10 / age}'
#
#
# try:
#     print(calculate_xfactor(0))
# except ValueError as error:
#     pass
# """
#
#
# code4 = """
# def calculate_xfactor(age):
#     if age <= 0:
#        return None
#     return f'{10 / age}'
#
# print(calculate_xfactor(0))
# """

class Point:
    color = 'red'
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Coordinates {self.x}, {self.y}')

point = Point('ssss', 'ssss')
point.color = 'white'
Point.color
print(Point.color)
point.draw()























































