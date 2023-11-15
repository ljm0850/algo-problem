N= int(input()) #색종이 개수, 크기는 10*10 고정
arr = [[0]*100 for _ in range(100)] #도화지 100*100고정
cnt = 0 #검은색 영역
for _ in range(N):
    x,y=map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[y+j][x+i] = 1
for i in arr:
    for j in i:
        if j == 1:
            cnt +=1
print(cnt)