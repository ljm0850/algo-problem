from collections import deque
def bfs(i,j):
    if N == 1 and M == 1:
        return 1
    que = deque()
    que.append((i,j,0))
    cnt = 1
    while que:
        cnt +=1
        for _ in range(len(que)):
            ci,cj,b = que.popleft()
            for way in range(4):
                ni,nj = ci+di[way],cj+dj[way]
                if ni == N-1 and nj == M-1:
                    return cnt
                if 0<=ni<N and 0<=nj<M and not visited[b][ni][nj]:
                    if arr[ni][nj] == 0:
                        visited[b][ni][nj] = visited[b][ci][cj] + 1
                        que.append((ni,nj,b))
                    else:
                        if b == 0:
                            visited[b+1][ni][nj] = visited[b][ci][cj] + 1
                            que.append((ni,nj,b+1))
    return -1
di = [1,0,-1,0]
dj = [0,1,0,-1]
N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for __ in range(2)]
visited[0][0][0] = 1
ans = bfs(0,0)
print(ans)