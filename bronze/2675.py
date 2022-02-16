T= int(input())

for tc in range(1,T+1):
    n,target= input().split()
    for i in target:
        print(i*int(n),end='')
    print('')