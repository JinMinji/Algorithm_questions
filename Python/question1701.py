#20210711 Cubeditor

def make_pi(word):  #kmp
    pi = [0 for _ in range(len(word)+1)]
    for i in range(0, len(word)//2):    # word가 i+1번째 글자까지만 맞을 때.
        cnt = 0
        for j in range(0, i+1):
            if word[j] == word[j-i-1]:
                cnt += 1
            else:
                break
        pi[i+1] = cnt

    return pi

def find(text, word):
    i = 0
    s = 0
    pi = make_pi(word)
    while i <= len(text)-len(word):
        cnt = 0
        for j in range(s, len(word)):
            if text[i+j] == word[j]:
                cnt = j

            else:
                i += len(word)
                s += pi[cnt]
                break
        if cnt >= len(word):
            return True
        i += 1

    return False

def longest_substring(target):
    max_len = 0
    for i in range(len(target)):
        # i는 부분분자열 길이.
        for j in range(len(target)-i):
            tmp_word = target[j:i+1]
            if find(target, tmp_word):
                max_len = i-1

    return max_len


if __name__ == '__main__':
    in_string = input()

    print(longest_substring(in_string))