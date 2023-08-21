# 20210601 주사위굴리기

# [1,2,3,4,5,6]
# 동쪽이동 -> [4,2,1,6,5,3]
# 서쪽이동 -> [3,2,6,1,5,4]
# 북쪽이동 -> [5,1,3,4,6,2]
# 남쪽이동 -> [2,6,3,4,1,5]

def dice_rolling(n):
    global x, y, cur_dice

    if n == 1:  # 동쪽 # 동쪽이동 -> [4,2,1,6,5,3]
        if y + 1 >= M:
            return
        y += 1
        cur_dice = [cur_dice[3], cur_dice[1], cur_dice[0], cur_dice[5], cur_dice[4], cur_dice[2]]

    elif n == 2:  # 서쪽 # 서쪽이동 -> [3,2,6,1,5,4]
        if y - 1 < 0:
            return
        y -= 1
        cur_dice = [cur_dice[2], cur_dice[1], cur_dice[5], cur_dice[0], cur_dice[4], cur_dice[3]]


    elif n == 3:  # 북쪽 # 북쪽이동 -> [5,1,3,4,6,2]
        if x - 1 < 0:
            return
        x -= 1
        cur_dice = [cur_dice[4], cur_dice[0], cur_dice[2], cur_dice[3], cur_dice[5], cur_dice[1]]

    elif n == 4:  # 남쪽 # 남쪽이동 -> [2,6,3,4,1,5]
        if x + 1 >= N:
            return
        x += 1
        cur_dice = [cur_dice[1], cur_dice[5], cur_dice[2], cur_dice[3], cur_dice[0], cur_dice[4]]

    if dice_map[x][y] == 0:
        dice_map[x][y] = cur_dice[5]
    else:
        cur_dice[5] = dice_map[x][y]
        dice_map[x][y] = 0

    print(cur_dice[0])

if __name__ == '__main__':
    global x, y
    N, M, x, y, K = map(int, input().split(' '))

    dice_map = list()
    for i in range(N):
        dice_map.append(list(map(int, input().split(' '))))

    roll = list(map(int, input().split(' ')))

    global cur_dice
    cur_dice = [0,0,0,0,0,0]

    for r in roll:
        dice_rolling(r)