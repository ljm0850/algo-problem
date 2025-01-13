import math
def solution(T:int,ls:list[str])->bool:
    def transPosition(position:str)->tuple[int]:
        return (ord(position[0])-65,int(position[1])-1)

    def check(r1:int,c1:int,r2:int,c2:int)->bool:
        if abs(r1-r2)>=3 or abs(c1-c2)>=3: return False
        gap = abs(r1-r2) + abs(c1-c2)
        if gap != 3: return False
        return True
    size = int(math.sqrt(T))
    visit = [[0] * size for _ in range(size)]
    sr,sc = transPosition(ls[0])
    br,bc = sr,sc
    visit[br][bc] = 1
    for i in range(1,T):
        position = ls[i]
        r,c = transPosition(position)
        if visit[r][c] or not check(br,bc,r,c): return False
        visit[r][c] = 1
        br,bc = r,c
    if not check(sr,sc,br,bc): return False
    return True

turn = 36
ls = [input() for _ in range(turn)]
ans = solution(turn,ls)
if ans:print("Valid")
else: print("Invalid")