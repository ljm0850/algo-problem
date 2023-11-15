import sys
from collections import deque
def solve(n:int,arr:list)->list:
    start = []
    ans = []
    # 절차의 마무리 점(다른 곳에서 이 점을 조건으로 삼지 않는 점)찾기
    for i in range(1, n + 1):
        if not arr[i]['cnt']:
            start.append(i)

    for s in start:
        que = deque()
        que.append(s)
        ans.append(s)
        while que:
            t = que.popleft()
            for temp in arr[t]['path']:
                arr[temp]['cnt'] -= 1	# 조건 하나 해결
                if not arr[temp]['cnt']: # 모든 조건이 충족 됬으면
                    que.append(temp)
                    ans.append(temp)
    return ans

N,M = map(int,sys.stdin.readline().split())
graph = [{'cnt':0,'path':[]} for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    graph[B]['cnt'] += 1	# 충족이 안된 조건의 개수 체크용
    graph[A]['path'].append(B)	# 조건
answer=solve(N,graph)
print(*answer)