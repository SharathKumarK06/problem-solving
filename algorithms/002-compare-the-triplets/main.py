#!/bin/python3

import os


def compareTriplets(a, b):
    # Check if array length is not 3
    if not (len(a) == len(b) == 3):
        return

    # Check if any element of a or b out of bound
    for i in a + b:
        if 1 >= i >= 100:
            return

    result = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
            pass
        else:
            continue
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

