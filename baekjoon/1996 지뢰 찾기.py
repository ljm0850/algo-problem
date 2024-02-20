N = int(input())
arr = [input() for _ in range(N)]
dr,dc = (1,-1,0,0,1,1,-1,-1),(0,0,1,-1,1,-1,1,-1)
mine = list()
check = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if arr[r][c].isdigit():
            mine.append((r,c))
            for d in range(8):
                nr,nc = r+dr[d],c+dc[d]
                if not (0<=nr<N and 0<=nc<N):
                    continue
                check[nr][nc] += int(arr[r][c])

for r in range(N):
    for c in range(N):
        if check[r][c] >= 10:
            check[r][c] = 'M'
        else:
            check[r][c] = str(check[r][c])
for r,c in mine:
    check[r][c] = '*'
for ans in check:
    print(''.join(ans))

