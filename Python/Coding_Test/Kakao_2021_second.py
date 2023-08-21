import json
import requests
import random

scom = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
dr = [0, -1, 0, 1, 0, 0, 0]
dc = [0, 0, 1, 0, -1, 0, 0]
tcommand = {scom[i]: i for i in range(7)}


class truck:
    # p: 트럭의 위치
    # load: 가지고있는 자전거의 양
    def __init__(self):
        self.p = 0
        self.load = 0

    def __str__(self):
        return str(self.p) + ' ' + str(self.load)

    def __repr__(self):
        return '(' + str(self.p) + ' ' + str(self.load) + ')'


# Locations API(1)
# 각 자전거 대여소가 보유한 자전거 수 반환
def getLocations(url, headers, bicycle):
    path = 'locations'
    req = requests.get('/'.join([url, path]), headers=headers)
    j = req.json()

    for id, cnt in [(i['id'], i['located_bikes_count']) for i in j['locations']]:
        bicycle[id] = cnt

    return bicycle


# Trucks API(2)
# 각 트럭의 위치와 싣고 있는 자전거 수 반환
def getTrucks(url, headers, trucks):
    path = 'trucks'
    req = requests.get('/'.join([url, path]), headers=headers)
    j = req.json()

    for id, location_id, bike_count in [(i['id'], i['location_id'], i['loaded_bikes_count']) for i in j['trucks']]:
        trucks[id].p = location_id
        trucks[id].load = bike_count

    return trucks


# Simulate API(3)
# 각 트럭이 행할 명령을 담아 서버에 전달
def putSimulate(url, headers, data):
    path = 'simulate'
    req = requests.put('/'.join([url, path]), headers=headers, data=data)

    return req.json()


# =========================API들 구현===================================

# A에서 B까지 이동하려면 어떻게 이동해야하는지 기록. -> map의 ID 기준
# ex) 문제 1 기준
# ID 0 = (4, 0)
# ID 6 = (3, 1)
# ID 0 -> ID 6 = [up, right] = [1, 2]
# 따라서 dcom = [1, 2]
def getDist(loc, f, t):
    dcom = [tcommand['up'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] > loc[t][0]]
    dcom.extend([tcommand['down'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] < loc[t][0]])
    dcom.extend([tcommand['right'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] < loc[t][1]])
    dcom.extend([tcommand['left'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] > loc[t][1]])
    return (abs(loc[f][0] - loc[t][0]) + abs(loc[f][1] - loc[t][1]), dcom)


# t: truck, bnum: bicycles, map: ID X의 (x, y) 좌표 저장, mmap: 지도에서 (x, y)에 있는 ID 저장,
# 트럭을 맵의 랜덤 방향으로 이동시키면서, 자전거의 개수가 평균보다 크면 트럭에 자전거를 담고,
# 자전거의 개수가 평균보다 작으면 자전거를 내려준다.
def truckmove(t, bnum, map, mmap, mean, comm, dest, all='not'):
    x, y = map[t.p][0], map[t.p][1]
    retcomm = []

    for i in comm:
        # Simulate API에 전달할 수 있는 트럭의 명령어는 최대 10까지 라서 커맨드의 길이가 너무 길어지면 break
        if len(retcomm) >= 10: break
        id = mmap[x][y]

        if id == dest and all == 'out':
            need = t.load
            retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
            bnum[id] += need
        elif all == 'in' and id == dest:
            need = min(bnum[id] - mean, 20 - t.load)
            retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
            bnum[id] -= need
        elif all == 'out':
            need = min(bnum[id] - mean, 20 - t.load)
            retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
            bnum[id] -= need
        elif all == 'in':
            need = min(mean - bnum[id], t.load)
            retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
            bnum[id] += need
        else:
            # ID X에 있는 자전거의 개수가 평균보다 작으면 트럭이 가진 자전거를 내려줌
            if bnum[id] < mean:
                need = min(mean - bnum[id], t.load)
                retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
                bnum[id] += need

            # ID X에 있는 자전거의 개수가 평균보다 많으면 트럭이 자전거를 가져감
            elif bnum[id] > mean:
                need = min(bnum[id] - mean, 20 - t.load)
                retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
                bnum[id] -= need

        retcomm.append(i)
        x += dr[i]
        y += dc[i]

    return retcomm


