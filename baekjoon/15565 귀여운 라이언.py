N,K = map(int,input().split())
nums = list(map(int,input().split()))
s,e = 0,0
cnt = 1 if nums[0] == 1 else 0
ans = N+1
while True:
    if cnt < K:
        e += 1
        if e == N:
            break
        if nums[e] == 1:
            cnt += 1
    else:
        ans = min(ans,e-s+1)
        if nums[s] == 1:
            cnt -= 1
        s += 1
if ans == N+1:
    print(-1)
else:
    print(ans)