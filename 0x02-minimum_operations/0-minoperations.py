#!/usr/bin/python3
"""
module for minOperations function.
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations needed
        result in exactly n H characters in the file.
    """
    if (not isinstance(n, int)) or n <= 1:
        return 0
    content = 1
    oldContent = content
    content *= 2
    op = 2
    while content < n:
        if n % content == 0:
            oldContent = content
            content *= 2
            op += 2
        else:
            tmp = content
            content += oldContent
            oldContent = tmp
            op += 1
    return op
