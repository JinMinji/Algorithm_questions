# 자리수 내림차순

num = input()

list = []
for i in num:
    list.append(i)

list.sort(reverse=True)

for _ in list:
    print (_ , end="")