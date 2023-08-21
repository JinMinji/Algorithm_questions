# 가장 인접한 공유기 사이의 최대거리
house, router = map(int, input().split(" "))

houses = list()
for i in range(house):
    houses.append(int(input()))

houses.sort()

max_gap = houses[-1]-houses[0]    # 공유기 사이 최대거리는 첫번째집 ~ 마지막집
min_gap = houses[1]-houses[0]     # 일단 최소 하나 간격은 떨어지므로, 첫번째와 두번째 집 사이 거리를 최소거리로 둔다.

result = 0

while min_gap <= max_gap:
    mid_gap = (min_gap+max_gap)//2
    router_num = router - 1 #맨 처음에 하나 설치하므로 -1
    house_index = 0
    for i in range(1, len(houses)):
        if houses[i] - houses[house_index] >= mid_gap:
            router_num -= 1
            house_index = i

    if router_num <= 0:
        min_gap = mid_gap + 1
        result = mid_gap
    else:
        max_gap = mid_gap - 1

print(result)



