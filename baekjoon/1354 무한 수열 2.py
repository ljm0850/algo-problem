def sol(N:int)->int:
    if N <= 0:
        return 1
    if dp.get(N,0):
        return dp[N]
    dp[N] = sol(N//P-X) + sol(N//Q-Y)
    return dp[N]

N,P,Q,X,Y = map(int,input().split())
dp = {}
ans = sol(N)
print(ans)