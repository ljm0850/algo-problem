N = int(input())

for i in range(N)[::-1]:
    ans = ' '*(N-i-1) + '*' * (2*i+1)
    print(ans)
for i in range(1,N):
    ans = ' '*(N-i-1) + '*' * (2*i+1)
    print(ans)