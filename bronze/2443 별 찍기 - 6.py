N = int(input())

for i in range(N):
    ans = ' '*i + '*'*(2*(N-i)-1)
    print(ans)