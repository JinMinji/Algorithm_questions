# 2750 수 정렬하기
# sorting algorithm 문제

number = int(input())

sorted_list = []

for _ in range(number):
    num = int(input())
    sorted_list.append(num)

sorted_list.sort()

for _ in sorted_list:
    print (_)
