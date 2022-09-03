from collections import deque
def solve():
    if N == K:
        return 0
    visited[N] = 0
    que = deque()
    que.append(N)
    while que:
        now = que.popleft()
        next = now*2
        while 0< next <= 100000:
            if visited[next] == -1:
                if next == K:
                    return visited[now]
                else:
                    visited[next] = visited[now]
                    que.append(next)
            next *= 2
        for next in (now-1,now+1):
            if 0<=next<=100000 and visited[next] == -1:
                visited[next] = visited[now] +1
                if next == K:
                    return visited[next]
                else:
                    que.append(next)

N,K = map(int,input().split())
visited = [-1]*100001
print(solve())
