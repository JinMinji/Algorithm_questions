#해킹, 골드4
import sys
import heapq

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for t in range(T):
        n, d, c = map(int, sys.stdin.readline().split())

        depend_dict = {node: [] for node in range(n+1)}
        for i in range(d):
            a, b, s = map(int, sys.stdin.readline().split())
            depend_dict[b].append([a, s])

        to_visit = list()
        to_visit.append(c)
        hacked = [-1 for i in range(n+1)]
        hacked[c] = 0
        while to_visit:
            virus = to_visit.pop(0)
            for next_com, sec in depend_dict[virus]:
                if hacked[next_com] == -1 or hacked[next_com] > hacked[virus] + sec:
                    hacked[next_com] = hacked[virus] + sec
                    to_visit.append(next_com)

        # print(hacked)
        print(n+1-hacked.count(-1), max(hacked))