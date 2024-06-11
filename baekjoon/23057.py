N = int(input())
nums = list(map(int,input().split()))
M = sum(nums)
total = set([0])
for num in nums:
    temp = set()
    for value in total:
        temp.add(value+num)
    total.update(temp)
print(total)
ans = M-len(total) + 1
print(ans)