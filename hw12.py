"""
Created on Dec 06 2017
@author: Han Zheng
Pledge: "I pledge my honor that I have abided by the Stevens Honor System." - hzheng12 
 
CS115 - hw12
"""


class Board(object):
    def __init__(self, width = 7, height = 6):
        """This is a constructor for Board objects that (in addition to self) takes two named arguments,
        one for the number of rows and one for the number of columns. """
        self.width = width
        self.height = height
        self.data = [[' ' for i in range(width)] for i in range(height)]

    def __str__(self):
        """This method returns a string (it does not print a string) representing
the Board object that calls it."""
        ret = ""
        for r in self.data:
            for x in r:
                ret += "|" + x
            ret += "|\n"
        ret += "-" * (self.width * 2 + 1) + "\n"
        for i in range(self.width):
            ret += " " + str(i)
        return ret

    def allowsMove(self, col):
        """This method should return True if the calling Board object can allow a move into column c (because there is space available).
        It returns False if c does not have space available or if it is not a valid column. """
        if not ((col < self.width) and (col > -1)):
            return False
        space = 0
        for x in range(self.height):
            space += 1 if self.data[x][col] == " " else 0
        return space > 0

    def addMove(self, col, ox):
        """This method should add an ox checker,
        where ox is a variable holding a string that is either "X" or "O", into column col."""
        if self.allowsMove(col):
            for x in range(self.height):
                if self.data[x][col] != " ":
                    self.data[x - 1][col] = ox
                    return
            self.data[self.height - 1][col] = ox

    def setBoard(self, move_string):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col < self.width:
                self.addMove(col, nextCh)
            nextCh = 'O' if nextCh == 'X' else 'X'

    def delMove(self,col):
        """This method should do the "opposite" of addMove. That is, it should remove the top checker from the column col.
        If the column is empty, then delMove should do nothing. """
        if (col < self.width) and (col > -1):
            for x in range(self.height):
                if self.data[x][col] != " ":
                    self.data[x][col] = " "
                    return

    def winsFor(self, ox):
        """This method should return True if the given checker, 'X' or 'O', held
in ox, has won the calling Board. It should return False otherwise."""
        def reverse(d):
            """return a reversed data set"""
            ret = []
            for row in d:
                r = []
                for x in reversed(row):
                    r.append(x)
                ret.append(r)
            return ret

        def diagnal(d, width, height):
            """see if there is a four in diagnal"""
            for diagonal in range(height + width - 1):
                count = 0
                for w in range(width):
                    h = diagonal - w
                    if h < 0:
                        break
                    if diagonal > width - 1:
                        if not w <= diagonal - width:
                            if d[w][h] == ox:
                                count += 1
                                if count > 3:
                                    return True
                            else:
                                count = 0
                    else:
                        if d[w][h] == ox:
                            count += 1
                            if count > 3:
                                return True
                        else:
                            count = 0
            return False

        for col in range(self.width):
            count = 0
            for row in range(self.height):
                if self.data[row][col] == ox:
                    count += 1
                    if count > 3:
                        return True
                else:
                    count = 0

        for row in range(self.height):
            count = 0
            for col in range(self.width):
                if self.data[row][col] == ox:
                    count += 1
                    if count > 3:
                        return True
                else:
                    count = 0

        return diagnal(self.data, self.width, self.height) \
               or diagnal(reverse(self.data), self.width, self.height)

    def hostGame(self):
        """This is a method that, when called from a connect four board object,
        will run a loop allowing the user(s) to play a game. """
        print("Welcome to Connect Four!")
        role = "O"
        while True:
            if self.winsFor(role):
                print(role + " wins -- Congratulations!")
                print(self)
                break
            role = "X" if role == "O" else "O"

            print(self)
            move = int(input(role + "'s choice: "))
            if not self.allowsMove(move):
                print("\n")
                continue
            print("\n")
            self.addMove(move, role)


board = Board(8,8)
board.hostGame()
