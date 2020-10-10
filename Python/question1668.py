def tcount(array):
    top = array[0]
    count = 1
    for i in array:
        if i > top:
            count += 1
            top = i
    return count

case_num = int(input())

trophies = list()

for i in range(case_num):
    trophies.append(int(input()))

print(tcount(trophies))
trophies.reverse()
print(tcount(trophies))