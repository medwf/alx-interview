#!/usr/bin/python3
"""
This module have a methods:
    solving N-Queens problem:
    for N = 4

    chessboard:

        0  0  0  0
        0  0  0  0
        0  0  0  0
        0  0  0  0
"""
from sys import argv, exit

def checkUsage() -> int:
    """
    Check usage that require
        to solving NQueens problem.
    Return:
        n <int> : represent n chessboard.
    """
    if len(argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    return N

class NQueen:
    """
    class N queen
        For Solving NQueens problem.
    """

    def __init__(self, N: int) -> None:
        """
        initialize what we need to solve this problem.

        Args:
            N <int> : The number of Queen,
                        and size of board chessboard NxN.
        """
        self.N = N
        self.chessboard = [[0 for _ in range(N)] for _ in range(N)]
        self.solutions = []

    def solve(self, column=0):
        """Helps Start solving this problem"""
        # 1. The Goal
        """
            starting with colum=0
            recursive by column + 1
            end if column == 4
        """
        if column == self.N:
            # add solution to self.solutions and return
            return
        # 2. choice
        for row in range(self.N):
            # 3. constraint
            # check if under attacks (row, column)
            if self.underAttack(row, column):
                return

            # if not
            # add 1 to chessboard for queen exist
            self.chessboard[row][column] = 1
            # recursive by column + 1
            self.solve(column + 1)
            # 4. undo last choice
            # delete that 1 to 0 queen removed.
            self.chessboard[row][column] = 0
    
    def underAttack(self, row, column) -> bool:
        """check constraint of this problem.
        Return:
            True: if under attack
            False: if not
        """
        Attacked = False
        # check if it's attacked or not.
        Attacked = self.checkRow(row)
        if not Attacked:
            Attacked = self.checkDiagonal(row, column)
        return Attacked

    def checkRow(self, row):
        """check if it under attack in same row"""
        for i in range(self.N):
            if self.chessboard[row][i] == 1:
                return True

    def checkDiagonal(self, row, colum):
        """check if it under attack in same diagonal"""
        # there is four way must be check
        # 1. up, left
        rowLeft = row - 1
        columUp = colum - 1
        while rowLeft > -1 and columUp > -1:
            if self.chessboard[rowLeft][columUp] == 1:
                return True
            rowLeft -= 1
            columUp -= 1

        # 2. up, right
        rowRight = row + 1
        columUp = colum + 1
        while rowRight < self.N and columUp > -1:
            if self.chessboard[rowRight][columUp] == 1:
                return True
            rowRight += 1
            columUp -= 1

        # 3. down left
        rowLeft = row - 1
        columDown = colum + 1
        while rowLeft > -1 and columDown < self.N:
            if self.chessboard[rowLeft][columDown] == 1:
                return True
            rowLeft -= 1
            columDown += 1

        # 4. down right
        rowRight = row - 1
        columDown = colum + 1
        while rowRight < self.N and columDown < self.N:
            if self.chessboard[rowRight][columDown] == 1:
                return True
            rowRight += 1
            columDown += 1
    

if __name__ == "__main__":
    N = checkUsage()
    positions_of_all_queen = NQueen(N)
    # print(positions_of_all_queen.N)
    # print(positions_of_all_queen.chessboard)
    # print(positions_of_all_queen.solutions)

