#20210621 장난감조립
dp = list()
pieces = list()

def assemble(piece, n):
    if dp[piece] != [-1]:     #이미 구한 값이 있으면 바로 넣어주고
        for i in dp[piece]:
            dp[i[0]] += i[1]*n

    elif len(pieces[piece]) == 0:    # 기본 부품
        dp[piece] += n
        dp[piece] = []

    else:                   #없으면 계산해야함
        for p in pieces[piece]:
            piece_name, piece_num = p
            piece_num *= n
            dp[piece] = assemble(piece_name, piece_num)

if __name__ == '__main__':
    N = int(input())
    M = int(input())

    pieces = [[] for i in range(N)]
    for i in range(M):
        X, Y, K = map(int, input().split())
        pieces[X-1].append([Y-1, K])

    dp = [[-1] for i in range(N)]
    assemble(N-1, 1)

    for i in range(N):
        if dp[N-1][i] != 0:
            print(i+1, dp[N-1][i])
