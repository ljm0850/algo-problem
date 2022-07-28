def solve(n:int)->int:
    dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n)]
    dp[0] = [0,1,1,1,1,1,1,1,1,1]
    for i in range(1,n):
        for j in range(10):
            for k in (1,-1):
                if 0<=j+k<10:
                    dp[i][j] += dp[i-1][j+k]
    return sum(dp[n-1])%1000000000

N = int(input())
ans = solve(N)
print(ans)