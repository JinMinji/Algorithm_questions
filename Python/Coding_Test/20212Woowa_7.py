def solution(grid, clockwise):
    answer = []
    for i in range(len(grid)):
        answer.append([0 for j in range(len(grid[i]))])

    if clockwise:
        tmp_list = []
        for i in range(len(grid)):
            print(grid[-(i+1)])
            for j in range(len(grid[-(i+1)])):
                tmp_list.append(grid[-(i+1)][j])

    cnt = 0
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if len(answer[i]) > grid:
                pass

    else:
        tmp_list = []
        for i in range(len(grid)):
            for j in range(len(grid[-(i + 1)])):
                tmp_list.append(grid[-(i + 1)][j])

        print(tmp_list)

    return answer


if __name__ == '__main__':
    # print(solution(["1","234","56789"], True))
    print(solution(["1", "234", "56789"], False))