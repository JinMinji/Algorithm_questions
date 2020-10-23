n = 4
horizontal = True

answer = [[0 for i in range(n)] for j in range(n)]

if horizontal:
    answer[0][1] = 1
    present_row = 0
    present_col = 1

else :
    answer[1][0] = 1
    present_row = 1
    present_col = 0

time = 1

for i in range(n**2):
    #오른쪽, 아래, 왼쪽아래, 오른쪽 위 4가지 이동방법이 있음
    #오른쪽으로 움직이는 경우 +1
    if present_row == 0 or present_row == n-1:
        print("1 in",present_row, present_col)
        if present_row == 0 and answer[1][present_col-1] != 0:
            time += 1
            answer[present_row][present_col+1] = time
            present_col += 1
            continue
        elif present_row == n-1 and (present_col+1 < n and answer[n-2][present_col+1] != 0):
            time += 1
            answer[present_row][present_col + 1] = time
            present_col += 1
            continue

    #아래로 움직이는 경우 +1
    if present_col == 0 or present_col == n-1:
        print("2 in")
        if present_col == 0 and answer[present_row-1][1] != 0:
            time += 1
            answer[present_row+1][0] = time
            present_row += 1
            continue
        elif present_col == n-1 and (present_row+1 < n and answer[present_row+1][present_col-1] != 0):
            time += 1
            answer[present_row+1][present_col] = time
            present_row += 1
            continue

    #왼쪽 아래로 움직이는 경우 +2
    if present_row == 0 or present_col == n-1:
        print("3 in")
        if present_row+1 < n:
            if answer[present_row+1][present_col-1] == 0:
                time += 2
                answer[present_row+1][present_col-1] = time
                present_row += 1
                present_col -= 1
                continue

    #오른쪽 위로 움직이는 경우 +2
    if present_row == 0 or present_col == n-1:
        print("4 in")
        if present_col+1 < n:
            if answer[present_row-1][present_col+1] == 0:
                time += 2
                answer[present_row-1][present_col+1] = time
                present_row -= 1
                present_col += 1
                continue

    if present_col+1 < n:
        if answer[present_row-1][present_col+1] == 0:
            time += 2
            answer[present_row - 1][present_col + 1] = time
            present_row -= 1
            present_col += 1
    if present_row+1 < n:
        if answer[present_row+1][present_col-1] == 0:
            time += 2
            answer[present_row+1][present_col-1] = time
            present_row += 1
            present_col -= 1




print(answer)