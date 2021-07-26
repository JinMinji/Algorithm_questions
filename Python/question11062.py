#20210719 카드 게임

dp = list()
cards = list()


def best_strategy(left, right, cnt):
    if left > right:
        return 0

    elif dp[left][right] != -1:
        return dp[left][right]

    else:
        if cnt%2 == 0:  #근우 차례, 근우가 큰 수를 가져갈 수 있도록.
            dp[left][right] = max(cards[left] + best_strategy(left+1, right, cnt+1), cards[right]+best_strategy(left, right-1, cnt+1))
            return dp[left][right]

        else:  #명우 차례, 명우가 적은 수를 가져갈 수 있도록 만들어야함.
            dp[left][right] = min(best_strategy(left + 1, right, cnt + 1), best_strategy(left, right - 1, cnt + 1))
            return dp[left][right]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        C = int(input())
        cards = list(map(int, input().split()))
        dp = [[-1 for i in range(len(cards))] for j in range(len(cards))]
        result = best_strategy(0, len(cards)-1, 0)  # left, right와 현재 차례를 넣어줌. 근우차례인지, 명우차례인지 구분.
        print(result)