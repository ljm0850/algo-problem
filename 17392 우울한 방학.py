def solution(num):
    value,day = 0,1
    while day <= num:
        value += day*day
        day += 1
    return value

N,M = map(int,input().split())
if N:
    promise = list(map(int,input().split()))
else:
    promise = []
total = M - sum(promise) - N
if total <= 0:
    print(0)
else:
    a,b = divmod(total,N+1)
    v = solution(a)
    ans = v*(N+1-b) + (v+(a+1)**2)*b
    print(ans)