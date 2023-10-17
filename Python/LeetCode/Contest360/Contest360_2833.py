# Contest360, Q1

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_cnt = 0
        l_cnt = 0
        cnt = 0
        for s in moves:
            if s == 'L':
                l_cnt += 1
            elif s == 'R':
                r_cnt += 1
            else:
                cnt += 1

        answer = abs(r_cnt-l_cnt) + cnt
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.furthestDistanceFromOrigin(moves = "L_RL__R"))
    print(test.furthestDistanceFromOrigin(moves = "_R__LL_"))
    print(test.furthestDistanceFromOrigin(moves = "_______"))

