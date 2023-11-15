def solve():
    maximum = 100000
    dp = [maximum] * max((k + 1),max(coins)+1)
    for coin in coins:
        dp[coin] = 1

    for i in range(1,k+1):
        for coin in coins:
            if i-coin > 0:
                dp[i] = min(dp[i],dp[i-coin]+1)
    if dp[k] != maximum:
        return dp[k]
    return -1

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
print(solve())