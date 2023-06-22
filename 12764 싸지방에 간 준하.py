from heapq import heappush,heappop
from sys import stdin
input = stdin.readline

N = int(input())
s_que,e_que = list(),list()
computer_que = list()
computer_cnt = dict()
total = 0
for _ in range(N):
    s,e = map(int,input().split())
    heappush(s_que,(s,e))

while s_que:
    if not e_que or s_que[0] < e_que[0]:
        s,e = heappop(s_que)
        if computer_que:
           num = heappop(computer_que)
           heappush(e_que,(e,num))
           computer_cnt[num] += 1
        else:
            total += 1
            heappush(e_que,(e,total))
            computer_cnt[total] = 1
    else:
        e,num = heappop(e_que)
        heappush(computer_que,num)
print(total)
for i in range(1,total):
    print(computer_cnt[i],end=' ')
print(computer_cnt[total])