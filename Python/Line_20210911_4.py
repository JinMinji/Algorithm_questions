prime_num = []


def divide_list(lst):
    if len(lst) == 1:   # len이 1이면 과정 종료, 들어온 값 return
        return lst

    # len 이 1이상이면,

    k = len(lst)
    ans = []

    p = 1
    for i in range(1, k + 1):   # 1~k까지 돌면서
        if i in prime_num and k % i == 0:   # 소수이면서 나눴을 때 나머지가 0인 최솟값을 찾는다.
            # len/p개씩 p개의 배열로 나눈다.
            p = i
            k = k//p   # p개의 배열 이므로, 배열 하나당 길이는 len/p
            break

    tmp_lst = [[] for _ in range(p)]
    for i in range(len(lst)):  # 배열을 나눈다.
        tmp_lst[i%p].append(lst[i])

    for i in range(p):
        ans.extend(divide_list(tmp_lst[i]))


    return ans  #반환한다.


def solution(n):
    answer = []

    # 에라토스테네스의 체를 활용하여 소수 먼저 구해두기
    a = [False, False] + [True] * (n - 1)
    global prime_num

    prime_num = []

    for i in range(2, n + 1):
        if a[i]:
            prime_num.append(i)

        for j in range(2 * i, n + 1, i):
            a[j] = False
    # 에라토스테네스의 체를 활용하여 소수 먼저 구해두기

    answer = divide_list([i for i in range(1, n+1)])    # [1, 2, 3, 4, ... ,n]을 인자로 넣는다.

    return answer


if __name__ == '__main__':
    print(solution(18))