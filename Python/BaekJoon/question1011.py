# Fly me to the Alpha Centauri, 골드 5

# 1 -> 1 : 1
# 2 -> 1, 1 : 2
# 3 -> 1, 1, 1 : 3
# 4 -> 1, 2, 1 : 3
# 5 -> 1, 2, 1, 1 : 4
# 6 -> 1, 2, 2, 1 : 4
# 7 -> 1, 2, 2, 1, 1 : 5
# 8 -> 1, 2, 2, 2, 1 : 5
# 9 -> 1, 2, 3, 2, 1 : 5
# 10 -> 1, 2, 3, 2, 1, 1 : 6
# 11 -> 1, 2, 3, 2, 2, 1 : 6
# 12 -> 1, 2, 3, 3, 2, 1 : 6
# 13 -> 1, 2, 3, 3, 2, 1, 1 : 7
# 14 -> 1, 2, 3, 3, 2, 2, 1 : 7
# 15 -> 1, 2, 3, 3, 3, 2, 1 : 7
# 16 -> 1, 2, 3, 4, 3, 2, 1 : 7
# 17 -> 1, 2, 3, 4, 3, 2, 1, 1 : 8
#
# def solutions(term):
#     for i in range(1, 2 ** 30):
#         if term <= i*(i+1):
#             # print(term, i, tmp, tmp + 1 ** 2, tmp + i)
#             if term <= i**2:
#                 return i * 2 - 1
#
#             else:
#                 return i * 2


if __name__ == '__main__':
    T = int(input())

    for t in range(T):
        start, end = map(int, input().split())
        term = end - start
        for i in range(1, 2 ** 30):
            if term <= i*(i+1):
                # print(term, i, tmp, tmp + 1 ** 2, tmp + i)
                if term <= i**2:
                    print(i * 2 - 1)
                    break

                else:
                    print(i * 2)
                    break

    # for i in range(1,20):
    #     print(i, ':', solutions(i))
