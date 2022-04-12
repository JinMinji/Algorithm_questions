# ACM Craft, 골드 3
import sys


def solutions(time, order, degree, target):
    total_time = [[] for i in range(len(time))]

    while any(0 <= x for x in degree):
        queue = list()
        while 0 in degree:      # 진입차수가 0인 건물을 queue에 넣는다
            idx = degree.index(0)
            queue.append(idx)
            degree[idx] = -1

        # print(queue)
        # print(degree)
        # print(total_time)
        #원대님은 똑똑하다

        for i in range(len(queue)):
            tmp_time = 0
            if total_time[queue[i]-1]:
                tmp_time = max(total_time[queue[i]-1])
            else:
                tmp_time = time[queue[i]-1]
            if queue[i] == target:
                if total_time[queue[i]-1]:
                    result = max(total_time[queue[i] - 1])
                else:
                    result = time[queue[i]-1]

                return result

            else:
                tmp_next = order[queue[i]]
                for n in tmp_next:
                    degree[n] -= 1
                    total_time[n-1].append(time[n-1] + tmp_time)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        times = list(map(int, sys.stdin.readline().split()))
        orders = [[] for _ in range(N+1)]
        indegree = [0 for _ in range(N+1)]
        indegree[0] = -1

        for k in range(K):
            a, b = map(int, input().split())
            orders[a].append(b)
            indegree[b] += 1

        W = int(input())

        print(solutions(times, orders, indegree, W))


