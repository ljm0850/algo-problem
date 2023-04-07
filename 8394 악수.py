def solution(n:int)->int:
    dp = [0]*(n+1)
    dp[0],dp[1] = 1,1
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%10
    return dp[n]

n = int(input())
ans = solution(n)
print(ans)

# import sys
# sys.setrecursionlimit(10000001)
#
# def fibo(n:int)->int:
#     if dp[n]:
#         return dp[n]
#     dp[n] = (fibo(n-1) + fibo(n-2))%10
#     return dp[n]
#
# n = int(input())
# dp = [0]*(n+1)
# dp[0],dp[1] = 1,1
# ans = fibo(n)
# print(ans)