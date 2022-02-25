# 가서 돌아오는 길은 어차피 같은 길을 밟고 돌아오면 되니까, 신경안써도 됨
# 가는 경로만 고려할 것
import copy

max_result = 0


def go_ahead(graph, info, can_go, w, s):
    global max_result

    for i in range(len(can_go)):
        tmp_can_go = copy.deepcopy(can_go)
        cur = tmp_can_go.pop(i)

        if info[cur] == 1:  #늑대
            w += 1
            if s <= w:
                w -= 1
                continue
            else:
                tmp_can_go.extend(graph.get(cur, []))
                go_ahead(graph, info, tmp_can_go, w, s)
                w -= 1

        else:
            s += 1
            tmp_can_go.extend(graph.get(cur, []))
            max_result = max(max_result, s)
            go_ahead(graph, info, tmp_can_go, w, s)
            s -= 1


def solution(info, edges):
    answer = 0
    graph = dict()
    for i in range(len(edges)):
        graph[edges[i][0]] = graph.get(edges[i][0], []) + [edges[i][1]]

    can_go = graph[0]
    # visited = [0 for i in range(len(info))]
    # visited[0] = 1

    # 부모 -> 자식 만 있으므로 방문체크 필요 없음.
    go_ahead(graph, info, can_go, 0, 1)

    answer = max_result

    return answer


if __name__ == '__main__':
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))