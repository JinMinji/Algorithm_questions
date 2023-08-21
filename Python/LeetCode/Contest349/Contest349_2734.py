# Contest349, Q2

class Solution:
    def smallestString(self, s: str) -> str:
        start = -1
        result = []
        for i in range(len(s)):
            if s[i] != 'a':
                start = i
                break
            result.append(s[i])

        if start == -1: # 다 'a'일 때
            result = list(s)
            result[-1] = 'z'
            return "".join(result)

        end = len(s)
        for i in range(start, len(s)):
            if s[i] == 'a':
                end = i
                break
            result.append(chr(ord(s[i])-1))

        answer = "".join(result) + s[end:]
        return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.smallestString(s = "cbabc"))
    # print(test.smallestString(s = "acbbc"))
    # print(test.smallestString(s = "leetcode"))
    print(test.smallestString(s="a"))