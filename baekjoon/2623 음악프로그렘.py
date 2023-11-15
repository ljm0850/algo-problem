import sys
from collections import deque
input = sys.stdin.readline
def solve(N:int,M:int)->list[int]:
    # 순서 만들기
    cnt = [0]*(N+1)
    path = [[] for _ in range(N + 1)]
    for _ in range(M):
        singer = list(map(int, input().split()))
        for idx in range(1, singer[0]):
            path[singer[idx]].append(singer[idx+1])
            cnt[singer[idx+1]] += 1
    # 시작점
    que = deque()
    value = list()
    for i in range(1,N+1):
        if cnt[i] == 0:
            que.append(i)
    # 탐색
    while que:
        now = que.popleft()
        value.append(now)
        for before in path[now]:
            cnt[before] -= 1
            if cnt[before] == 0:
                que.append(before)
    return value

N,M = map(int,input().split())
answer = solve(N,M)
if len(answer)==N:
    for ans in answer:
        print(ans)
else:
    print(0)