T= int(input())

for i in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    h= h1+h2
    m= m1+m2
    
    if m >= 60:
        h +=1
        m -=60
    
    while h > 12 :
        h -= 12

    print(f'#{i} {h} {m}')