#20210727 이모티콘
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.

dp_con = list()

def min_making_time(n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 2

    if n == 3:
        return 3
    if dp_con[n] != 0:  #이미 구한 값이면 그대로 리턴
        return dp_con[n][n]


if __name__ == '__main__':
    N = int(input())

    dp_con = [[0 for i in range(10001)] for i in range(10001)]
    print(min_making_time(N))
