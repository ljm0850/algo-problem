def solve(nums:list,n:int)->int:
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

N = int(input())
target = list(map(int,input().split()))
ans=solve(target,N)
print(ans)