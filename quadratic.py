"""
Created on Nov 17 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - lab11
"""

import math

class QuadraticEquation(object):
    """a class to represent quadratic equation"""

    def __init__(self, a, b, c):
        """initialize the quadratic equation with coefficient a, b and c"""
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
            return
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c


    def discriminant(self):
        """find the discriminant of the quadratic equation"""
        return self.__b ** 2 - 4 * self.__a * self.__c

    def root1(self):
        """compute the 1st root of the quadratic equation"""
        disc = self.discriminant()
        if disc < 0:
            return None
        return ((- self.__b + math.sqrt(disc)) / (2 * self.__a))

    def root2(self):
        """compute the 2nd root of the quadratic equation"""
        disc = self.discriminant()
        if disc < 0:
            return None
        return ((- self.__b - math.sqrt(disc)) / (2 * self.__a))

    def __str__(self):
        """Gets a user-friendly string representation of the quadratic euqation."""
        _a = str(self.__a)
        _b = str(self.__b)
        _c = str(self.__c)

        if abs(self.__a) == 1.0:
            _a = "x^2 " if self.__a > 0 else "-x^2 "
        else:
            _a = (_a if self.__a > 0 else "- " + _a[1:]) + "x^2 "

        if abs(self.__b) == 1.0:
            _b = "+ x " if self.__b > 0 else "- x "
        elif self.__b == 0:
            _b = ""
        else:
            _b = ("+ " + _b if self.__b > 0 else "- " + _b[1:]) + "x "

        if abs(self.__c) == 1.0:
            _c = "+ 1.0 " if self.__c > 0 else "- 1.0 "
        elif self.__c == 0:
            _c = ""
        else:
            _c = ("+ " + _c if self.__c > 0 else "- " + _c[1:]) + " "

        return _a + _b + _c + "= 0"





























