"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 04 Oct 2017
"""
import sys

sys.setrecursionlimit(10000)



def pascal_row(n):
    def pascal_add(row):
        if len(row) <= 1:
            return []
        return [row[0] + row[1]] + pascal_add(row[1:])
    def pascal_helper(n, row):
        if n == 0:
            return row
        return pascal_helper(n - 1, [1] + pascal_add(row) + [1])
    return pascal_helper(n, [1])


def pascal_triangle(n):
    if n < 0:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]


