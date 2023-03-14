import sys
sys.setrecursionlimit(100000)
def recur(n:int)->int:
    if n == 0:
        return 0
    if dp[n]:
        return dp[n]
    dp[n] = recur(n-1) + recur(n-2)
    return dp[n]

n = int(input())
if n == 0:
    print(0)
else:
    dp = [0]*(n+1)
    dp[1]= 1
    ans = recur(n)
    print(ans)