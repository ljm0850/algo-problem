from itertools import permutations
N = int(input())
value = permutations(range(1,N+1),N)
for v in value:
    print(*v)