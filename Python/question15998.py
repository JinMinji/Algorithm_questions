# 카카오머니
import sys


def gcd(x, y):  # greatest common divisor
    while y != 0:
        r = x % y
        x = y
        y = r

    return x


def lcm(x, y):  # least common multiple
    return int(x * y / gcd(x, y))


def divisor_min(start, num):
    min_divisor = 0

    tmp = num // (start + 1)
    # print(tmp)
    if tmp == 0:
        min_divisor = num
    else:
        min_divisor = num // tmp
    # for i in range(start+1, num + 1):
    #     if num % i == 0:
    #         min_divisor = i
    #         break

    return min_divisor


if __name__ == "__main__":
    # N : 로그의 개수, 숫자형으로 입력받기
    N = int(sys.stdin.readline())

    # 로그를 담을 배열 생성
    logs = list()

    # 충전 단위가 될 수 있는 수를 담은 배열

    # 잔액 0으로 초기화
    balance = 0
    answer = -1
    min_max = [0, 0]

    # N번 돌면서 로그 입력받기
    for i in range(N):
        # logs.append(list(map(int, input().split())))
        a, b = map(int, sys.stdin.readline().split())

        tmp_min = 0
        tmp_max = 0
        if (balance + a) > 0:
        #단순 입출금 로그 모순 체크
            if balance + a != b:
                answer = 0
                break

        # 연결된 통장에서 돈을 가져올 때
        else:
            # 충전단위는 b보단 크면서, -(balance + a) + b의 약수여야 한다.
            if b == 0:
                tmp_min = 1
            else:
                tmp_min = divisor_min(b, -(balance + a) + b)
            tmp_max = -(balance + a) + b

        print(min_max, tmp_min, tmp_max)

        if min_max[0] == 0:
            min_max = [tmp_min, tmp_max]

        else:
            # min 끼리는 최소공배수 구하기
            tmp_min = lcm(min_max[0], tmp_min)
            # max 끼리는 최대공약수 구하기
            tmp_max = gcd(min_max[1], tmp_max)

        if tmp_min > tmp_max:
            answer = 0
            break
        min_max = [tmp_min, tmp_max]

        # 잔액 업데이트
        balance = b

    if answer == 0:
        # 유효한 충전단위가 없으면 -1
        print(-1)

    elif min_max[0] == 0:
        print(1)

    else:
        if min_max[0] <= 9*(10**18):
            print(min_max[0])
        else:
            print(-1)



