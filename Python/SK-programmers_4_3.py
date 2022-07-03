# 제출코드 - 백트래킹

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_best_way(grid, k, visited, cur, rest_k, n):
    global answer

    i, j = cur
    # print(i, j)
    if i == len(grid) - 1 and j == len(grid[0]) - 1:  # 도착지점이면 현재상태와 비교하여 answer 업데이트
        if answer > n:
            answer = n

    if rest_k == 0:  # 남은 이동횟수가 없을 때
        if grid[i][j] == '.':  # 아니면 평지일 경우 야영하거나,
            rest_k = k
            find_best_way(grid, k, visited, cur, rest_k, n + 1)

        else:  # 평지가 아니면 탐색중단.
            pass

    else:  # 남은 이동횟수가 있을 때
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):    #범위 내에 있는지 확인
                if grid[x][y] != '#' and visited[x][y] == 0 and n < answer:     # 강이 아니면서 방문하지 않은 곳일 경우
                    visited[x][y] = 1
                    find_best_way(grid, k, visited, [x, y], rest_k - 1, n)      #이동횟수를 소무하여 확인해본다.
                    visited[x][y] = 0

                if grid[x][y] == '.' and visited[x][y] == 0 and n + 1 < answer:   # 평지면, 야영도 해본다.
                    visited[x][y] = 1
                    find_best_way(grid, k, visited, [x, y], k, n+1) #이동횟수는 k로, 야영횟수는 + 1
                    visited[x][y] = 0


def solution(grid, k):
    global answer
    answer = float('inf')
    visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    visited[0][0] = 1
    find_best_way(grid, k, visited, [0, 0], k, 0)

    return answer


if __name__ == "__main__":
    # print(solution(["..FF", "###F", "###."], 4))
    print(solution(["..FF", "###F", "###."], 5))
    print(solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6))
