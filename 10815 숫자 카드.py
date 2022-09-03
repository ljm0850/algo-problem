cnt = [0]*20000000
N = int(input())
cards = list(map(int,input().split()))
for card in cards:
    if card >=0:
        cnt[card] = 1
    else:
        cnt[20000000+card] = 1


N2 = int(input())
target = list(map(int,input().split()))
ans = []
for t in target:
    if t <0:
        t += 20000000
    if cnt[t]:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)