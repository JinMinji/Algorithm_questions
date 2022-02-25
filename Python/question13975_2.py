# 파일 합치기 3
import heapq

if __name__ == '__main__':
    T = int(input())

    result = list()

    for t in range(T):
        K = int(input())
        files = list(map(int, input().split(' ')))

        heapq.heapify(files)

        tmp_res = 0
        while len(files) > 1:
            a = heapq.heappop(files)
            b = heapq.heappop(files)
            tmp_res += a+b
            heapq.heappush(files, a+b)

        result.append(tmp_res)

    for i in range(len(result)):
        print(result[i])