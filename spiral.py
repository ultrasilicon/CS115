"""
 I pledge my honor that I have abided by the Stevens Honor System
 
 By Tim Zheng 
 05 Oct 2017
"""

import sys
import turtle
sys.setrecursionlimit(10000)

def square_spiral(walls):
    turtle.speed(0)
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(89.9)
            turtle.forward(distance)
            square_spiral_helper(distance + initial * (count % 2), initial, count + 1)
    return square_spiral_helper(1, 1, 0)



square_spiral(10000)