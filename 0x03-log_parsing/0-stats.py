#!/usr/bin/python3
"""
this module for interview project log parsing
"""
from sys import stdin
from re import fullmatch


def printOutput(totalSize, status):
    """print status numbers"""
    print(f"File size: {totalSize}")
    for key, value in sorted(status.items()):
        print('{}: {}'.format(key, value))


def run():
    """run code"""
    try:
        while True:
            # count = 0
            status = {
                "200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0
            }
            totalSize = 0
            for _ in range(10):
                line = stdin.readline()[:-1]
                pattern = (
                    r'^(\d+\.\d+\.\d+\.\d+) - '
                    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
                    r'"GET (.+)" '
                    r'(\d{3}) '
                    r'(\d+)$'
                )
                if fullmatch(pattern, line):
                    statusCode = fullmatch(pattern, line).group(4)
                    responseSize = int(fullmatch(pattern, line).group(5))
                    if statusCode in status:
                        status[statusCode] += 1
                    totalSize += int(responseSize)
                else:
                    continue
            printOutput(totalSize, status)
    except (KeyboardInterrupt, EOFError):
        printOutput(totalSize, status)


if __name__ == '__main__':
    run()
