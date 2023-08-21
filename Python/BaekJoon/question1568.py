bird = int(input())

i = 1
time = 0
num = 0

while num < bird:
    if num + i <= bird:
        num += i
    else :
        i = 1
        num += i
    i += 1
    time += 1

print(time)