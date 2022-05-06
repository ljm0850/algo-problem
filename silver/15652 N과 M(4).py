def check(string):
    if len(string) == M:
        print(' '.join(string))
        return
    for i in range(1,N+1):
        if string and string[-1] <= str(i):
            check(string+str(i))
        elif not string:
            check(string+str(i))
N,M = map(int,input().split())
check('')