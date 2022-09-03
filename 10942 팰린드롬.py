import sys
def make_dp(n:int,nums:list)->list:
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(1,n):
        for start in range(n-length):
            end = start + length
            if nums[start] == nums[end]:
                if start +1 == end:
                    dp[start][end] = 1
                elif dp[start+1][end-1]:
                    dp[start][end] = 1
    return dp

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
record = make_dp(N,nums)
M = int(sys.stdin.readline())
for _ in range(M):
    S,E = map(int,sys.stdin.readline().split())
    print(record[S-1][E-1])
