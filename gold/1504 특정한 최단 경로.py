import heapq,sys
def dijkstra(start):
    h = [(start,0)]
    short_cut = [basic] * (N+1)
    short_cut[start] = 0
    while h:
        now,length = heapq.heappop(h)
        if short_cut[now] < length:
            continue
        for next_item in graph[now]:
            next,way = next_item[0],next_item[1]
            next_length = length + way
            if next_length < short_cut[next]:
                short_cut[next] = next_length
                heapq.heappush(h,(next,next_length))
    return short_cut

basic = 1111111111
N,E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c, = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,sys.stdin.readline().split())

graph_1 = dijkstra(1)
graph_v1 = dijkstra(v1)
graph_v2 = dijkstra(v2)

way1 = graph_1[v1] + graph_v1[v2] + graph_v2[N]
way2 = graph_1[v2] + graph_v2[v1] + graph_v1[N]

ans = min(way1,way2)
if ans >= basic:
    print(-1)
else:
    print(ans)