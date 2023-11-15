import sys
N,K = map(int,sys.stdin.readline().split())
nums = sorted(list(map(int,input().split())))
print(nums[K-1])
