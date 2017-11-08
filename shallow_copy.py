"""
Created on Nov 06 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 -
"""

def shallow_copy(L):
    ret = []
    for m in L:
        ret.append(m)
    return ret


def deep_copy(L):
    ret = []
    for x in L:
        if type(x) is list:
            ret.append(deep_copy(x))
        else:
            ret.append(x)
    return ret


def create_board(r, c):
    ret = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(0)
        ret.append(row)
    return ret


def create_board_comp(r, c):
    return [[0 for _ in range(c)] for _ in range(r)]

board = create_board(32, 32)


def print_board(board):
    print("\n-" + "----" * len(board))
    for r in board:
        print("|", end = "")
        for c in r:
            print(" " + str(c) + " |", end = "")
        print("\n-" + "----" * len(board))


ragged = [[1,10,9,6],[3],[4,12,17,1,13],[8,7]]

def find_max_2d(L):#
    i = 0
    j = 0
    coordinate = (0,0)
    ret = L[0][0]
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] > ret:
                ret = L[i][j]
                coordinate = (i, j)
    return str(ret) + str(coordinate)


def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def selection_sort(L):
    length = len(L)
    min_index = i = 0
    for i in range(length - 1):

        print("-------------")
        for x in L[i + 1:]:
            print( L[i + 1:])
            if x < L[min_index]:
                min_index = i
        if min_index != i:
            print("min:"+str(min_index))
            print("sub:"+str(i)+ str(min_index))
            swap(L, i, min_index)
            print(L)




# S = [[1, 2], [3, 4], [5, 6]]
# T = deep_copy(S)
# T[0][1] = 22
# print(S)
# print(T)

# print_board(board)
# print(find_max_2d(ragged))
LL = [1,2,7,74,6,8,3,-2]
selection_sort(LL)
print(LL)

















