def solve(n:int,nums:list)->int:
    dp = [nums[i] for i in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+nums[i])
    return max(dp)

N = int(input())
target = list(map(int,input().split()))
ans=solve(N,target)
print(ans)