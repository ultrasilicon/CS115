# I pledge my honor that I have abided by the Stevens Honor System
#
# By Tim Zheng

from cs115 import map, reduce


def add(x, y):
    """Returns the sum of x and y"""
    return x + y


def mult(x, y):
    """Returns the product of x and y"""
    return x * y


def factorial(x):
    """Returns the factorial of x"""
    return reduce(mult, range(1, x + 1))


def divides(n):
    def div(k):
        return n % k == 0
    return div


def mean(x):
    """Returns the mean of the list x"""
    return reduce(add, x) / len(x)


def prime(x):
    """Returns whether x is a prime number"""
    if x > 1:
        return sum(map(divides(x), range(2, x))) == 0
    return False



print(map(prime, range(1, 11)))

