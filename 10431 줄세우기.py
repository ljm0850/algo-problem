def solution(arr:list)->int:
    cnt = 0
    N = len(arr)
    for i in range(1,N):
        for j in range(i+1,N):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
                cnt += 1
    return cnt

T = int(input())
for tc in range(1,T+1):
    nums = list(map(int,input().split()))
    ans = solution(nums)
    print(nums[0],ans)