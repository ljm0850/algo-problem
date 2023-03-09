from math import comb
def solution(M:int,nums:list[int])->int:
    total = 0
    cnt = [0]*M
    cnt[0] = 1
    for num in nums:
        total = (total+num)%M
        cnt[total] += 1
    value = 0
    for v in cnt:
        value += comb(v,2)
    return value

N,M = map(int,input().split())
nums = list(map(int,input().split()))
ans = solution(M,nums)
print(ans)