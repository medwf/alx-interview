#!/usr/bin/python3
"""
This module have a methods:
    solving N-Queens problem:
"""
from sys import argv

def checkUsage() -> int:
    """
    Check usage that require
        to solving NQueens problem.
    Return:
        n <int> : represent n chessboard.
    """
    if len(argv) <= 1:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n

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



if __name__ == "__main__":
    N = checkUsage()
    positions_of_all_queen = NQueen(N)
    # print(positions_of_all_queen.N)
    # print(positions_of_all_queen.chessboard)
    # print(positions_of_all_queen.solutions)

