#스타트링크, 골드5
import sys
sys.setrecursionlimit(10**5)


def solutions(to_vist, res):
    global F, S, U, D, result, visited

    next_visit = list()
    # print(to_vist)
    while to_vist:
        cur = to_vist.pop()
        if cur == G:    # 링크에 도착하면 return
            result = res
            return

        if 0 < cur <= F and visited[cur] == 0:  #이미 방문한 곳은 확인할 필요가 없음
            visited[cur] = 1
            up_stairs = cur + U
            next_visit.append(up_stairs)
            down_stairs = cur - D
            next_visit.append(down_stairs)

    res += 1
    if next_visit:
        solutions(next_visit, res)
    else:
        return


if __name__ == "__main__":
    F, S, G, U, D = map(int, input().split())
    #F : 전체 층
    #S : 가야하는 층
    #G : 내 시작위치
    #U : 올라가는 층
    #D : 내려가는 층

    result = -1
    visited = [0 for i in range(F+1)]
    solutions([S], 0)

    if result == -1:
        print("use the stairs")
    else:
        print(result)