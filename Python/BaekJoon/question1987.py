#20210521 알파벳

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def isPossible(x,y):    # 범위 검사
    return 0<=x<R and 0<=y<C

def how_far(num, start, visited):       # 현재까지의 이동횟수, 현재위치, 방문한 알파벳 내역
    i, j = start    # 현재위치부터 상, 하, 좌, 우
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if isPossible(x,y):
            if board[x][y] not in visited:    # xy좌표 기준으로 방문여부는 안해줘도 당연함.
                visited.append(board[x][y])
                num += 1
                how_far(num, [x,y], visited)
            else:
                dist_list.append(num)
                print(num, x,y)
                print(visited)

if __name__ == '__main__':
    R, C = map(int, input().split(" "))

    board = list()
    for i in range(R):
        board.append(input())

    max_dist = 0
    dist_list = list()
    visited_alpha = list()
    visited_alpha.append(board[0][0])   # 맨 첫번째에서 시작

    how_far(1,[0,0],visited_alpha)      # 맨 첫번째 칸부터! 칸 수는 1, 위치는 [0][0], 방문한알파벳은 board[0][0]

    max_dist = max(dist_list)

    print(max_dist)