#색종이 붙이기, 골드2
import sys
dx = [0, 1, 1]  # 오른쪽, 아래, 대각선오른쪽아래
dy = [1, 0, 1]


def change_to_visited(lst):
    for _ in lst:
        pass



def check_five_way(cur, visited, tmp_res):
    global paper, result

    cur_i, cur_j = cur

    for x in range(0, 5):
        # 1칸 덮기 ~ 2칸 덮기
        tmp_lst = list()
        for y in range(0, x+1):
            if paper[cur_i+x][cur_j+y] == 1 and paper[cur_i+y][cur_j+x] == 1:
                if visited[cur_i+x][cur_j+y] == 0 and visited[cur_i+y][cur_j+x] == 0:
                    tmp_lst.append([cur_i+x][cur_j+y])
                    tmp_lst.append([cur_i+y][cur_j+x])
                else:
                    pass


            tmp_lst.pop()

        solution(visited, tmp_res)


def solution(visited, tmp_res):
    global paper, result, total_sum

    if tmp_res > result:
        return

    if len(visited) >= total_sum:
        if tmp_res < result:
            result = tmp_res
        return

    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and [i, j] not in visited:
                visited.append([i, j])
                check_five_way([i, j], visited, tmp_res+1)
                visited.pop()


if __name__ == "__main__":
    paper = list()
    total_sum = 0
    for i in range(10):
        paper.append(list(map(int, sys.stdin.readline().split())))
        total_sum += sum(paper[i])

    result = 100
    solution([], 0)

    print(result)