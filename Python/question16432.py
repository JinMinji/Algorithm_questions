## 20210705 떡장수와 호랑이

def dfs(start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        visited.append(node)
        if tteoks.get(node, []):
            need_visit.extend(tteoks[node])
        else:  # 더이상 갈 곳이 없다 ? 도착지거나, 길이 끊김
            if node // 10 == N - 1:  # 도착지일경우
                return visited

            else:  # 길이 끊김.
                visited.pop()  # 넣었던거 도로 빼주고
                if visited and node in tteoks[visited[-1]]:  # 나에게 왔던 길을 끊어줘야함. 이 길로는 다시 오지않게
                    tteoks[visited[-1]].remove(node)

    return []  # 다 돌았는데도 못찾았으면, 끝.


def find_way(graph):
    way = [-1]

    for _ in range(1, 10):
        if graph.get(_, []):  # 모든 시작점에서 확인.
            res = dfs(_)
            if len(res) == N:
                way = res
                return way  # 더 찾을 것도 없이 바로 return

    return way


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
                    tteoks[from_i] = tteoks.get(from_i, []) + [to_i]  # tteok[23] 이면, 2번째날 3번떡.

        yesterday = today

    answer = list()
    if N != 1:
        answer = find_way(tteoks)

    else:
        answer.append(yesterday[0])

    print(answer[0])

    for i in range(1, len(answer)):
        print(answer[i] % 10)
