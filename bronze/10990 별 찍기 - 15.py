N = int(input())

for i in range(1,N+1):
    if i == 1:
        ans = ' '*(N-i) + '*'
    else:
        ans = ' '*(N-i) + '*' + ' '*(2*i-3) + '*'
    print(ans)