def check(ls):
    if len(ls) == M:
        print(*ls)
        return
    for i in nums:
        if ls and not i in ls:
            check(ls+[i])
        elif not ls:
            check(ls+[i])
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
check([])