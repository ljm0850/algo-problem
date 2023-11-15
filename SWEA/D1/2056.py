T = int(input())

for i in range(T):
 
    target = list(input())

    year = target[0]+target[1]+target[2]+target[3]
    month = target[4]+target[5]
    day = target[6]+target[7]
    
    if (int(target[4]+target[5]) > 13) or (int(target[4]+target[5]) <= 0) :
        print(f'#{i+1} -1')
    elif int(target[4]+target[5]) in [1,3,5,7,8,10,12]:
        if int(target[6]+target[7]) > 31:
            print(f'#{i+1} -1')
        else : print(f'#{i+1} {year}/{month}/{day}')

    elif int(target[4]+target[5]) in [9,11,4,6] :
        if int(target[6]+target[7]) > 30:
            print(f'#{i+1} -1')
        else: print(f'#{i+1} {year}/{month}/{day}')

    elif int(target[4]+target[5]) == 2 :
        if int(target[6]+target[7]) > 28 :
            print(f'#{i+1} -1')
        else : print(f'#{i+1} {year}/{month}/{day}')
    else :
        print(f'#{i+1} -1')
