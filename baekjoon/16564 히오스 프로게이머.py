# N개의 캐릭터, 현재 레벨은 Xi, 레벨을 최대 총합 K 만큼, 팀 목표 레벨 T = min(Xi), 최대 T
# N<= 백만, K<= 10억

import sys
from bisect import bisect_left

def solution(N:int,K:int,levels:list[int])->int:
    levels.sort()
    sum_levels = [0]*(N+1)
    for i in range(N):
        sum_levels[i+1] = sum_levels[i] + levels[i]

    s,e = levels[0] + K//N, levels[0] + K
    value = s
    while s <= e:
        mid = (s+e) //2
        idx = bisect_left(levels, mid)
        cnt = idx * mid - sum_levels[idx]
        if cnt <= K:
            value = mid
            s = mid + 1
        else:
            e = mid -1
    return value

N,K = map(int,input().split())
levels = list(int(sys.stdin.readline()) for _ in range(N))

ans = solution(N,K,levels)
print(ans)