def solution(rows, columns):
    answer = [[0 for i in range(columns)] for i in range(rows)]

    cur_r = 0
    cur_c = 0
    cur_cnt = 1

    answer[0][0] = cur_cnt

    visit_state = [[0 for i in range(columns)] for i in range(rows)]
    visit_state[cur_r][cur_c] = 2

    while any(0 in i for i in answer):
        # 추가조건 : 더 이상 0이 쓰여 있는 칸에 다른 숫자를 쓸 수 없게 된다면 -?
        if cur_cnt % 2 == 0:  # 짝수라면
            cur_r += 1
            if cur_r >= rows:
                cur_r = 0

            if visit_state[cur_r][cur_c] != 2:
                visit_state[cur_r][cur_c] = 2
                cur_cnt += 1
                answer[cur_r][cur_c] = cur_cnt
            else:
                break

        else:  # 홀수라면
            cur_c += 1
            if cur_c >= columns:
                cur_c = 0

            if visit_state[cur_r][cur_c] != 1:
                visit_state[cur_r][cur_c] = 1
                cur_cnt += 1
                answer[cur_r][cur_c] = cur_cnt

            else:
                break

        for i in range(len(answer)):
            print(answer[i])

        print()

    return answer


if __name__ == '__main__':
    print(solution(3, 4))
    print(solution(3, 3))