#바이러스

def virus(graph, start):
    visited = list()
    to_visit = list()
    to_visit.append(start)

    while to_visit:
        node = to_visit.pop()

        if node not in visited:
            visited.append(node)
            to_visit.extend(graph[node])

    return len(visited)-1


if __name__ == '__main__':
    N = int(input())

    C = int(input())

    network = [[] for i in range(N+1)]
    for i in range(C):
        com1, com2 = map(int, input().split())

        network[com1].append(com2)
        network[com2].append(com1)

    start = 1   # 1번 컴퓨터가 웜바이러스에 감염되었을 때

    print(virus(network, start))
