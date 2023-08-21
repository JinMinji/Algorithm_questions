def solution(board, moves):
    result_stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result_stack.append(board[j][i-1])
                board[j][i-1] = 0
                if len(result_stack) >= 2:
                    while result_stack[-1] == result_stack[-2]:
                        result_stack.pop()
                        result_stack.pop()
                        answer += 2
                        if len(result_stack) < 2:
                            break
                break

    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])