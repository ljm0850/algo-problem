def sol(i):
    global ans
    if i == len(cctvs):
        ans = min(ans,check())
        return
    r,c = cctvs[i]
    if arr[r][c] == 1:
        for d in range(4):
            changeRC = CCTVwatching(d,r,c)
            sol(i+1)
            backArr(changeRC)
    elif arr[r][c] == 2:
        for d in range(4):
            changeRC = CCTVwatching(d,r,c) + CCTVwatching((d+2)%4,r,c)
            sol(i+1)
            backArr(changeRC)
    elif arr[r][c] == 3:
        for d in range(4):
            changeRC = CCTVwatching(d,r,c) + CCTVwatching((d+1)%4,r,c)
            sol(i+1)
            backArr(changeRC)
    elif arr[r][c] == 4:
        for d in range(4):
            changeRC = CCTVwatching(d,r,c) + CCTVwatching((d+1)%4,r,c) + CCTVwatching((d+2)%4,r,c)
            sol(i+1)
            backArr(changeRC)
    else:
        changeRC = CCTVwatching(0,r,c) + CCTVwatching(1,r,c) + CCTVwatching(2,r,c) + CCTVwatching(3,r,c)
        sol(i+1)
        backArr(changeRC)

def CCTVwatching(d:int,r:int,c:int)->list[int]:
    ls = []
    while True:
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 6:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 7
                ls.append((nr, nc))
            r,c = nr,nc
        else:
            break
    return ls

def backArr(ls:list[int])->None:
    while ls:
        r,c = ls.pop()
        arr[r][c] = 0

def check():
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                cnt += 1
    return cnt

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dr,dc = (1,0,-1,0),(0,1,0,-1)
cctvs = []
for r in range(N):
    for c in range(M):
        if 0 < arr[r][c] < 6:
            cctvs.append((r,c))
ans = N*M
sol(0)
print(ans)