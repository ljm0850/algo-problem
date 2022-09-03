def solve(start_r:int,start_c:int,start_alpha:str)->int:
    cnt = 1
    ps_set = set([(start_r,start_c,start_alpha)])
    while ps_set:
        r,c,path = ps_set.pop()
        for way in range(4):
            nr,nc = r+dr[way],c+dc[way]
            if 0<=nr<R and 0<=nc<C:
                alpha = board[nr][nc]
                if alpha not in path:
                    ps_set.add((nr,nc,path+alpha))
                    cnt = max(cnt,len(path)+1)
    return cnt
dr,dc = [0,0,1,-1],[1,-1,0,0]
R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]
ans = solve(0,0,board[0][0])
print(ans)