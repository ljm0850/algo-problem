def solve(ls):
    if len(ls) == M:
        print(*ls)
        return
    for num in nums:
        if ls:
            if ls[-1] <= num:
                solve(ls+[num])
        else:
            solve([num])

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
solve([])
