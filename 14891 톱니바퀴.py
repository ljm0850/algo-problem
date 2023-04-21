from collections import deque
def moveWheel(w:int,d:int)->None:
    global wheels
    check = [False]*4
    check[w] = True
    ls = [(w,d)]
    while ls:
        now,way = ls.pop()
        # 왼쪽 바퀴 체크
        next_wheel = now - 1
        if 0<=next_wheel and not check[next_wheel] and wheels[now][6] != wheels[next_wheel][2]:
            ls.append((next_wheel,-way))
            check[next_wheel] = True
        # 오른쪽 바퀴 체크
        next_wheel = now + 1
        if next_wheel <4 and not check[next_wheel] and wheels[now][2] != wheels[next_wheel][6]:
            ls.append((next_wheel,-way))
            check[next_wheel] = True
        # 바퀴 이동
        if way == 1:
            wheels[now].appendleft(wheels[now].pop())
        else:
            wheels[now].append(wheels[now].popleft())

wheels = [deque(map(int,input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    w,d = map(int,input().split())
    moveWheel(w-1,d)

ans = 0
n = 1
for wheel in wheels:
    if wheel[0]:
        ans += n
    n *= 2
print(ans)