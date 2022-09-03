import sys
def total():
    temp = []
    for _ in range(n):
        volume = int(sys.stdin.readline())
        temp.append(volume)
    return temp

def solve():
    dp = [0]
    dp.append(grape[0])
    if n >= 2:
        dp.append(grape[0]+grape[1])
    for i in range(3,n+1):
        dp.append(max(dp[i-1],dp[i-2]+grape[i-1],dp[i-3]+grape[i-1]+grape[i-2]))
    return dp[-1]

n = int(sys.stdin.readline())
grape = total()
ans=solve()
print(ans)