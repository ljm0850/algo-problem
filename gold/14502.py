from collections import deque

def make_arr(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(N):
        for j in range(M):
            if narr[i][j] == 0:
                narr[i][j] = 1
                make_arr(cnt+1)
                narr[i][j] = 0

def virus():
    global ans
    visted = [[0]*M for _ in range(N)]
    que = deque()
    for i in range(N):
        for j in range(M):
            if narr[i][j] == 2:
                que.append((i,j))
                visted[i][j] = 1
    cnt = 0
    while que:
        r,c = que.popleft()
        cnt += 1
        if ans >= n-cnt:
            return
        for way in range(4):
            nr = r + dr[way]
            nc = c + dc[way]
            if 0<=nr<N and 0<=nc<M and not visted[nr][nc] and narr[nr][nc]==0:
                que.append((nr,nc))
                visted[nr][nc] = 1
    if ans<n-cnt :
        ans = n-cnt

dr = [1,0,-1,0]
dc = [0,1,0,-1]
N,M = map(int,input().split())      # N*M 크기 연구소
pole = 3
ans = 0
narr = []
for _ in range(N):
    temp = list(map(int,input().split()))
    narr.append(temp)
    for p in temp:
        if p == 1:
            pole +=1
n = N*M-pole        # 0,2가 총 몇칸인지
make_arr(0)
print(ans)