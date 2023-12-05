def recur(value:int,idx:int,cur:int):
    global best_value,worst_value
    if cur == 0:
        best_value = max(best_value,value)
        worst_value = min(worst_value,value)
        return
    nidx,ncur = idx + 1,cur - 1
    if cnt[0]:
        cnt[0] -= 1
        recur(value+nums[idx],nidx,ncur)
        cnt[0] += 1
    if cnt[1]:
        cnt[1] -= 1
        recur(value-nums[idx],nidx,ncur)
        cnt[1] += 1
    if cnt[2]:
        cnt[2] -= 1
        recur(value*nums[idx],nidx,ncur)
        cnt[2] += 1
    if cnt[3]:
        cnt[3] -= 1
        if value >= 0:
            recur(value//nums[idx],nidx,ncur)
        else:
            recur((-value//nums[idx])*-1,nidx,ncur)
        cnt[3] += 1

N = int(input())
nums = list(map(int,input().split()))
cnt = list(map(int,input().split()))
max_value = 1000000000
best_value,worst_value = -max_value,max_value
recur(nums[0],1,N-1)
print(best_value)
print(worst_value)