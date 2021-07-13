# 20210705 드래곤 앤 던전 두번째 풀이
import math

h_atk = 1  # 영웅의 공격력
h_hp = 1  # 영웅의 체력
m_hp_max = 1  # 몬스터의 최대체력
m_atk_max = 1  # 몬스터의 최대공격력


def battle(h_hp):
    max_hp = h_hp
    tmp_atk = h_atk

    for room in Dungeon:
        if room[0] == 1:
            m_atk, m_hp = room[1], room[2]
            if math.ceil(m_hp / tmp_atk) <= math.ceil(h_hp / m_atk):
                h_hp -= (math.ceil(m_hp / tmp_atk) - 1) * m_atk

            else:
                return False

        # while True:
        #	m_hp -= tmp_atk
        #	if m_hp <= 0:
        #		break
        #	h_hp -= m_atk
        #	if h_hp <= 0:
        #		return False
        else:  # 포션
            tmp_atk += room[1]
            h_hp = min(max_hp, h_hp + room[2])  # 최대생명력 이상으로 체력이 늘어날 수 없음.

    return True


def lower_bound():
    start = 1  # 1이상이어야 함.
    end = (N * m_hp_max * m_atk_max) // h_atk + 1  # 나머지있으면 그냥 올림해주는걸로.
    # 몬스터의 최대 공격력, 최대 체력.
    # 방은 N개
    # 내 공격력은 -되지 않으므로 최소 초기입력값인 h_atk 으로 나눌 수 있음.
    answer = 1

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
        # Dungeon.append(list(map(int, input().split())))
        T, atk, hp = map(int, input().split())
        if T == 1:
            if atk > m_atk_max:
                m_atk_max = atk
            if hp > m_hp_max:
                m_hp_max = hp

        Dungeon.append([T, atk, hp])

    print(int(lower_bound()))

