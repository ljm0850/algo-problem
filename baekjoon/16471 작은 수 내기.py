N = int(input())
p1 = sorted(map(int,input().split()),reverse=True)
p2 = sorted(map(int,input().split()),reverse=True)
p2_idx = 0
cnt = 0
for my_card in p1:
    if my_card < p2[p2_idx]:
        cnt += 1
        p2_idx += 1
if cnt > N//2:
    print("YES")
else:
    print("NO")