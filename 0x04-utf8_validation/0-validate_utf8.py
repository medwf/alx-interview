#!/usr/bin/python3
"""
This module for method UTF-8 Validation
"""
from typing import List


def countBytes(number: int) -> int:
    """
    Count bytes in number
    Args:
        num <int>: represent byte
    return:
        int : number of bytes.
    """
    count = 0
    # 128 == (1 << 7)
    check = 128
    while number & check:
        count += 1
        check >>= 1
    return count


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data List[int]: list of integer.

    return:
        True if data is valid UFT8 else False
    """
    NumBytes = 0
    for byte in data:
        if not NumBytes:
            NumBytes = countBytes(byte)
            if not NumBytes:
                continue
            elif NumBytes == 1 or NumBytes > 4:
                return False
        else:
            if countBytes(byte) != 1:
                return False
        NumBytes -= 1
    return NumBytes == 0
