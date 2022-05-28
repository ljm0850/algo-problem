N = int(input())

for i in range(1,N+1):
    ans = '*'*i + ' '*(2*(N-i)) + '*'*i
    print(ans)
for i in range(1,N)[::-1]:
    ans = '*' * i + ' ' * (2 * (N - i)) + '*' * i
    print(ans)