import sys,copy
from collections import deque
def solve(target:list)->int:
    que = deque()
    que.append(target)
    cnt,ans = 0,0
    while cnt < 5:
        cnt += 1
        for _ in range(len(que)):
            original_arr = que.popleft()
            for way in range(4):
                arr = copy.deepcopy(original_arr)
                move(way,arr)
                if arr != original_arr:
                    que.append(arr)
    for nocs in que:
        for noc in nocs:
            ans = max(ans,max(noc))
    if N == 1:
        ans = target[0][0]
    return ans

def move(way:int,arr:list)->list:
    # 진행방향 조절
    row,column = default,default
    if way == 0:
        row = row[::-1]
    elif way == 2:
        column = column[::-1]
    # 결합
    for r in row:
        for c in column:
            # 진행방향과 반대되는 nr,nc
            nr, nc = r - dr[way], c - dc[way]
            if arr[r][c] == 0:
                continue
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == arr[r][c]:
                    arr[r][c] *= 2
                    arr[nr][nc] = 0
                    break
                elif arr[nr][nc] == 0:
                    nr,nc = nr-dr[way],nc-dc[way]
                    continue
                break
    # 결합이후 이동방향으로 이동 할 수 있으면 이동
    for r in row:
        for c in column:
            nr,nc = r + dr[way], c + dc[way]
            value = arr[r][c]
            if value == 0:
                continue
            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc]==0:
                    nr,nc = nr+dr[way],nc+dc[way]
            arr[r][c] = 0
            arr[nr-dr[way]][nc-dc[way]] = value
    return arr

dr = (1,-1,0,0)
dc = (0,0,1,-1)
N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
default = [num for num in range(N)]
answer = solve(arr)
print(answer)