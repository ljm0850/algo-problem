import heapq,sys
imput = sys.stdin.readline
def solve(C:int,R:int)->int:
    INF = 10001
    dr,dc = (1,0,-1,0),(0,1,0,-1)
    arr = [input() for _ in range(R)]
    check = [[INF] * C for _ in range(R)]
    check[0][0] = 0
    h = []
    heapq.heappush(h, (0, 0, 0))
    while h:
        cnt,r,c = heapq.heappop(h)
        if cnt > check[r][c]:
            continue
        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if 0<=nr<R and 0<=nc<C and cnt < check[nr][nc]:
                if nr == R-1 and nc == C-1:
                    return cnt
                elif arr[nr][nc] == '0' and cnt < check[nr][nc]:
                        check[nr][nc] = cnt
                        heapq.heappush(h,(cnt,nr,nc))
                elif cnt+1 < check[nr][nc]:
                    check[nr][nc] = cnt+1
                    heapq.heappush(h,(cnt+1,nr,nc))
    return check[R-1][C-1]
M,N = map(int,input().split())
ans = solve(M,N)
print(ans)