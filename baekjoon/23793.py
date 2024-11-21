import sys
from heapq import heappush,heappop
input = sys.stdin.readline

def dijkstra(start:int,N:int,graph:list[tuple[int]],avoid=0)->list[int]:
    short_cut = [INF]*(N+1)
    short_cut[start] = 0
    ls = [(0,start)]
    while ls:
        value,node = heappop(ls)
        if value > short_cut[node]:continue
        for next_node,added_value in graph[node]:
            total_value = value + added_value
            if total_value >= short_cut[next_node]: continue
            short_cut[next_node] = total_value
            if next_node != avoid:
                heappush(ls,(total_value,next_node))
    return short_cut

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
X,Y,Z = map(int,input().split())

INF = float('inf')
X_shortcut = dijkstra(X,N,graph,Y)
Y_shortcut = dijkstra(Y,N,graph)
ans = [X_shortcut[Y] + Y_shortcut[Z],X_shortcut[Z]]
for value in ans:
    if value == INF: print(-1,end=' ')
    else: print(value,end=' ')