N,M = map(int,input().split())
nums = list(map(int,input().split()))
start,end = 0,0
now_num = nums[0]
ans = 0
while start<N:
    if now_num <M:
        end += 1
        if end == N:
            break
        now_num += nums[end]
    elif now_num > M:
        now_num -= nums[start]
        start += 1
        if start > end:
            end += 1
            if end == N:
                break
            now_num += nums[end]
    else:
        ans += 1
        end += 1
        if end == N:
            break
        now_num += nums[end] - nums[start]
        start += 1
print(ans)