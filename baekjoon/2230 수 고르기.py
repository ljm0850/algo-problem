import sys
input = sys.stdin.readline
def solution(N:int,nums:list[int],M:int)->int:
    if M == 0:
        return 0
    nums.sort()
    s,e = 0,0
    value = 2000000000
    while e< N:
        now = nums[e] - nums[s]
        if now >= M:
            s += 1
            value = min(value,now)
        else:
            e += 1
    return value

N,M = map(int,input().split())
nums = [int(input()) for _ in range(N)]
ans = solution(N,nums,M)
print(ans)