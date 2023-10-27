import sys
input =sys.stdin.readline
sys.setrecursionlimit(350000)
def inrange(r,c,R,C):
    if 0<=r<R and 0<=c<C:
        return True
    return False

def dfs(r,c,R,C):
    global ans
    check[r][c] = 2
    v = maze[r][c]
    nr,nc = r+direction[v][0],c+direction[v][1]
    if not inrange(nr,nc,R,C):
        check[r][c] = 1
        return True
    if check[nr][nc] == 1:
        check[r][c] = 1
        return True
    elif check[nr][nc] == 2:
        return False
    value = dfs(nr,nc,R,C)
    if value:
        check[r][c] = 1
        return True
    return False

N,M = map(int,input().split())
maze = [input().rstrip() for _ in range(N)]
direction = {'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
check = [[0]*(M) for _ in range(N)]
for r in range(N):
    for c in range(M):
        if not check[r][c]:
            dfs(r,c,N,M)
ans = 0
for r in range(N):
    for c in range(M):
        if check[r][c] == 1:
            ans += 1
print(ans)