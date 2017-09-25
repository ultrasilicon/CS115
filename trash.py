"""
 I pledge my honor that I have not abided by the Stevens Honor System
 
 By Tim Zheng 
 21 Sep 2017
"""

from cs115 import map, reduce, filter



def addToTicker(date, event):
    length = 0

    for character in date:
        length += 1
    for character in event:
        length += 1
    if length + 7 < 31:
        print("**On "+ date+", "+event+"**")
    else:
        print("Too long, try again.")


def interleave(s1, s2):
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    return s1[0] + s2[0] + interleave(s1[1:], s2[1:])


def x_count(x, lst):
    if lst == []:
        return 0
    return  x_count(x, lst[1:]) + (1 if x == lst[0] else 0)


def x_count1(x, lst):
    count = 0
    for member in lst:
        if member == x:
            count += 1
    return count




