#14931, 종이 조각, 골드3
import sys


def find(a, b, visited, cur_total):
    global result

    is_continue = True
    for i in range(a, N):
        for j in range(b, M):
            if visited[i][j] == 0:
                is_continue = False
                x = i
                y = j
                break
        if not is_continue:
            break
    if is_continue:
        return  # 끝까지 0인게 없다 == 방문할 곳이 더이상 없다.

    # 1개일 때

    find(x, y, visited, cur_total)

    # 세로로 숫자 만들기
    v_num = ""
    for i in range(x, N):
        if visited[i][y] == 0:
            visited[i][y] = 1
            v_num += str(visited[i][y])
            find(i, y, visited, cur_total+ int(v_num))
        else:
            break

    # 가로로 숫자 만들기
    h_num = ""
    for j in range(y, M):
        if visited[x][j] == 0:
            -visited[x][j] = 1
            h_num += str(visited[x][j])
            find(x, j, visited, cur_total+int(h_num))

    if cur_total > result:
        result = cur_total


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    # N은 최대가 4고,,
    # 자릿수가 큰 수를 여러개 만들수록 이득이다.
    # 0으로는 시작할 수 없다. -> 이득이 아님.
    paper = list()
    for i in range(N):
        paper.append(list(map(int, sys.stdin.readline().split())))

    result = 0
    # 내 위치가 0이 아니면,
    # 가로로 1 ~ M-j 길이만큼!
    # 세로로는 1 ~ N-i 만큼! 만들 수 있다.

    tmp_visited = [[0 for _ in range(M)] for _ in range(N)]
    find(0, 0, tmp_visited, 0)

    print(result)