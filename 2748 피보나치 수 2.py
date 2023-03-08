def recur(n):
    if dp[n]:
        return dp[n]
    elif n == 0:
        return 0
    dp[n] = recur(n-1) + recur(n-2)
    return dp[n]

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
ans = recur(n)
print(ans)