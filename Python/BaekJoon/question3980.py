#20210804 선발배치

max_val = 0
positions = list()  #이미 배치 완료된 포지션인지 확인
member_ability = list()


def max_ability(mem, cur_sum):
    global max_val
    if mem == 11:
        max_val = max(cur_sum, max_val)
        return

    for i in range(11):
        if member_ability[mem][i] != 0 and positions[i] == 0:   # 능력치가 0이 아니면서, 아무도 포지션을 선점하지 않았을 경우
            positions[i] = 1
            max_ability(mem+1, cur_sum + member_ability[mem][i])
            positions[i] = 0


if __name__ == '__main__':
    TC = int(input())

    for _ in range(TC):
        max_val = 0
        positions = [0 for _ in range(11)]  # 초기화
        member_ability = list()
        for i in range(11):
            member_ability.append(list(map(int, input().split())))

        max_ability(0, 0)

        print(max_val)
