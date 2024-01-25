import sys
input = sys.stdin.readline

dir = {'D':(1,0),'L':(0,-1),'R':(0,1),'U':(-1,0)}
R,C = map(int,input().split())
arr = [input().strip() for _ in range(R)]
check = [[0]*C for _ in range(R)]
cnt = 0
for origin_r in range(R):
    for origin_c in range(C):
        if check[origin_r][origin_c]:
            continue
        r,c = origin_r,origin_c
        path = {(r,c)}
        while True:
            dr,dc = dir[arr[r][c]]
            r,c = r+dr,c+dc
            if check[r][c]:
                value = check[r][c]
                break
            elif (r,c) in path:
                cnt += 1
                value = cnt
                break
            path.add((r,c))
        while path:
            r,c = path.pop()
            check[r][c] = value
print(cnt)