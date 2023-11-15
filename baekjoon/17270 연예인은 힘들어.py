from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def dijkstra(N:int,startNode:int)->list[int]:
    global graph
    shortcut = [0]*(N+1)
    ls = [(0,startNode)]
    while ls:
        length,node = heappop(ls)
        for nextNode in graph[node]:
            if nextNode == startNode:
                continue
            nextLength = length+graph[node][nextNode]
            if (shortcut[nextNode] == 0) or nextLength < shortcut[nextNode]:
                shortcut[nextNode] = nextLength
                heappush(ls,(nextLength,nextNode))
    return shortcut

def solution(V:int,J:int,S:int)->int:
    start = {J,S}
    J_length = dijkstra(V,J)
    S_length = dijkstra(V,S)
    ans,value = [-1],10001*V
    for node in range(1,V+1):
        if node in start:
            continue
        if (J_length[node] == 0) or (S_length[node] == 0):
            continue

        nowValue = J_length[node] + S_length[node]
        if (nowValue < value):
            ans = list()
            value = nowValue

        if (nowValue == value) and (J_length[node] <= S_length[node]):
            ans.append(node)
    if ans:
        ans.sort(key= lambda x:(J_length[x],x))
        return ans[0]
    else:
        return -1

V,M = map(int,input().split())
graph = [dict() for _ in range(V+1)]
for _ in range(M):
    a,b,c =map(int,input().split())
    if not graph[a].get(b) or graph[a][b] > c:
        graph[a][b] = c
        graph[b][a] = c

J,S = map(int,input().split())
ans = solution(V,J,S)
print(ans)