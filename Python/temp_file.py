def solutions(str):
    str = str[2:]
    str = str[:-2]

    tmp_lst = str.split(',')

    tmp_dict = dict()
    for i in range(len(tmp_lst)):
        tmp_key, tmp_val = tmp_lst[i].split(':')
        tmp_key = tmp_key.replace("'", '')
        tmp_key = tmp_key.replace(" ", '')
        tmp_val = int(tmp_val)
        tmp_dict[tmp_key] = tmp_val

    return tmp_dict

if __name__ == '__main__':
    tmp_str = "[{'x': 559, 'y': 213, 'width': 50, 'height': 32}]"
    print(solutions(tmp_str))