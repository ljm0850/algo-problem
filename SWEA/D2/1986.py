T = int(input())

for i in range(1,T+1):
    N = int(input())
    pl =0
    mi =0
    for j in range(0,N+1,2):
        mi -= j
    for k in range(1,N+1,2):
        pl += k
    
    print(f'#{i} {pl+mi}')