# Contest371, Q2

from typing import List

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        answer = set()
        access_cnt = dict()
        access_times.sort(key=lambda x : x[1])
        for i in range(len(access_times)):
            if access_times[i][0] in access_cnt:
                access_cnt[access_times[i][0]].append(access_times[i][1])
                cur_times = access_cnt[access_times[i][0]]
                if len(cur_times) >= 3:
                    cnt = 1
                    for k in range(len(cur_times)-2, -1, -1):
                        # print(access_times[i][0], cur_times[k], cur_times[k-1], '---', int(cur_times[k]) - int(cur_times[k-1]))
                        if int(cur_times[-1]) - int(cur_times[k]) < 100:
                            cnt += 1
                            print(cnt, 'cnt')
                            if cnt >= 3:
                                answer.add(access_times[i][0])
                                break
                        else:
                            break
            else:
                access_cnt[access_times[i][0]] = [access_times[i][1]]
        
        return list(answer)
        
if __name__ == "__main__":
    test = Solution()
    # print(test.findHighAccessEmployees(access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]))
    # print(test.findHighAccessEmployees(access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))
    # print(test.findHighAccessEmployees(access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]))
    print(test.findHighAccessEmployees([["eazbkekis","1034"],["relf","1126"],["afwpabwyds","1114"],["afwpabwyds","1105"],["relf","1031"],["afwpabwyds","1010"],["vzqpz","1047"],["relf","1103"]]))
