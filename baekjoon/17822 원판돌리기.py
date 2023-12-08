# N개의 원판, 50이하
# 원판당 M 개의 수, 50이하
# T번(1000 이하) 스핀, 번호가 x의 배수인 판을 d방향(0일 경우 시계, 1일 경우 반시계)으로 k칸 회전
# 회전마다 arr 갱신 시 1000번 * 50개의 원판 * 50개의 수 = 2,500,000

def spin(arr:list[list[int]],R:int,C:int,x:int,d:int,k:int)->int:
    dir = 1 - 2*d
    for idx in range(x-1,R,x):  # idx 원판 회전
        vecter = M-(M+dir*k)%M
        arr[idx] = arr[idx][vecter:] + arr[idx][:vecter]
    return remove_num(arr,R,C)
    
def remove_num(arr:list[list[int]],R:int,C:int)->int:
    flag = True
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 0:
                continue
            nums_position = dfs(arr,r,c,R,C)
            if len(nums_position) == 1:
                continue
            flag = False
            for rr,rc in nums_position:
                arr[rr][rc] = 0
    if flag:
        return balance(arr,R,C)
    return 0

def balance(arr:list[list],R:int,C:int)->int:
    total,cnt = 0,0
    temp = list()
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 0:
                continue
            total += arr[r][c]
            cnt += 1
            temp.append((r,c))
    if total == 0:
        return 1
    aver = total / cnt
    for r,c in temp:
        if arr[r][c] > aver:
            arr[r][c] -= 1
        elif arr[r][c] < aver:
            arr[r][c] += 1
    return 0



def dfs(arr,sr,sc,R,C):
    dr,dc = (1,-1,0,0),(0,0,1,-1)
    check = set()
    check.add((sr,sc))
    value = arr[sr][sc]
    ls = [(sr,sc)]
    while ls:
        r,c = ls.pop()
        for d in range(4):
            nr,nc = r+dr[d],(c+dc[d])%C
            if 0<=nr<R and arr[nr][nc] == value and not (nr,nc) in check:
                check.add((nr,nc))
                ls.append((nr,nc))
    return check

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for _ in range(T):
    x,d,k = map(int,input().split())
    flag = spin(arr,N,M,x,d,k)
    if flag:
        break
ans = 0
for ls in arr:
    ans += sum(ls)
print(ans)