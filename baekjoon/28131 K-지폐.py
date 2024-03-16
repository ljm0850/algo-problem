from heapq import heappop,heappush
import sys
input = sys.stdin.readline
def solution(graph:list[dict],N:int,S:int,T:int,K:int,INF:int)->int:
    que = [(0,S)]
    shortcut = [[INF]*(K) for _ in range(N+1)]
    while que:
        nowCost,nowNode = heappop(que)
        idx = nowCost%K
        if shortcut[nowNode][idx] < nowCost:
            continue

        for nextNode in graph[nowNode]:
            for addedCost in graph[nowNode][nextNode]:
                totalCost = nowCost + addedCost
                nextIdx = totalCost % K
                if shortcut[nextNode][nextIdx] > totalCost:
                    shortcut[nextNode][nextIdx] = totalCost
                    heappush(que,(totalCost,nextNode))
    return shortcut[T][0]

N,M,K = map(int,input().split())
S,T = map(int,input().split())
graph = [dict() for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u][v] = graph[u].get(v,[]) + [w]
INF = float('inf')
ans = solution(graph,N,S,T,K,INF)
if ans != INF:
    print(ans)
else:
    print('IMPOSSIBLE')