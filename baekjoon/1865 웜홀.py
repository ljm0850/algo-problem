def solve(start):
    time[start] = 0
    for i in range(N):
        for now in range(1,N+1):
            for next in total[now]:
                if time[next] > time[now] + total[now][next]:
                    time[next] = time[now] + total[now][next]
                    if i == N-1:
                        print('YES')
                        return
    print('NO')

TC = int(input())

for tc in range(TC):
    N,M,W = map(int,input().split())        # N = 지점, M = 도로, W = 웜홀
    INF = 10000 * (N+1)
    total = [{} for _ in range(N+1)]
    for _ in range(M):
        S,E,T = map(int,input().split())
        if total[S].get(E):
            total[S][E] = min(total[S][E],T)
            total[E][S] = total[S][E]
        else:
            total[S][E] = T
            total[E][S] = T
    for _ in range(W):
        S,E,T = map(int,input().split())
        if total[S].get(E):
            total[S][E] = min(total[S][E],-T)
        else:
            total[S][E] = -T
    time = [INF]*(N+1)
    solve(1)