#!/usr/bin/python3
"""
Reads stdin line by line
and computes metrics
"""
from sys import stdin


stat_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0


def print_stats():
    """
    prints the stats for input in the correct give
    every 10 lines or key interruption
    """
    print("File size: {}".format(total_size))
    for key, val in sorted(stat_codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))


if __name__ == '__main__':
    try:
        for line_num, line in enumerate(stdin, 1):
            try:
                stat = line.split()
                total_size += int(stat[-1])
                if stat[-2] in stat_codes.keys():
                    stat_codes[stat[-2]] += 1
            except:
                pass
            if not line_num % 10:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
