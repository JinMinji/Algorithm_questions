# 20210825 놀이공원
# t분 동안 태울 수 있는 어린이 수 =
def can_ride_num(t, times):
    result = 0
    for n in times:
        result += t//n

    return result

def find(N, times):

    start = 0
    end = N*30
    result = N*30

    while start > end:
        mid = start+end //2

        if can_ride_num(mid, times) > N:
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    while True:






if __name__ == '__main__':

    N, M = map(int, input().split())

    times = map(int, input().split())

    print(find(N, times))

