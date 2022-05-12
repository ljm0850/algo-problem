def solve(ls):
    if len(ls) == M:
        print(*ls)
        return
    for num in range(1,N+1):
        if not num in ls:
            solve(ls+[num])

N,M = map(int,input().split())
solve([])
