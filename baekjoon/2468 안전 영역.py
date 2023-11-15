from collections import deque
def check(h):
    global ans
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <=h:
                visited[i][j] = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                que = deque()
                que.append((i,j))
                cnt += 1
                while que:
                    r,c = que.popleft()
                    for way in ([1,0],[-1,0],[0,1],[0,-1]):
                        nr,nc = r+way[0],c+way[1]
                        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            que.append((nr,nc))
    if ans < cnt:
        ans = cnt
    return cnt

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for h in range(101):
    if not check(h) :
        break
print(ans)