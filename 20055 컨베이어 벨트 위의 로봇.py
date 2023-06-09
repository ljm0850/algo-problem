from collections import deque
def solution(K:int)->int:
    cnt = 0
    value = 0
    while cnt < K:
        value += 1
        move_belt()
        drop_robot()
        cnt = move_robots(cnt)
        drop_robot()
        cnt = add_robot(cnt)
    return value

def move_belt()->None:
    global belt1,belt2
    a = belt1.pop()
    b = belt2.popleft()
    belt1.appendleft(b)
    belt2.append(a)
    for i in range(N-1)[::-1]:
        if robots[i]:
            robots[i] = False
            robots[i+1] = True

def drop_robot():
    global robots,belt1
    robots[-1] = False

def move_robots(cnt):
    for i in range(N-1)[::-1]:
       T = belt1[i+1]
       if robots[i] and not robots[i+1] and durability[T]:
           robots[i] = False
           robots[i+1] = True
           durability[T] -= 1
           if durability[T] == 0:
               cnt += 1
    return cnt

def add_robot(cnt):
    T = belt1[0]
    if robots[0] == False and durability[T]:
        robots[0] = True
        durability[T] -= 1
        if durability[T] == 0:
            cnt += 1
    return cnt

def belt(s:int,e:int,d)->deque:
    que = deque()
    for i in range(s,e+1,d):
        que.append(i)
    return que



N,K = map(int,input().split())
durability = [0] + list(map(int,input().split()))
belt1,belt2 = belt(1,N,1),belt(2*N,N-1,-1)
robots = deque([False]*N)
ans = solution(K)
print(ans)