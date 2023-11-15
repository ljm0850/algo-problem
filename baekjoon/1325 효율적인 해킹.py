from sys import stdin
input = stdin.readline

def dfs(node):
    stack = [node]
    cnt = 1
    visited = [False] * (n+1)
    visited[node] = True
    while stack:
        x = stack.pop()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

total = []
for i in range(n+1):
    total.append(dfs(i))

max = max(total)
for i in range(n+1):
    if max == total[i]:
        print(i, end=' ')