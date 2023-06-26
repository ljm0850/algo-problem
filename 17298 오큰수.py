import sys
input = sys.stdin.readline

def solution(N:int,nums:list[int])->list[int]:
    answer = [-1]*(N)
    ls = []
    for i in range(N):
        while ls and nums[ls[-1]] < nums[i]:
            answer[ls.pop()] = nums[i]
        ls.append(i)
    return answer

N = int(input())
nums = list(map(int,input().split()))
ans = solution(N,nums)
print(*ans)