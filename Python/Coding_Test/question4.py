def find_short(n, s, a, graph):
    shortest = 1000000
    visited = []
    for x, f in graph[s].items():
        if x == a:
            if shortest > f:
                shortest = f
        else:
            if shortest > f:
                if n > 0:
                    shortest = min(shortest,(f + find_short(n-1, x, a, graph)))
    return shortest

def solution(n, s, a, b, fares):
    route = dict()
    for i in fares:
        if i[0] not in route:
            route[i[0]] = {i[1]:i[2]}
        else:
            route[i[0]][i[1]] = i[2]

        if i[1] not in route:
            route[i[1]] = {i[0]:i[2]}
        else:
            route[i[1]][i[0]] = i[2]

    print(route)

    a_route = find_short(n, s, a, route) + find_short(n, a, b, route)
    b_route = find_short(n, s, b, route) + find_short(n, b, a, route)
    c_route = find_short(n, s, a, route) + find_short(n, s, b, route)

    answer = min(a_route, b_route)
    answer = min(c_route, answer)

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))


import heapq


def find_shor(n, start, arrive, graph):
    shortest = 100000 # 최댓값으로 설정
    for i in graph:
        if i[0] == start:
            print(i[2])
            if shortest > i[2]:
                if i[1] == arrive :
                    shortest = i[2]
                    print(shortest)
                else :
                    fare = i[2]
                    while fare < shortest:
                        if n > 0:
                            fare = i[2] + find_short(n-1, i[1], arrive, graph)

        return shortest