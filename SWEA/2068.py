T = int(input())

for i in range(T):
    target = map(int,input().split())
    max = 0
    for j in target :
        if j > max :
            max = j
    print(f'#{i+1} {max}')        

