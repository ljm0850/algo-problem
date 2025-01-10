import sys
input = sys.stdin.readline

def primeNumList(N:int)->list[int]:
    ls = [True]*(N+1)
    for num in range(2,N):
        if ls[num] == False: continue
        total = 2*num
        while total <= N:
            ls[total] = False
            total += num
    numList = list()
    for i in range(2,N+1):
        if ls[i]: numList.append(i)
    return numList

def solution(nums:list[int])->list[tuple[int]]:
    inf = 100000
    primeNums = primeNumList(inf)
    ans = list()
    for num in nums:
        for div in primeNums:
            cnt = 0
            while num % div == 0 and num != 1:
                num //= div
                cnt += 1
            if cnt:
                ans.append((div,cnt))
    return ans

T = int(input())
nums = [int(input()) for _ in range(T)]
ans = solution(nums)
for value in ans:
    print(*value)