from collections import deque
import sys
input = sys.stdin.readline
def findRedBlueGoal(R:int,C:int,arr:list[list[str]])->tuple[tuple[int]]:
    for r in range(R):
        for c in range(C):
            match arr[r][c]:
                case '#'|'.':
                    continue
                case 'B':
                    arr[r][c] = '.'
                    blue = (r,c)
                case 'R':
                    arr[r][c] = '.'
                    red = (r,c)
                case 'O':
                    goal = (r,c)
    return red,blue,goal

def gravity(R,C,d,red,blue,arr):
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    v1 = red[0] * dr[d] + red[1] * dc[d]
    v2 = blue[0] * dr[d] + blue[1] * dc[d]
    if v1 > v2:balls = [red,blue]
    else:balls = [blue,red]

    value = list()
    for i in range(2):
        ball = balls[i]
        r,c = ball
        while True:
            nr,nc = r+dr[d], c+dc[d]
            if not (0<=nr<R and 0<=nc<C) or arr[nr][nc] == '#':
                break
            elif arr[nr][nc] == 'O':
                r,c = nr,nc
                break
            elif (nr,nc) in value:
                break
            r,c = nr,nc
        value.append((r,c))
    if v1 > v2:
        return value
    else: return value[::-1]

def bfs(R,C,red,blue,goal,arr):
    check = set()
    que = deque()
    que.append((red,blue))
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            red,blue = que.popleft()
            for d in range(4):
                newRed,newBlue = gravity(R,C,d,red,blue,arr)
                if newBlue == goal:
                    continue
                if newRed == goal:
                    return cnt
                if (newRed,newBlue) in check:
                    continue
                check.add((newRed,newBlue))
                que.append((newRed,newBlue))
    return -1

R,C = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(R)]
red,blue,goal = findRedBlueGoal(R,C,arr)
ans = bfs(R,C,red,blue,goal,arr)
print(ans)