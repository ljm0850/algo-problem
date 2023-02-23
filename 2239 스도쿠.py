# pypy만 정답
# python3로 시간 내에 맞추려면 findNums를 제거하고 전체 r,c의 상황을 파악해둔 global 변수 선언하는 형식 필요
def fillBlank(idx:int)->None:
    if len(blank) == idx:
        for r in range(9):
            for c in range(9):
                print(arr[r][c],end='')
            print()
        exit()
    r,c = blank[idx]
    nums = findNums(r,c)
    for num in nums:
        arr[r][c] = num
        fillBlank(idx+1)
        arr[r][c] = 0

def findNums(r:int,c:int)->list:
    check = [False]*10
    for i in range(9):
        check[arr[r][i]] = True
        check[arr[i][c]] = True
    R,C = r//3,c//3
    for dr in range(3):
        nr = 3*R + dr
        for dc in range(3):
            nc = 3*C + dc
            check[arr[nr][nc]] = True
    value = []
    for i in range(1,10):
        if check[i] == False:
            value.append(i)
    return value

arr = [list(map(int,input())) for _ in range(9)]
blank = []
for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            blank.append((r,c))
fillBlank(0)