def solve(n):
    print('*'*n)
    if n == N:
        return
    solve(n+1)
    print('*'*n)

N = int(input())

solve(1)