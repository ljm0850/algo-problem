import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
nums = list(map(int,input().split()))
gap = 0
for _ in range(Q):
    order = list(map(int,input().split()))
    if order[0] == 1:
        nums[(order[1]-1-gap)%N] += order[2]
    elif order[0] == 2:
        gap += order[1]
    else:
        gap -= order[1]
    gap = (gap+N)%N
ans = nums[-gap:] + nums[:-gap]
print(*ans)
