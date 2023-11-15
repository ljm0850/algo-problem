import sys,heapq
input = sys.stdin.readline
N = int(input())
ans = []
for _ in range(N):
    temp = -float(input())
    if len(ans) <7:
        heapq.heappush(ans,temp)
        continue
    else:
        if ans[0] < temp:
            heapq.heappop(ans)
            heapq.heappush(ans,temp)
ans.sort(reverse=True)
for num in ans:
    print(f'{-num:.3f}')