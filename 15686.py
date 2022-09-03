def total_length(h,c):
    temp = [[] for _ in range(h)]
    for i in range(h):
        for j in chicken:
            temp[i].append(abs(home[i][0] - j[0]) + abs(home[i][1] - j[1]))
    return temp

def delivery(cnt,i):        # cnt = 현재 남은 점포 수,i = 폐점을 논의할 치킨집 index
    global ans
    if cnt == M:
        total = 0
        for way in length:
            total += min(way)
        if total < ans:
            ans = total
        return
    elif i < c:
        delivery(cnt,i+1)           # 생존
        sol = []                    # 값 되돌릴때 쓸 용도
        for ii in range(h):
            sol.append(length[ii][i])
            length[ii][i] = 100
        delivery(cnt-1,i+1)         # 폐점
        for ii in range(h):
            length[ii][i] = sol[ii]

N,M = map(int,input().split())          # N 은 50이하, M은 13이하
city = [list(map(int,input().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))
h = len(home)
c = len(chicken)

length = total_length(h,c)
ans = 10000
delivery(c,0)
print(ans)