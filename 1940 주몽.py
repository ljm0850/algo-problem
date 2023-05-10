import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
materials = list(map(int,input().split()))
materials.sort()
s,e = 0,N-1
ans = 0
while s < e:
    T = materials[s] + materials[e]
    if T == M:
       ans +=1
       s += 1
       e -= 1
    elif T > M:
        e -= 1
    else:
        s += 1
print(ans)