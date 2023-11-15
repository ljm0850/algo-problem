import sys
input = sys.stdin.readline
from collections import deque
N,M,R = map(int,input().split())
visit = [0]*(N+1)
visit[R] = 1
graph = [set() for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].add(v)
    graph[v].add(u)
que = deque()
que.append(R)
cnt = 1
while que:
    now_node = que.popleft()
    for next_node in sorted(graph[now_node]):
        if not visit[next_node]:
            cnt += 1
            visit[next_node] = cnt
            que.append(next_node)
for idx in range(1,N+1):
    print(visit[idx])
