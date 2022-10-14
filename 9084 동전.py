def solve(target:int, coins:list)->int:
    dp = [0] * (target+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1,target+1):
            if i>=coin:
                dp[i] += dp[i-coin]
    return dp[target]

T = int(input())
for tc in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    ans = solve(M,coins)
    print(ans)