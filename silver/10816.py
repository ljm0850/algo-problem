N = int(input())                                    # 500,000 이하
cards= list(map(int,input().split()))               # -10,000,000 이상 10,000,000 이하
M = int(input())
target = list(map(int,input().split()))
solve= []
cnt_dic = {}
for card in cards:
    if card in cnt_dic:
        cnt_dic[card] += 1
    else:
        cnt_dic[card] = 1

for t in target:
    temp = cnt_dic.get(t)
    if temp != None:
        solve.append(temp)
    else:
        solve.append(0)
print(*solve)