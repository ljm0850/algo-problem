from collections import deque

def findAir(r:int,c:int)->deque:
    arr[r][c] = 2
    ls = [(r,c)]
    air = deque()
    while ls:
        r,c = ls.pop()
        flag = False
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    ls.append((nr, nc))
                elif arr[nr][nc] == 1:
                    flag = True
        if flag:
            air.append((r, c))
    return air

R,C = map(int,input().split())
C += 2
arr = [[0]*(C)] + [[0]+list(map(int,input().split())) + [0] for _ in range(R)] + [[0]*(C)]
R += 2
dr,dc = (1,-1,0,0),(0,0,1,-1)
air = findAir(0,0)
cheese =set()

for r in range(1,R-1):
    for c in range(1,C-1):
        if arr[r][c] == 1:
            cheese.add((r,c))
cnt,ans =0,0
while cheese:
    ans = len(cheese)
    cnt += 1
    for _ in range(len(air)):
        r,c = air.popleft()
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<R and 0<=nc<C:
                if arr[nr][nc] == 1:
                    cheese.remove((nr,nc))
                    air += findAir(nr,nc)
print(cnt)
print(ans)