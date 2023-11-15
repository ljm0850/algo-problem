def solution(N:int,K:int,nums:list[int])->int:
    cnt = dict()
    value = 0
    s = 0
    for e in range(N):
        num = nums[e]
        if cnt.get(num):
            cnt[num] += 1
            while cnt[num] > K:
                cnt[nums[s]] -= 1
                s += 1
        else:
            cnt[num] = 1
        value = max(value,e-s+1)
    return value

N,K = map(int,input().split())
nums = list(map(int,input().split()))
ans = solution(N,K,nums)
print(ans)