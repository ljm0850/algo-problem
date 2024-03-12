import sys
input = sys.stdin.readline
from heapq import heappush,heappop

def dijkstra(N,startNode,graph):
    INF = 100001
    que = [(0,startNode)]
    shortCut = [INF]*(N+1)
    shortCut[startNode] = 0
    while que:
        length,node = heappop(que)
        if shortCut[node] < length:
            continue
        for nextNode,addedLength in graph[node]:
            totalLength = length+addedLength
            if shortCut[nextNode] > totalLength:
                shortCut[nextNode] = totalLength
                heappush(que,(totalLength,nextNode))
    return shortCut


T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    K = int(input())
    startRoom = list(map(int,input().split()))
    total = list()
    for node in startRoom:
        total.append(dijkstra(N,node,graph))

    minValue = 10000000
    ans = 0
    for m in range(1,N+1):
        value = 0
        for k in range(K):
            value += total[k][m]
        if minValue > value:
            minValue = value
            ans = m
    print(ans)

# import sys
# input = sys.stdin.readline
#
# INF = 1000001
# T = int(input())
# for _ in range(T):
#     N,M = map(int,input().split())
#     graph = [[INF]*(N+1) for _ in range(N+1)]
#     for _ in range(M):
#         a,b,c = map(int,input().split())
#         graph[a][b] = c
#         graph[b][a] = c
#     K = int(input())
#     startRoom = list(map(int,input().split()))
#
#     for i in range(1,N+1):
#         graph[i][i] = 0
#
#     for m in range(1,N+1):
#         for s in range(1,N+1):
#             for e in range(1,N+1):
#                 length = graph[s][m] + graph[m][e]
#                 if graph[s][e] > length:
#                     graph[s][e] = length
#                     graph[e][s] = length
#
#     minValue = INF*(N+1)
#     ans = 0
#
#     for i in range(1,N+1):
#         value = 0
#         for node in startRoom:
#             value += graph[i][node]
#         if minValue > value:
#             minValue = value
#             ans = i
#     print(ans)