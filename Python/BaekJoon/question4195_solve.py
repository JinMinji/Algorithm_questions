#풀이방법 신기함..

array = input()

for i in range(9, -1, -1): #(9~0)
    for j in array:
        if int(j) == i:
            print(i, end='')