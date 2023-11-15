N = int(input())
dp = [False]*(max(5,N+1))
dp[2],dp[4] = True,True
for i in range(4,N+1):
    if dp[i-1] == False or dp[i-3] == False:
        dp[i] = True

if dp[N] == True:
    print("SK")
else:
    print("CY")