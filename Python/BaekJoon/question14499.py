# 20210528 주사위굴리기

# 처음 주사위 윗면 1 -> 바닥면 6
# 동쪽으로 이동시 6 -> 3 -> 1 -> 4
# 남쪽으로 이동시 6 -> 5 -> 1 -> 2

# dice = [[0,0], [1,1], [2,2], [3,3], [4,4], [5,5], [6,6]]

dice = [0,0,0,0,0,0,0]
dice_top = [0, 6, 5, 4, 3, 2, 1]
# dice_change = [[0,0,0,0]
#                ,[dice[3], dice[4], dice[2], dice[5]]
#                ,[dice[3], dice[4], dice[6], dice[1]]
#                ,[dice[4], dice[1], dice[2], dice[5]]
#                ,[dice[1], dice[3], dice[2], dice[5]]
#                ,[dice[3], dice[4], dice[2], dice[5]]
#                ,[dice[3], dice[4], dice[2], dice[5]]
#                ]

dice_change = [ [0, 0, 0, 0, 0]
               ,[0, 3, 4, 5, 2]
               ,[0, 3, 4, 1, 6]
               ,[0, 1, 6, 2, 5]
               ,[0, 6, 1, 2, 5]
               ,[0, 3, 4, 6, 1]
               ,[0, 3, 4, 2, 5]
               ]

def change():
    if dice_map[x][y] != 0:
        dice[cur_bottom] = dice_map[x][y]

    else:
        dice_map[x][y] = dice[cur_bottom]

def roll_dice(n):
    global cur_bottom
    global x, y
    if n == 1:      #동쪽
        if y + 1 < M:
            y += 1
            cur_bottom = dice_change[cur_bottom][n]
            change()
            return dice[dice_top[cur_bottom]]

    elif n == 2:    #서쪽
        if y - 1 >= 0:
            y -= 1
            cur_bottom = dice_change[cur_bottom][n]
            change()
            return dice[dice_top[cur_bottom]]

    elif n == 3:    #북쪽
        if x - 1 >= 0:
            x -= 1
            cur_bottom = dice_change[cur_bottom][n]
            change()
            return dice[dice_top[cur_bottom]]

    elif n == 4:    #남쪽
        if x + 1 < N:
            x += 1
            cur_bottom = dice_change[cur_bottom][n]
            change()
            return dice[dice_top[cur_bottom]]


if __name__ == '__main__':
    global x, y
    N, M, x, y, K = map(int, input().split(' '))

    dice_map = list()
    for i in range(N):
        dice_map.append(list(map(int, input().split(' '))))

    global cur_bottom
    cur_bottom = 6

    roll = list(map(int, input().split(' ')))
    for r in roll:
        a = roll_dice(r)
        if a != None:
            print(a)