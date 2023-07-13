# 최선의 방식은 아님
# 두개의 우선순위 큐를 운용하여 삭제되야 하는데 아직 삭제가 안된 목록을 rm_pri_que에서 관리
from collections import deque
from heapq import heappop,heappush

def solution(N:int,L:int,nums:list[int])->list[int]:
    ans = [0]*(N)
    pri_que = []
    rm_pri_que = []
    que = deque()
    for i in range(L):
        num = nums[i]
        que.append(num)
        heappush(pri_que,num)
        ans[i] = pri_que[0]

    for i in range(L,N):
        num = nums[i]
        que.append(num)
        heappush(rm_pri_que,que.popleft())
        while rm_pri_que and rm_pri_que[0] == pri_que[0]:
            heappop(rm_pri_que)
            heappop(pri_que)
        heappush(pri_que,num)
        ans[i] = pri_que[0]
    return ans

N,L = map(int,input().split())
nums = list(map(int,input().split()))
ans = solution(N,L,nums)
print(*ans)