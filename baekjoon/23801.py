from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def dijkstra(start:int,N:int,graph:list[tuple[int]])->list[int]:
    INF = float('inf')
    shortcut = [INF]*(N+1)
    shortcut[start] = 0
    ls = [(0,start)]
    while ls:
        length,node = heappop(ls)
        if length > shortcut[node]: continue
        for next_node,added_legth in graph[node]:
            total_length = length + added_legth
            if total_length >= shortcut[next_node]: continue
            shortcut[next_node] = total_length
            heappush(ls,(total_length,next_node))
    return shortcut
# input
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
X,Z = map(int,input().split())
P = int(input())
point = list(map(int,input().split()))
# logic
X_shortcut = dijkstra(X,N,graph)
Z_shortcut = dijkstra(Z,N,graph)
ans = float('inf')
for p in point:
    if (X_shortcut[p] == 0) or (Z_shortcut[p] == 0): continue
    ans = min(ans,X_shortcut[p]+Z_shortcut[p])
print(ans) if ans != float('inf') else print(-1)