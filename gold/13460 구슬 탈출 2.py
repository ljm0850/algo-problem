from collections import deque
import copy
def make_arr(n,m):
    arr = [[] for _ in range(n)]
    balls = []
    for r in range(n):
        row = input()
        for c in range(m):
            if row[c] == 'R' or row[c]=='B':
                balls.append((row[c],r,c))
        arr[r].extend(row)
    for ball in balls:
        arr[ball[1]][ball[2]] = '.'
    return arr,balls

def solve(balls_info):
    que = deque()
    que.append(balls_info)
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            balls_origin=que.popleft()
            balls_origin.sort()
            if cnt == 11:
                return -1
            for way in range(4):
                balls = copy.deepcopy(balls_origin)
                br = False
                # 공 움직일 순서대로 정렬
                if way == 0:
                    balls.sort(key=lambda x:x[1], reverse=True)
                elif way == 1:
                    balls.sort(key=lambda x:x[1])
                elif way == 2:
                    balls.sort(key=lambda x:x[2], reverse=True)
                else:
                    balls.sort(key=lambda x:x[2])
                # 공 움직이기
                complete = False
                for i in range(2):
                    if br:
                        break
                    ball = balls[i]
                    another_ball = balls[(i+1)%2]
                    color,r,c = ball[0],ball[1],ball[2]
                    nr,nc = r+dr[way],c+dc[way]
                    while 0<=nr<N and 0<=nc<M:
                        if arr[nr][nc] == '.' and (nr != another_ball[1] or nc != another_ball[2]):
                            r,c, = nr,nc
                            balls[i] = (color,r,c)
                            nr,nc = r+dr[way],c+dc[way]
                        elif arr[nr][nc] == 'O':
                            if color == 'R':
                                complete = True
                                balls[i] = (color,0,0)
                                break
                            else:
                                br = True
                                complete = False
                                break
                        else:
                            break
                if complete:
                    return cnt
                if not br and sorted(balls) != balls_origin:
                    que.append(balls)
    return -1

dr = (1,-1,0,0)
dc = (0,0,1,-1)

N,M = map(int,input().split())
arr,balls = make_arr(N,M)
ans=solve(balls)
print(ans)