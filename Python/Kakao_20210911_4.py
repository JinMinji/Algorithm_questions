from itertools import permutations

for i in range(k, 11):
    if apeach[i] < n:
        ryan[i] = apeach[i] + 1
        solve(n - ryan[i], i + 1)
        ryan[i] = 0
        solve(n, i + 1)

    else:
        for j in range(0, n + 1):
            ryan[i] = j
            solve(n - j, i + 1)
            ryan[i] = 0
            solve(n, i + 1)

def solution(n, info):
    answer = [-1]
    # n의 범위가 10이고, info의 범위도 0~11이므로! 다 돌아보자
    score = [i for i in range(11)]
    per_score = list(permutations(score, n))

    max_gap = 0
    for i in range(len(per_score)):
        tmp_score = [0 for i in range(11)]

        for j in range(len(per_score[i])):
            tmp_score[per_score[i][j]] += 1

        tmp_ryan = 0
        tmp_apeach = 0

        for _ in range(11):
            if tmp_score[_] > info[_]:
                tmp_ryan += _

            else:
                tmp_apeach += _

        tmp_gap = tmp_ryan - tmp_apeach
        if max_gap < tmp_gap:
            max_gap = tmp_gap

            tmp_score.reverse()
            answer = tmp_score

    return answer


if __name__ == '__main__':
    print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))