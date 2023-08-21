#20210513 크게만들기

N, K = map(int, input().split(" "))

s_number = input()
#string으로 받는다.

list_number = list()

for i in range(len(s_number)):
    list_number.append([i, int(s_number[i])])

list_number.sort(key=lambda x : x[1])

for i in range(K):
    list_number.pop(0)

list_number.sort(key=lambda x: x[0])

#result = ''.join(str(num[1]) for num in list_number)
#print(result)

for _ in list_number:
    print(_[1], end='')


