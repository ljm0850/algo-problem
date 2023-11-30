T= int(input())
credits=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in range(1,T+1):
    N,K =input().split()
    n= int(N)
    k= int(K)
    point = []
    for j in range(n):
        a,b,c = map(int,input().split())
        point.append(0.35*a + 0.45*b + 0.2*c)
    point2 = sorted(point)[::-1]

    grade = point2.index(point[k-1])+1

    # if grade <= 1*(n/10):
    #     print(f'#{i} {credits[0]}')

    # elif grade <= 2*(n/10):
    #     print(f'#{i} {credits[1]}')

    # elif grade <= 3*(n/10):
    #     print(f'#{i} {credits[2]}')
    # elif grade <= 4*(n/10):
    #     print(f'#{i} {credits[3]}')
    # elif grade <= 5*(n/10):
    #     print(f'#{i} {credits[4]}')
    # elif grade <= 6*(n/10):
    #     print(f'#{i} {credits[5]}')
    # elif grade <= 7*(n/10):
    #     print(f'#{i} {credits[6]}')
    # elif grade <= 8*(n/10):
    #     print(f'#{i} {credits[7]}')
    # elif grade <= 9*(n/10):
    #     print(f'#{i} {credits[8]}')
    # else :
    #     print(f'#{i} {credits[9]}')
    for k in range(1,10):
        if grade*10/n <= k :
            print(f'#{i} {credits[k-1]}')
            break