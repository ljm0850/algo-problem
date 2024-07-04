def solution(N:int,S:int,M:int,volume:list[int])->int:
    volume = [0]+volume
    dp = [set() for _ in range(N+1)]
    dp[0].add(S)
    for i in range(1,N+1):
        for v in dp[i-1]:
            if v+volume[i]<=M:
                dp[i].add(v+volume[i])
            if v-volume[i]>=0:
                dp[i].add(v-volume[i])
    if dp[N]:
        return max(dp[N])
    else:
        return -1

N,S,M = map(int,input().split())
volume = list(map(int,input().split()))
ans = solution(N,S,M,volume)
print(ans)