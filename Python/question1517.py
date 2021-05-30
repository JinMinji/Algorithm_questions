#20210527 버블소트

def bubble_sort(b_list):
    swap = 0
    for i in range(len(b_list)-1):
        for j in range(1, len(b_list)-i):
            if b_list[j-1] > b_list[j]:
                tmp = b_list[j-1]
                b_list[j-1] = b_list[j]
                b_list[j] = tmp
                #b_list[j-1], b_list[j] = b_list[j], b_list[j-1]
                swap += 1
    return swap

if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, input().split(' ')))

    print(bubble_sort(num_list))

