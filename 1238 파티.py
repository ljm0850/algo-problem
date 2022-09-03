import heapq,sys
def dijkstra(start):
    h1 = [(start,0)]
    h2 = [(start,0)]
    maximum = 1000000
    shortcut1 = [maximum]*(N+1)
    shortcut2 = [maximum]*(N+1)
    while h1:
        now,now_time = heapq.heappop(h1)
        if shortcut1[now] < now_time:
            continue
        for next,use_time in road1[now]:
            next_time = now_time+use_time
            if next_time < shortcut1[next]:
                shortcut1[next] = next_time
                heapq.heappush(h1,(next,next_time))

    while h2:
        now,now_time = heapq.heappop(h2)
        if shortcut2[now] < now_time:
            continue
        for next,use_time in road2[now]:
            next_time = now_time+use_time
            if next_time < shortcut2[next]:
                shortcut2[next] = next_time
                heapq.heappush(h2,(next,next_time))

    total = [0]*(N+1)
    for i in range(1,N+1):
        total[i] = shortcut1[i]+shortcut2[i]
    total[X] = 0
    print(max(total))

N,M,X = map(int,sys.stdin.readline().split())    # N= 마을의 수, M = 단방향 도로의 수 , X = 모일 마을
road1 = [[] for _ in range(N+1)]
road2 = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int,sys.stdin.readline().split())
    road1[s].append((e,t))
    road2[e].append((s,t))
dijkstra(X)