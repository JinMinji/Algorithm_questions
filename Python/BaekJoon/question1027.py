# 고층 건물, 골드 4


if __name__ == '__main__':
    N = int(input())

    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if j < i:
                term = (buildings[i] - buildings[j]) / (i-j)
                can_see = True
                for k in range(j+1, i):
                    if buildings[j] + term * (k - j) <= buildings[k]:
                        can_see = False
                        break
                if can_see:
                    cnt += 1

            else:
                term = (buildings[j] - buildings[i]) / (j - i)
                can_see = True
                for k in range(i+1, j):
                    if buildings[i] + term * (k - i) <= buildings[k]:
                        can_see = False
                        break
                if can_see:
                    cnt += 1

        # print(i,cnt)
        answer = max(cnt, answer)

    print(answer)