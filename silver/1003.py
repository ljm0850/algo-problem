T = int(input())
for tc in range(1,T+1):
    n = int(input())
    fibo0 = 1
    fibo1 = 0
    temp = 0
    for i in range(n):
        fibo0,fibo1 = fibo1,fibo1+fibo0
    print(fibo0,fibo1)