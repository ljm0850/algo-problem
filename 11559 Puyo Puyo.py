from heapq import heappush,heappop
def solution(arr:list[list[str]])->int:
    # 최초 전체 탐색
    ls = []
    ck = set()
    for r in range(R):
        for c in range(C):
            if arr[r][c] != '.' and not (r,c) in ck:
                temp = dfs(r,c)
                ck.update(temp)
                if len(temp) >= 4:
                    for p in temp:
                        heappush(ls,p)
    value = 0
    while ls:
        value += 1
        search = set()
        ck.clear()
        # 폭파
        while ls:
            r,c = heappop(ls)
            search.add(c)
            for nr in range(1,r+1)[::-1]:
                arr[nr][c] = arr[nr-1][c]
            arr[0][c] = '.'
        # 재탐색
        for r in range(R):
            for c in search:
                if arr[r][c] != '.' and not (r,c) in ck:
                    temp = dfs(r,c)
                    ck.update(temp)
                    if len(temp) >= 4:
                        for p in temp:
                            heappush(ls,p)
    return value

def dfs(r:int,c:int)->set:
    color = arr[r][c]
    ls = [(r,c)]
    check = set()
    check.add((r,c))
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<R and 0<=nc<C and not (nr,nc) in check and arr[nr][nc] == color:
                ls.append((nr,nc))
                check.add((nr,nc))
    return check

R,C = 12,6
dr,dc = (1,0,-1,0),(0,1,0,-1)
arr = []
for _ in range(R):
    t = []
    t.extend(input())
    arr.append(t)
ans = solution(arr)
print(ans)