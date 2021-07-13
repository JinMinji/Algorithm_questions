# 20210705 드래곤 앤 던전
global h_atk, h_hp
h_atk = 0
h_hp = 0


def battle(h_hp):
    max_hp = h_hp
    tmp_atk = h_atk

    for room in Dungeon:
        if room[0] == 1:
            m_atk, m_hp = room[1], room[2]
            while True:
                m_hp -= tmp_atk
                if m_hp <= 0:
                    break
                h_hp -= m_atk
                if h_hp <= 0:
                    return False
        else:  # 포션
            tmp_atk += room[1]
            h_hp = min(max_hp, h_hp + room[2])  # 최대생명력 이상으로 체력이 늘어날 수 없음.

    return True


def lower_bound():
    start = 0
    end = 12345600000000  # 얼마나 크게 잡아야하는징,,
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        if battle(mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


if __name__ == '__main__':
    N, h_atk = map(int, input().split())

    Dungeon = list()
    end = 0
    for i in range(N):
        Dungeon.append(list(map(int, input().split())))
    #         T, atk, hp = map(int, input().split()

    print(lower_bound())
