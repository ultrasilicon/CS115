"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 03 Oct 2017
"""

"""
memoization:
1. If jey is in the memo, re turn the value associated with the key
2. Do work! Use recursion to complete your answer, but store the result in a local variable
3. Put the result in the memo and then return the retult.
"""


def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
        memo[n] = result
        return result

    return fib_helper(n, {})


def LCS_memo(s1, s2):
    """returns the length of the longest common sub sequence in strings s1 and s2"""
    def LCS_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if s1 == '' or s2 == '':
            result = 0
        elif s1[0] == s2[0]:
            result = 1 + LCS_helper(s1[1:], s2[1:], memo)
        else:
            result = max(LCS_helper(s1, s2[1:], memo), LCS_helper(s1[1:], s2, memo ))
        memo[(s1, s2)] = result
        return result
    return LCS_helper(s1, s2, {})


def subSet(target, lst):
    """determines whether or not it is possible to create target sum using the values in the list, values in the list can be positive negative or zero"""
    def subSetHelper(target, lst, memo):
        if (target, lst) in memo:
            return memo[(target, lst)]
        if target == 0:
            result = True
        elif len(lst) == 0:
            result = False
        else:
            result = subSetHelper(target - lst[0], lst[1:], memo) or subSetHelper(target, lst[1:], memo)

        memo[(target, lst)] = result
        return result
    return subSetHelper(target, lst, {})



print()

