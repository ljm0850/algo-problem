N = int(input())
check = list(map(int,input().split()))
ls = [0]*N
cnt = 0
for i in range(N):
    if ls[i] == check[i]:
        continue
    cnt += 1
    for j in range(3):
        if i+j == N:
            break
        ls[i+j] = (ls[i+j]+1)%2
print(cnt)