from collections import deque

def tomato():
    visited = [[0]*M for _ in range(N)]
    que = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                que.append((i, j))
                visited[i][j] = 1
    cnt = -1
    while que:
        cnt +=1
        for _ in range(len(que)):
            r,c = que.popleft()
            for way in range(4):
                nr = r + dr[way]
                nc = c + dc[way]
                if 0<=nr<N and 0<=nc<M and box[nr][nc] == 0:
                    que.append((nr,nc))
                    box[nr][nc] = 1
    for i in range(N):
        if 0 in box[i]:
            cnt = -1
            break
    return cnt

dr = [1,-1,0,0]
dc = [0,0,1,-1]
M,N = map(int,input().split())      # 1000 이하, M*N 크기의 상자
box = [list(map(int,input().split())) for _ in range(N)]
print(tomato())
