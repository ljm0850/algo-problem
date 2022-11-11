import sys
import heapq
def dijkstra(arr:list[list[int]],N:int):
    short_cut = [[1250]*N for _ in range(N)]
    short_cut[0][0] = arr[0][0]
    h = [(0,0,arr[0][0])]
    while h:
        r,c,rupee = heapq.heappop(h)
        if rupee > short_cut[r][c]:
            continue
        if r==c==N-1:
            return rupee

        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if not (0<=nr<N and 0<=nc<N):
                continue
            next_rupee = rupee + arr[nr][nc]
            if next_rupee < short_cut[nr][nc]:
                short_cut[nr][nc] = next_rupee
                heapq.heappush(h,(nr,nc,next_rupee))
    return short_cut[N-1][N-1]

dr,dc = (0,0,1,-1),(1,-1,0,0)
cnt = 0
while True:
    cnt += 1
    N = int(sys.stdin.readline())
    if N == 0:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    ans = dijkstra(arr,N)
    print(f'Problem {cnt}: {ans}')