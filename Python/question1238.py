# 20210615 파티
import heapq


# 가는 것 + 돌아오는 것 Max를 찾자.

def dijkstra(graph, start):
    times = {x: 100000 for x in graph}  #start부터 해당노드까지의 거리를 담을 딕셔너리. Max 값으로 100000 사용
    times[start] = 0        # 시작노드는 거리 0
    queue = list()      # 거리순으로 정렬하여 담아줄 우선순위큐

    heapq.heappush(queue, [times[start], start])    # 첫 정점 (시작노드) 부터 넣어주고, 하나씩 뽑아서 탐색,

    while queue:    # 없으면, 더이상 탐색할 수 있는 노드가 없다는 의미.
        cur_time, cur_node = heapq.heappop(queue)

        if times[cur_node] < cur_time:  # 이미 작은 값이 담겨있으면, 더 볼 것도 없음
            continue

        for adjacent, adj_time in graph[cur_node].items():  # 인접 노드들을 다 체크해보자
            tmp_time = cur_time + adj_time

            if tmp_time < times[adjacent]:  # 새로운 값이 저장된 값보다 작으면,
                times[adjacent] = tmp_time  # 갱신
                heapq.heappush(queue, [tmp_time, adjacent]) # 갱신된 값으로 체크해야하므로, 큐에 넣어준다.

    return times


if __name__ == '__main__':
    N, M, X = map(int, input().split())
    students_to_X = dict()
    students_from_X = dict()
    for i in range(M):
        x1, x2, time = map(int, input().split())
        if x1 in students_from_X:
            students_from_X[x1][x2] = time
        else:
            students_from_X[x1] = {x2: time}

        if x2 in students_to_X:   # 역방향으로도 저장. 파티 가는 길 찾기  위해서!
            students_to_X[x2][x1] = time
        else:
            students_to_X[x2] = {x1: time}

    to_X = dijkstra(students_to_X, X)
    from_X = dijkstra(students_from_X, X)

    result = 0
    for i in range(1, N+1):
        result = max(result, (to_X[i] + from_X[i]))

    print(result)

# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3