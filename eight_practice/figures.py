from abc import ABC, abstractmethod
import math

class SecondDimensionFigure(ABC):
    '''Абстрактный класс 2D фигуры'''
    @abstractmethod
    def get_area():
        '''Абстрактный метод рассчёта площади'''
        pass

    @abstractmethod 
    def get_perimeter():
        '''Абстрактный метод рассчёта периметра'''
        pass

class ThirdDimensionFigure(ABC):
    '''Абстрактный класс 3D фигуры'''
    @abstractmethod
    def get_area():
        '''Абстрактный метод рассчёта площади'''
        pass

    @abstractmethod 
    def get_perimeter():
        '''Абстрактный метод рассчёта периметра'''
        pass

    @abstractmethod 
    def get_volume():
        '''Абстрактный метод рассчёта объёма'''
        pass

class Circle(SecondDimensionFigure):
    def __init__(self, radius=1):
        
        self.radius = radius

    def get_area(self):
        '''Метод рассчёта площади'''
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return 2 * math.pi * self.radius

class Square(SecondDimensionFigure):
    def __init__(self, side=1):
        self.side = side

    def get_area(self):
        '''Метод рассчёта площади'''
        return self.side ** 2

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return 4 * self.side

class Rectangle(SecondDimensionFigure):
    def __init__(self, sideA=1, sideB=1):
        self.sideA = sideA
        self.sideB = sideB

    def get_area(self):
        '''Метод рассчёта площади'''
        return self.sideA * self.sideB

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return 2 * self.sideA + 2 * self.sideB

class Sphere(ThirdDimensionFigure):
    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        '''Метод рассчёта площади'''
        return 4 * math.pi * self.radius ** 2

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return math.inf

    def get_volume(self):
        '''Метод рассчёта объёма'''
        return 4/3 * math.pi * self.radius ** 3

class Cube(ThirdDimensionFigure):
    def __init__(self, side=1):
        self.side = side

    def get_area(self):
        '''Метод рассчёта площади'''
        return 6 * self.side ** 2

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return 12 * self.side

    def get_volume(self):
        '''Метод рассчёта объёма'''
        return self.side ** 3

class Cuboid(ThirdDimensionFigure):
    def __init__(self, sideA=1, sideB=1, sideC=1):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def get_area(self):
        '''Метод рассчёта площади'''
        return 2 * (self.sideA * self.sideB + self.sideA * self.sideC + self.sideC * self.sideB)

    def get_perimeter(self):
        '''Метод рассчёта периметра'''
        return 4 * self.sideA + 4 * self.sideB + 4 * self.sideC

    def get_volume(self):
        '''Метод рассчёта объёма'''
        return self.sideA * self.sideB * self.sideC