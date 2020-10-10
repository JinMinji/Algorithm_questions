# 나이순, 가입순 정렬

member_num = int(input())

member_list = []

for _ in range(member_num):
    a = input().split()
    member_list.append((int(a[0]), a[1]))

member_list = sorted(member_list, key=lambda x: x[0])
# 특정원소를 기준으로 해서 정렬하면, 나머지 원소는 Stable(특정원소가 동일값일 경우, 처음 입력된 순서 유지)
# min = 0
#
# for i in range(member_num):
#     for j in range(i, member_num):
#         if member_list[j][0] < member_list[min][0]:
#             min = j
#
#     member_list[i], member_list[min] = member_list[min], member_list[i]

for i in member_list:
    print (i[0], i[1])

