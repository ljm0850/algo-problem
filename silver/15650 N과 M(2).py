def check(ls):
    if len(ls) == M:
        print(*ls)
        return
    for i in range(1,N+1):
        if ls and ls[-1] < i:
            check(ls+[i])
        elif not ls:
            check(ls+[i])
N,M = map(int,input().split())
check([])