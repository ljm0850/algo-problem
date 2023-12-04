T = int(input())
for tc in range(1,T+1):
    N,L = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    dp = [0]*(L+1)
    
    for point,calorie in data:
        for i in range(calorie,L+1)[::-1]:
            dp[i] = max(dp[i],dp[i-calorie]+point)
    print(f'#{tc} {max(dp)}')