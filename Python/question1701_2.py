#20210711 Cubeditor

def make_pi(word):
    pi = [0 for _ in range(len(word))]
    longest_len = 0
    i = 1
    while i < len(word):
        if word[i] == word[longest_len]:
            longest_len += 1
            pi[i] = longest_len
            i += 1
        else:
            if longest_len != 0:
                longest_len = pi[longest_len-1]
            else:
                pi[i] = 0
                i += 1
    return pi


if __name__ == '__main__':
    input_string = input()

    max_len = 0
    for i in range(len(input_string)):
        max_len = max(max_len, max(make_pi(input_string[i:])))

    print(max_len)
