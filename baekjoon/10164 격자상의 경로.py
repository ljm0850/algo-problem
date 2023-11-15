N,M,K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for r in range(N):
    arr[r][0] = 1
for c in range(M):
    arr[0][c] = 1

def solution(r,c):
    if arr[r][c]:
        return arr[r][c]
    arr[r][c] = solution(r-1,c) + solution(r,c-1)
    return arr[r][c]

if K:
    r,c = (K-1)//M,(K-1)%M
    ans = solution(r,c) * solution(N-r-1,M-c-1)
else:
    ans = solution(r,c)
print(ans)