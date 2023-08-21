#20210804 소수경로
prime_list = list()

possible = list()
visited = list()

def is_prime_number(num):
    for i in range(2, num):
        if num%i == 0:
            return False

    return True

for i in range(1000, 9999):
    if is_prime_number(i):
        prime_list.append(i)


def prime_change(from_n, to_n):
    dist = [-1 for _ in range(10000)]
    dist[from_n] = 0
    nexts = list()

    nexts.append(from_n)
    visited[from_n] = 1

    while nexts:
        now_num = nexts.pop(0)
        if now_num == to_n:
            return str(dist[now_num])

        for i in range(4):  # 만약, 1234에서 2를 구하려면, (1234//100)%10 = 2, 2를 바꿔줘야하므로, 1234 - 2*100 + x*100
            set_num = now_num - ((now_num // (10 ** i)) % 10) * (10 ** i)
            for j in range(10):
                tmp_num = set_num + j * (10 ** i)
                if tmp_num in prime_list and visited[tmp_num] == 0:
                    nexts.append(tmp_num)
                    visited[tmp_num] = 1
                    dist[tmp_num] = dist[now_num] + 1

    return "Impossible"


if __name__ == '__main__':
    T = int(input())
    results = list()
    for i in range(T):
        A, B = map(int, input().split())
        possible = list()   #초기화
        visited = [0 for i in range(10000)]
        results.append(prime_change(A, B))

    for _ in results:
        print(_)
