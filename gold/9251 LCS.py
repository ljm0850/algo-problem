def solve():
    for i in range(n1):
        for j in range(n2):
            if t1[i] == t2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

t1 = input()
t2 = input()
n1 = len(t1)
n2 = len(t2)
dp = [[0]*(n2+1) for _ in range(n1+1)]
solve()
print(dp[n1][n2])