"""
Created on Dec 10 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""


def swap(lst, a, b):
    c = lst[a]
    lst[a] = lst[b]
    lst[b] = c


def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[minimum] > lst[j]:
                minimum = j
        if i != minimum:
            swap(lst, i, minimum)
    return lst


print("Test Selection Sort " + str(selection_sort([4, 7, 2, 2, 2, 6, 9, 5, 5, 1, 0])))


def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(0, i):
            if lst[i] < lst[j]:
                swap(lst, i, j)
            else:
                continue
    return lst


print("Test Insertion Sort " + str(insertion_sort([4, 7, 2, 2, 2, 6, 9, 5, 5, 1, 0])))


def binary_search(lst, x):
    first = 0
    last = len(lst)

    while first <= last:
        i = (first + last) / 2
        if lst[i] == x:
            return i
        elif lst[i]



print(binary_search([1,2,3,4,5,6,7,8,10,23,34,45,78,90], 10))







































