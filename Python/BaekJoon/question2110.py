house, router = map(int, input().split(" "))

houses = list()
for i in range(house):
    houses.append(int(input()))

houses.sort()
routers = list()
routers.append(houses[0])
routers.append(houses[-1])
# 일단, 양 끝에 공유기를 넣어준다.
router -= 2
# 잔여 공유기의 개수

def pick_router(array):
    global router
    if len(array) <= 2:
        return
    if router == 0:
        return

    mid = len(array)//2
    minus = mid
    plus = mid

    for i in range(len(array)):
        if minus == array[i]:
            routers.append(minus)
            router -= 1
            return pick_router(array[:i]), pick_router(array[i:])

        if plus == array[i]:
            routers.append(plus)
            router -= 1
            return pick_router(array[:i]), pick_router(array[i:])

        minus -= 1
        plus += 1

pick_router(houses)

routers.sort()
min_val = routers[1]-routers[0]

for i in range(1,len(routers)):
    if min_val > routers[i] - routers[i-1]:
        min_val = routers[i] - routers[i-1]

print(min_val)