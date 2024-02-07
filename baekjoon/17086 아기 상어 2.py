from collections import deque
R,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
que = deque()
for r in range(R):
    for c in range(C):
        if arr[r][c] == 1:
            que.append((r,c))

dr,dc = (1,1,1,0,0,-1,-1,-1),(1,0,-1,1,-1,1,0,-1)
while que:
    r,c = que.popleft()
    cnt = arr[r][c] + 1
    for d in range(8):
        nr,nc = r+dr[d],c+dc[d]
        if not (0<=nr<R and 0<=nc<C) or arr[nr][nc]:
            continue
        arr[nr][nc] = cnt
        que.append((nr,nc))
ans = 0
for r in range(R):
    ans = max(ans,max(arr[r]))
print(ans-1)