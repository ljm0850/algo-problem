def solution(R,C,arr,moving):
    dr,dc = (0,1,1,1,0,0,0,-1,-1,-1),(0,-1,0,1,-1,0,1,-1,0,1)
    
    me = ()
    robots = set()
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '.':
                continue
            elif arr[r][c] == 'I':
                me = (r,c)
            else:
                robots.add((r,c))
    
    for cnt in range(len(moving)):
        d = moving[cnt]
        # 종수 이동
        r,c = me
        arr[r][c] = '.'
        nr,nc = r+dr[d], c+dc[d]
        me = (nr,nc)
        if arr[nr][nc] == 'R':  # 이동 지점에 로봇이 있으면
            return cnt
        arr[nr][nc] = 'I'

        # 로봇 이동
        next_robots = set()
        boom = set()
        for _ in range(len(robots)):
            robot = robots.pop()
            arr[robot[0]][robot[1]] = '.'
            vecter = robot_moving(me,robot)
            nr,nc = robot[0] + vecter[0], robot[1] + vecter[1]
            if (nr,nc) in next_robots:
                boom.add((nr,nc))
            else:
                if arr[nr][nc] == 'I':
                    return cnt
                next_robots.add((nr,nc))
        for r,c in boom:
            next_robots.remove((r,c))
        for r,c in next_robots:
            arr[r][c] = 'R'
        robots = next_robots

    return 0

def robot_moving(me,robot):
    r,c = 0,0
    if me[0] > robot[0]:
        r = 1
    elif me[0] < robot[0]:
        r = -1
    if me[1] > robot[1]:
        c = 1
    elif me[1] < robot[1]:
        c = -1
    return (r,c)


R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
moving = list(map(int,input()))
flag = solution(R,C,arr,moving)
if flag:
    print(f'kraj {flag+1}')
else:
    for ls in arr:
        print(''.join(ls))