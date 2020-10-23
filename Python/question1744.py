#20210524 수 묶기

def max_total():
    total = 0
    turning = 0
    cnt = 0
    for i in range(0,len(num_list)-1,2):
        if num_list[i] <= 0: # 음수면, 음수끼리 곱하거나 0을 곱해서 -를 없애주는게 좋다!
            if num_list[i+1] <= 0:
                total += num_list[i]*num_list[i+1]
                cnt += 2
            else:
                total += num_list[i]
                turning = i+1
                cnt += 1
                break
        else:
            turning = i
            break
    if cnt < len(num_list[:turning]):
        total += num_list[cnt]
    cnt = 0
    if num_list[turning] == 1:
        total+= 1
        cnt += 1
        if (turning+1) < len(num_list):
            turning += 1

    for i in range(len(num_list)-1, turning,-2):
        total += num_list[i]*num_list[i-1]
        cnt += 2
    if cnt < len(num_list[turning:]):
        total += num_list[turning]

    return total

if __name__ == '__main__':
    N = int(input())
    num_list = list()
    for _ in range(N):
        num_list.append(int(input()))

    num_list.sort()

    print(max_total())