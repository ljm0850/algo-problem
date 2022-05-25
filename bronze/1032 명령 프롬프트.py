N = int(input())
ans = list(input())
l = len(ans)
for _ in range(N-1):
    t = list(input())
    for i in range(l):
        if ans[i] != t[i]:
            ans[i] = '?'
for t in ans:
    print(t,end='')