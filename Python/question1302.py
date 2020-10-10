case_num = int(input())

books = dict()

for i in range(case_num):
    name = input()
    if name in books:
        books[name] += 1
    else :
        books[name] = 1

max_num = max(books.values())
max_books = [k for k,v in books.items() if v == max_num]
max_books.sort()

max_book = max_books[0]

print(max_book)
