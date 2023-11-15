def check():
    global cnt,solve
    for i in range(N):
        for j in range(N):
            if home[i][j] == 1:
                cnt += 1
                hcnt = 0
                stack = [(i, j)]
                while stack:
                    hcnt += 1
                    c, r = stack.pop()
                    home[c][r] = 0
                    for way in range(4):
                        nc = c + dc[way]
                        nr = r + dr[way]
                        if 0 <= nc < N and 0 <= nr < N and home[nc][nr] and not (nc, nr) in stack:
                            stack.append((nc, nr))
                solve.append(hcnt)

N = int(input())
home = [list(map(int,input())) for _ in range(N)]
cnt = 0
solve = []
dc = (1,-1,0,0)
dr = (0,0,1,-1)
check()
solve.sort()
print(len(solve))
for sol in solve:
    print(sol)
