from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    check = [[0] * C for _ in range(R)]
    check[0][0] = 1
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()
        d = check[r][c] + 1
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] == 1 and check[nr][nc] == 0:
                if nr == R - 1 and nc == C - 1:
                    return d
                check[nr][nc] = d
                q.append((nr, nc))

    return -1