# 우체국, 골드4 - 더 짧은 풀이. 원리가 뭘까요
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    # N은 최대 10만.
    # 10만번만 도는 거면 그것도 괜찮다.

    # 누적합.
    villages = list()
    total_people = 0
    for i in range(N):
        villages.append(list(map(int, sys.stdin.readline().split())))
        total_people += villages[i][1]

    villages.sort()
    # 어차피 정답이되는 장소는 어떤 마을의 위일라나..?

    answer = 0
    cnt = 0
    for i in range(N):
        cnt += villages[i][1]
        if cnt >= (total_people/2):
            answer = i
            break

    print(villages[answer][0])