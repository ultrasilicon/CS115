"""
Created on Oct 31 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""

import math

def mapSqr(L):
    ret = []
    for e in L:
        ret.append(e * e)
    return ret

def findMax(L):
    ret = L[0]
    i = 1
    while i < len(L):
        if ret < L[i]:
            ret = L[i]
        i += 1
    return ret

def findMinMax(L):
    if L == []:
        return None
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)


def sequentialSearch(lst, key):
    i = 0
    while i < len(lst):
        if lst[i] == key:
            return i
        i += 1
    return -1

print(sequentialSearch([1,2,-3,4,5], 1op))


