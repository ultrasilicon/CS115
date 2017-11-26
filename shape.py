"""
Created on Nov 21 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115
"""

from abc import ABCMeta, abstractproperty


class Shape(metaclass=ABCMeta):
    def __init__(self, x, y, name="Shape"):
        self.__x = x
        self.__y = y
        self.__name = name

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @abstractproperty
    def area(self):
        pass

    def __str__(self):
        return self.__name + "at (" + str(self.__x) + ", " + str(self.__y) + ")"


if __name__ == "__main__":
    try:
        a = Shape(10,20)
    except TypeError as error:
        print("error:", error)




















