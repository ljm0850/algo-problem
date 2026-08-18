# N은 정원 구획의 개수, K는 연속해서 심을 수 있는 꽃의 최대 개수
# N <= 10만, k <= N
# 버릴? 구역에 대한 정보를 dp에 기록

from collections import deque
import sys

def solution(N:int, K:int, profits:list[int])->int:
    nums = [0] + profits + [0]
    dp = [0]*(N+2)
    sliding_window_idx = deque([0])
    for i in range(1,N+2):
        # 범위 밖 idx 제거
        while sliding_window_idx[0] < i-K-1:
            sliding_window_idx.popleft()
        dp[i] = nums[i]+dp[sliding_window_idx[0]]
        while sliding_window_idx and dp[sliding_window_idx[-1]] >= dp[i]:
            sliding_window_idx.pop()
        sliding_window_idx.append(i)
    return sum(profits)-dp[N+1]

input = sys.stdin.readline
N,K = map(int,input().split())
profits = [int(input()) for _ in range(N)]
ans = solution(N,K,profits)
print(ans)