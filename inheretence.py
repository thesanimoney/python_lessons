class Animal:
    def eat(self):
        print('i can eat')

    def sleep(self):
        print('i can sleep')

    name = 'Alice'

class Dog(Animal):

    def bark(self):
        print('i can bark')


cat = Animal()
dog = Dog()

print(dog.name, dog.eat())
dog.bark()
cat.sleep()
cat.eat()