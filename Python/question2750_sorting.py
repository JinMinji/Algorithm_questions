# 버블정렬로 풀어보기

number = int(input())

array = []

for _ in range(number):
    num = int(input())
    array.append(num)

for i in range(0, number):
    for j in range(1, number-i):
        if array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]

for _ in array:
    print (_)