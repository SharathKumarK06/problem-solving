#!/bin/python3

import os

max_limit = 10 ** 10


def aVeryBigSum(ar):
    if not (1 <= len(ar) <= 10):
        return

    if all(0 > i or i > max_limit for i in ar):
        return

    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

