from collections import deque
def solve(nums:list[int])->int:
    value = 0
    que = deque([i for i in range(1,N+1)])
    for num in nums:
        if que[0] != num:
            point = que.index(num)
            if point <= len(que)//2:
                que.rotate(-point)
                value += point
            else:
                que.rotate((len(que)-point))
                value += len(que)-point
        que.popleft()
    return value

N,M = map(int,input().split())
target = list(map(int,input().split()))
ans = solve(target)
print(ans)