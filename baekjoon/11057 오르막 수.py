def solve(n:int)->int:
    dp = [[0]*10 for _ in range(n)]
    for i in range(10):
        dp[0][i] = 1
    for step in range(1,n):
        for i in range(10):
            dp[step][i] = sum(dp[step-1][:i+1])%10007
    return sum(dp[n-1])%10007

N = int(input())
ans = solve(N)
print(ans)