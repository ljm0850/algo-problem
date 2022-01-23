T=int(input())

for i in range(T):
    a,b = map(int,input().split())
    
    # c = a**b % 10
    # print(c)
    
    a %= 10
    if a in (1,5,6) :
        print(a)
    
    #2 4 8 6
    elif a == 2 :
        if b % 4 == 0:
            print(6)
        elif b % 4 == 1:
            print(2)
        elif b % 4 == 2:
            print(4)
        else :
            print(8)
    #3 9 7 1
    elif a == 3:
        if b % 4 == 0:
            print(1)
        elif b % 4 == 1:
            print(3)
        elif b % 4 == 2:
            print(9)
        else :
            print(7)
    #4 6
    elif a == 4:
        if b % 2 == 0:
            print(6)
        else:
            print(4)
    # 7 9 3 1
    elif a == 7:
        if b % 4 == 0:
            print(1)
        elif b % 4 ==1:
            print(7)
        elif b % 4 ==2:
            print(9)
        else :
            print(3)
    # 8 4 2 6
    elif a ==8:
        if b % 4 == 0:
            print(6)
        elif b%4 == 1:
            print(8)
        elif b%4 == 2:
            print(4)
        else:
            print(2)
    else:
        if b % 2 == 0:
            print(1)
        else :
            print(9)