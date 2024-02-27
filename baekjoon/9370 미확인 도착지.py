import sys
input = sys.stdin.readline
from heapq import heappush,heappop

def dijkstra(n,INF,start,graph):
    ls = [(0,start)]
    shortcut = [INF]*(n+1)
    shortcut[start] = 0

    while ls:
        nowLength,nowNode = heappop(ls)
        if shortcut[nowNode] < nowLength:
            continue

        for nextNode in graph[nowNode]:
            nextLength = nowLength + graph[nowNode][nextNode]
            if shortcut[nextNode] > nextLength:
                shortcut[nextNode] = nextLength
                heappush(ls,(nextLength,nextNode))
    return shortcut

INF = 1000*50000+1
T = int(input())
for tc in range(T):
    n,m,t = map(int,input().split())    # 교차로, 도로, 목적지 후보
    s,g,h = map(int,input().split())    # 출발지, 목격된 도로
    graph = [dict() for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a][b] = d
        graph[b][a] = d
    startShortcut = dijkstra(n,INF,s,graph)
    gShortcut = dijkstra(n,INF,g,graph)
    hShortcut = dijkstra(n,INF,h,graph)
    ans = list()
    for _ in range(t):
        target = int(input())
        if (startShortcut[target] == startShortcut[g] + gShortcut[h]+hShortcut[target]) or (startShortcut[target] == startShortcut[h]+hShortcut[g]+gShortcut[target]):
            ans.append(target)
    ans.sort()
    print(*ans)