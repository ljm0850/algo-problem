import sys
input = sys.stdin.readline
def changeArr(y:int,x:int)->None:
    global arr
    ls = [(y,x)]
    while ls:
        r,c= ls.pop()
        for way in range(4):
            nr,nc = changeRC(r+dr[way],c+dc[way])
            if arr[nr][nc] == 0:
                arr[nr][nc] = 1
                ls.append((nr,nc))

def changeRC(r:int,c:int)->tuple[int]:
    if r < 0:
        r = N + r
    elif r >= N:
        r = r - N
    if c < 0:
        c = M + c
    elif c >= M:
        c = c - M
    return r,c

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dr,dc = (1,0,-1,0),(0,1,0,-1)
ans = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            ans += 1
            changeArr(r,c)
print(ans)