# 피자판매, 골드 2
def cnt(K, pizza):
    res = 0

    for i in range(len(pizza)):
        cur = pizza[i]
        if cur == K:
            res += 1
            continue
        for j in range(1, len(pizza)):
            cur += pizza[(i+j) % len(pizza)]
            if cur == K:
                res += 1
                break
            if cur > K:
                break
    return res


def cnt2(a, b):
    res = 0

    for i in range(1, N):
        res += cnt(i, a) * cnt(N-i, b)

    return res


if __name__ == '__main__':
    N = int(input())

    m, n = map(int, input().split())

    pizza_a = list()
    for i in range(m):
        pizza_a.append(int(input()))

    pizza_b = list()
    for i in range(n):
        pizza_b.append(int(input()))

    answer = cnt(N, pizza_a) + cnt(N, pizza_b) + cnt2(pizza_a, pizza_b)

    print(answer)