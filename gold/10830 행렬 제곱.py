import sys
def matrix(X,Y):
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] = (ans[i][j]+X[i][k] * Y[k][j])%1000
    return ans

def solve(l):
    if l == 1:
        return A
    temp = solve(l//2)
    if l % 2:
        ans = matrix(matrix(temp,temp),A)
    else:
        ans = matrix(temp,temp)
    return ans

N,B = map(int,input().split())
A = []
for _ in range(N):
    arr = list(map(int,sys.stdin.readline().split()))
    for i in range(N):
        arr[i] %= 1000
    A.append(arr)

answer = solve(B)
for a in answer:
    print(*a)