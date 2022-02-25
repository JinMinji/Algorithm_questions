from itertools import combinations


def solution(n, info):
    answer = [-1]   # 이길 방법이 없으면 [-1]

    info.reverse()    # 0점부터 10점 순서로 볼 수 있게 reverse

    can_pick = list()

    for i in range(len(info)):
        for j in range(info[i]+1):
            can_pick.append(i)

    check_list = list(combinations(can_pick, n))

    max_gap = 0

    for i in range(len(check_list)):
        tmp_score = [0 for i in range(11)]
        for j in check_list[i]:
            tmp_score[j] += 1

        tmp_ryan = 0
        tmp_apeach = 0

        for k in range(len(info)):
            if tmp_score[k] > info[k]:
                tmp_ryan += k

            elif info[k] > 0:
                tmp_apeach += k

        if max_gap < tmp_ryan - tmp_apeach:
            max_gap = tmp_ryan - tmp_apeach
            answer = list(reversed(tmp_score))

    return answer


if __name__ == '__main__':
    print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))