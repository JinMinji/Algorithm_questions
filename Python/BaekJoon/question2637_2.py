#20210621 장난감조립
result = list()


def sum_list(A, B, N):       # 리스트 덧셈
    sum_res = [a+b*N for a, b in zip(A, B)]
    return sum_res


def assemble(piece):
    if not any(input_pieces[piece]):   # 다 0일 때 => 기본 부품
        result[piece][piece] = 1

    elif not any(result[piece]):  # 결과에 들어와 있는게 없다는 건, 아직 결과를 구하지 않았다는 것!
        for i in range(1, N+1):
            if input_pieces[piece][i] != 0:
                result[piece] = sum_list(result[piece], assemble(i), input_pieces[piece][i])
    #else : # 결과가 이미 구해진 것들은, 그대로 return!

    return result[piece]


if __name__ == '__main__':
    N = int(input())
    M = int(input())

    input_pieces = [[0 for i in range(N+1)] for i in range(N+1)]
    # input_pieces[n] => 부품 n을 1개 만들기 위해 필요한 부품별 개수, (중간부품도 포함됨)
    for i in range(M):
        X, Y, K = map(int, input().split())
        input_pieces[X][Y] = K

    result = [[0 for i in range(N+1)] for i in range(N+1)]

    answer = assemble(N)  # 부품 N => 만들고자하는 결과물, 1개 만듦!

    for i in range(N):
        if answer[i] != 0:
            print(i, answer[i])
