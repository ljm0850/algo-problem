def findNum(r:int,c:int)->list:
    check = [False]*10
    # 가로 & 세로
    for i in range(9):
        check[arr[i][c]] = True
        check[arr[r][i]] = True
    # 3*3
    R,C = r//3,c//3
    for dr in range(3):
        nr = 3*R+dr
        for dc in range(3):
            nc = 3*C+dc
            check[arr[nr][nc]] = True
    value = []
    for i in range(1,10):
        if not check[i]:
            value.append(i)
    return value

def solution(idx:int)->None:
    if len(blank) == idx:
        for i in range(9):
            print(*arr[i])
        exit()
    r,c = blank[idx]
    nums = findNum(r,c)
    for num in nums:
        arr[r][c] = num
        solution(idx+1)
        arr[r][c] = 0

arr = [list(map(int,input().split())) for _ in range(9)]
blank = []
for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            blank.append((r,c))
solution(0)