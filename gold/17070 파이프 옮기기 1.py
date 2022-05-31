import sys

def solve():
    dp = [[[0] * N for _ in range(N)] for __ in range(N)]
    dp[0][0][1] = 1
    for i in range(N):
        for j in range(2,N):
            if not arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
                dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
            if not arr[i][j]:
                dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
                dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]
    ans = 0
    for k in range(3):
        ans += dp[k][N-1][N-1]
    return ans

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for __ in range(N)]
ans = solve()
print(ans)