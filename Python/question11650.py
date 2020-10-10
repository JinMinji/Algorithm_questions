casenum = int(input())

pos_list = []

for _ in range(casenum):
    x, y = input().split()
    x, y = int(x), int(y)
    pos_list.append((x, y))

pos_list = sorted(pos_list, key=lambda x: x[1])
pos_list = sorted(pos_list, key=lambda x: x[0])
#pos_list = sorted(pos_list)
# 기본적으로 튜플에서는, 알아서 다음원소도 정렬해줌.

for i in pos_list:
    print(i[0], i[1])

