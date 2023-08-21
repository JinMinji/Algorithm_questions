#20210518 크게만들기 세번째풀이
#stack 써야함.

N, K = map(int, input().split(" "))

number = input()

list_number = list()
for _ in number:
    list_number.append(int(_))

result = list()

del_num = 0

while del_num < K:
    for i in range(N):
        if len(result) == 0 or del_num == K:
            result.append(list_number[i])
        else:
            while len(result) > 0 and list_number[i] > result[-1]:
                if del_num < K:
                    result.pop()
                    del_num += 1
                else:
                    break
            result.append(list_number[i])

result = result[:N-K]
4
print(''.join(map(str,result)))

