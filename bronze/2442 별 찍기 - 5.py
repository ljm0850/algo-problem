N = int(input())

for i in range(N)[::-1]:
    ans = ' '*i + '*'*(2*N-1-2*i)
    print(ans)