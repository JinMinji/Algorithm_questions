n = int(input())

tmp = []

for i in range(n+1):
    if i <= 2:
        tmp.append(i)
    else :
        tmp.append((tmp[i-1]+tmp[i-2])%15746)

print(tmp[n])