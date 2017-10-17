'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def completeFiveDigit(s):
    return "0" * (5 - len(s)) + s

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def compress(s):
    def compress_helper(s, buf):
        if s == "":
            return [buf]
        if s[0] != buf[0]:
            if buf[1] != 0:
                return [buf] + compress_helper(s[1:], [s[0]] + [1])
        return compress_helper(s[1:], [s[0]] + [buf[1] + 1])

    def compress_by_section(lst, maxLen):
        if lst == []:
            return ""
        if lst[0][1] >= maxLen:
            return "1111100000"  + compress_by_section([lst[0][0] + [lst[0][1]-31]] + lst[1:], maxLen)
        return completeFiveDigit(numToBinary(lst[0][1] - 1)) + compress_by_section(lst[1:], maxLen)

    if s[0] == "1":
        return "00000" + compress_by_section(compress_helper(s, ["0",0]), MAX_RUN_LENGTH)[1:]
    else:
        return compress_by_section(compress_helper(s, ["0",0]), MAX_RUN_LENGTH)



def decompress(s):
    def decompress_by_section(s, blockSize):
        if s == "":
            return []
        if len(s) < blockSize:
            return [binaryToNum(s)]
        return [binaryToNum(s[0:blockSize]) + 1] + decompress(s[blockSize:]) # first arg +1


    # def decompress_helper(lst):
        # if lst == []:
        #     return ""
        # return ("0" if zero else "1" )* lst[0]

    return decompress_by_section(s, COMPRESSED_BLOCK_SIZE)


print(decompress(compress("10001100000111100001111000011110")))







