# 20210507 최소 회의실 개수

N = int(input())    # N : 회의 개수

meetings = list()
for _ in range(N):
    meetings.append(list(map(int, input().split(" "))))

meetings.sort(key=lambda x:x[0])

result = 1
endtimes = list()
endtimes.append(0)

while len(meetings) > 0:
    m = meetings.pop(0)
    s = m[0]
    e = m[1]
    can = False
    for i in range(len(endtimes)):
        if s >= endtimes[i]:
            endtimes[i] = e
            endtimes.sort()
            can = True
            break
    if can == False:
        result += 1
        endtimes.append(e)

print(result)