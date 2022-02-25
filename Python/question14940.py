# 쉬운 최단거리
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상, 하, 좌, 우


def is_possible(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


if __name__ == '__main__':
    n, m = map(int, input().split(" "))

    input_map = list()

    target_i = -1
    target_j = -1

    for i in range(n):
        input_map.append(list(map(int, input().split(" "))))
        if target_i == -1: # 목표지점을 찾지 못했으면,
            for j in range(m):  # 목표지점 탐색
                if input_map[i][j] == 2:
                    target_i = i
                    target_j = j
                    break

    # 거리 결과를 담을 리스트
    result_map = [[-1 for j in range(m)] for i in range(n)]

    result_map[target_i][target_j] = 0
    to_visit = list()
    to_visit.append([target_i, target_j])

    while to_visit:
        i, j = to_visit.pop(0)
        cur = result_map[i][j]
        for _ in range(4):      # 상하좌우 확인하면서
            x = i + dx[_]
            y = j + dy[_]
            if is_possible(n, m, x, y): # 범위 내 값인지 확인
                if input_map[x][y] == 0:
                    continue
                elif target_i == x and target_j == y:
                    continue
                elif result_map[x][y] == -1 or result_map[x][y] > cur + 1:   # 방문한 적 없는지 확인, 방문했어도 최단경로면 업데이트
                    result_map[x][y] = cur + 1
                    to_visit.append([x, y])

    for i in range(n):      # 원래 못가는 땅은 0으로 출력.
        for j in range(m):
            if input_map[i][j] == 0:
                result_map[i][j] = 0

    for i in range(n):
        for j in range(m):
            print(result_map[i][j], end=' ')
        print()