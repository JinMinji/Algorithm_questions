def check(cur_sum, right_lst, target):
    if cur_sum == target + sum(right_lst):
        return True
    else:
        return False


def weight(cur_sum, idx, right_lst, weights, t):
    if idx == len(weights):
        return check(cur_sum, right_lst, t)
    else:
        tmp = weight(cur_sum + weights[idx], idx+1, right_lst, weights, t)
        if not tmp:
            tmp = weight(cur_sum, idx+1, right_lst, weights, t)
            if not tmp:
                right_lst.append(weights[idx])
                tmp = weight(cur_sum, idx+1, right_lst, weights, t)

        return tmp


def solutions(weights, target):
    return weight(0, 0, [], weights, target)
