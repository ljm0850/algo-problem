K,N = map(int,input().split())          # K: 가지고 있는 랜선의 개수 10,000 이하, N: 필요한 랜선의 개수 1,000,000 이하
length=[]
length = [int(input()) for _ in range(K)]
s = 1
e = length[0]
for i in length:
    if i > e:
        e = i
while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for i in length:
        cnt += i // mid
    if cnt >=N:
        s = mid +1
    else:
        e = mid -1
print(e)