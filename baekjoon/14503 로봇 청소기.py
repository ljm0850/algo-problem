import sys
# N = row , M = column
N,M = map(int,sys.stdin.readline().split())
position = tuple(map(int,sys.stdin.readline().split()))
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# 북동남서
dr,dc = (-1,0,1,0),(0,1,0,-1)

def solve(now:tuple[int,int,int])->int:
    ans = 0
    while True:
        r,c,d = now
        # 현재 위치 청소
        arr[r][c] = 2
        ans += 1
        cnt = 0
        while True:
            # 왼쪽
            nd = (d+3)%4
            nr,nc = r+dr[nd],c+dc[nd]
            if arr[nr][nc] == 0:
                now = (nr,nc,nd)
                break
            else:
                if cnt < 4:
                    d = nd
                    cnt += 1
                else:
                    nr,nc = r-dr[d],c-dc[d]
                    if arr[nr][nc] != 1:
                        r,c = nr,nc
                        cnt = 0
                    else:
                        return ans
ans = solve(position)
print(ans)