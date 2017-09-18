# I pledge my honor that I have abided by the Stevens Honor System
# 
# By Tim Zheng 
# 18 Sep 2017

from cs115 import map



def powerSet(lst):
    """returns power set of a list, the set of all subsets of the list"""
    if lst == []:
        return [[]]
    lose_it = powerSet(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it


print(powerSet(['a', 'b', 'c']))