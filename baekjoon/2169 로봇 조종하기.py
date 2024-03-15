import sys
input = sys.stdin.readline
def solution(R,C,arr):
    for c in range(1,C):    # 첫째줄 처리
        arr[0][c] += arr[0][c-1]
    for r in range(1,R):
        leftMovingArr = arr[r][:]
        rightMovingArr = arr[r][:]
        leftMovingArr[0] += arr[r-1][0]
        for c in range(1,C):
            leftMovingArr[c] += max(arr[r-1][c],leftMovingArr[c-1])
        rightMovingArr[-1] += arr[r-1][-1]
        for c in range(C-2,-1,-1):
            rightMovingArr[c] += max(arr[r-1][c],rightMovingArr[c+1])
        for c in range(C):
            arr[r][c] = max(leftMovingArr[c],rightMovingArr[c])
    return arr[R-1][C-1]

R,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
ans = solution(R,C,arr)
print(ans)