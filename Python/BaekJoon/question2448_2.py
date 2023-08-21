# 별 찍기 - 11, 골드 4

def make_star(edge_loc):
    x, y = edge_loc
    global result
    result[x][y] = '*'

    result[x+1][y-1] = '*'
    result[x+1][y+1] = '*'

    result[x+2][y-2] = '*'
    result[x+2][y-1] = '*'
    result[x+2][y] = '*'
    result[x+2][y+1] = '*'
    result[x+2][y+2] = '*'


def merge_triangle(star_arr):
    for i in range(len(star_arr)):
        pass


if __name__ == '__main__':
    N = int(input())

    result = [[' ' for i in range(N*2)] for i in range(N)]

    for i in range(N//3):

        if i % 2 == 0:
            print(i, '번째 줄, 홀수개')
            for j in range(i//2+1):
                make_star([3 * i, N - 6*j])
                print(3 * i, N - 6 * j)
                print(3 * i, N + 6 * j)
                make_star([3 * i, N + 6 * j])

        else:
            print(i, '번째 줄')
            for j in range(i//2 + 1):
                make_star([3 * i, N - (3 + 6 * j)])
                print(3 * i, N - (3 + 6 * j))
                print(3 * i, N + (3 + 6 * j))
                make_star([3 * i, N + (3 + 6 * j)])
            pass

    for r in range(N):
        for c in range(N*2):
            print(result[r][c], end='')
        print()
