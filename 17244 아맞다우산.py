import sys
from collections import deque
from itertools import permutations


def find_path(start_point: tuple) -> dict:
    global arr
    value = {}
    que = deque()
    check = [[0]*(N) for _ in range(M)]
    que.append(start_point)
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            r, c = que.popleft()
            for way in range(4):
                nr, nc = r+dr[way], c+dc[way]
                if 0 <= nr < M and 0 <= nc < N and not check[nr][nc] and arr[nr][nc] != '#':
                    check[nr][nc] = 1
                    que.append((nr, nc))
                    if (nr, nc) in obj or (nr, nc) in (start, end):
                        value[(nr, nc)] = cnt
    return value


def solve(start: tuple, end: tuple, obj: set):
    answer = sys.maxsize
    shortcut = {}
    shortcut[start] = find_path(start)
    shortcut[end] = find_path(end)
    for position in obj:
        shortcut[position] = find_path(position)
    total = []
    if obj:
        total = permutations(list(obj), len(obj))

    if total:
        for nodes in total:
            temp = 0
            temp += shortcut[start][nodes[0]]
            temp += shortcut[end][nodes[-1]]
            for idx in range(1, len(nodes)):
                temp += shortcut[nodes[idx-1]][nodes[idx]]
            answer = min(temp, answer)
    else:
        answer = shortcut[start][end]
    return answer


N, M = map(int, sys.stdin.readline().split())
arr = []
obj = set()
for m in range(M):
    row = sys.stdin.readline().strip()
    arr.append(row)
    for n in range(N):
        if row[n] == 'S':
            start = (m, n)
        elif row[n] == 'X':
            obj.add((m, n))
        elif row[n] == 'E':
            end = (m, n)

dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
ans = solve(start, end, obj)
print(ans)
