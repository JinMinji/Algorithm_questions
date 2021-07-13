#20210711 가르침
from itertools import combinations

words = list()

def how_many_words(K):
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # 알파벳 a~z ASCII는 97~122

    tmp_list = [97 + i for i in range(0, 26)]
    # a = 97, n = 110, t = 116, i = 105
    tmp_list.remove(97)
    tmp_list.remove(110)
    tmp_list.remove(116)
    tmp_list.remove(105)
    tmp_list.remove(99)

    pop_list = list(combinations(tmp_list, K-5))
    # a = 97, n = 110, t = 116, i = 105, c = 99

    max_word = 0
    for i in range(len(pop_list)):
        cnt = 0
        for word in words:
            ispossible = True
            for j in range(4, len(word)-4):
                if ord(word[j]) not in pop_list[i] and word[j] not in ['a', 'n', 't', 'i', 'c']:
                    ispossible = False
                    break
            if ispossible:
                cnt += 1

        max_word = max(cnt, max_word)

    return max_word


if __name__ == '__main__':
    N, K = map(int, input().split())

    words = list()
    for i in range(N):
        words.append(input())

    # anta tica -> antic 5개는 필수.
    if K < 5:
        print(0)

    else:
        print(how_many_words(K))