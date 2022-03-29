import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
set_nums = list(set(nums))
set_nums.sort()
solve = {}
for i in range(len(set_nums)):
    solve[set_nums[i]] = i

for j in nums:
    print(solve[j],end=' ')