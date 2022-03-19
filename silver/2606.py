def infested(n):
    global check
    global cnt
    cnt += 1
    check[n] = 1
    for i in connect[n]:
        if not check[i]:
            infested(i)

n = int(input())
e_n = int(input())
edge = [list(map(int,input().split())) for _ in range(e_n)]
connect = [[] for _ in range(n+1)]
for i in edge:
    x,y = i
    connect[x].append(y)
    connect[y].append(x)

check = [0]*(n+1)
cnt = -1
infested(1)
print(cnt)

