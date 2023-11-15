R,C = map(int,input().split())
arr = []
ls = []
for r in range(R):
    collumn = input()
    arr.append(collumn)
    if not ls:
        for c in range(C):
            if collumn[c] == 'I':
                ls = [(r,c)]
check = [[False]*C for _ in range(R)]
check[ls[0][0]][ls[0][1]] = True
dr,dc = (1,0,-1,0),(0,1,0,-1)
ans = 0
while ls:
    r,c = ls.pop()
    for way in range(4):
        nr,nc = r+dr[way],c+dc[way]
        if 0<=nr<R and 0<=nc<C and not check[nr][nc] and arr[nr][nc] !='X':
            if arr[nr][nc] == 'P':
                ans += 1
            check[nr][nc] = True
            ls.append((nr,nc))
if ans:
    print(ans)
else:
    print('TT')
