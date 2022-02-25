dx = [0, 1, 0, +1]  # → ↓ ← ↑
dy = [1, 0, -1, 0]


def solution(n, jump):
    answer = [[0 for i in range(n)] for i in range(n)]

    answer[0][0] = 1
    cur_x = 0   # 현재 x
    cur_y = 1   # 현재 y
    cnt = 0     # 상하좌우 진행 방향을 전환해줄 cnt 변수
    j_cnt = 0   # jump한 개수를 담을 변수
    cur_num = 1 # 현재 위치에 담을 숫자. 1~n*n


    while 0 in answer:
        if answer[cur_x][cur_y] == 0:
            if j_cnt == jump:
                cur_num += 1
                answer[cur_x, cur_y] = cur_num
                j_cnt = 0

            else:
                j_cnt += 1

        cur_x += dx[cnt % 4]
        cur_y += dy[cnt % 4]

    return answer


if __name__ == '__main__':
    print(solution(5, 3))
    print(solution(4, 1))
    print(solution(3, 10))