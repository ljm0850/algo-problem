import sys
input = sys.stdin.readline
def solution(N:int,C:int,total:list[int])->int:
    value = 0
    total.sort()
    s,e = 1,total[N-1] - total[0]
    while s<= e:
        m = (s+e)//2
        now = total[0]
        cnt = 1

        for i in range(1,N):
            if total[i] >= now + m:
                cnt += 1
                now = total[i]
        if cnt >= C:
            s = m + 1
            value = m
        else:
            e = m - 1
    return value

N,C = map(int,input().split())
total = [int(input()) for _ in range(N)]
ans = solution(N,C,total)
print(ans)