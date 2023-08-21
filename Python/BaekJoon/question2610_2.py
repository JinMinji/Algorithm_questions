#20210617 회의준비 2번째 도전
import copy

def floyd_warshall(graph):
    min_cost = copy.deepcopy(graph)

    for k in range(len(graph)): # 경유지
        for i in range(len(graph)):
            for j in range(len(graph)):
                min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

    return min_cost
#------------floyd------------#


def dfs(graph, start):
    global visited

    to_visit = list()
    team_min_cost = len(graph)
    team_min_index = start
    to_visit.append(start)

    while to_visit:
        cur = to_visit.pop(0)
        max_cost = 0
        for c in range(N):
            cost = graph[cur][c]
            if cost != N and c != cur:      # 연결이 끊기지 않았고, 자기 자신이 아닐 때
                max_cost = max(max_cost, cost)  # max 값 찾기.
                if visited[c] == 0:
                    visited[c] = 1
                    to_visit.append(c)
        if team_min_cost > max_cost:
            team_min_cost = max_cost
            team_min_index = cur

    leaders.append(team_min_index+1)


if __name__ == '__main__':
    N = int(input())    # 사람수
    M = int(input())    # 관계수

    connections = [[N for i in range(N)] for i in range(N)]
    # 총 사람 수가 대화비용의 MAX

    for i in range(N):
        connections[i][i] = 0
    # 자기 자신은 0

    for i in range(M):
        p1, p2 = map(int, input().split())
        connections[p1-1][p2-1] = 1     #index이므로 -1 해줘야 함
        connections[p2-1][p1-1] = 1
    # 입력 받기. 관계가 있으면 비용 1

    # 모든 정점에 대한 최단경로 구하기 : Floyd-Warshall
    communication_cost = floyd_warshall(connections)

    global leaders
    leaders = list()  # 대표리스트. 정렬해서 출력해줘야해서 리스트에 넣어줌.
    global visited  # 방문 확인
    visited = [0 for i in range(N)]  # 1 <= N <= 100

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(communication_cost, i)

    leaders.sort()

    print(len(leaders))
    for leader in leaders:
        print(leader)

