def find_nw(nr:int,nc:int,w:int)->int:
    if arr[nr][nc] in ('|', '-', '+'):
        return w
    elif arr[nr][nc] == '1':
        if w == 0:
            return 3
        else:
            return 1
    elif arr[nr][nc] == '2':
        if w == 1:
            return 3
        else:
            return 0
    elif arr[nr][nc] == '3':
        if w == 1:
            return 2
        else:
            return 0
    elif arr[nr][nc] == '4':
        if w == 0:
            return 2
        else:
            return 1
    return -1

def find_block(r:int,c:int,nr:int,nc:int,arr:list)->str:
    temp = []
    for way in range(4):
        nnr,nnc = nr+dr[way], nc+dc[way]
        if 0<=nnr<R and 0<=nnc<C and not (r == nnr and c == nnc) and arr[nnr][nnc] != ".":
            block = arr[nnr][nnc]
            if block =='|':
                # 빈 블럭의 위치가 nnr보다 높다면
                if nr < nnr:
                    if r < nr:
                        temp.append('|')
                    elif c < nnc:
                        temp.append('4')
                    elif c > nnc:
                        temp.append('1')
                # 빈 블럭의 위치가 nnr보다 낮다면
                elif nr > nnr:
                    if r > nr:
                        temp.append('|')
                    # 왼쪽에서 왔네?
                    elif c < nnc:
                        temp.append('3')
                    elif c > nnc:
                        temp.append('2')
            elif block  == '-':
                # 빈 블럭의 column이 왼쪽
                if nc < nnc:
                    if c < nc:
                        temp.append('-')
                    # 밑에서 왔네?
                    elif r > nr:
                        temp.append('1')
                    elif r < nr:
                        temp.append('2')
                # 빈 블럭의 column이 오른쪽
                elif nc > nnc:
                    if c > nc:
                        temp.append('-')
                    elif r > nr:
                        temp.append('4')
                    elif r < nr:
                        temp.append('3')
            elif block == '+':
                # 빈 블록이 왼쪽
                if nc < nnc:
                    if c < nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('2')
                    elif r > nr:
                        temp.append('1')
                # 빈 블록이 오른쪽
                elif nc > nnc:
                    if c > nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('3')
                    elif r > nr:
                        temp.append('4')
                # 빈 블록이 위쪽
                elif nr < nnr:
                    if r < nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('4')
                    elif c > nc:
                        temp.append('1')
                # 빈 블록이 아래쪽
                elif nr > nnr:
                    if r > nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('3')
                    elif c > nc:
                        temp.append('2')
            elif block == '1':
                # 아래서 왔네
                if nr > nnr and nc == nnc:
                    if r > nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('3')
                    elif c > nc:
                        temp.append('2')
                # 오른쪽에서 왔네
                elif nr == nnr and nc > nnc:
                    if c > nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('3')
                    elif r > nr:
                        temp.append('4')
            elif block == '2':
                # 위에서 왔네
                if nr < nnr and nc == nnc:
                    if r < nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('4')
                    elif c > nc:
                        temp.append('1')
                # 오른쪽에서 왔네
                elif nr == nnr and nc > nnc:
                    if c > nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('3')
                    elif r > nr:
                        temp.append('4')
            elif block == '3':
                # 위에서 왔네
                if nr < nnr and nc == nnc:
                    if r < nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('4')
                    elif c > nc:
                        temp.append('1')
                # 왼쪽에서 왔네
                elif nr == nnc and nc < nnc:
                    if c < nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('2')
                    elif r > nr:
                        temp.append('1')
            elif block == '4':
                # 아래쪽에서 왔네
                if nr > nnr and nc == nnc:
                    if r > nr:
                        temp.append('|')
                    elif c < nc:
                        temp.append('3')
                    elif c > nc:
                        temp.append('2')
                # 왼쪽에서 왔네
                elif nr == nnr and nc < nnc:
                    if c < nc:
                        temp.append('-')
                    elif r < nr:
                        temp.append('2')
                    elif r > nr:
                        temp.append('1')
    if len(temp) == 1:
        return temp[0]
    else:
        return '+'

def solve(arr:list,start:tuple)->tuple:
    start_r,start_c = start[0],start[1]
    for way in range(4):
        nr,nc = start_r + dr[way], start_c + dc[way]
        if 0<=nr<R and 0<=nc<C and arr[nr][nc] != ".":
            start_way = way

    stack = [(start_r,start_c,start_way)]
    while stack:
        r,c,w = stack.pop()
        nr,nc = r+dr[w], c+dc[w]
        nw = find_nw(nr,nc,w)
        # 다음길이 막혀 있을 경우
        if nw == -1:
            next_block = find_block(r,c,nr,nc,arr)
            return (nr+1,nc+1,next_block)
        stack.append((nr,nc,nw))

block = [ '|','-','+','1','2','3','4']
dr,dc = (-1,1,0,0),(0,0,-1,1)   # 상하좌우
R,C = map(int,input().split())
arr = []
for r in range(R):
    column = input()
    arr.append(column)
    for c in range(C):
        if column[c] == "M":
            start = (r,c)
        elif column[c] == "Z":
            end = (r,c)
ans = solve(arr,start)
print(*ans)