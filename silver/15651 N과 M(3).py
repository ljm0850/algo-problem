def solve(ls,length):
    if length == M:
        print(*ls)
        return
    for i in range(1,N+1):
        solve(ls+[i],length+1)

N,M = map(int,input().split())

nums = [i for i in range(1,N+1)]
solve([],0)