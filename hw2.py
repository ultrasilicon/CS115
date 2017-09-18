# I pledge my honor that I have abided by the Stevens Honor System
# 
# By Tim Zheng 
# 14 Sep 2017

#K360
import sys
from cs115 import map, reduce, filter

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.


def letterScore(letter, lst):
    """takes as input a single letter string called letter and a list where each element in that list is itself a list of the form [character,value] where character is a single letter andvalue is a number associated with that letter."""
    if lst == []:
        return 0
    if lst[0][0] == letter:
        return lst[0][1]
    return letterScore(letter, lst[1:])


def wordScore(S, scorelist):
    """take as input a string S and a scorelist in the format described above, which will have only lowercase letters, and should return as output the scrabble score of that string."""
    if len(S) == 0:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def removeOne(letter, lst):
    """remove one letter from lst"""
    if lst == []:
        return []
    if lst[0] == letter:
        return lst[1:]
    return [lst[0]] + removeOne(letter, lst[1:])


def canForm(word, lst):
    """return if input word can be formed by members of input list"""
    if lst == [] and len(word) > 0:
        return False
    elif len(word) == 0:
        return True
    if not word[0] in lst:
        return False
    return canForm(word[1:], removeOne(word[0], lst))


def scoreList(Rack):
    """takes as input a Rack which is a list of lower-case letters and returns a list of all of the words in the global Dictionary that can be made from those letters and the score for each one."""
    def scoreListHelper(dict, Rack):
        if dict == []:
            return []
        if canForm(dict[0], Rack):
            return [[dict[0], wordScore(dict[0], scrabbleScores)]] + scoreListHelper(dict[1:], Rack)
        else:
            return scoreListHelper(dict[1:], Rack)
    return scoreListHelper(Dictionary, Rack)


def bestWord(Rack):
    """ takes as input a Rack as above and returns a list with two elements: the highest possible scoring word from that Rack followed by its score."""
    def bestWordHelper(scoreLst, word):
        if scoreLst == []:
            return word
        if scoreLst[0][1] >= word[1]:
            return bestWordHelper(scoreLst[1:], scoreLst[0])
        else:
            return bestWordHelper(scoreLst[1:], word)
    return bestWordHelper(scoreList(Rack), ['', 0])
