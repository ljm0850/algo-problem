# N * N 배열 (3<= N <=20) => 최대 400명의 학생
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다. => 좋아 하는 학생이 어디에 앉았는지 확인하는 변수(check) 필요, 이를 체크하기 위한 N*N 임시 배열?
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다. => 주변이 얼마나 비어있는지 기록해둔 배열 필요
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

def empty_arr(N:int)->list[list[int]]:
    empty = [[4]*N for _ in range(N)]
    for i in range(N):
        empty[i][0] -= 1
        empty[i][N-1] -= 1
        empty[0][i] -= 1
        empty[N-1][i] -= 1
    return empty

def check_friends_position(N:int,friends:list[int])->list[tuple[int]]:
    temp = [[0]*(N) for _ in range(N)]
    # 좋아하는 학생 근처 체크
    for friend in friends:
        if not check[friend]:
            continue
        r,c = check[friend]
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if 0<=nr<N and 0<=nc<N:
                temp[nr][nc] += 1
    # 좋아하는 학생 몇칸인지 확인
    total = list()
    value = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                continue

            if temp[r][c] > value:
                total.clear()
                total.append((r,c))
                value = temp[r][c]
            elif temp[r][c] == value:
                total.append((r,c))
    return total

def fix_empty(N:int,r:int,c:int,arr:list[list])->None:
    for d in range(4):
        nr,nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<N:
            arr[nr][nc] -= 1

def check_empty(total:list[tuple[int]],empty:list[list[int]])->list[tuple[int]]:
    value = 0
    temp = list()
    for r,c in total:
        if empty[r][c] > value:
            temp.clear()
            temp.append((r,c))
            value = empty[r][c]
        elif empty[r][c] == value:
            temp.append((r,c))
    return temp

def counting_point(N:int,arr:list[list[int]],friends_arr:list[set[int]])->int:
    total = 0
    for r in range(N):
        for c in range(N):
            cnt = 0
            me = arr[r][c]
            for d in range(4):
                nr,nc = r+dr[d],c+dc[d]
                if 0<=nr<N and 0<=nc<N and arr[nr][nc] in friends_arr[me]:
                    cnt += 1
            if cnt != 0:
                total += 10**(cnt-1)
    return total

N = int(input())
n = N*N
arr = [[0]*N for _ in range(N)]
check = [()]*(n+1)
dr,dc = (1,-1,0,0),(0,0,1,-1)
empty = empty_arr(N)
friends_arr = [set() for _ in range(n+1)]
for _ in range(n):
    me,*friends = list(map(int,input().split()))
    friends_arr[me] = set(friends)
    total = check_friends_position(N,friends)
    if len(total) == 1:
        r,c = total.pop()
        check[me] = (r,c)
        arr[r][c] = me
        fix_empty(N,r,c,empty)
        continue
    # 빈칸 확인
    total = check_empty(total,empty)
    r,c = total[0]
    check[me] = (r,c)
    arr[r][c] = me
    fix_empty(N,r,c,empty)
ans = counting_point(N,arr,friends_arr)
print(ans)