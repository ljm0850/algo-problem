N,K = map(int,input().split())
coin = [int(input()) for _ in range(N)]
cnt = 0
for i in coin[::-1]:
    if K // i :
        cnt += K//i
        K -= K//i*i
    if not K:
        break
print(cnt)