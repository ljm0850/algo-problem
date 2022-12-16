def find_fibo(n:int)->int:
    if n == 0:
        return 0
    elif dp[n]:
        return dp[n]
    dp[n]= find_fibo(n-2) + find_fibo(n-1)
    return dp[n]

n = int(input())
dp = [0]*(n+1)
if n >= 1:
    dp[1] = 1
ans = find_fibo(n)
print(ans)