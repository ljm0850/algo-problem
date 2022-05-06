from collections import deque
import sys
input = sys.stdin.readline
def check():
    visited = [0]*(K+1)
    que = deque()
    que.append(1)
    while que:
        t = que.popleft()
        for i in tree[t]:
            if not visited[i]:
                visited[i] = 1
                ans[i] = t
                que.append(i)


K = int(input())
tree = [[] for _ in range(K+1)]
ans = [0]*(K+1)
for _ in range(K-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
check()
for i in range(2,K+1):
    if ans[i]:
        print(ans[i])