import sys
sys.setrecursionlimit(250000)
def solution(R:int,C:int)->int:
    arr = [list(map(int, input().split())) for _ in range(R)]
    dr,dc = (-1,0,1,0),(0,-1,0,1)
    ls = [(R-1,C-1)]
    while ls:
        r,c = ls.pop()
        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if 0<=nr<R and 0<=nc<C and arr[nr][nc] > arr[r][c] and not (r,c) in total[nr][nc]:
                ls.append((nr,nc))
                total[nr][nc].add((r,c))
    return recur(0,0)

def recur(r:int,c:int)->int:
    if dp[r][c]:
        return dp[r][c]
    value = 0
    for nr,nc in total[r][c]:
        value += recur(nr,nc)
    dp[r][c] = value
    return dp[r][c]

M,N = map(int,input().split())
dp = [[0]*(N) for _ in range(M)]
total = [[set() for __ in range(N)] for _ in range(M)]
dp[M-1][N-1] = 1
ans = solution(M,N)
print(ans)
