from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def dijkstra(start:int,N:int,graph:list[tuple[int]])->list[int]:
    INF = float('inf')
    shortcut = [INF]*(N+1)
    shortcut[start] = 0
    ls = [(0,start)]
    for length,node in ls:
        shortcut[node] = length
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
# dijkstra
shortcut_ls = list()
for i in range(P):
    p = point[i]
    shortcut_ls.append(dijkstra(p,N,graph))
# bruteforce
ans = float('inf')
for i in range(P):
    v1 = shortcut_ls[i][X]
    if v1 >= ans: continue
    p1 = point[i]
    for j in range(P):
        if i == j: continue
        p2 = point[j]
        v2 = shortcut_ls[j][p1]
        if v1+v2 >= ans:continue
        for k in range(P):
            if i == k or j == k: continue
            v3 = shortcut_ls[k][p2] + shortcut_ls[k][Z]
            ans = min(ans,v1+v2+v3)
if ans == float('inf'):
    print(-1)
else:
    print(ans)