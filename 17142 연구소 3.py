from itertools import combinations
from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
virus_total = []
total = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            continue
        total += 1
        if arr[r][c] == 2:
            virus_total.append((r,c))
virus_comb = list(combinations(virus_total,M))
dr,dc = (1,-1,0,0,),(0,0,1,-1)
max_cnt = 2500
ans = max_cnt

for virus in virus_comb:
    que = deque(virus)
    check = [[False]*N for _ in range(N)]
    for r,c in virus:
        check[r][c] = True

    value,cnt = 0,len(virus_total)
    while que:
        if cnt == total:
            ans = min(ans,value)
            break
        for _ in range(len(que)):
            r,c = que.popleft()
            for d in range(4):
                nr,nc = r+dr[d], c+dc[d]
                if 0<=nr<N and 0<=nc<N and arr[nr][nc] !=1 and not check[nr][nc]:
                    que.append((nr,nc))
                    check[nr][nc] = True
                    if arr[nr][nc] != 2:
                        cnt += 1
        value += 1
if ans != max_cnt:
    print(ans)
else:
    print(-1)