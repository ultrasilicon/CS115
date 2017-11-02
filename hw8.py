"""
Created on Nov 01 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw8
"""


def TcToNum(S):
    """Takes as input string S of 8 bits representing an integer in two's-complement, and returns the corresponding integer."""
    def TcToNumHelper(S):
        if S == "":
            return 0
        return TcToNumHelper(S[:-1]) * 2 + int(S[-1])
    return TcToNumHelper(S[1:]) if S[0] == "0" else TcToNumHelper(S[1:]) - 128


def NumToTc(n):
    """Takes as input an integer n, and returns a string representing the two's-complement representation of that integer."""
    def numToBinary(n):
        if n == 0:
            return ""
        return numToBinary(int(n / 2)) + str(n % 2)

    def completeSevenDigit(s):
        '''complete 7 digit if the binary string is not long enough, fill higher digits with 0.'''
        return "0" * (7 - len(s)) + s

    if n >= 128 or n < -128:
        return 'Error'
    if n >= 0:
        return "0" + completeSevenDigit(numToBinary(n))
    else:
        return "1" + completeSevenDigit(numToBinary(n + 128))