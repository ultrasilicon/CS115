"""
Created on Nov 02 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw
"""

import random

MAX_TRIES = 7

print('''--- welcome to Guess Number ---

I\'m thinking of a number between 1 and 100.
Try to guess the number in %d attempt''' % MAX_TRIES, end='')

if MAX_TRIES > 1:
    print('s...')



def guess():
    number = random.randint(1, 100)
    tries = 0

    while tries != MAX_TRIES:
        guess = int(input('Enter guess %d: ' % tries))
        if guess < number:
            print('Too small')
        elif guess > number:
            print('Too big')
        else:
            print('\n Congratulations! You guessed the number %d, and it took you only %d tr' % (number, tries)\
                  , end=('ies.' if number > 1 else 'y.s'))
            return
        tries += 1
    print('you lose!')


guess()
