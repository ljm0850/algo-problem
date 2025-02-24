from collections import deque
def solution(N:int,cmds:list[int])->deque[int]:
    ans = deque()
    for card in range(1,N+1):
        cmd = cmds[N-card]
        match cmd:
            case 1:
                ans.appendleft(card)
            case 2:
                temp = ans.popleft()
                ans.appendleft(card)
                ans.appendleft(temp)
            case 3:
                ans.append(card)
    return ans

N = int(input())
cmds = list(map(int,input().split()))
ans = solution(N,cmds)
print(*ans)