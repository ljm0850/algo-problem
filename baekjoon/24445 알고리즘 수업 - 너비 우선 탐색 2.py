from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,N+1):
    graph[i].sort(reverse=True)

visit = [0]*(N+1)
visit[R] = 1
que = deque([R])

cnt = 2
while que:
    node = que.popleft()
    for nextNode in graph[node]:
        if visit[nextNode]:
            continue
        que.append(nextNode)
        visit[nextNode] = cnt
        cnt += 1

for i in range(1,N+1):
    print(visit[i])