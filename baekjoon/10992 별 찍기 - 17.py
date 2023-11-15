def solve(n):
    for i in range(1,n+1):
        if i == 1:
            print(' '*(n-1)+'*')
        elif i == n:
            print('*'*(2*i-1))
        else:
            print(' '*(n-i)+'*' + ' '*(2*i-3)+'*')

N = int(input())
solve(N)