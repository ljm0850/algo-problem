import sys
input = sys.stdin.readline
def solution(N:int,M:int,C:int)->int:
    arr = [0] + [[0] + list(map(int, input().split())) for _ in range(C)]
    if N<=M:
        small = [0]+list(map(int, input().split()))
        big = [0]+list(map(int, input().split()))
    else:
        big = [0]+list(map(int, input().split()))
        small = [0]+list(map(int, input().split()))
    s,b = min(N,M),max(N,M)

    dp = [[0]*(b+1) for _ in range(s+1)]

    for sIdx in range(1,s+1):
        for bIdx in range(1,b+1):
            dp[sIdx][bIdx] = max(dp[sIdx-1][bIdx],dp[sIdx][bIdx-1],dp[sIdx-1][bIdx-1]+arr[small[sIdx]][big[bIdx]])
    return dp[s][b]

N,M,C = map(int,input().split())
ans = solution(N,M,C)
print(ans)