cnt = 0

def pung(bas):  # 같은 인형이 두개면 펑!
    global cnt
    while len(bas) >= 2 and bas[-1] == bas[-2]:  # 위에서부터 터지므로, 아래는 고려해줄필요 없이 상단 2개만 비교
        bas.pop()
        bas.pop()
        cnt += 2
    return bas


def solution(board, moves):
    answer = 0
    basket = list()
    while moves:
        now = moves.pop(0) -1
        for i in range(len(board[0])):
            if board[i][now] != 0:
                basket.append(board[i][now])
                basket = pung(basket)
                board[i][now] = 0
                break

    answer = cnt

    return answer

if __name__ =='__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))