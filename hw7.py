"""
Created on Oct 24 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw6
"""

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')
}


def numToBaseB(N, B):
    """convert base 10 number N to the same number of base B and return."""
    if N == 0:
        return "0"
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))


def baseBToNum(S, B):
    """convert a number of base B, which is S, to the same base 10 number and return."""
    if S == "":
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])


def baseToBase(B1, B2, SinB1):
    """convert SinB1 from base B1 to base B2"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)


def add(S,T):
    """add two binary, S and T, by converting them to decimal and add them. And then return the result."""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)


def addB(S, T):
    """add two binary, S and T and return the result. This function uses full adder, and operate fully by binary."""
    diff = len(S) - len(T)
    if diff > 0:
        T = "0" * diff + T
    if diff < 0:
        S = "0" * diff + S

    def addBHelper(C, S, T):
        if S == "":
            return "" if C == "0" else "1"
        return addBHelper(FullAdder[(C, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(C, S[-1], T[-1])][0]
    return addBHelper("0", S, T)

print(addB("011", "100"))