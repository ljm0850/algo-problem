from collections import deque
def check(n):
    global arr
    visited = [[0]*(N) for _ in range(N)]
    cnt = 0
    if n == 1:
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 'G':
                    arr[r][c] = 'R'

    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                que = deque()
                que.append((i,j))
                visited[i][j] = 1
                t = arr[i][j]
                cnt += 1
                while que:
                    r,c=que.popleft()
                    for way in range(4):
                        nr,nc = r+dr[way],c+dc[way]
                        if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and t == arr[nr][nc]:
                            visited[nr][nc] = 1
                            que.append((nr,nc))
    if n == 0:
        print(cnt,end=' ')
        check(1)
        return
    print(cnt)

dr=[1,0,-1,0]
dc=[0,1,0,-1]

N = int(input())
arr = [list(input()) for _ in range(N)]
check(0)