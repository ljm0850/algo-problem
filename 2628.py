X,Y =map(int,input().split())
N = int(input())
xls=[0,X] #시작점과 끝점 추가
yls=[0,Y]

for i in range(N):
    a,b=map(int,input().split())
    if a == 0:
        yls.append(b)
    else:
        xls.append(b)

#버블정렬
for i in range(len(xls))[::-1]:
    for j in range(i):
        if xls[j] > xls[j+1]:
            xls[j],xls[j+1] = xls[j+1],xls[j]
for i in range(len(yls))[::-1]:
    for j in range(i):
        if yls[j] > yls[j+1]:
            yls[j],yls[j+1] = yls[j+1],yls[j]
max_x=0
max_y=0
#최대 간격 구하기
for i in range(len(xls)-1):
    if (xls[i+1] - xls[i])>max_x:
        max_x=(xls[i+1] - xls[i])
for j in range(len(yls)-1):
    if (yls[j+1]-yls[j]) > max_y:
        max_y=(yls[j+1]-yls[j])
print(max_x*max_y)