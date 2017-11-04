"""
Created on Nov 02 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - lab9
"""

from cs5png import *

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """

    """if it is or, all the pixel with x or y that can be divided by 10 is painted black, which shows grids with width 10."""
    if col%10 == 0  and  row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

def mult(c, n):
    """ mult uses only a loop and addition
        to multiply c by the integer n
    """
    result = 0
    for x in range(n):
        result += c
    return result


def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c
         for a total of n times. It returns the final z.
    """
    z = 0
    for x in range(n):
        z = z ** 2 + c
    return z


def inMSet(c, n):
    """ inMSet takes in
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
        Then, it should return
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    i = 0
    for x in range(n):
        z = z ** 2 + c
        if abs(z) >=2:
            return False
    return True


def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in
            pix, the CURRENT pixel column (or row)
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that corresponds to pix
    """
    return floatMin + (floatMax - floatMin) / pixMax * pix


def mset(width, height):
    """ creates a width * height image of the Mandelbrot set
    """
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()



# print(scale(100, 200, -1.5, 1.5))
mset(300,200)
# test()