Y = int(input())

if Y % 400 == 0 :
    print(1)
elif (Y % 4 ==0) and (Y % 100 !=0) :
    print(1)
else:
    print(0)