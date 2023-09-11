def solution(N:int,nums:list[int])->str or int:
    if N == 1:
        return 'A'
    if N == 2:
        if nums[0] != nums[1]:
            return 'A'
        else:
            return nums[0]
    if nums[0] == nums[1]:
        a = 0
    else:
        a = int((nums[2] - nums[1]) / (nums[1] - nums[0]))
    b = nums[1] - a * nums[0]

    for i in range(1,N):
        if nums[i] != a * nums[i-1] + b:
            return 'B'
    return a*nums[-1] + b

N = int(input())
nums = list(map(int,input().split()))
ans = solution(N,nums)
print(ans)