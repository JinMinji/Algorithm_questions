# 별 찍기 - 11, 골드 4

def print_star(start_pos):
    star = '*'
    space = ' '
    first_line = '' + space * start_pos
    first_line += star + space * 2
    second_line = '' + space * (start_pos - 1)
    second_line += star + space + star + space
    third_line = '' + space * (start_pos - 2)
    third_line += star * 5
    print(first_line)
    print(second_line)
    print(third_line)


if __name__ == '__main__':
    N = int(input())

    for i in range(N//3):
        print_star(N-(3*i))

