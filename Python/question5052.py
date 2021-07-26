#20210721 전화번호 목록
nums = [0,1,2,3,4,5,6,7,8,9]

def is_consistent(nlist):
    for i in range(len(nlist)):
        



    return True

if __name__ == '__main__':
    T = int(input())
    result = list()
    for i in range(T):
        N = int(input())
        numbers = list()
        for j in range(N):
            numbers.append(input())

        if is_consistent(numbers):
            result.append("YES")

        else:
            result.append("NO")

    for r in result:
        print(r)
