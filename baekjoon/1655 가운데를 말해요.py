import sys,heapq
input = sys.stdin.readline

N = int(input())
maximum_heap = []
minimum_heap = []

a = int(input())
maximum_heap.append(-a)
print(a)
if N > 1:
    b = int(input())
    if a < b:
        heapq.heappush(minimum_heap,b)
    else:
        a = -heapq.heappop(maximum_heap)
        heapq.heappush(maximum_heap, -b)
        heapq.heappush(minimum_heap, a)
    print(-maximum_heap[0])

for _ in range(N-2):
    num = int(input())
    if len(maximum_heap) == len(minimum_heap):
        heapq.heappush(maximum_heap,-num)
    else:
        heapq.heappush(minimum_heap,num)

    if -maximum_heap[0] > minimum_heap[0]:
        a = -heapq.heappop(maximum_heap)
        b = heapq.heappop(minimum_heap)
        heapq.heappush(maximum_heap,-b)
        heapq.heappush(minimum_heap,a)
    print(-maximum_heap[0])