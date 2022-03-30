def check(n,cnt):
    global visit
    visit[n] = cnt
    for ch in sol[n]:
        if visit[ch] == -1 or visit[ch] > cnt+1:
            check(ch,cnt+1)

N,M = map(int,input().split())          # N = 유저의 수, M = 친구 수
connect = [list(map(int,input().split())) for _ in range(M)]
sol = [[] for _ in range(N+1)]
ans = 1000000000
for i in range(M):
    sol[connect[i][0]].append(connect[i][1])
    sol[connect[i][1]].append(connect[i][0])
for j in range(1,N+1):
    visit = [-1]*(N+1)
    check(j,0)
    t = sum(visit)
    if ans > t:
        ans = t
        ans_num = j
print(ans_num)