import sys
input = sys.stdin.readline

N,K,M = map(int,input().split())
K2 = 2*K
Target = []
max_length = 1000000000
for _ in range(N):
    length = int(input())
    if length <= K:
        continue
    elif length < K2:
        length -= K
    else:
        length -= K2
    Target.append(length)
s,e = 1,max_length
v = -1
while s < e:
    m = (s+e) // 2
    cnt = 0
    for l in Target:
        cnt += l // m
    if cnt < M:
        e = m
    else:
        s = m+1
        v = m
print(v)
