def check(n):
    if dp[n]:
        return dp[n]
    dp[n] = (check(n-1)+check(n-2))%10007
    return dp[n]

n = int(input())

dp = [0]*1001
dp[1] = 1
dp[2] = 2
print(check(n)%10007)