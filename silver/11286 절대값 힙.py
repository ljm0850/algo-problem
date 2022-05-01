import heapq
import sys
def heap(num):
    global sol
    if num:
        heapq.heappush(sol,(abs(num),num))
    else:
        if sol:
            print(heapq.heappop(sol)[1])
        else:
            print(0)

N = int(input())
sol = []
for _ in range(N):
    heap(int(sys.stdin.readline()))