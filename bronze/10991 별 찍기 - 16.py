N = int(input())

for i in range(1,N+1):
    ans = ' '*(N-i) + ('*' + ' ' )*i
    print(ans)