import sys
input = sys.stdin.readline
from collections import deque

def solution()->str:
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    que = deque()
    que.append(1)
    check = [False for _ in range(N+1)]
    check[1] = True

    ans,cnt = 0,0
    while que:
        for _ in range(len(que)):
            node = que.popleft()
            isLeaf = True
            for next_node in graph[node]:
                if not check[next_node]:
                    check[next_node] = True
                    que.append(next_node)
                    isLeaf = False
            if isLeaf:
                ans += cnt
        cnt += 1
    if ans%2:
        return 'Yes'
    else:
        return 'No'
ans = solution()
print(ans)