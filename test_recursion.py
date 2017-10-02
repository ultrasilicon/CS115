# I pledge my honor that I have abided by the Stevens Honor System
# 
# By Tim Zheng 
# 12 Sep 2017

from cs115 import reduce
import math


def tower(x):
    """returns 2^(2(....)) with n twos using recursion"""
    if x == 0:
        return 1
    return 2 ** tower(x - 1)


def power(x, y):
    return x ** y


def r_power(x, y):
    if y == 0:
        return 1
    return x * r_power(x, y - 1)


def power_tail(x, y):
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x)
    return power_tail_helper(x, y, 1)


def length(lst):
    """returns the length of the list"""
    if lst == []:
        return 0
    return 1 + length(lst[1:])


def reverse(lst):
    """returns the length of the list"""
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]


def member(x, lst):
    if lst == []:
        return False
    if lst[0] == x:
        return True
    return member(x, lst[1:])


def tower_reduce(x):
    if x == 0:
        return 1
    return reduce(power, [2] * tower_reduce(x - 1))


def tower_reduce_m(x):
    if x == 0:
        return 1
    return reduce(power, [2] * tower_reduce(x - 1))


def my_map(f, lst):
    """returns a new list where the function f has been applies to every elements in the original list"""
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])


def my_reduce(f, lst):
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst == []:
        raise TypeError('my_resuce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])


def prime(n):
    """Returns whether or not integer is prime"""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x : n % x == 0, possible_divisors)
    return len(divisors) == 0


def primes(n):
    """returns a range of primes in the range [2, n] computed via the sieve of Erathosthenes"""
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x : x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Linear Recursion
def myFilter(f, l):
    return [] if l == [] else ([l[0]] if f(l[0]) else []) + myFilter(f, l[1:])


print(myFilter(lambda x: x % 2 == 0, [0,0,2,3,0]))

