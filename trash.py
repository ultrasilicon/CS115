"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 21 Sep 2017
"""


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

print(interleave("tim", "cat"))


