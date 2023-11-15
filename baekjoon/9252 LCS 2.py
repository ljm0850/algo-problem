def solve(a:str,b:str)->tuple:
    dp = [[(0,'')]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1] = (dp[i][j][0]+1,dp[i][j][1]+a[i])
            else:
                if dp[i][j+1][0] > dp[i+1][j][0]:
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
    return dp[len(a)][len(b)]

t1 = input()
t2 = input()
ans=solve(t1,t2)
print(ans[0])
print(ans[1])