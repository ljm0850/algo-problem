N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
cnt= N
for a in A:
    a -= B
    if a > 0:
        cnt += a//C
        if a % C :
            cnt +=1
print(cnt)
