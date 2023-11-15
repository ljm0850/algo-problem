T = int(input())
nums = [int(input()) for _ in range(T)]
N = max(nums)
N += 1
# 기본값 1은 1로만 만드는 경우
dp = [1]*(N)
# 2로 만드는 경우 추가
for i in range(2,N):
    dp[i] += dp[i-2]
# 3으로 만드는 경우 추가
for i in range(3,N):
    dp[i] += dp[i-3]
for num in nums:
    print(dp[num])