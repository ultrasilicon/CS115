# I pledge my honor that I have abided by the Stevens Honor System
# 
# By Tim Zheng 
# 15 Sep 2017



def dot(L, K):
    """output the dot product of the lists L and K"""
    if L == [] or K == []:
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])


def explode(S):
    """take a string S as input and should return a list of the characters"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])


def ind(e, L):
    """takes in an element e and a sequence L where by "sequence" we mean either a list or a string, Then, ind should return the index at which e is first found in L"""
    if L == []:
        return 0
    def ind_helper(e, L, n):
        if L == []:
            return n
        if L == '':
            return n
        if e == L[0]:
            return n
        return ind_helper(e, L[1:], n + 1)
    return ind_helper(e, L, 0)


def removeAll(e, L):
    """ takes in an element e and a list L. Then, removeAll should return another list that is identical to L except that all elements identical to e have been removed."""
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])


def even(X):
    """Return if input X is even"""
    if X % 2 == 0 :
        return True
    else:
        return False


def myFilter(func, L):
    """My implementation of python filter, return a filtered list with filter func(x)"""
    if L == []:
        return []
    if func(L[0]) == False:
        return myFilter(func, L[1:])
    return [L[0]] + myFilter(func, L[1:])



def deepReverse(L):
    """"takes as input a list of elements where some of those elements may be lists themselves. """
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[0:len(L)-1])
    return [L[-1]] + deepReverse(L[0:len(L)-1])


def m_deepReverse(L):
    """"takes as input a list of elements where some of those elements may be lists themselves. """
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[0:len(L)-1])
    return [L[-1]] + deepReverse(L[0:len(L)-1])




print(dot([5,3], [6,4]))
print(explode("hello world"))
print(ind('hi', ['hello', 42, True]))
print(removeAll(42, [ 55, 77, 42, 11, 42, 88 ]))
print(myFilter(even, [0, 1, 2, 3, 4, 5, 6]))
print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))