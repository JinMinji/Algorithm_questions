def beauty_max(s):
    max_result = 0
    if s.count(s[0]) == len(s):  # 만약 다 같은 문자열이면, 더 고려하지말고 0리턴.
        return 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                max_result = max(max_result, j - i)
    return max_result


def solution(s):
    answer = 0

    all_substring = []
    # 모든 부분 문자열 구하기
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            all_substring.append(s[i:j])

            # 부분 문자열마다 max값 더하기
    for i in all_substring:
        answer += beauty_max(i)

    return answer