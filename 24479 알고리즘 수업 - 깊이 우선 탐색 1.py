import sys
input = sys.stdin.readline
def dfs(s,N):
    visited = [False]*(N+1)
    ls = [s]
    value = [0]*(N+1)
    cnt = 0
    while ls:
        now_node = ls.pop()
        if visited[now_node]:
            continue
        cnt += 1
        value[now_node] = cnt
        visited[now_node] = True
        for next_node in graph[now_node]:
            ls.append(next_node)
    return value

N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for ls in graph:
    ls.sort(reverse=True)

answer = dfs(R,N)
for i in range(1,N+1):
    print(answer[i])