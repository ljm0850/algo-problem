N= int(input())
for tc in range(N):
    an,*als = map(int,input().split())
    bn,*bls = map(int,input().split())
    count_a=[0]*5
    count_b=[0]*5
    for a in als:
        count_a[a] += 1
    for b in bls:
        count_b[b] += 1
    for i in range(4,0,-1):
        if count_a[i] > count_b[i]:
            print('A')
            break
        elif count_a[i] < count_b[i]:
            print('B')
            break
    else:
        print('D')