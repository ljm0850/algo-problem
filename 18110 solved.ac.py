import sys
input = sys.stdin.readline
def custom_round(n:float)->int:
    N = int(n)
    if n - N >= 0.5:
        return N + 1
    return N
n = int(input())
d = custom_round(n*15/100)
points = [int(input()) for _ in range(n)]
points.sort()
if n != 2*d:
    total = sum(points[d:n-d])
    print(custom_round(total/(n-2*d)))
else:
    print(0)