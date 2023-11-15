import sys
input = sys.stdin.readline
def findArea(r,c):
    global arr
    arr[r][c] = True
    ls = [(r,c)]
    cnt = 1
    while ls:
        r,c = ls.pop()
        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if 0<=nr<M and 0<=nc<N and arr[nr][nc] == False:
                arr[nr][nc] = True
                cnt += 1
                ls.append((nr,nc))
    return cnt
M,N,K = map(int,input().split())
arr = [[False]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for r in range(y1,y2):
        for c in range(x1,x2):
            arr[r][c] = True
ans = []
dr,dc = (1,0,-1,0),(0,1,0,-1)
for r in range(M):
    for c in range(N):
        if arr[r][c] == False:
            ans.append(findArea(r,c))
ans.sort()
print(len(ans))
print(*ans)