import math

n, a, b = map(int, input().split(' '))

def find_order(a):
    row_list = []
    row = int(math.log2(a))

    if row >= 1:
        while row >= 1:
            row_list.append(2**row)
            a = a - (2 ** row)
            if a == 0:
                break
            row = int(math.log2(a))

    if a != 0:
        row_list.append(a)

    return row_list

result = 0
print(find_order(a))
for i in find_order(a):
    result += 2**(i+1)

print(find_order(b))
for i in find_order(b):
    result += 2**i

print(result)