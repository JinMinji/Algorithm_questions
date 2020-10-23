# ATM문제 2021.05.03

num = int(input())

times = list(map(int, input().split(' ')))

times.sort()

result = 0

for i in range(len(times)+1):
    for j in range(i):
        result += times[j]

print(result)