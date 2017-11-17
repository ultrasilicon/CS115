'''
CS 115, Sky OOP Activity

Author: <your name here>
Pledge: <write pledge>
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement the missing sections of the Star class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import math
from random import randint

class Star(object):

    def __init__(self, x, y):
        '''Initializes the PRIVATE fields x and y with the values received as
        arguments. You may assume x and y are valid integers.'''
        self.__x = x
        self.__y = y

    # Write properties for x and y.
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Write the method that checks if this Star is equal to another Star here.
    # Two Stars are equal if their x and y coordinates are equal. Be sure
    # to overload the correct operator for use with ==.
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def distance_to(self, other):
        '''Computes the distance to the other Star passed as an argument to
        the method.
        Recall the distance formula (not written in valid Python syntax):
        d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
        '''
        return math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)

    def __str__(self):
        '''Returns the string representation of the location of the Star, such
        as (3, 2) or (-1, 5). Note the space after the comma.'''
        return '(' + str(self.__x) + ', ' + str(self.__y) + ')'


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Implement the missing sections of the Sky class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sky(object):

    def __init__(self):
        '''Initializes the Sky object with between 5-10 Stars randomly
        generated.'''
        self.__stars = []
        for _ in range(randint(5, 10)):
            self.__stars.append(Star(randint(-100, 100), randint(-100, 100)))

    def westernmost_star(self):
        '''Returns the westernmost Star in the Sky (Star with the lowest x
        value).'''
        min = self.__stars[0].x
        ind = 0
        for i in range(len(self.__stars)):
            if self.__stars[i].x < min:
                ind = i
                min = self.__stars[i].x
        return self.__stars[ind]

    def northernmost_star(self):
        '''Returns the northernmost Star in the Sky (Star with the highest y
        value).'''
        max = self.__stars[0].y
        ind = 0
        for i in range(len(self.__stars)):
            if self.__stars[i].y > max:
                ind = i
                max = self.__stars[i].y
        return self.__stars[ind]



    def __str__(self):
        '''Returns a string representation of the list of coordinates of the
        Stars in the Sky.'''
        return '[' + ', '.join(map(str, self.__stars)) + ']'

if __name__ == '__main__':
    star1 = Star(3, 6)
    star2 = Star(4, -3)
    print('Star 1: %s' % star1)
    print('Star 2: %s' % star2)
    print('Star 1\'s x-coordinate: %d' % star1.x)
    print('Star 2\'s y-coordinate: %d' % star2.y)
    print('Stars equal? %s' % (star1 == star2))
    print('Distance? %.2f' % star1.distance_to(star2))

    sky = Sky()
    print('\nStars in sky at:')
    print(sky)
    print('Westernmost star at: %s' % sky.westernmost_star())
    print('Northernmost star at: %s' % sky.northernmost_star())
