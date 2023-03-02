def solution(nums:list[int],total:int)->int:
    s,e = 1,max(nums)
    while s <= e:
        mid = (s+e)//2
        value = 0
        for num in nums:
            if num <= mid:
                value += num
            else:
                value += mid
            if value > total:
                e = mid - 1
                break
        if value <= total:
            s = mid + 1
    return e


N = int(input())
arr = list(map(int,input().split()))
value = int(input())
ans = solution(arr,value)
print(ans)