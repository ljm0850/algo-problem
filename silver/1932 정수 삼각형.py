import sys
def solve():
    for i in range(1,n):
        for j in range(i+1):
            if 0<j<i:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            else:
                dp[i][j] = dp[i-1][j-1]+triangle[i][j]
n = int(input())
triangle = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(d+1) for d in range(n)]
dp[0][0] = triangle[0][0]
solve()
print(max(dp[n-1]))