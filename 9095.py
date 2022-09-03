def makenum(n):
    global dp
    if dp[n] :
        return dp[n]

    dp[n] = makenum(n-1)+makenum(n-2)+makenum(n-3)
    return dp[n]

T = int(input())

for tc in range(T):
    n = int(input())
    dp = [0]*12
    dp[1],dp[2],dp[3] = 1,2,4
    print(makenum(n))