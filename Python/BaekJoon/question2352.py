# 20210507 반도체설계

N = int(input())

port_input = list(map(int, input().split()))

# pre_portnum = 0
# cur_portnum = port_input[0]
#
# result = 1
#
# for _ in range(1, N):
#     # port_input[_] : next_portnum
#     if cur_portnum < port_input[_]:
#         result += 1
#         pre_portnum = cur_portnum
#         cur_portnum = port_input[_]
#     elif cur_portnum > port_input[_] and port_input[_] > pre_portnum:
#         cur_portnum = port_input[_]
# print(result)


connectedList = list()
connectedList.append([1, port_input[0]])

for _ in range(1, N):
    if connectedList[-1][1] < port_input[_]: # 안 꼬였을 때,
        connectedList.append([_+1, port_input[_]])

    elif connectedList[-1][1] > port_input[_]: # 꼬였을 때,
        if
        connectedList.pop()
        connectedList.append([_+1, port_input[_]])
    else:

result = len(connectedList)

print(result)
