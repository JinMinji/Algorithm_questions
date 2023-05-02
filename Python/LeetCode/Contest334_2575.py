# Contest 334, Q2

from typing import List

def divisibilityArray(word: str, m: int) -> List[int]:
    answer = [0 for i in range(len(word))]

    num = list(int(n) for n in word)

    remain = 0

    for i in range(len(word)):
        remain = remain * 10 + num[i]
        remain %= m
        if remain == 0:
            answer[i] = 1

    return answer


if __name__ == '__main__':
    word = input()
    m = int(input())
    answer = divisibilityArray(word, m)
    print(answer)