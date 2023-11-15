T = int(input())
for tc in range(1,T+1):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    length = (x1-x2)**2 + (y1-y2)**2
    length2 = (r1+r2)**2
    length3 = (r1-r2)**2
    if length == 0 and r1 == r2:
        print(-1)
    elif length == 0 and r1 != r2:
        print(0)
    elif length < length2 and length3<length:
        print(2)
    elif length == length2 or length == length3:
        print(1)
    else:
        print(0)
