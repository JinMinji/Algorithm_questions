def segment(x, space):
    # Write your code here
    min_lst = list()
    cur_segments = list()
    for i in range(x):
        cur_segments.append(space[i])

    cur_min = min(cur_segments)
    min_lst.append(cur_min)
    min_index = cur_segments.index(cur_min)

    for i in range(x, len(space)):
        cur_segments.pop(0)
        cur_segments.append(space[i])
        if min_index < i:
            cur_min = min(cur_segments)
            min_lst.append(cur_min)
            min_index = cur_segments.index(cur_min)

        elif cur_min > space[i]:
            cur_min = space[i]
            min_index = i
            min_lst.append(space[i])

    return max(min_lst)

if __name__ == '__main__':
    print(segment(3, [2,5,4,6,8]))