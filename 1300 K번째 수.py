def solution(N:int,K:int)->int:
    s, e = 1, K
    ans = 0
    while s <= e:
        m = (s + e) // 2
        value = 0
        for i in range(1, N + 1):
            value += min(m // i, N)
        if value >= K:
            e = m - 1
            ans = m
        else:
            s = m + 1
    return ans

N,K = int(input()),int(input())
ans = solution(N,K)
print(ans)