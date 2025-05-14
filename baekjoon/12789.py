from collections import deque

def solution(N:int,que:deque[int])->bool:
    stack = list()
    cnt = 1
    while cnt < N:
        if stack and stack[-1] == cnt:
            stack.pop()
            cnt += 1
        elif not que: return False
        else:
            value = que.popleft()
            if value == cnt: cnt += 1
            else:stack.append(value)
    return True

N = int(input())
que = deque(map(int,input().split()))
ans = solution(N,que)
if ans:print("Nice")
else:print("Sad")