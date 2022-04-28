coins = [500,100,50,10,5,1]
pay = 1000-int(input())
cnt = 0
for coin in coins:
    if pay >= coin:
        cnt += pay//coin
        pay -= coin*(pay//coin)
print(cnt)