def solve(ls):
    if len(ls) == M:
        print(*ls)
        return
    for num in nums:
        if ls:
            if num >= ls[-1]:
                solve(ls+[num])
        else:
            solve(ls+[num])

N,M = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()
solve([])