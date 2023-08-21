# 20210705 떡장수와 호랑이 두번째풀이

def find_way(graph):    # 끝까지 가는 길을 찾아 그 경로를 반환하고, 길이 없으면 -1만 들어있는 리스트 반환.
    # 시작지점 하나씩 돌기
    for start in range(1, 10):   # 떡은 1~9번 떡이 있음
        if graph.get(start, []): # 값이 있으면, 거기서부터 시작.
            route = list()
            to_visit = list()
            to_visit.append(start)
            while to_visit:
                node = to_visit.pop()   # DFS이므로 뒤부터 탐색
                if len(route) > node // 10:
                    continue
                route.append(node)
                if graph.get(node, []):     # 값이 있으면!
                    to_visit.extend(graph[node])

                else:   # 값이 없으면
                    if len(route) == N:     # 마지막날이라 없는거거나,
                        return route
                    else:   # 더 이상 방법이 없어서 없는 것.
                        route.remove(node)  # 일단 돌아가고,
                        if route:
                            graph[route[-1]].remove(node)   # route의 맨 마지막에는 node의 부모가 담겨있다.
                            # 부모와의 연결을 끊어, 다시 방문하지 않도록 한다.
                            if not graph.get(route[-1], []):
                                route.pop()     # 마지막값이, 더이상 연결된 애가 없으면, 막혀있는 거니까 돌아가 준다.
                                # 연결된 애가 남아있다면, 아직 탐색중인 거니까 그냥 쭉 탐색
    # 다 돌았는데도 리턴 못한 거면, 방법이 없다는 뜻
    return [-1]


if __name__ == '__main__':
    N = int(input())
    tteoks = dict()  # 딕셔너리로 그래프 생성

    yesterday = list(map(int, input().split()))
    yesterday.pop(0)  # 떡 개수는 필요없음

    for i in range(1, N):
        today = list(map(int, input().split()))
        today.pop(0)  # 떡 개수는 필요없음
        for y in yesterday:  # 1 <= y <= 9  떡종류는 무조건 한자리수.
            for t in today:
                if y != t:  # 어제, 오늘이 같은 떡이 아니면
                    from_i = (i - 1) * 10 + y
                    to_i = i * 10 + t
                    tteoks[from_i] = tteoks.get(from_i, []) + [to_i]
        from_i = (i - 1) * 10 + y

        tteoks[from_i] = list(set(tteoks.get(from_i, [])))

        yesterday = today   # 하루가 지남.

    answer = list()
    if N == 1:  # 위 로직을 안탐. 그냥 출력.
        answer.append(yesterday[0])

    else:
        answer = find_way(tteoks)

    print(answer[0])

    for i in range(1, len(answer)):
        print(answer[i] % 10)
