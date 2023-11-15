N,M = map(int,input().split())      # N장의 카드(3~100)(3장고름), 합이 M에 가깝게(10~300,000)
cards = list(map(int,input().split()))
max_sum = 0
cards.sort()
bp = 0
for i in range(N):
    pick = cards[i]
    target = M-pick
    s = i+1
    e = N-1
    while s<e:
        sum_num = cards[s]+cards[e]
        if sum_num == target:
            max_sum = sum_num + pick
            bp = 1
            break
        elif sum_num < target:
            if sum_num + pick > max_sum:
                max_sum = sum_num + pick
            s +=1
        else:
            e -=1
    if bp == 1:
        break
print(max_sum)