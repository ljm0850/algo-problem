import sys
input = sys.stdin.readline
command = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
ward = []
R,C = map(int,input().split())
arr = [input().strip() for _ in range(R)]
r,c = map(lambda x:x-1,map(int,input().split()))
moving = input().strip()
for move in moving:
    if move == 'W':
        ward.append((r,c))
    else:
        dr,dc = command[move]
        r,c = r+dr, c+dc
now = (r,c)
ans = [['#']*C for _ in range(R)]
dr,dc = (1,-1,0,0),(0,0,1,-1)
for r,c in ward:
    if ans[r][c] == '.':
        continue
    ans[r][c] = '.'
    alpha = arr[r][c]
    ls = [(r,c)]
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if not (0<=nr<R and 0<=nc<C) or ans[nr][nc] == '.' or arr[nr][nc] != alpha:
                continue
            ans[nr][nc] = '.'
            ls.append((nr,nc))
r,c = now
ans[r][c] = '.'
for d in range(4):
    nr,nc = r+dr[d],c+dc[d]
    if not (0<=nr<R and 0<=nc<C):
        continue
    ans[nr][nc] = '.'
for answer in ans:
    print(''.join(answer))