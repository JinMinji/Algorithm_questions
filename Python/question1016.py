#제곱ㄴㄴ수, 골드1

#에라토스테네스의 체
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    prime_check = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_check[i]:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                prime_check[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if prime_check[i] == True]


if __name__ == "__main__":
    min_num, max_num = map(int, input().split())
    array_size = max_num - min_num + 1

    prime_check = [True for i in range(array_size)]
    #제곱 ㄴㄴ수면 True, 아니면 False

    for i in range(2, int(max_num**0.5)+1): #제곱근까지만 확인해도 됨.
        #i**2 이 범위내에 있으면서, 배수 체크를 아직 안했을 때
        tmp_square = i**2
        start = 0
        if min_num % tmp_square == 0:
            start = tmp_square * (min_num // tmp_square)
        else:
            start = tmp_square * ((min_num // tmp_square) + 1)

        for j in range(start, max_num+1, tmp_square):
            prime_check[j - min_num] = False

    # print(prime_check)
    print(prime_check.count(True))