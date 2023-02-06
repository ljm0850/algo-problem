def solution(N:int,nums:list[str])->int:
    check = set()
    n = len(nums[0])
    k = n-1
    while k >= 0:
        for idx in range(N):
            target = nums[idx][k:]
            if not target in check:
                check.add(target)
            else:
                k -= 1
                break
        else:
            return n - k

N = int(input())
nums = [input() for _ in range(N)]
ans = solution(N,nums)
print(ans)