import sys

sys.setrecursionlimit(10 ** 5)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_best_way(answer, grid, k, cur, rest_k, n):
    # 그리드, 이동횟수, 방문내용을 담은 list, 현재 위치, 남은 이동횟수, 현재까지의 야영횟수
    i, j = cur
    print(i, j)
    if rest_k == 0:  # 남은 이동횟수가 없을 때
        if i == len(grid) - 1 and j == len(grid[0]) - 1:  # 도착지점이면 현재상태와 비교하여 answer 업데이트
            if answer > n:
                answer = n
        elif grid[i][j] == '.':  # 아니면 평지일 경우 야영하거나,
            rest_k = k
            find_best_way(answer, grid, k, cur, rest_k, n + 1)

        else:  # 평지가 아니면 탐색중단.
            pass

    else:  # 남은 이동횟수가 있을 때
        if n > answer:
            return
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]

            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] != '#':
                    find_best_way(answer, grid, k, [x, y], rest_k - 1, n)

                if grid[x][y] == '.':  # 평지일경우 야영도 해본다
                    find_best_way(answer, grid, k, [x, y], k, n + 1)


def solution(grid, k):
    answer = float('inf')
    find_best_way(answer, grid, k, [0, 0], k, 0)

    return answer


if __name__ == "__main__":
    print(solution(["..FF", "###F", "###."], 4))
