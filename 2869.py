A,B,V = map(int,input().split())        #A미터 올라감 B미터 미끄러짐 목표는 V미터
move = A-B
now = B
cnt = (V-A)//move
V -= cnt*move
while now < V:
    now -= B
    now += A
    cnt += 1
print(cnt)