#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reachTheEnd' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER maxTime
#
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def is_possible(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.'


def find_course(grid, cur_time, cur, to_visit, visited, maxTime):
    i, j = cur
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return True

    if cur_time >= maxTime:
        return False

    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if is_possible(grid, x, y):
            cur_time += 1


def reachTheEnd(grid, maxTime):
    # Write your code here
    cur = [0, 0]
    visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    to_visit = list()
    to_visit.append(cur)
    cur_time = 0

    answer = 'No'

    while to_visit:
        i, j = to_visit.pop(0)
        if visited[i][j] == 0:
            visited[i][j] = 1
            for _ in range(4):
                x = i + dx[_]
                y = j + dy[_]
                if visited[x][y] == 0 and is_possible(grid, x, y):
                    cur_time += 1
                    if find_course(grid, cur_time, [x, y], to_visit, visited, maxTime):
                        return 'Yes'

                    cur_time -= 1

    return answer

if __name__ == '__main__':
    print(reachTheEnd(['..', '..'], 3))