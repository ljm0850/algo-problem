from collections import deque

def bfs():
    global arr
    que = deque()
    que.append((0,0))
    cnt = 0
    while True:
        cheeze = [[0]*M for _ in range(N)]
        visited = [[0]*M for _ in range(N)]
        que.append((0,0))
        visited[0][0] = 1
        while que:
            i,j = que.popleft()
            for way in range(4):
                ni,nj = i+di[way], j+dj[way]
                if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                    if not arr[ni][nj]:
                        visited[ni][nj] = 1
                        que.append((ni,nj))
                    else:
                        cheeze[ni][nj] += 1
        cz = 0
        for ii in range(N):
            for jj in range(M):
                if cheeze[ii][jj] >= 2:
                    arr[ii][jj] = 0
                    cz = 1
        if not cz:
            return cnt
        cnt += 1

di = [1,0,-1,0]
dj = [0,1,0,-1]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = bfs()
print(ans)