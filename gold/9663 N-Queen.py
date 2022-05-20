def is_ok(n):
    for i in range(n):
        if chess[n] == chess[i] or abs(chess[n]-chess[i]) == abs(n-i):
            return False
    return True

def solve(n):
    global ans
    if n == N:
        ans += 1
        return
    for i in range(N):
        chess[n] = i
        if is_ok(n):
            solve(n+1)

N = int(input())
chess = [-1]*N
ans = 0
solve(0)
print(ans)