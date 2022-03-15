N,M = map(int,input().split())
set_n = set()
set_m = set()
for _ in range(N):
    set_n.add(input())
for _ in range(M):
    set_m.add(input())
solve = list(set_n & set_m)
solve.sort()

print(len(solve))
for i in solve:
    print(i)