import sys
C,N = map(int,input().split())
INF = sys.maxsize
dp = [INF]*1101
cities = []
for _ in range(N):
    city = list(map(int,input().split()))
    cities.append(city)
    custom,pay = city[1],city[0]
    dp[custom] = min(dp[custom],pay)
    while custom < C:
        dp[custom+city[1]] = min(dp[custom+city[1]],dp[custom]+pay)
        custom += city[1]

for city in cities:
    custom,pay = city[1],city[0]
    for i in range(1,C):
        if dp[i] != INF:
            dp[i+custom] = min(dp[i+custom],dp[i]+pay)
print(min(dp[C:]))