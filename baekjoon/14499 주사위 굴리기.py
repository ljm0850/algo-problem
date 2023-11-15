def inrange(x:int,y:int)->bool:
    if 0<=x<M and 0<=y<N:
        return True
    return False

# [1,2,3,4,5,6] 에서
# 동쪽 이동시 [4,2,1,6,5,3]
# 서쪽 이동시 [3,2,1,6,5,4]
# 북쪽 이동시 [5,1,3,4,6,2]
# 남쪽 이동시 [2,6,3,4,1,5]
def moveDice(cmd:int,dice:list[int])->list[int]:
    if cmd == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    elif cmd == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
    elif cmd == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]
    return dice
N,M,y,x,K = map(int,input().split())
arr =  [list(map(int,input().split())) for _ in range(N)]
cmds = list(map(int,input().split()))
dice = [0,0,0,0,0,0]
dx,dy = (0,1,-1,0,0),(0,0,0,-1,1)
for cmd in cmds:
    nx,ny = x+dx[cmd],y+dy[cmd]
    if not inrange(nx,ny):
        continue
    x,y = nx,ny
    dice = moveDice(cmd,dice)
    if arr[y][x] == 0:
        arr[y][x] = dice[5]
    else:
        dice[5] = arr[y][x]
        arr[y][x] = 0
    print(dice[0])
