T= int(input())

for i in range(T):
    target = list(map(int,input().split()))
    if target[0] < target[1] :
        print(f'#{i+1} <')
    elif target[0] == target[1] :
        print(f'#{i+1} =')
    else :
        print(f'#{i+1} >')
