import sys
N=int(input())

nums = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
nums.sort()
[print(*num) for num in nums]