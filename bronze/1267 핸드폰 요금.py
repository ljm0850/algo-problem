def Type_Y():
    total = 0
    for data in calling_data:
        total += (data//30)*10
        if data - (data//30)*30 >=0 :
            total += 10
    return total

def Type_M():
    total = 0
    for data in calling_data:
        total += (data//60)*15
        if data -(data//60)*60 >=0 :
            total += 15
    return total

N = int(input())
calling_data = list(map(int,input().split()))

Y = Type_Y()
M = Type_M()

if M > Y:
    print('Y',Y)
elif Y > M:
    print('M',M)
else:
    print('Y','M',Y)