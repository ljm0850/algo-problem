import sys
input = sys.stdin.readline

def solution(N:int,M:int,graph:list)->int:
    # dp[a][b] 는 b개의 도시를 거쳐 a 지점에 도착했을때 최대값
    dp = [[0]*(M+1) for _ in range(N+1)]
    # 1에서 출발함, 2개 도시 거쳤을때 세팅
    for i in range(2,N+1):
        dp[i][2] = graph[1][i]
    # i는 도시, j는 거쳐간 도시의 수, k는 i도시에 도착하기 위해선 i보다 작은 지점에서 출발해야 하므로 i미만의 도시
    for i in range(2,N+1):
        for j in range(3,M+1):
            for k in range(1,i):
                if graph[k][i] and dp[k][j-1]:
                    dp[i][j] = max(dp[i][j],dp[k][j-1]+graph[k][i])
    return max(dp[N])

N,M,K = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a,b,c = map(int,input().split())
    if a < b:
        graph[a][b] = max(graph[a][b],c)
ans = solution(N,M,graph)
print(ans)