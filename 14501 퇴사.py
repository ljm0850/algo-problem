N = int(input())
works = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(N+2)

for i in range(1,N+1):
    time,pay = works[i-1][0],works[i-1][1]
    if i+time<=N+1:
        dp[i+time] = max(dp[i+time],max(dp[:i+1])+pay)
print(max(dp))