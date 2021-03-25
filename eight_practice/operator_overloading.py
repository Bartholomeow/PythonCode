import math

class Person:
    '''Класс, представляющий человека'''
    def __init__(self, name='Vasya', age=18, sex='М'):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'Name = {self.name}; age = {self.age}; sex = {self.sex}'

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __add__(self, other):
        if self.sex != other.sex:
            return Person(name='Child', age=0, sex=math.nan)
        else:
            return Person(name='Friendship', age=0, sex=math.nan)

    def __sub__(self, other):
        return Person(name='Enmity', age=0, sex=math.nan)
