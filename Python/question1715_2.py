#20210513 카드정렬하기. 옛날에 풀었던 문제

N = int(input())
cards_num = list()

for _ in range(N):
    cards_num.append(int(input()))

cards_num.sort()

result = 0

while len(cards_num) >= 2:
    num1 = cards_num.pop(0)
    num2 = cards_num.pop(0)

    result += num1 + num2
    cards_num.append(num1 + num2)
    cards_num.sort()

print(result)