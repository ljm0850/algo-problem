def check(n):
    global dp
    if dp[n]:
        return dp[n]

    for i in range(n):
        dp[n] += check(i)*check(n-i-1)
    return dp[n]

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
print(check(n))