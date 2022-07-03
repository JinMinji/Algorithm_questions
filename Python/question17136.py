#색종이 붙이기, 골드2
import sys
dx = [0, 1, 1]  # 오른쪽, 아래, 대각선오른쪽아래
dy = [1, 0, 1]


def solution(cur, visited):
    global result, paper

    cur_i, cur_j = cur
    # 현위치가 무조건 덮는 색종이의 왼쪽 상단이라고 생각하고 check.
    # 1칸으로 덮기
    for i in range(cur_i, 10):
        for j in range(cur_j, 10):
            if paper[i][j] == 1 and [i, j] not in visited:
                visited.append([i, j])
                solution([i, j], visited)
                for x in range(1, 5):
                    for y in range(0, x):
                        if visited[x][y] != 1 or visited[y][x] != 1:
                            break

                visited.pop()

    # 2칸으로 덮기
    # 3칸으로 덮기
    # 4칸으로 덮기
    # 5칸으로 덮기


if __name__ == "__main__":
    paper = list()
    for i in range(10):
        paper.append(list(map(int, sys.stdin.readline().split())))

    result = 100
    visited = []
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                visited.append([i, j])
                solution([i, j], visited)
                visited.pop()

    print(result)