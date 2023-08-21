#20210720 개미굴 두번째 풀이

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = []

class linkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next

            cur.next = node

    # def getindex(self, data):
    #     cur = self.head
    #     i = 0
    #
    #     while cur:
    #         if cur.data == data:
    #             return i
    #         else:
    #             cur = cur.next
    #             i += 1
    #     return -1

def draw_map(map_info):



if __name__ == '__main__':
    N = int(input())

    starts = list() #처음 시작할 head들을 담아줄 리스트
    feeds = list()  #모든 feed 종류를 담아줄 리스트

    # step1. insert
    lList = list()
    for i in range(N):
        info = list(map(int, input().split()))

        info.pop(0)    # 맨앞에 개수는 빼준다

        now = Node()
        for f in range(len(info)):
            if f == 0:  # 시작일때! head 맞춰주기.
                if info[f] not in starts:
                    starts.append(info[f])
                    tmp_list = linkedList()     # 새 연결리스트.
                    tmp_node = Node(info[f])    # 새 노드
                    tmp_list.append(tmp_node)   # 새연결리스트에 노드 삽입
                    lList.append(tmp_list)      # 연결리스트 목록에 새연결리스트 삽입
                    now = tmp_list.head

                else:   #이미 시작노드에 있을 때
                    start_index = starts.index(info[f])     # 어차피 인덱스 똑같으니까
                    now = lList[start_index].head.data

            else:
                if info[f] not in now.next: # next에 동일한 먹이가 없으면,
                    now_node = Node(info[f])
                    now.next.append(now_node)
                    now = now_node

                else:  # next에 동일한 먹이가 있으면,
                    tmp_i = now.next.index(info[f])

                    tmp = lList[start_index].head
                    now = tmp.next


        informations.append(info)

    # step2:print
    draw_map(informations)

