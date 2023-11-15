def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if size[a] < size[b]:
        par[a] = b
    elif size[a] > size[b]:
        par[b] = a
    else:
        par[a] = b
        size[b] += 1

ans = 0
N,M = map(int,input().split())
par = [i for i in range(N+1)]
size = [0 for i in range(N+1)]
f,*Fact = list(map(int,input().split()))
for i in range(1,f):
    union(Fact[0],Fact[i])
total_party = []
for pp in range(M):
    n,*party = list(map(int,input().split()))
    total_party.append(party)
    for i in range(1,n):
        union(party[0],party[i])
t = 0
if Fact:
    t = find(Fact[0])
for sol in total_party:
    for s in sol:
        if t == find(s):
            break
    else:
        ans += 1
print(ans)
