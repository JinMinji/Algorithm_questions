# 도서관

# 데이터 입력 start
N, M = map(int,input().split(" "))  # N:책 개수, M:한번에 들 수 있는 책 개수
books = list(map(int, input().split(" ")))      # books:책위치 리스트
# 데이터 입력 end

books.sort()

result = 0

max_distance = max(abs(books[0]), abs(books[-1]))

takes = list()

# 왼쪽 구간 (음수)
while len(books) > 0 and books[0] < 0:
    takes.append(books.pop(0))
    if len(takes) == M:
        result += abs(takes[0])*2
        takes = []

if len(takes) > 0:
    result += abs(takes[0])*2
    takes = []

# 오른쪽 구간 (양수)
while len(books) > 0 and books[-1] >= 0:
    takes.append(books.pop(-1))
    if len(takes) == M:
        result += abs(takes[0])*2
        takes = []

if len(takes) > 0:
    result += abs(takes[0])*2
    takes = []

result -= max_distance

print(result)