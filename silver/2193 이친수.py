def solve():
    for i in range(2,N+1):
        dp[0][i] = dp[1][i-1] + dp[0][i-1]
        dp[1][i] = dp[0][i-1]
    return dp[0][N] + dp[1][N]

N = int(input())
dp = [[0]*(N+1) for _ in range(2)]
dp[1][1] = 1
ans = solve()
print(ans)
