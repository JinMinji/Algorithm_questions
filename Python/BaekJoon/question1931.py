#1931, 회의실 배정, 실버 1


if __name__ == "__main__":
    N = int(input())
    meetings = []
    for i in range(N):
        meetings.append(list(map(int, input().split())))

    meetings.sort(key=lambda x: (x[1], x[0]))

    answer = 0
    cur = 0
    for m in range(len(meetings)):
        if meetings[m][0] >= cur:
            answer += 1
            cur = meetings[m][1]

    print(answer)
