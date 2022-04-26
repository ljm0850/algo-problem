from collections import deque
def play(now):
    global ans
    que = deque()
    que.append(now)
    while que:
        p = que.popleft()
        if p == 100:
            ans = visited[p] -1
            return
        for i in range(1,7):
            np = p+i
            for ladder in ladders:
                if np == ladder[0]:
                    np = ladder[1]
            for snake in snakes:
                if np == snake[0]:
                    np = snake[1]
            if np <= 100 and not visited[np]:
                visited[np] = visited[p] +1
                que.append(np)

N,M = map(int,input().split())
ladders = [list(map(int,input().split())) for _ in range(N)]
snakes = [list(map(int,input().split())) for _ in range(M)]
visited=[0]*101
visited[1] = 1
ans = 111
play(1)
print(ans)