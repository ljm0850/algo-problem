import sys

n,m = map(int,sys.stdin.readline().split())
arr = [0]+list(map(int,sys.stdin.readline().split()))
prefix = [0 for i in range(n+1)]
for i in range(1,n+1):
    prefix[i] = prefix[i-1] + arr[i]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(prefix[b]-prefix[a-1])