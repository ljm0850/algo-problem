import sys
from heapq import heappush,heappop
N,K = map(int,sys.stdin.readline().split())
jewel = []

for _ in range(N):
    M,V = map(int,sys.stdin.readline().split())
    jewel.append((M,V))
jewel.sort(reverse=True)
backpack = [int(sys.stdin.readline()) for _ in range(K)]
backpack.sort()
ans = 0

can_theft = []
# 무게순으로 가방에 보석을 넣음
for bag in backpack:
    while jewel and bag >= jewel[-1][0]:
        # 무게상 훔칠수 있으면 can_theft에 넣음, value 순서로
        heappush(can_theft,-jewel.pop()[1])
    # 해당 가방에 넣을 것중 가장 값비싼거 추가
    if can_theft:
        ans -= heappop(can_theft)
    # 넣을 보석도 없고 더이상 남은 보석이 없음
    elif not jewel:
        break
print(ans)