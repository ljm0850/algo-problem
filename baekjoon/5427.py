from collections import deque
def find_position(row: int, col: int, arr: list[list[str]])->tuple[deque, deque]:
    fire = deque()
    me = deque()
    for r in range(row):
        for c in range(col):
            if arr[r][c] == '*':
                fire.append((r,c))
            elif arr[r][c] == '@':
                me.append((r,c))
    return me,fire

def inrange(r,c,R,C):
    if 0<=r<R and 0<=c<C:
        return True
    return False

def solution(R,C,arr):
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    me,fire = find_position(R,C,arr)
    cnt = 0
    check = [[False]*C for _ in range(R)]
    check[me[0][0]][me[0][1]] = True
    while me:
        cnt += 1
        for _ in range(len(fire)):
            r,c = fire.popleft()
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if inrange(nr,nc,R,C) and arr[nr][nc] != '*' and arr[nr][nc] != '#':
                    arr[nr][nc] = '*'
                    fire.append((nr,nc))
        for _ in range(len(me)):
            r,c = me.popleft()
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if not inrange(nr,nc,R,C):
                    return cnt
                if check[nr][nc] == True:
                    continue
                if arr[nr][nc] == '.':
                    me.append((nr,nc))
                    check[nr][nc] = True
    return -1

if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        w,h = map(int,input().split())
        arr = [list(input().strip()) for _ in range(h)]
        ans = solution(h,w,arr)
        if ans == -1: print("IMPOSSIBLE")
        else: print(ans)