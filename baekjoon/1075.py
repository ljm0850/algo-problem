N=int(input())
F=int(input())

n=(N//100)*100
if F-n%F == 100:
    print('00')
elif n%F == 0:
    print('00')
elif F-n%F <10:
    print(0,end='')
    print(F-n%F)
else:
    print(F-n%F)