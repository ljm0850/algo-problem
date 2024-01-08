N,M = map(int,input().split())
graph = [[0]*(M+1)]
for _ in range(N):
    graph.append(list(map(int,input().split())))
# dp[j][i] => 0부터 j번째 까지 회사를 고려했을때 i금액에서의 best 값에 대한 정보, 정보는 [최대 수익금,j번째 회사에는 얼마를 투자했는지]로 구성
dp = [[[0,0]for __ in range(M+1)] for _ in range(N+1)]

for company_idx in range(1,M+1):
    for total_money in range(1,N+1):
        for now_company_money in range(total_money+1):
            value = dp[total_money][company_idx][0]
            new_value = dp[total_money-now_company_money][company_idx-1][0] + graph[now_company_money][company_idx]

            if new_value > value:
                dp[total_money][company_idx] = [new_value,now_company_money]

total = N
ans = [0]*M
for i in range(M,0,-1):
    value = dp[total][i][1]
    ans[i-1] = value
    total -= value
print(dp[N][M][0])
print(*ans)