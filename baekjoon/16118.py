import sys
input = sys.stdin.readline
from heapq import heappush,heappop
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    c *= 2
    graph[a].append((b,c))
    graph[b].append((a,c))
INF = 800000000
# 여우
fox_shortcut = [INF]*(N+1)
fox_shortcut[1] = 0
hq = [(0,1)]
while hq:
    length,node = heappop(hq)
    if fox_shortcut[node] < length:
        continue
    for next_node,l in graph[node]:
        next_length = length + l
        if fox_shortcut[next_node] > next_length:
            fox_shortcut[next_node] = next_length
            heappush(hq,(next_length,next_node))

# 늑대
wolf_shortcut = [[INF]*(2) for _ in range(N+1)]
wolf_shortcut[1] = [0,INF]
hq = [(0,0,1)]
while hq:
    length,cnt,node = heappop(hq)
    if wolf_shortcut[node][cnt] < length:
        continue
    ncnt = cnt^1
    for next_node,l in graph[node]:
        if cnt ==0: l //= 2
        else: l *= 2
        next_length = length + l
        if wolf_shortcut[next_node][ncnt] > next_length:
            wolf_shortcut[next_node][ncnt] = next_length
            heappush(hq,(next_length,ncnt,next_node))
# 계산
ans = 0
for i in range(2,N+1):
    if fox_shortcut[i] < min(wolf_shortcut[i]):
        ans += 1
print(ans)