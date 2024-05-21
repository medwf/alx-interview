#!/usr/bin/python3
"""
This module for method UTF-8 Validation
"""
from typing import List, Union


def validUTF8(data: List[int]):
    """
    determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data List[int]: list of integer.

    return:
        True if data is valid UFT8 else False
    """
    for char in data:
        if char > 254:
            return False
    return True
