def solve(i:int,total:int)->None:
    global ans
    if i == N:
        return
    if total + nums[i] == S:
        ans += 1
    solve(i+1,total+nums[i])
    solve(i+1,total)

N,S = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0
solve(0,0)
print(ans)