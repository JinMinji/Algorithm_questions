#2109 순회강연, 골드3
import sys
import heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip('\n'))
    proposal = list()
    for i in range(N):
        money, time = map(int, sys.stdin.readline().split())
        proposal.append([time, money])

    result = 0
    if proposal:
        proposal.sort(reverse=True)
        cur_time = proposal[0][0]
        can_choice = list()
        # print(proposal)

        while True:
            time = proposal[0][0]
            if time != cur_time:
                # 현재 시간과 다르면, 시간을 1씩 줄이면서, 선택할 수 있는 강연 목록에서
                # 강연비가 가장 비싼 순서대로 뽑고, 결과값에 더한다 (음수이므로 -를 붙여 준다.)
                cur_time -= 1
                if can_choice:
                    result -= heapq.heappop(can_choice)
                continue

            if time == cur_time:    #현재 시간과 같으면, 선택할 수 있는 강연 목록에 추가한다.
                time, money = proposal.pop(0)
                heapq.heappush(can_choice, -money)

            if not proposal:    #강연이 더이상 없으면,
                cur_time = time
                # print("남은 시간 : ", cur_time, can_choice)
                for i in range(cur_time):
                    # print(i)
                    if can_choice:
                        result -= heapq.heappop(can_choice)

                    else:
                        break

                break

    print(result)