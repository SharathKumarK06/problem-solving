#!/bin/python3

import os


def simpleArraySum(ar):
    if not (0 < len(ar) <= 1000):
        return

    items_sum = 0
    for i in ar:
        if 0 >= i or i > 1000:
            return
        items_sum += i

    return items_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

