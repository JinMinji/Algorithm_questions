# 계수정렬 알고리즘 Counting Sort
# 수의 범위가 제한되어있을 때 사용가능, 빠름
# 데이터의 개수가 많을 때, input은 readline이용
import sys

casenum = int(input())

list = []
for _ in range(10001):
    list.append(0)
# == list = [0]*10001

for _ in range(casenum):
    value = int(sys.stdin.readline())
    list[value] += 1

for i in range(len(list)) :
    if list[i] != 0:
        for j in range(list[i]):
            print(i)
