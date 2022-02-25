#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#
answer = 0

tmp_ascii = dict()
for i in range(1, 27):
    tmp_ascii[chr(96 + i)] = i // 3 + 1


def countSubstrings(input_str):
    # Write your code here
    global answer
    global tmp_ascii

    for i in range(len(input_str)):
        cur_sum = 0
        answer += 1
        for j in range(i, len(input_str)):
            cur_sum += tmp_ascii[input_str[j]]
            if j - i != 0 and cur_sum % (j - i + 1) == 0:
                answer += 1

    return answer

if __name__ == '__main__':
    print(countSubstrings('bef'))