#정렬

input_num, k = map(int, input().split(" "))

arr = list(map(int, input().split(" ")))
arr.sort()

print(arr[k-1])

