T= int(input())

for i in range(1,T+1):
    texts = input().strip()

    if texts == texts[::-1] :
        print(f'#{i} 1')
    else :
        print(f'#{i} 0')