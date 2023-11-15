from collections import deque
import sys

# 0인 부분만 계산하여 해당 지점에선 얼마나 지나다닐수 있는지 기록
def make_record(R,C):
    if target[R][C] == '1' or record[R][C]:
        return
    visit = {(R,C):True}
    cnt = 1
    que= deque()
    que.append((R,C))
    while que:
        r,c = que.popleft()
        for way in range(4):
            nr = r + dr[way]
            nc = c + dc[way]
            if 0<=nr<N and 0<=nc<M and not visit.get((nr,nc)) and target[nr][nc] == '0':
                if ans[nr][nc]:
                    cnt += ans[nr][nc]
                    continue
                visit[(nr,nc)] = True
                que.append((nr,nc))
                cnt += 1
    
    # 지나온 경로들에 같은 값 기록
    keys = visit.keys()
    for key in keys:
        # (R,C)는 같은 경로를 지나가는 길인지 체크하는 용
        record[key[0]][key[1]] = (cnt,(R,C))

def solve(r,c):
    if target[r][c] == '0':
        return
    cnt = 1
    check = {}
    # 주변에 0인 지점들에 기록된 값의 합
    for way in range(4):
        nr = r + dr[way]
        nc = c + dc[way]
        if 0<=nr<N and 0<=nc<M and target[nr][nc]=='0' and not check.get(record[nr][nc][1]):
            cnt += record[nr][nc][0]
            check[record[nr][nc][1]] = True
    ans[r][c] = cnt % 10

dr = (0,0,1,-1)
dc = (1,-1,0,0)
N,M = map(int,sys.stdin.readline().split())
target = [sys.stdin.readline() for _ in range(N)]
ans = [[0]*M for _ in range(N)]
record = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        make_record(i,j)
for i in range(N):
    for j in range(M):
        solve(i,j)
for a in ans:
    print("".join(map(str,a)))