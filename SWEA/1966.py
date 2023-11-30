T= int(input())

for i in range(1,T+1):
    N = int(input())
    target = list(map(int,input().split()))
    
    for j in reversed(range(N)):
        for k in range(j):
            if target[k] > target[k+1]:
                target[k],target[k+1] = target[k+1],target[k]
    print(f'#{i}',end=' ')
    print(*target)

