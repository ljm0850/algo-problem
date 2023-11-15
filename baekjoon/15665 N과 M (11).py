def solve(cur:int,n:int,value:list)->None:
    if cur == 0:
        print(*value)
        return
    for i in range(n):
        solve(cur-1,n,value+[nums[i]])

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums = sorted(list(set(nums)))
solve(M,len(nums),[])