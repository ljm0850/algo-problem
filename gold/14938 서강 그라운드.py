import heapq
def dijkstra(start):
    global ans
    heap = [(start,0)]
    while heap:
        now,way = heapq.heappop(heap)
        for next,length in road_length[now]:
            if next == start:
                continue
            next_way = way + length
            if short_cut[start][next] > next_way:
                short_cut[start][next] = next_way
                heapq.heappush(heap,(next,next_way))
    return

def solve(start):
    global ans
    item = items[start]
    for area in range(1,n+1):
        if short_cut[start][area] <= m:
            item += items[area]
    if ans < item:
        ans = item

n,m,r = map(int,input().split())      # n = 지역의 개수, m = 수색 범위, r = 길의 개수
items = [0]+list(map(int,input().split()))
road_length = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int,input().split())
    road_length[a].append((b,c))
    road_length[b].append((a,c))
INF = 2000
short_cut = [[INF]*(n+1) for _ in range(n+1)]
ans = 0
for i in range(1,n+1):
    dijkstra(i)
for i in range(1,n+1):
    solve(i)
print(ans)