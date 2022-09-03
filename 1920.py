N = int(input())            # 100,000 이하
nums = list(map(int,input().split()))     #N개의 수, -2**31이상 2**31 미만
M = int(input())            # 100,000 이하
target = list(map(int,input().split()))   #M개의 수, -2**31이상 2**31 미만

nums.sort()

for i in target:
    s = 0
    e = N-1
    solve = 0
    while s<=e :
        mid = (s+e)//2
        if i == nums[mid]:
            solve = 1
            break
        elif i < nums[mid]:
            e = mid - 1
        else:
            s = mid + 1
    print(solve)