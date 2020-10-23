#20210512 성냥개비

input_num = int(input())

cases = list()
for _ in range(input_num):
    cases.append(int(input()))
# 0 : 6
# 1 : 2
# 2 : 5
# 3 : 5
# 4 : 4
# 5 : 5
# 6 : 6
# 7 : 3
# 8 : 7
# 9 : 6


# 최소 2개 ~ 7개
# 2개 : 1
# 3개 : 7
# 4개 : 4
# 5개 : 2, 3, 5
# 6개 : 0, 6, 9
# 7개 : 8

# 큰 수
# 짝수면 무조건 1로 채우는 게 제일 큼
# 홀수면 3으로 만들 수 있는 최대인 7을 제일 앞에두고 1로 채운다.


# 작은 수
# 8, 0, 1 활용
# 7개 이상이면 8이 무조건 들어가야함.
# 나머지가 1이면 -> 1 / 10
# 나머지 2 -> 1
# 나머지 3 -> 7 / 22 / 200
# 나머지 4 -> 4 / 20
# 나머지 5 -> 2
# 나머지 6 -> 6


for case in cases:
    max_result = ''
    min_result = ''

    N = case

    if (N%2) > 0:
        max_result += '7'
        for i in range(N//2-1):
            max_result += '1'

    else:
        for i in range(N//2):
            max_result += '1'

    max_result = int(max_result)

# MAX 값 구하기 종료

    if N%7 == 0:
        for i in range(N // 7):
            min_result += '8'

    elif N%7 == 1:
        for i in range(N // 7-1):
            min_result += '8'
        min_result = '10'+ min_result

    elif N%7 == 2:
        if N // 7 > 0:
            for i in range(N // 7):
                min_result += '8'
            min_result = '1' + min_result
        else:
            min_result = 1

    elif N % 7 == 3:
        if N // 7 > 2:
            for i in range(N // 7 - 2):
                min_result += '8'
            min_result = '200' + min_result
        elif N // 7 == 1:
            min_result = 22
        elif N // 7 == 2:
            min_result = 200
        else:  #N//7 == 0
            min_result = 7

    elif N % 7 == 4:
        if N // 7 > 0:
            for i in range(N // 7 - 1):
                min_result += '8'
            min_result = '20' + min_result
        else:
            min_result = 4

    elif N % 7 == 5:
        if N // 7 > 0:
            for i in range(N // 7):
                min_result += '8'
            min_result = '2' + min_result
        else:
            min_result = 2

    else: # (N % 7 == 6)
        if N // 7 > 0:
            for i in range(N // 7):
                min_result += '8'
            min_result = '6' + min_result
        else:
            min_result = 6

    min_result = int(min_result)

    print(min_result, max_result)