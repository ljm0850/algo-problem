import sys
input = sys.stdin.readline
N,L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
ls = []

for r in range(N):
    check = [False]*(N+1)
    ls.append((0,arr[r][0]))
    while ls:
        c,h = ls.pop()
        nc = c + 1
        if nc==N:
            ans += 1
            break
        gap = h-arr[r][nc]
        if gap == 0:
            ls.append((nc,h))
        elif gap == 1:
            if c+L >= N:
                break
            for l in range(1,L+1):
                if arr[r][c+l] == arr[r][nc] and not check[c+l]:
                    check[c+l] = True
                else:
                    break
            else:
                ls.append((nc,arr[r][nc]))
        elif gap == -1:
            if nc-L <0:
                break
            for l in range(1,L+1):
                if arr[r][c] == arr[r][nc-l] and not check[nc-l]:
                    check[nc-l] = True
                else:
                    break
            else:
                ls.append((nc,arr[r][nc]))

for c in range(N):
    ls.append((0,arr[0][c]))
    check = [False]*(N+1)
    while ls:
        r,h = ls.pop()
        nr = r + 1
        if nr == N:
            ans += 1
            break
        gap = h-arr[nr][c]
        if gap == 0:
            ls.append((nr,h))
        elif gap == 1:
            if r + L >= N:
                break
            for l in range(1,L+1):
                if arr[nr][c] == arr[r+l][c] and not check[r+l]:
                    check[r+l] = True
                else:
                    break
            else:
                ls.append((nr,arr[nr][c]))
        elif gap == -1:
            if nr - L < 0:
                continue
            for l in range(1,L+1):
                if arr[r][c] == arr[nr-l][c] and not check[nr-l]:
                    check[nr-l] = True
                else:
                    break
            else:
                ls.append((nr,arr[nr][c]))
print(ans)