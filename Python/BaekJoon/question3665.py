#20210621 최종순위
# 위상정렬
from collections import deque
from collections import defaultdict

def topological(graph, degree):  # topological sorting
    sorted_graph = list()
    queue = deque()
    print(degree)
    print(graph)
    for i in range(1, n+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        if len(queue) > 1:
            return "?"
        current = queue.popleft()
        sorted_graph.append(current)
        print(sorted_graph)

        for i in graph[current]:
            degree[i] -= 1
            if degree == 0:
                queue.append(i)

    if len(sorted_graph) < n:
        return "IMPOSSIBLE"

    return ' '.join(str(i) for i in sorted_graph)


if __name__ == '__main__':
    result = list()     # 각 테스트 케이스의 결과값을 string으로 받아서 넣어줄 것.
    TC = int(input())   # 테스트 케이스 수
    for tc in range(TC):
        # -- input --
        n = int(input())    # 팀의 수
        last_year = list(map(int, input().split()))
        m = int(input())    # 등수 바뀐 쌍
        change_team_pair = list()
        for i in range(m):
            change_team_pair.append(list(map(int, input().split())))
        # -- input --

        # 입력받은 등수를 graph로 변환
        original_graph = defaultdict(list)
        result_graph = defaultdict(list)
        indegree = [0 for i in range(n+1)] #진입차수
        indegree[0] = 0
        for i in range(1, n):   # 2 ≤ n ≤ 500
            original_graph[last_year[i-1]] = [last_year[i]]
            result_graph[last_year[i-1]] = [last_year[i]]
            indegree[last_year[i]] = 1

        for x, y in change_team_pair:
            rank_x = last_year.index(x)
            rank_y = last_year.index(y)
            if rank_x > rank_y:   # 원래 rank가 더 작은 수가 앞으로 가도록
                x, y = y, x
                rank_x, rank_y = rank_y, rank_x

            if rank_x - rank_y == -1:   # 붙어있을 때
                # step1
                result_graph[x].extend(original_graph[y])
                # step2
                if rank_x > 0:
                    result_graph[rank_x - 1].append(y)
                    indegree[y] += 1
                # step3
                result_graph[x].remove(y)
                #step4
                indegree[x] += 1
                indegree[y] -= 1

            else: # 한칸 이상 떨어져있을 때
                result_graph[y] = result_graph[y].append(x)
                indegree[x] += 1
        # ------

        this_year = topological(result_graph, indegree)

        result.append(this_year)

    for i in range(TC):
        print(result[i])


