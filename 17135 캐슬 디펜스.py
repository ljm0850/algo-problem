# enemy를 set으로 하지 말고 r를 기준으로 2중 배열로 사용 했으면[[r == 0인 값들], [r==1인 값들]] length 구할때 break 하기도 쉽고, 34번째 줄도 쉬웠을듯
from copy import deepcopy
def position(M:int,s:int,cnt:int,army:list[int]):
    if cnt == 0:
        fire(army)
        return
    for i in range(s,M):
        position(M,i+1,cnt-1,army+[i])

def fire(army:list[int]):
    global ans
    Target = deepcopy(enemy)
    cnt = 0
    value = 0
    while Target:
        Temp = set()
        for soldier in army:
            T_r,T_c,T_l = 0,0,INF
            for r,c in Target:
                length = abs(soldier-c) + r - cnt + 1
                if length <= D:
                    if T_l > length:
                        T_r,T_c,T_l = r,c,length
                    elif T_l == length and T_c > c:
                        T_r, T_c, T_l = r, c, length

            if T_l != INF:
                Temp.add((T_r,T_c))
        for r,c in Temp:
            Target.remove((r,c))
            value += 1
        cnt += 1
        Temp = set()
        for r,c in Target:
            if r - cnt < 0:
                Temp.add((r,c))
        for r,c in Temp:
            Target.remove((r,c))
    ans = max(ans,value)

N,M,D = map(int,input().split())
INF = N+M+1
enemy = set()
for r in range(N)[::-1]:
    T = input().split()
    for c in range(M):
        if T[c] == '1':
            enemy.add((r,c))
ans = 0
position(M,0,3,[])
print(ans)