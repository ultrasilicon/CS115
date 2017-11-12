"""
Created on Nov 09 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""

def num_matches(l1, l2):
    l1.sort()
    l2.sort()
    i = j = ret = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            ret += 1
            i += 1
            j += 1
    return ret


def keep_matches(l1, l2):
    l1.sort()
    l2.sort()
    i = j = 0
    ret = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            ret.append(l1[i])
            i += 1
            j += 1
    return ret


def drop_matches(l1, l2):
    l1.sort()
    l2.sort()
    i = j = 0
    ret = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ret.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            ret.append(l2[j])
            j += 1
        else:
            i += 1
            j += 1
    ret += l1[i:len(l1)]
    # while i < len(l1):
    #     ret.append(l1[i])
    #     i += 1
    ret += l2[j:len(l2)]
    # while j < len(l2):
    #     ret.append(l2[j])
    #     j += 1
    return ret

print(drop_matches([1, 5, 2, 3, 100], [1, 2, 4, 5]))

