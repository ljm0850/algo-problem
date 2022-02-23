import sys
sys.stdin=open('input.txt')

def check(ls,num):          # 0 - 5 , 1-3, 2-4 맞은편 숫자 찾기
    a=ls.index(num)
    if a ==0:
        return ls[5]
    elif a==5:
        return ls[0]
    elif a==1:
        return ls[3]
    elif a==3:
        return ls[1]
    elif a==2:
        return ls[4]
    else:
        return ls[2]

n=int(input())
dice_ls=[list(map(int,input().split())) for _ in range(n)]
max_total = 0
for i in range(1,7):            #첫 주사위의 바닥눈
    a = i
    total = 0
    for dice in dice_ls:
        top = check(dice,a)
        if (top != 6) and (a != 6):
            total +=6
        elif (top != 5) and (a !=5):
            total +=5
        else:
            total +=4
        a = top
    if max_total < total:
        max_total = total
print(max_total)

