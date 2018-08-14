from time import time

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=''):
        self.name = newname
    def __str__(self):
        # return 'animal:' + str(self.get_name()) + ':' + str(self.get_age())
        return self.__class__.__name__ + ':' + str(self.get_name()) + ':' + str(self.get_age())

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return self.__class__.__name__ + ':' + str(self.name) + ':' + str(self.age)
        # return 'cat:' + str(self.name) + ':' + str(self.age)


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
    def speak(self):
        print('meep')
    # def __str__(self):
        # return self.__class__.__name__ + ':' + str(self.name) + ':' + str(self.age)
        # return 'rabbit:' + str(self.name) + ':' + str(self.age)


peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy, mopsy.get_parent1(), mopsy.get_parent2())


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
##    def __str__(self):
##        return "person:" + str(self.name) + ':' + str(self.age)
    
p = Person('Nik', 3)
print(p)
p1 = Person('Mat', 5)
p1.age_diff(p)
p.age_diff(p1)       

import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have a homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I\'m watching tv')
    def __str__(self):
        return 'student:' + str(self.name) + ':' + str(self.age) + ':' + str(self.major)

    

# How to create class, which objects can change over time?
# Classes which provide mutations of objects.
# Radiation can change the objects. Is it a class too?
    
class MyAnimal():
    def __init__(self):
        self.born_time = round(time())

    def age(self):
        return round(time()) - self.born_time
        
        