def solve(qid=1):
    url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
    path = 'start'
    token = '2562932a03eccf9dd89313c02efcce67'
    param = {'problem': qid}
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

    # 문제 1번과 2번에 따라서 값을 정해놓음
    # msize: map 크기
    # mean: 모든 좌표의 자전거들을 평균값으로 두려고 함. ID X에 mean보다 자전거가 많을 수록 우선 방문
    msize = 0
    mean = 15

    if qid == 1:
        msize = 5
        mean = 2
    else:
        msize = 60
        mean = 3

    mymap = [[msize - i - 1 + msize * j for j in range(msize)] for i in range(msize)]

    # 0번 ID부터 지도 위치를 구하기 쉽도록 단순하게 map을 사용해서 매핑
    pos = {mymap[i][j]: (i, j) for i in range(msize) for j in range(msize)}

    # 문제에 따라 트럭 수를 저장해놓음
    tnum = [0, 5, 10]

    # 자전거들의 정보를 담기 위한 2차원 리스트
    bicycles = [0 for _ in range(msize * msize)]

    # 트럭 객체를 만들어 놓음
    trucks = [truck() for _ in range(tnum[qid])]

    req = requests.post('/'.join([url, path]), headers=headers, data=json.dumps(param))
    j = req.json()
    auth_key = j['auth_key']
    headers = {'Authorization': auth_key, 'Content-Type': 'applications/json'}

    next_command = [0 for _ in range(tnum[qid])]
    prev_bicycle = getLocations(url, headers, bicycles)

    for i in range(720):
        # 트럭의 목적지를 '랜덤'으로 만듦
        trucksdes = [int(random.uniform(0, msize * msize)) for i in range(len(trucks))]
        bicycles = getLocations(url, headers, bicycles)
        mmin = 100000000
        mini = 0
        mmax = -1000000000
        maxi = 0

        # 자전거수가 가장 많은 위치와 가장 적은 위치를 구함
        # 자전거수가 많은 곳은 반납이 많은 곳이고, 자전거수가 적은 곳은 소비가 많은 곳이라고 생각
        # (즉, 두 곳 모두 트럭이 우선적으로 이동해야 하는 장소)

        for i, j in enumerate([prev_bicycle[i] - bicycles[i] for i in range(len(bicycles))]):
            if mmin > j:
                mmin, mini = j, i
            if mmax < j:
                mmax, maxi = j, i

        trucks = getTrucks(url, headers, trucks)
        # 자전거 개수가 0개 이므로, 트럭들을 가장 우선적으로 빠르게 이동해야 하는 곳(매우 긴급)
        emergen = [i[0] for i in enumerate(bicycles) if i[1] == 0]

        i = 0

        # 트럭 하나에 20개씩 옮길 수 있기 때문에 개수 나누기
        while i < min(int(mmin / 20), tnum[qid]):
            trucksdes[i] = mini
            i += 1
        while i < min(int(mmax / 20), tnum[qid]):
            trucksdes[i] = maxi
            i += 1

        for i in range(tnum[qid]):
            t = trucks[i]
            # 만약 매우 긴급하게 자전거를 하차해야하는 곳이 있다면, 해당 위치로 트럭을 우선 이동
            if len(emergen) > 0:
                trucksdes[i] = emergen.pop()
            idx, next_command[i] = getDist(pos, t.p, trucksdes[i])

        nextcommand = []

        for i in range(tnum[qid]):
            t = trucks[i]
            ncom = truckmove(t, bicycles, pos, mymap, mean, next_command[i], -1, 'not')
            nextcommand.append({'truck_id': i, 'command': ncom})

        j = putSimulate(url, headers=headers, data=json.dumps({'commands': nextcommand}))
        print(j['time'])
        # 현재 자전거 수를 이전의 자전거 수로 백업
        prev_bicycle = [i for i in bicycles]

    req = requests.get(url + '/score', headers=headers)
    print(req.json()['score'])


if __name__ == '__main__':
    solve()



#https://www.youtube.com/watch?v=V_Q7vOpuFu8