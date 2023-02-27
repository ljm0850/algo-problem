N = int(input())
nums = list(map(int,input().split()))
ai,aj,nai = nums[0],nums[0],nums[0]
for num in nums:
    if num - nai > aj - ai:
        aj = num
        ai = nai
    elif num < nai:
        nai = num
    print(aj-ai,end=' ')
