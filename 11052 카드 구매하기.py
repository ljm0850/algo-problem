N = int(input())
card_price = [0]+list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
    for j in range(1,N+1):
        if i-j >=0:
            dp[i] = max(dp[i],dp[i-j]+card_price[j])
print(dp[N])