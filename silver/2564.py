def change1(x,y):               #0,0을 기준으로 남-동-북-서 를 일직선으로
    global N
    global M
    if x == 1:
        a=2*N+M-y
    elif x == 2:
        a=y
    elif x == 3:
        a=2*N+M+y
    else:
        a=N+M-y
    return a

def change2(x,y):               #N-1,M-1을 기준으로 북 서 남 동 을 일직선으로
    global N
    global M
    if x == 1:
        a = N-y
    elif x == 2:
        a = N+M+y
    elif x == 3:
        a = N+y
    else:
        a = 2*(N+M)-y
    return a

N,M = map(int,input().split())          #가로 세로 길이
n = int(input())                    #상점의 개수
store=[]
total=0
for _ in range(n):
    x,y = map(int,input().split())                  #x의 1은 북,2는 남 3은 서 4는 동
    store.append([x,y])
now_x,now_y = map(int,input().split())

for i in store:
    type1 = abs(change1(now_x,now_y)-change1(i[0],i[1]))
    type2 = abs(change2(now_x,now_y)-change2(i[0],i[1]))
    if type1 > type2:
        total += type2
    else:
        total += type1
print(total)