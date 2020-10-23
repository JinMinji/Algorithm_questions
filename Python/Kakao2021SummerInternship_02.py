def Manhattan_check(room, x, y):
    # 왼쪽에서 오른쪽으로, 위에서 아래로 확인하면서 진행하므로, 오른쪽, 아래쪽만 check
    if x + 1 <= 4:  # 오른쪽 한칸 옆 체크
        if room[x + 1][y] == 'P':
            return False
        if x + 2 <= 4:  # 오른쪽 두칸 옆 체크
            if room[x + 2][y] == 'P' and room[x + 1][y] != 'X':  # 중간 파티션 체크
                return False
        if y + 1 <= 4:  # 대각선 오른쪽 아래 체크
            if room[x + 1][y + 1] == 'P' and (room[x + 1][y] != 'X' or room[x][y + 1] != 'X'):
                # 오른쪽옆, 아래 둘 다 파티션이 있는지 체크
                return False
    if y + 1 <= 4:  # 아래쪽 한칸 옆 체크
        if room[x][y + 1] == 'P':
            return False
        if x - 1 >= 0:  # 대각선 왼쪽아래 체크
            if room[x - 1][y + 1] == 'P' and (room[x - 1][y] != 'X' or room[x][y + 1] != 'X'):
                # 왼쪽옆, 아래 둘 다 파티션이 있는지 체크
                return False
        if y + 2 <= 4:  # 아래쪽 두칸 옆 체크
            if room[x][y + 2] == 'P' and room[x][y + 1] != 'X':  # 중간 파티션 체크
                return False

    return True


def solution(places):
    answer = []
    for room in places:
        can = True
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if not Manhattan_check(room, i, j):
                        can = False
                        break
            if not can:
                answer.append(0)
                break
        if can:
            answer.append(1)

    return answer


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))