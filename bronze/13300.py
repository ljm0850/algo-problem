N,K = map(int,input().split())
member = [[0]*2 for _ in range(6)]      #학년별,성별로 나눔
for _ in range(N):
    S,Y = map(int,input().split())
    member[Y-1][S] += 1
room=0
for y in range(6):
    for s in range(2):
        room += member[y][s]//K
        if member[y][s] % K != 0:
            room +=1
print(room)