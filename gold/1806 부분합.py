import sys
def solve(target:int,arr:list)->int:
    cnt = 200000
    s,e = 0,0
    sum_num = arr[0]
    while e<N:
        if sum_num >= target:
            cnt = min(cnt, e - s + 1)
            sum_num -= arr[s]
            if cnt == 1:
                return 1
            s += 1
        else:
            e += 1
            if e < N:
                sum_num += arr[e]
    if cnt != 200000:
        return cnt
    return 0

N,S = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
ans = solve(S,nums)
print(ans)