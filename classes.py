
"""class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Parrots name is {self.name} and parrots age is {self.age}'

parrot1 = Parrot('Serhii', 12)

print(parrot1)
"""
import Eccommerce.Login.LoginForm


"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass(self):
        if self.marks < 65:
            print('you failed, score is ', self.marks)
        elif self.marks > 65:
            print('you have passed exams, your score is ', self.marks)


student1 = Student('Alice', 67)
student2 = Student('Mark', 62)
"""

"""class Complex:
    def __init__(self, real, imag, third):
        self.real = real
        self.imag = imag
        self.third = third

    def add(self, number, number2):
        real = self.real + number.real + number2.real  # self.real is the real part of n1, number.real is the real part of n2
        imag = self.imag + number.imag + number2.imag  # self.imag is the imaginary part of n1, number.imag is the imaginary part of n2
        this = self.third + real + imag
        result = Complex(real, imag, this)  # Create a new Complex object with the sum
        return result


n1 = Complex(5,6, 0)
n2 = Complex(-4,4, 0)
n3 = Complex(4,4, 0)


result = n1.add(n2, n3)
print(result.real)
print(result.imag)
print(result.third)"""

"""class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def Pcalc(self):
        p = self.a + self.b + self.c
        return p
    

first = Triangle(2,5,7)
print(first.Pcalc())"""
