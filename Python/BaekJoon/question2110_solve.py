# Gap의 최댓값을 이진탐색으로 찾는다.

house, router = map(int, input().split(" "))

houses = list()
for i in range(house):
    houses.append(int(input()))

houses.sort()

max_gap = houses[-1]-houses[0]
min_gap = houses[1]-houses[0] #이건 약간 이해가 안됨.

result = 0

while min_gap <= max_gap:
    mid = (max_gap+min_gap)//2
    value = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if houses[i] >= value + mid:
            count += 1
            value = houses[i]
    if count >= router:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid - 1
print(result)



