# python으로 제출시 시간초과.. pypy...
import sys
def dust_diffusion():
    global home
    dust = []
    for r in range(R):
        for c in range(C):
            if home[r][c] >0:
                cnt = 0
                split = home[r][c] //5
                for way in range(4):
                    nr,nc = r+dr[way],c+dc[way]
                    if 0<=nr<R and 0<=nc<C and home[nr][nc] != -1:
                        cnt += 1
                        dust.append((nr,nc,split))
                home[r][c] -= split * cnt
    while dust:
        r,c,d = dust.pop()
        home[r][c] += d

def air_cleaner():
    global home
    dust = []
    p1,p2 = cleaner[0],cleaner[1]
    for c in range(C-1):
        if home[p1][c] >0:
            dust.append((p1,c+1,home[p1][c]))
            home[p1][c] = 0
        if home[p2][c] >0:
            dust.append((p2,c+1,home[p2][c]))
            home[p2][c] = 0

    for c in range(1,C):
        if home[0][c] >0:
            dust.append((0,c-1,home[0][c]))
            home[0][c] = 0
        if home[-1][c] >0:
            dust.append((-1,c-1,home[-1][c]))
            home[-1][c] = 0

    for r in range(p1):
        if home[r][0] >0:
            dust.append((r+1,0,home[r][0]))
            home[r][0] = 0

    for r in range(1,p1+1):
        if home[r][-1]>0:
            dust.append((r-1,-1,home[r][-1]))
            home[r][-1] = 0

    for r in range(p2+1,R):
        if home[r][0] >0:
            dust.append((r-1,0,home[r][0]))
            home[r][0] = 0

    for r in range(p2,R-1):
        if home[r][-1] >0:
            dust.append((r+1,-1,home[r][-1]))
            home[r][-1] = 0

    while dust:
        r,c,d = dust.pop()
        if home[r][c] == -1:
            continue
        home[r][c] = d

def solve():
    ans = sum(sum(home[r]) for r in range(R))
    ans += 2
    print(ans)

dr,dc = (0,1,0,-1),(1,0,-1,0)
R,C,T = map(int,sys.stdin.readline().split())
home = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    if home[i][0] == -1:
        cleaner.append(i)

for time in range(T):
    dust_diffusion()
    air_cleaner()
solve()
