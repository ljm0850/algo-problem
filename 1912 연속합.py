def solve():
    ans = nums[0]
    before = 0
    for num in nums:
        before = max(before+num,num)
        if before > ans:
            ans = before
    return ans

n = int(input())
nums = list(map(int,input().split()))
print(solve())