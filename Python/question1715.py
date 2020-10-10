# 그리디
import heapq
case_num = int(input())

cards = list()
for i in range(case_num):
    heapq.heappush(cards,int(input()))

result = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    new_card = card1 + card2
    result += new_card
    heapq.heappush(cards, new_card)

print(result)