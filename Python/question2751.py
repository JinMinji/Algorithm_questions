# 고급정렬, 그러나 문제유형이 뻔하므로 빨리풀어야하는 문제
# 공간복잡도보다 시간복잡도가 중요하다면 pypy3
# NlogN

input_num = int(input())

num_list = []
for i in range(input_num):
    num_list.append(int(input()))

num_list = sorted(num_list)

for i in num_list:
    print(i)