# I pledge that I have abided Stevens Honor System Han Zheng


from cs115 import range, map, reduce
import math


def dbl(x):
    """Returns twice its input x
       input x: a number (int or float)"""
    return 2 * x


def inverse(x):
    """Return inverted x,
       input x: a number (int or float)"""
    return 1 / x


def add(a, b):
    """Add a to b, and return the sum
       input a, b: numbers (int or float)"""
    return a + b


def e(x):
    """approximates the mathematical value e using a Taylor expansion,
        Return the sum of expansion from 0 to input x."""
    return reduce(add, map(inverse, map(math.factorial, range(0, x + 1))))


def error(x):
    """return the error of function e(), comparing to the real math.e()function"""
    return abs(math.e - e(x))


print(error(3))
