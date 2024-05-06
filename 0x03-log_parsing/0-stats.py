#!/usr/bin/python3
"""
Log parsing
"""
from sys import stdin


def print_stats(stats: dict, file_size: int) -> None:
    """a methods that print output status"""
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


def run():
    """run code"""
    filesize, count = 0, 0
    stats = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
        }
    try:
        for line in stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise


if __name__ == '__main__':
    run()
