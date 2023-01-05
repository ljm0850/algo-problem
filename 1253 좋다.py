def check(arr,num):
    start,end = 0,N-2
    while start < end:
        value = arr[start] + arr[end]
        if value < num:
            start += 1
        elif value > num:
            end -=  1
        else:
            return True
    return False

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
ans = 0
for idx in range(N):
    tempArr = nums[:idx] + nums[idx+1:]
    num = nums[idx]
    if check(tempArr,num): ans += 1
print(ans)