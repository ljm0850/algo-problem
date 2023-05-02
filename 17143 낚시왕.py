import sys
input = sys.stdin.readline
def catch_shark(c:int)->int:
    for r in range(R):
        if arr[r][c]:
            size = arr[r][c][2]
            sharks.remove((r,c,arr[r][c][0],arr[r][c][1],arr[r][c][2]))
            arr[r][c] = ()
            return size
    return 0

def nextRC(r:int,c:int,s:int,d:int)->tuple[int,int,int]:
    nc,nr,nd = c,r,d
    if d in D:
        if check.get((d,r,s)):
            nd,nr = check[(d,r,s)]
        else:
            T = R-1
            for _ in range(s):
                nr += dr[nd]
                if nr == 0:
                    nd = 2
                elif nr == T:
                    nd = 1
            check[(d,r,s)] = (nd,nr)
    else:
        if check.get((d,c,s)):
            nd,nc = check[(d,c,s)]
        else:
            T = C - 1
            for _ in range(s):
                nc += dc[nd]
                if nc == 0:
                    nd = 3
                elif nc == T:
                    nd = 4
            check[(d,c,s)] = (nd,nc)
    return nr,nc,nd

def move_shark()->None:
    global sharks
    temp = {}
    for r,c,s,d,z in sharks:
        arr[r][c] = ()
        nr,nc,d = nextRC(r,c,s,d)
        if temp.get((nr,nc)):
            if temp[(nr,nc)][2] < z:
                temp[(nr,nc)] = (s,d,z)
        else:
            temp[(nr,nc)] = (s,d,z)
    sharks = set()
    for P,S in  temp.items():
        sharks.add((P[0],P[1],S[0],S[1],S[2]))
        arr[P[0]][P[1]] = S

R,C,M = map(int,input().split())
arr = [[() for _ in range(C)] for _ in range(R)]
sharks = set()
check = {}
D = set((1,2))
dr,dc = (0,-1,1,0,0),(0,0,0,1,-1)

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    r,c = r-1,c-1
    if d in D:
        if r == 0:
            d = 2
        elif r == R-1:
            d = 1
    else:
        if c == 0:
            d = 3
        elif c == C-1:
            d = 4
    arr[r][c] = (s,d,z)
    sharks.add((r,c,s,d,z))
ans = 0
for fisherman in range(C):
    ans += catch_shark(fisherman)
    move_shark()
print(ans)