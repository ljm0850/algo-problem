import sys
input = sys.stdin.readline
def solution(R:int,C:int,arr:list[str])->int:
    i = min(R,C)-1
    while i >= 1:
        for r in range(R-i):
            for c in range(C-i):
                if arr[r][c] == arr[r][c+i] == arr[r+i][c] == arr[r+i][c+i]:
                    return (i+1)**2
        i -= 1
    return 1

N,M = map(int,input().split())
arr = [input() for _ in range(N)]
ans = solution(N,M,arr)
print(ans)