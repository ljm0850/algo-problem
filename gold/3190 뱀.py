from collections import deque
def solve():
    ans = 0
    go = 0       # 진행 방향 index
    snake = deque()
    snake.append((0,0))
    while True:
        # 방향을 틀어야 할 때
        if spin and spin[0][0] == ans:
            if spin[0][1] == 'D':
                go = (go+1)%4
            elif spin[0][1] == 'L':
                go = (go+3)%4
            spin.popleft()

        r,c = snake[0][0],snake[0][1]           # 머리좌표
        nr,nc = r+way[go][0],c+way[go][1]       # 다음 이동할좌표
        if not 0<=nr<N or not 0<=nc<N or board[nr][nc]==2:
            break
        snake.appendleft((nr,nc))
        if not board[nr][nc] == 1:
            tail_r,tail_c = snake.pop()
            board[tail_r][tail_c] = 0
        board[nr][nc] = 2
        ans += 1
    return ans +1
N = int(input())        # 보드 크기
K = int(input())        # 사과 개수

board = [[0]*N for _ in range(N)]
board[0][0] = 2         # 뱀을 2로 표시
for _ in range(K):
    apple = list(map(int,input().split()))
    board[apple[0]-1][apple[1]-1] = 1           # 사과를 1로 표시
spin = deque()
L = int(input()) # 방향 변환 수
for _ in range(L):
    sec,commend = input().split()
    spin.append((int(sec),commend))

way = [(0,1),(1,0),(0,-1),(-1,0)]
print(solve())