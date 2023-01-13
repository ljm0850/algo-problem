def solution(N:int,P:int,Q:int)->int:
    if dp.get(N):
        return dp[N]
    dp[N] = solution(N//P,P,Q) + solution(N//Q,P,Q)
    return dp[N]

N,P,Q = map(int,input().split())
dp = dict()
dp[0] = 1

ans = solution(N,P,Q)
print(ans)