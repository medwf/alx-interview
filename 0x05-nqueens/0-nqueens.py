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

    def __init__(self, N) -> None:
        """
        initialize what we need to solve this problem.

        Args:
            N <int> : The number of Queen,
                        and size of board chessboard NxN.
        """
        self.N = N
        self.chessboard = [[0 for _ in range(N)] for _ in range(N)]
        self.solutions = []
        self.positions = []

    def solve(self, column=0):
        """Helps Start solving this problem"""
        # 1. The Goal
        if column == self.N:
            position = [[0 for _ in range(self.N)] for _ in range(self.N)]
            # add solution to self.solutions and return
            solution = []
            for Row in range(self.N):
                for Column in range(self.N):
                    if self.chessboard[Row][Column] == 1:
                        solution.append([Row, Column])
                        position[Row][Column] = self.chessboard[Row][Column]
            if sum(position[0]) == 1:
                self.positions.append(position)
            self.solutions.append(solution)
            return
        # 2. choice
        for row in range(self.N):
            # 3. constraint
            if not self.underAttack(row, column):
                self.chessboard[row][column] = 1
                self.solve(column + 1)
                self.chessboard[row][column] = 0

    def underAttack(self, row, column) -> bool:
        """check constraint of this problem.
        Return:
            True: if under attack
            False: if not
        """
        Attacked = False
        Attacked = self.checkRow(row, column)
        if not Attacked:
            Attacked = self.checkDiagonal(row, column)
        return Attacked

    def checkRow(self, row, column):
        """check if it under attack in same row"""
        for i in range(self.N):
            if self.chessboard[row][i] == 1:
                return True
        return False

    def checkDiagonal(self, row, colum):
        """check if it under attack in same diagonal"""
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
        columUp = colum - 1
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
        rowRight = row + 1
        columDown = colum + 1
        while rowRight < self.N and columDown < self.N:
            if self.chessboard[rowRight][columDown] == 1:
                return True
            rowRight += 1
            columDown += 1
        return False

    def result(self):
        """print result"""
        for solution in self.solutions:
            print(solution)

    def resultGraph(self):
        """print Queen position in chessboard"""
        print("\nChessboard :\n")
        for index, position in enumerate(self.positions):
            print(f"\tSolution {index + 1}:")
            for row in position:
                for index, column in enumerate(row):
                    if index == 0:
                        print('\t\t', end='')
                    if index <= self.N:
                        print("|", end='')
                    if column == 1:
                        print(" Q ", end='')
                    else:
                        print(" . ", end='')
                print("|")
            print()


if __name__ == "__main__":
    positions_of_all_queen = NQueen(N=checkUsage())
    positions_of_all_queen.solve()
    positions_of_all_queen.result()
    # if you want to print graphic position plz try it.
    # positions_of_all_queen.resultGraph()
