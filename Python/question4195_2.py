# 친구 네트워크

def how_many(a, b, friends_map):
    network = list()
    to_check = [a, b]

    while to_check:
        cur = to_check.pop(0)
        if cur not in network:
            network.append(cur)
            to_check.extend(friends_map[cur])

    return len(network)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        F = int(input())

        friends_map = dict()

        for f in range(F):
            a, b = map(str, input().split(' '))
            friends_map[a] = friends_map.get(a, [])
            friends_map[a].append(b)
            friends_map[b] = friends_map.get(b, [])
            friends_map[b].append(a)

            print(how_many(a, b, friends_map))
            # print(friends_map)




