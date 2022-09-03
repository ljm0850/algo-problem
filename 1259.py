while True:
    a=input()
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] !=  a[-1-i]:
            print('no')
            break
    else:
        print('yes')