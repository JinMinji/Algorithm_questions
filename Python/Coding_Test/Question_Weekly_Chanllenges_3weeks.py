# 2021 네이버 상반기 4번 문제
# 퍼즐조각 채우기

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def solution(game_board, table):
    answer = -1

    visited = [[0 for j in range(table[0])] for i in range(len(table))]


    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1 and visited[i][j] == 0:
                pass


    return answer