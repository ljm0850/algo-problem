# 마주보는것
# 0,6
# 1,4
# 2,3
# def absolute(x):
#     if x >0 :
#         return x
#     elif x == 0 :
#         return 0
#     else :
#         return -x

T= int(input())
total = 0
dicels=[1,2,3,4,5]
for i in range(T):
    dice = list(map(int,input().split()))
    if i==0:
        dicels.pop(dice[5-dice.index(6)])
