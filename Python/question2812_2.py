#20210513 크게만들기 두번째풀이


N, K = map(int, input().split(" "))

number = input()

list_number = list()
for _ in number:
    list_number.append(int(_))

result = list()

while K > 0:
    if K+1 < len(list_number):
        max_val = max(list_number[:K+1])
    elif K < len(list_number):
        max_val = max(list_number[:K])
    else:
        list_number = []
        break
    for i in range(K+1):
        if list_number[i] == max_val:
            K = K-len(list_number[:i])
            result.append(list_number[i])
            list_number = list_number[i:]
            list_number.pop(0)
            break

result.extend(list_number)


print(''.join(map(str, result)))

