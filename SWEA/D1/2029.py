T = int(input())

for i in range(T):
    target = list(map(int,input().split()))

    print(f'#{i+1} {target[0]//target[1]} {target[0]%target[1]}')