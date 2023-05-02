#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaximumMex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER x
#

def getMaximumMex(arr, x):
    # Write your code here
    # 빼거나, 더할 수 있다.
    arr.sort()

    tmp_set = list(set(arr))

    answer = 0

    for i in range(len(arr)):
        # print(tmp_set[i], i)
        if i not in arr:
            # add
            j = i - x
            while j >= 0:
                if arr.count(j) > 1:
                    arr[arr.index(j)] = i
                    break
                else:
                    j -= x

            if j >= 0:
                continue


            else:
                j = i + x
                while j <= len(tmp_set) + 1:
                    if arr.count(j) > 0:
                        arr[arr.index(j)] = i
                        break
                    else:
                        j += x

                if j <= len(tmp_set) + 1:
                    continue

                else:
                    answer = i
                    break

    return answer


if __name__ == '__main__':
    # print(getMaximumMex([1, 3, 4], 2))
    print(getMaximumMex([0, 1, 2, 2, 0, 0, 10], 3))
