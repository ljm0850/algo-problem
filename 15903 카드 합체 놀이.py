from heapq import heappush,heappop,heapify
def solution(cards:list[int],cnt:int)->int:
    heapify(cards)
    for _ in range(cnt):
        a = heappop(cards)
        b = heappop(cards)
        c = a + b
        for __ in range(2):
            heappush(cards,c)
    return sum(cards)

n,m = map(int,input().split())
cards = list(map(int,input().split()))
ans = solution(cards,m)
print(ans)