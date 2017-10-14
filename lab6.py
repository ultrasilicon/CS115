'''
Created on Oct. 12 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12

CS115 - Lab 6
'''
def isOdd(n):
    return n % 2 != 0

'''Even numbers' rightmost digits are 0, because one digit can only reach maximum number, 1. When it exceeds 1, it will be zero, and the left digit will be added by one. In the same way, for odd numbers the rightmost digit is 1, since it is not even.'''
'''When every final digit is taken off, the original number is divided by 2'''
'''If we get N/2, and we wanna find N, we just add one digit at the first digit. if it is even number, we add 0, for odd numbers, we add 1'''
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ("0" * 8 +  numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    return count(increment(s), n - 1)

'''2*1 + 0*3 + 1*9 + 2*27 == 59.'''
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToTernary(int(n / 3)) + str(n%3)


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
