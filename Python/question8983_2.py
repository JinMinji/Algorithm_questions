# 20210524 사냥꾼
import bisect

def hunting():
    result = 0
    animals_loc.sort(key=lambda x:x[0])
    for ani in animals_loc: #n
        i = bisect.bisect_right(loc, ani[0])
        if i < M and abs(ani[0]-loc[i])+ani[1] <= L:
            result += 1
        elif i > 0 and abs(ani[0]-loc[i-1])+ani[1] <= L:
            result += 1

    return result

if __name__ == "__main__":
    M, N, L = map(int, input().split(" "))
    loc = list(map(int, input().split(" ")))
    loc.sort()
    animals_loc = list()
    for _ in range(N):
        animals_loc.append(list(map(int, input().split(" "))))

    print(hunting())
