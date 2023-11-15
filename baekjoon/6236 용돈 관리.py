import sys
input = sys.stdin.readline
def solution(payments:list[int])->int:
    s,e = min(payments),sum(payments)
    ans = s
    while s <= e:
        m = (s+e) // 2
        if check(m):
            ans = m
            e = m-1
        else:
            s = m+1
    return ans
def check(money:int)->bool:
    now = money
    cnt = M
    for i in range(N):
        if now >= payments[i]:
            now -= payments[i]
        else:
            now = money
            cnt -= 1
            if now >= payments[i]:
                now -= payments[i]
            else:
                return False
        if cnt == 0:
            return False
    return True

N,M = map(int,input().split())
payments = [int(input()) for _ in range(N)]
ans = solution(payments)
print(ans)