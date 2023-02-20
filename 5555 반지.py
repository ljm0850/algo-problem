from collections import deque
def check(Q,A):
    que = deque(A)
    for idx in range(len(A)):
        for s in range(len(Q)):
            if Q[s] != que[s]:
                break
        else:
            return True
        que.append(que.popleft())
    return False

Target = input()
n = int(input())
ans = 0
for _ in range(n):
    temp = check(Target,input())
    if temp:
        ans += 1
print(ans)
