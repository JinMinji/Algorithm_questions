import sys
sys.setrecursionlimit(10**5)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def is_go(x, y, visited, n, k):
    if visited[x][y] == [-1, -1] or (visited[x][y][0] > n or visited[x][y][0] < k):
        return True


def find_best_way(answer, grid, k, visited, cur, rest_k, n):
    # for i in range(len(visited)):
    #     print(visited[i])
    #
    # print('----------')
    # 현재 min answer, 그리드, 이동횟수, 방문내용을 담은 list, 현재 위치, 남은 이동횟수, 현재까지의 야영횟수
    i, j = cur

    print(i, j)
    if rest_k == 0:  # 남은 이동횟수가 없을 때
        if i == len(grid) - 1 and j == len(grid[0]) - 1:  # 도착지점이면 현재상태와 비교하여 answer 업데이트
            print("In")
            if answer > n:
                answer = n
        elif grid[i][j] == '.':  # 아니면 평지일 경우 야영하거나,
            rest_k = k
            find_best_way(answer, grid, k, visited, cur, rest_k, n + 1)

        else:  # 평지가 아니면 탐색중단.
            pass

    else:  # 남은 이동횟수가 있을 때
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] != '#' and is_go(x, y, visited, n, rest_k - 1) and n < answer:
                    visited[x][y] = [n, rest_k - 1]
                    find_best_way(answer, grid, k, visited, [x, y], rest_k - 1, n)

                if grid[x][y] != '.' and is_go(x, y, visited, n+1, rest_k) and n < answer: #야영해볼수있으면 해본다.
                    find_best_way(answer, grid, k, visited, [x, y], k, n+1)


def solution(grid, k):
    answer = float('inf')
    visited = [[[-1, -1] for i in range(len(grid[0]))] for i in range(len(grid))]
    # 현재까지의 야영횟수, 현재까지의 남은 k개수
    visited[0][0] = [0, 0]
    find_best_way(answer, grid, k, visited, [0, 0], k, 0)

    return answer


if __name__ == "__main__":
    print(solution(["..FF", "###F", "###."], 4))