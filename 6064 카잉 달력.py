def check(M,N,x,y):
    while x<= M*N:
        if (x-y)%N == 0:
            return x
        x += M
    return -1

T = int(input())
for tc in range(1,T+1):
    M,N,x,y = map(int, input().split())
    print(check(M,N,x,y))