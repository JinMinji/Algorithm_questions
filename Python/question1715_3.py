#20210513 카드 정렬하기 두번쨰풀이
import heapq

N = int(input())
cards_num = list()

for _ in range(N):
    heapq.heappush(cards_num, int(input()))

result = 0

while len(cards_num) >= 2:
    num1 = heapq.heappop(cards_num)
    num2 = heapq.heappop(cards_num)

    result += num1 + num2
    heapq.heappush(cards_num, num1 + num2)

print(result)
