import heapq,sys
input = sys.stdin.readline
def solution(n):
    arr = [input() for _ in range(n)]
    dr,dc = (1,0,-1,0),(0,1,0,-1)
    h = [(0,0,0)]
    check = [[2500]*n for _ in range(n)]
    N = n-1
    while h:
        cnt,r,c = heapq.heappop(h)
        if check[r][c] < cnt:
            continue
        for way in range(4):
            nr,nc = r+dr[way], c+dc[way]
            if 0<=nr<n and 0<=nc<n:
                if nr == N and nc == N:
                    return cnt
                if check[nr][nc] <= cnt:
                    continue
                elif arr[nr][nc] == '1':
                    heapq.heappush(h,(cnt,nr,nc))
                    check[nr][nc] = cnt
                else:
                    heapq.heappush(h,(cnt+1,nr,nc))
                    check[nr][nc] = cnt+1

n = int(input())
ans = solution(n)
print(ans)
