row, col = map(int, input().split())

input_lst = []

for i in range(row):
    col_lst = input()
    input_lst.append(col_lst)

row_x = [0]*row
col_x = [0]*col

for i in range(row):
    for j in range(col):
        if input_lst[i][j] == "X":
            row_x[i] = 1
            col_x[j] = 1

result = max(row_x.count(0), col_x.count(0))

print(result)