solve = [[0]*100 for _ in range(100)] # x,y축이 0으로 된 리스트 형성(x,y <=100)
#사각형 주어진 영역의 값 1로 변경
for _ in range(4):
    x1,y1,x2,y2= map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            solve[i][j] = 1
#sum
total = 0
for ii in range(100):
    for jj in range(100):
        total+=solve[ii][jj]
print(total)