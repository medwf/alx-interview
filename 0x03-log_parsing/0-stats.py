#!/usr/bin/python3
"""
this module for interview project log parsing
"""
from sys import stdin
from re import match


def run():
    """run code"""
    while True:
        status = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
        totalSize = 0
        for _ in range(0, 10):
            line = stdin.readline()
            pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET (.+)" (\d{3}) (\d+)$'
            if match(pattern, line):
                # ipAddress = match(pattern, line).group(1)
                # dateTime = match(pattern, line).group(2)
                # requestedPath = match(pattern, line).group(3)
                statusCode = match(pattern, line).group(4)
                responseSize = int(match(pattern, line).group(5))
                status[statusCode] += 1
                totalSize += int(responseSize)
            else:
                continue
        print(f"File size: {totalSize}")
        for key, value in status.items():
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    run()
