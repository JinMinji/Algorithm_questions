#20210714 문자열 폭발 두번째풀이

def after_explosion(text, bomb):
    result = list()
    for c in range(len(text)):
        result.append(text[c])
        if text[c] == bomb[-1]:
            is_same = True
            if len(result) >= len(bomb):
                for i in range(len(bomb)):
                    if result[-i-1] != bomb[-i-1]:
                        is_same = False
                        break
                if is_same:
                    for _ in range(len(bomb)):
                        result.pop()

    return result


if __name__ == '__main__':
    in_string = input()
    explosion_word = input()

    list_res = after_explosion(in_string, explosion_word)

    if list_res:
        for d in list_res:
            print(d, end='')
    else:
        print("FRULA")