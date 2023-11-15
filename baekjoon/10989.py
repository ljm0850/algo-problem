import sys
N = int(sys.stdin.readline())
solve = [0]*(10001)
for a in range(N):
    solve[int(sys.stdin.readline())] += 1
for a in range(10001):
    if solve[a] != 0:
        for b in range(solve[a]):
            print(a)