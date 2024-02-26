def solution(T:int,arr:list[int]):
    arr.sort()
    if arr[-1] < T:
        return -1

    L = len(arr)
    s,e = 0,L-1
    while s<e:
        m = (s+e)//2
        if arr[m] == T:
            return 0
        elif arr[m] <T:
            s = m+1
        else:
            e = m
    return arr[e]-T

N,T = map(int,input().split())
busTime = list()
for _ in range(N):
    S,I,C = map(int,input().split())
    for cnt in range(C):
        busTime.append(S+I*cnt)
ans = solution(T,busTime)
print(ans)