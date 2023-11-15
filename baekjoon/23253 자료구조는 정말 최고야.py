import sys
input = sys.stdin.readline
def solution(N:int,books:list[list[int]],booksIdx:dict)->str:
    check = set()
    for book in books:
        check.add(book[-1])
    for cnt in range(1,N+1):
        if cnt in check:
            check.remove(cnt)
            idx = booksIdx[cnt]
            books[idx].pop()
            if books[idx]:
                check.add(books[idx][-1])
        else:
            return "No"
    return "Yes"

N,M = map(int,input().split())
books = []
booksIdx = {}
for idx in range(M):
    T = input()
    temp = list(map(int,input().split()))
    books.append(temp)
    for book in temp:
        booksIdx[book] = idx
ans = solution(N,books,booksIdx)
print(ans)