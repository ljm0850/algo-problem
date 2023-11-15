def solve(arr:list)->int:
    cnt = [0,0]
    temp = arr[0]
    for alpha in arr:
        if alpha != temp:
            cnt[int(temp)] += 1
            temp = alpha
    cnt[int(temp)] += 1
    return min(cnt)

target = list(input())
ans=solve(target)
print(ans)