from collections import deque

def solution(R,C,arr):
    def areaCheck(r:int, c:int, arr:list[str])->tuple[int]:
        check[r][c] = True
        sheep, wolf = 0, 0
        que = deque()
        que.append((r, c))
        while que:
            r, c = que.popleft()
            match arr[r][c]:
                case 'o': sheep += 1
                case 'v': wolf += 1
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < R and 0 <= nc < C) or check[nr][nc]:
                    continue
                check[nr][nc] = True
                if arr[nr][nc] == '#': continue
                que.append((nr, nc))
        return (sheep,wolf)
    check = [[False] * C for _ in range(R)]
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    aliveSheep, aliveWolf = 0, 0
    # 탈출 가능한 외각 처리
    for r in range(R):
        if check[r][0]:continue
        check[r][0] = True
        if arr[r][0] != '#':
            sheep,wolf = areaCheck(r,0,arr)
            aliveSheep += sheep
            aliveWolf += wolf
    for c in range(C):
        if check[0][c]:continue
        check[0][c] = True
        if arr[0][c] != '#':
            sheep,wolf = areaCheck(0,c,arr)
            aliveSheep += sheep
            aliveWolf += wolf
    # 울타리 내부 확인
    for r in range(R):
        for c in range(C):
            if check[r][c]:continue
            check[r][c] = True
            if arr[r][c] != '#':
                sheep,wolf = areaCheck(r,c,arr)
                if sheep > wolf:
                    aliveSheep += sheep
                else:
                    aliveWolf += wolf
    return aliveSheep,aliveWolf

R,C = map(int,input().split())
arr = [input() for _ in range(R)]
ans = solution(R,C,arr)
print(*ans)