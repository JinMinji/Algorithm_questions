def solution(grid, clockwise):
    answer = []
    for i in range(len(grid)):
        answer.append([0 for j in range(len(grid[i]))])

    cnt = 0
    if clockwise:
        tmp_list = []
        for i in range(len(grid)):
            for j in range(len(grid[-(i + 1)])):
                tmp_list.append(grid[-(i + 1)][j])

        for i in range(len(answer)):
            for j in range(len(answer)):
                tmp_idx = 2*i+1
                if len(answer[j]) > tmp_idx:
                    answer[j][tmp_idx] = tmp_list[cnt]
                    cnt += 1

                tmp_idx = 2*i
                if len(answer[j]) > tmp_idx:
                    answer[j][tmp_idx] = tmp_list[cnt]
                    cnt += 1

    else:
        return solution(solution(grid, True), True)

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer


if __name__ == '__main__':
    print(solution(["1", "234", "56789"], True))
    print(solution(["1", "234", "56789"], False))