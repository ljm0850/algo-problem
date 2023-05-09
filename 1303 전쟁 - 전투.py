import sys
input = sys.stdin.readline
def power(r:int,c:int)->int:
    team = arr[r][c]
    check[r][c] = True
    ls = [(r,c)]
    cnt = 1
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<R and 0<=nc<C and not check[nr][nc] and team == arr[nr][nc]:
                check[nr][nc] = True
                ls.append((nr,nc))
                cnt += 1
    return cnt**2

C,R = map(int,input().split())
arr = [input().rstrip() for _ in range(R)]
check = [[False]*C for _ in range(R)]
dr,dc = (1,-1,0,0),(0,0,1,-1)
my_team,enemy_team = 0,0
for r in range(R):
    for c in range(C):
        if check[r][c]:
            continue
        value = power(r,c)
        if arr[r][c] == 'W':
            my_team += value
        else:
            enemy_team += value
print(my_team,enemy_team)