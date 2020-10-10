# 해시문제라해도, python 에서는 그냥 딕셔너리 사용해서 풀어도 됨
num = int(input())
nset = set(map(int, input().split()))
casenum = int(input())
k = list(map(int, input().split()))

for _ in k:
    if _ not in nset:
        print('0')
    else:
        print('1')




