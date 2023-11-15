import sys
sys.stdin=open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = []
    for _ in range(100):        #ladder 완성
        arr = list(map(int,input().split()))+[0] #x+1 때문에 list 범위를 벗어나서 [0]추가
        ladder.append(arr)
    for i in range(100):        #당첨 지점 찾기
        if ladder[99][i] == 2:
            x=i
    y=99        #현재 y좌표

    while 0 < y :       #사다리 타기
        if (ladder[y][x+1] == 1) and (x<99) : #오른쪽으로 탈수 있으면 오른쪽으로 쭉 이동
            while (ladder[y][x+1] == 1)and x<99:
                x +=1
        elif (ladder[y][x-1] == 1) and (x>0):   #오른쪽 이동이 안되면 왼쪽으로 쭉 이동
            while (ladder[y][x-1] ==1) :
                x -=1
        y -=1
    print(f'#{tc} {x}')
