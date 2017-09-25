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


def subSet(target, lst):
    """determines whether or not it is possible to create target sum using the values in the list, values in the list can be positive negative or zero"""
    if target == 0:
        return True
    if lst == []:
        return False
    use_it = subSet(target - lst[0], lst[1:])
    lose_it = subSet(target, lst[1:])
    return use_it or lose_it


def subSetWithValues(target, lst):
    """determines whether or not it is possible to create the taret sum using the values in the list, values in the list can be positive, negative or zero. the function returns a tuple of exatly two items, the first is a Boolean that indicates if the sum is possible anf False if it's not the second element is a list of all the values that add up to make the target sum."""
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subSetWithValues(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subSetWithValues(target, lst[1:])


def LCS(s1, s2):
    """returns the length of the longest common sub sequence in strings s1 and s2"""
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[0] == s2[0]:
        # return 1 + max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))


def vLCS(s1, s2):
    """returns the length of the longest common sub sequence in strings s1 and s2"""
    if s1 == '' or s2 == '':
        return (0,'')
    if s1[0] == s2[0]:
        result = vLCS(s1[1:], s2[1:])
        return (1 + result[0], s1[0] + result[1])
    useS1 = vLCS(s1, s2[1:])
    useS2 = vLCS(s1[1:], s2)
    return useS1 if useS1[0] >= useS2[0] else useS2


def coin_row(lst):
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))


def v_coin_row(lst):
    if lst == []:
        return [0,[]]
    use_it = v_coin_row(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = v_coin_row(lst[1:])
    return [new_sum, [lst[0]] + use_it[1]] if new_sum > lose_it[0] else lose_it


def distance(first, second):
    if first == "":
        return len(second)
    if second == "":
        return  len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first, second[1:])
    return 1 + min(substitution, deletion, insertion)




print(distance("hell", "hello"))













