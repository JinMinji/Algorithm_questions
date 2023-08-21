# 피자판매, 골드 2, 맞았습니다!


def pizza_cnt(pizza):
    global N
    tmp_max = max(N, sum(pizza))
    pizza_cnt = [0 for i in range(tmp_max+1)]
    pizza_cnt[0] = 1    # 0만큼 선택하는 방법도 1개

    for i in range(len(pizza)):
        cur = 0
        # i조각부터 피자조각을 선택하는 경우의 수
        for j in range(len(pizza)-1):
        # 끝까지 선택하는 것 : 전부 선택.
        # 이건 어떤 조각에서 시작하든 포함되는 경우이므로,
        # len -1 까지만 돌고, 전체를 마지막에 한번만 체크해준다.
            cur += pizza[(i+j) % len(pizza)]
            pizza_cnt[cur] += 1

    pizza_cnt[sum(pizza)] += 1

    return pizza_cnt


def two_pizza(A, B):
    global N
    result = 0
    #Pizza A에서 k크기,
    #Pizza B에서 N-k크기 만큼 가져오는 방법

    a_cnt = pizza_cnt(A)
    b_cnt = pizza_cnt(B)

    # print(a_cnt)
    # print(b_cnt)
    for i in range(N+1):
        result += a_cnt[i]*b_cnt[N-i]

    return result


if __name__ == '__main__':
    N = int(input())

    m, n = map(int, input().split())

    pizza_a = list()
    for i in range(m):
        pizza_a.append(int(input()))

    pizza_b = list()
    for i in range(n):
        pizza_b.append(int(input()))

    answer = two_pizza(pizza_a, pizza_b)

    print(answer)