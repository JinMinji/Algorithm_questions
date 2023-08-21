#5주차 모음사전
def solution(word):
    answer = 0
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    # 'A'       -> 'E'      : 1*5 + 1*5*5 + 1*5*5*5 + 1*5*5*5*5 => 5 + 5**2 + 5**3 + 5**4
    # 'AA'      -> 'AE'     : 1*1*5 + 1*1*5*5 + 1*1*5*5*5       => 5 + 5**2 + 5**3
    # 'AAA'     -> 'AAE'    : 1*1*1*5 + 1*1*1*5*5               => 5 + 5**2
    # 'AAAA'    -> 'AAAE'   : 1*1*1*1*5                         => 5
    # 'AAAAA'   -> 'AAAAAE' : 1*1*1*1*1                         => 1

    m = [1 + 5 + 5 ** 2 + 5 ** 3 + 5 ** 4, 1 + 5 + 5 ** 2 + 5 ** 3, 1 + 5 + 5 ** 2, 1 + 5, 1]
    for i in range(len(word)):
        answer += vowels[word[i]] * m[i] + 1

    return answer


if __name__ == '__main__':
    print('')
    print(solution('AAAAE'))
    print(solution('AAAE'))
    print(solution('I'))
    print(solution('EIO'))


