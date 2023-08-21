#주사위 쌓기, 골드 4
import sys
sys.setrecursionlimit(10**5)

def max_dice(pre_top, cur, cur_total):
    global N, result, dices, set_side

    if cur >= N:
        #0~N-1 까지의 dices를 돌면 N개의 dice를 모두 확인한 것이므로
        #여기에서의 total 값으로 return
        result = max(result, cur_total)
        # print(result, cur)
        return

    bottom_idx = dices[cur].index(pre_top)
    top_idx = set_side[bottom_idx]

    tmp = list()
    for i in range(1, 7):   #위, 아랫면의 숫자를 제외하고 max 값을 한 면으로 몬다.
        if i != dices[cur][bottom_idx] and i != dices[cur][top_idx]:
            tmp.append(i)

    tmp_max = max(tmp)

    # print(cur, cur_total, tmp_max)
    max_dice(dices[cur][top_idx], cur+1, cur_total+tmp_max)


if __name__ == "__main__":
    N = int(input())

    dices = list()
    for i in range(N):
        dices.append(list(map(int, input().split())))

    set_side = dict()
    # 0 <-> 5
    # 1 <-> 3
    # 2 <-> 4
    set_side[0] = 5
    set_side[1] = 3
    set_side[2] = 4
    set_side[3] = 1
    set_side[4] = 2
    set_side[5] = 0

    # 맨 첫번째 주사위의 바닥면을 고른 후, 이후를 탐색하여 최댓값을 갱신해준다.
    result = 0
    for i in range(1, 7):
        # cur_bottom = i
        # cur_top = set_side[i]
        # tmp = list()
        # for i in range(1, 7):  # 위, 아랫면의 숫자를 제외하고 max 값을 한 면으로 몬다.
        #     if i != dices[0][cur_bottom] and i != dices[0][cur_top]:
        #         tmp.append(i)

        # tmp_total = max(tmp)
        max_dice(i, 0, 0)

    print(result)