#k진수 소수찾기

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    changed_num = ''
    if k == 10:
        changed_num = str(n)

    else:       # 소수 만들기
        while n // k >= 1:
            remain = n % k
            n = n // k
            changed_num = str(remain) + changed_num

            if n < k:
                changed_num = str(n) + changed_num

    num_list = changed_num.split('0')

    for i in range(len(num_list)):
        if num_list[i] != '' and isPrime(int(num_list[i])):
            answer += 1

    return answer


if __name__ == '__main__':
    # print(solution(437674, 3))
    print(solution(110011, 10))
