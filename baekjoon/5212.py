def clearArrRow(R,C,arr,asc):
    range_r = range(R) if asc else range(R-1,-1,-1)
    flag = True
    for r in range_r:
        if flag == False: break
        for c in range(C):
            if arr[r][c] == groundSign:
                flag = False
                break
        else:
            for c in range(C):
                arr[r][c] = ''
def clearArrCol(R,C,arr,asc):
    range_c = range(C) if asc else range(C - 1, -1, -1)
    flag = True
    for c in range_c:
        if flag == False: break
        for r in range(R):
            if arr[r][c] == groundSign:
                flag = False
                break
        else:
            for r in range(R):
                arr[r][c] = ''

def solution(R,C,arr,groundSign,seaSign):
    ls = list()
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    for r in range(R):
        for c in range(C):
            if arr[r][c] == seaSign:continue
            cnt = 0
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if not (0<=nr<R and 0<=nc<C) or arr[nr][nc] == seaSign:
                    cnt += 1
            if cnt >= 3: ls.append((r,c))
    while ls:
        r,c = ls.pop()
        arr[r][c] = seaSign
    clearArrCol(R,C,arr,True)
    clearArrCol(R,C,arr,False)
    clearArrRow(R,C,arr,True)
    clearArrRow(R,C,arr,False)
    return arr

R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
groundSign = 'X'
seaSign = '.'
ans = solution(R,C,arr,groundSign,seaSign)
I = len(ans)
for i in range(I):
    value = ''.join(ans[i])
    if value: print(value)