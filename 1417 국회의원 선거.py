import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())
me = - int(input())
others = []
for _ in range(N-1):
    heappush(others,-int(input()))
cnt = 0
if others:
    while me >= others[0]:
        cnt += 1
        me -= 1
        heappush(others,heappop(others)+1)
print(cnt)