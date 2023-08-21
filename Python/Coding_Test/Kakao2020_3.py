dx = [0, 0, 1, -1]  # 이동 방법 : 상,하,좌,우
dy = [1, -1, 0, 0]

def findway(pos):
    x, y = pos


def solution(key, lock):
    answer = True
    # 돌리는 경우의 수 4개
    # key 크기는 최대 20개 => 위, 아래 이동 방법 20*20*20*20 = 160000 이하,,,,,,,,,,?
    # 상하좌우 말고, 그냥 맨 -20,-20에서 시작해서 좌,하만 비교하면서 내려오는데!
    # 살아있는애들만 비교하되, 홈이 있는 위치의 i, j 보다 살아있는 애들 범위가 적으면 -> 그냥 바로 잘라버리기

    maxi = len(key)
    for i in range(4):
        x = 0
        y = 0
        while -maxi < x < maxi and -maxi < y < maxi:


    return answer


if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]]	))