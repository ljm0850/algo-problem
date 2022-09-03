def combination(a,b):
    if dp[a][b]:
        return dp[a][b]
    dp[a][b] = combination(a-1,b) + combination(a-1,b-1)
    return dp[a][b]

n,m = map(int,input().split())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0],dp[i][i] = 1,1
print(combination(n,m))