def solution(X:int,coins:list[int])->list[int]:
    a,b,c,d = 0,0,0,0
    # [a,b,c,d]
    # 25원 처리
    money = X-(coins[0]+5*coins[1]+10*coins[2])
    if money >0:
        d = money // 25
        if money % 25:
            d += 1
        d = min(d,coins[3])

    # 10원 처리
    money = X - (coins[0]+5*coins[1]+25*d)
    if money >0:
        c = money // 10
        if money % 10:
            c += 1
        c = min(c,coins[2])
    # 5원
    money = X - (coins[0]+10*c+25*d)
    if money >0:
        b = money // 5
        if money % 5:
            b += 1
        b = min(b,coins[1])
    # 1원
    money = X - (5*b+10*c+25*d)
    a = money
    if a > coins[0] or a<0:
        return [0,0,0,0]

    if c >= 3 and (coins[0] - a) >= 5 and (coins[3]-d)>=1:
        a,c,d = a+5,c-3,d+1
    return [a,b,c,d]

X,*coins = map(int,input().split())
ans = solution(X,coins)
print(*ans)

# def solution(X:int,coins:list[int])->list[int]:
#     a,b,c,D = 0,0,0,0
#     # 25원 처리
#     money = X-(coins[0]+5*coins[1]+10*coins[2])
#     if money >0:
#         D = money // 25
#         if money % 25:
#             D += 1
#         D = min(D,coins[3])
#     value = [0]*4
#     maxCnt = 0
#
#     for d in range(D,coins[3]+1):
#         # 10원 처리
#         if X - (25*d) <0:
#             break
#         money = X - (coins[0] + 5 * coins[1] + 25 * d)
#         if money >0:
#             money = X - (coins[0]+5*coins[1]+25*d)
#             c = money // 10
#             if money % 10:
#                 c += 1
#             c = min(c,coins[2])
#         # 5원
#         money = X - (coins[0]+10*c+25*d)
#         if money >0:
#             b = money // 5
#             if money % 5:
#                 b += 1
#             b = min(b,coins[1])
#         # 1원
#         money = X - (5*b+10*c+25*d)
#         a = money
#         if not (a > coins[0] or a<0):
#             cnt = a+b+c+d
#             if maxCnt < cnt:
#                 maxCnt = cnt
#                 value = [a,b,c,d]
#     if maxCnt == 0:
#         return [0,0,0,0]
#     return value
#
# X,*coins = map(int,input().split())
# ans = solution(X,coins)
# print(*ans)