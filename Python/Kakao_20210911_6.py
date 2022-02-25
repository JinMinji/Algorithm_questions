def solution(board, skill):
    answer = 0
    for s in range(len(skill)):
        x1 = skill[s][1]
        y1 = skill[s][2]
        x2 = skill[s][3]
        y2 = skill[s][4]
        degree = skill[s][5]

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if skill[s][0] == 1:  # 공격
            degree *= -1

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] += degree

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer


if __name__ == '__main__':
