def turn(ls):
    a = ls[0]
    ls.remove(a)
    ls.append(a)

K=int(input())                                  #1이상 20이하
arr = [[0]*1001 for _ in range(1001)]     #0번=동 1번=서 2번=남 3번=북
n=[]
e=[]
w=[]
s=[]
meter_ls=[]
for _ in range(6):
    way,meter=map(int,input().split())
    meter_ls.append(meter)
    if way == 1:
        e.append(meter)
    elif way == 2:
        w.append(meter)
    elif way == 3:
        s.append(meter)
    else:
        n.append(meter)
#모양에 따라 동,서,남,북이 11/22 로 나뉘어짐, 시작점을 고정하기 위해 turn 이후 계산
if len(n) == 1:
    if len(w) == 1:
        while True:                                                             #ㄱ자형
            if meter_ls[0] == n[0] and meter_ls[1] == w[0]:
                total = meter_ls[0]*meter_ls[1] - meter_ls[3]*meter_ls[4]
                break
            else:
                turn(meter_ls)
    else:
        while True:
            if meter_ls[0] == n[0] and meter_ls[5] == e[0]:
                total = meter_ls[0]*meter_ls[5] - meter_ls[2]*meter_ls[3]
                break
            else:
                turn(meter_ls)
else:
    if len(w) == 1:
        while True:
            if meter_ls[1] == w[0] and meter_ls[2] == s[0]:
                total = meter_ls[1] * meter_ls[2] - meter_ls[4]*meter_ls[5]
                break
            else:
                turn(meter_ls)

    else:                               # ㄴ자형
        while True:
            if meter_ls[4] == s[0] and meter_ls[5] == e[0]:
                total = meter_ls[4]*meter_ls[5] -meter_ls[1]*meter_ls[2]
                break
            else:
                turn(meter_ls)
print(total*K)