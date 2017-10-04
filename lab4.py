"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 29 Sep 2017
"""
from cs115 import filter

def knapsack(capacity, itemList):
    """which returns both the maximum value and the list of items (itemList) that make this value, without exceeding the capacity of your knapsack"""
    if itemList == []:
        return [0,[]]
    if capacity == 0:
        return [0, []]
    if capacity - itemList[0][0] < 0:
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity - itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    if itemList[0][1] + use_it[0] >= lose_it[0]:
        return [itemList[0][1] + use_it[0]] + [[itemList[0]] + use_it[1]]
    else:
        return [lose_it[0]] + [lose_it[1]]
