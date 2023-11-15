from collections import deque
import sys
input = sys.stdin.readline
N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
que = deque()
que.append(X)
ans = []
check = [False]*(N+1)
check[X] = True
cnt = 0
while que and (cnt < K):
    cnt += 1
    for _ in range(len(que)):
        now = que.popleft()
        for next_node in graph[now]:
            if not check[next_node]:
                check[next_node] = True
                que.append(next_node)
                if cnt == K:
                    ans.append(next_node)
if ans:
    ans.sort()
    for city in ans:
        print(city)
else:
    print(-1)