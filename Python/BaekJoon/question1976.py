# 20210507 여행가자!

N = int(input())    #도시 개수

M = int(input())    #여행할 도시 수

roads = list()

for _ in range(N):
    roads.append(list(map(int, input().split(" "))))

plan = list(map(int, input().split()))      #index+1 인 상태

visited = list()
temp = list()

visited.append(plan[0]-1)
temp.append(plan[0]-1)

while len(temp) > 0:
    i = temp.pop(0)
    for n in range(len(roads[i])):
        if roads[i][n] == 1:
            if n not in visited:
                visited.append(n)
                temp.append(n)

# index기준으로 변경한 상태이므로, 다시 -1해서 탐색

can = True
for _ in plan:
    if _-1 not in visited:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")



