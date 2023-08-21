#20210711 문자열폭발


def after_explosion(original, bomb):
    result = ''
    text = original

    is_exist_bomb = True

    while is_exist_bomb:
        is_exist_bomb = False
        tmp_res = ''
        t = 0
        while t <= len(text) - len(bomb):
            cnt = 0
            for b in range(len(bomb)):
                if text[t + b] == bomb[b]:
                    cnt += 1
                else:
                    cnt = 0
                    break

            if cnt == len(bomb):
                is_exist_bomb = True
                t += len(bomb) - 1
            else:
                tmp_res += text[t]

            t += 1
        text = tmp_res

    result = text

    return result


if __name__ == '__main__':
    in_string = input()
    explosion_word = input()

    print(after_explosion(in_string, explosion_word))