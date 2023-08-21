#방 번호, 골드 3
import sys

def find_max(min_cost, ):
    pass

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    costs = list()
    for i in range(N):
        costs = list(map(int, sys.stdin.readline().split()))

    money = int(sys.stdin.readline())

    #0을 제외하고 최소비용
    start_min_cost = min(costs[1:])
    start_min_num = costs.index(start_min_cost)

    #0을 포함한 최소비용
    min_cost = min(costs)
    cost_min_num = costs.index(min_cost)

    #자릿수가 클수록 큰 수
    #동일한 자릿수일 경우 큰숫자를 앞으로

    # 적어도 하나의 숫자는 만들 수 있음.
    if money // min_cost < 2:
        print(cost_min_num)
    else:
        if min_cost == 0:
            money - start_min_cost

        else:
            find_max(money - (money // min_cost)*min_cost, )
