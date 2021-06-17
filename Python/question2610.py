#20210615 회의준비 28% 틀렸습니다
import copy

parent = list()


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    tmp_parent1 = find(a)
    tmp_parent2 = find(b)

    if tmp_parent1 > tmp_parent2:
        parent[a] = tmp_parent2
    else:
        parent[b] = tmp_parent1


def union_find(graph):
    for i in range(N+1):    # index 0은 안씀
        parent.append(i)
        # 자기 자신으로 부모노드 설정.
    for i in range(N+1):
        for j in range(N+1):
            if graph[i][j] == 1:    # 연결되어 있으면!
                union(i, j)

    return parent
#-------------union find--------------#


def floyd_warshall(graph):
    min_cost = copy.deepcopy(graph)

    for k in range(len(graph)): # 경유지
        for i in range(len(graph)):
            for j in range(len(graph)):
                min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

    return min_cost
#------------floyd------------#


if __name__ == '__main__':
    N = int(input())    # 사람수
    M = int(input())    # 관계수

    connections = [[N for i in range(N+1)] for i in range(N+1)]
    # 총 사람 수가 대화비용의 MAX

    for i in range(N+1):
        connections[i][i] = 0
    # 자기 자신은 0

    for i in range(M):
        p1, p2 = map(int, input().split())
        connections[p1][p2] = 1
        connections[p2][p1] = 1
    # 입력 받기. 관계가 있으면 비용 1

    # 팀 쪼개기 : union-find
    root_list = union_find(connections)
    team = dict()
    for mem in range(len(root_list)):
        team[root_list[mem]] = team.get(root_list[mem], []) + [mem]

    # 대표 정하기 : Floyd-Warshall
    leaders = list()    # 대표리스트. 정렬해서 출력해줘야해서 리스트에 넣어줌.
    communication_cost = floyd_warshall(connections)

    # 전체 대화비용의 총합 최소가 아니라, 최대대화비용의 최소를 찾는 문제!

    # max_cost_list = [N for i in range(N)]
    # for i in list(team.keys()):        # 팀별로
    #     for member in team[i]:
    #         max_cost = 0
    #         for to_mem in team[i]:
    #             max_cost = max(max_cost, communication_cost[member][to_mem])
    #         max_cost_list[member] = max_cost

    max_cost_list = list()
    for i in range(len(communication_cost)):
        max_cost = 0
        for c in range(1, len(communication_cost[i])):
            if (root_list[i] == root_list[c]):  # root 비교, -> 같은 팀인지
                max_cost = max(max_cost, communication_cost[i][c])
        max_cost_list.append(max_cost)

    for root in list(team.keys()):
        leader = root
        for member in team[root]:
            if max_cost_list[member] < max_cost_list[leader]:
                leader = member
        leaders.append(leader)

    leaders.sort()
    leaders.pop(0)      # 0은 빼준다!
    print(len(leaders))
    for leader in leaders:
        print(leader)