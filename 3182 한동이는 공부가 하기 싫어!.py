def check(n):
    global ans,gcnt
    visited = [0]*(N+1)
    visited[n] = 1
    stack = [n]
    cnt = 0
    while stack:
        cnt += 1
        t = stack.pop()
        next_t = target[t]
        if not visited[next_t]:
            visited[next_t] = 1
            stack.append(next_t)
    if cnt > gcnt:
        ans = n
        gcnt = cnt

N = int(input())
target = [0]+[int(input()) for _ in range(N)]
gcnt = 0
ans = 0
for i in range(1,N+1):
    check(i)
print(ans)