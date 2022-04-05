from collections import deque

def check():
    global ans
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                continue
            elif arr[i][j] == '-':
                ans +=1
                que = deque()
                que.append((i,j))
                while que:
                    r,c = que.popleft()
                    arr[r][c] = 0
                    nr = r
                    nc = c + 1
                    if nc < M and arr[nr][nc] == '-':
                        que.append((nr,nc))
            elif arr[i][j] == '|':
                ans += 1
                que = deque()
                que.append((i, j))
                while que:
                    r, c = que.popleft()
                    arr[r][c] = None
                    nr = r + 1
                    nc = c
                    if nr < N and arr[nr][nc] == '|':
                        que.append((nr, nc))

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
ans = 0
check()
print(ans)