# def bubblesort(ls):
#     l = len(ls)
#     for i in range(l)[::-1]:
#         for j in range(i):
#             if ls[j] < ls[j+1]:
#                 ls[j],ls[j+1] = ls[j+1],ls[j]
#     return ls

def check(number):
    temp = number
    stack = [temp%10]
    temp = temp // 10
    while temp !=0:
        if stack[-1]  >= temp % 10:
            stack.append(temp % 10)
            temp //= 10
        else:
            return -1
    return number

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    solve = []
    for i in range(N-1):
        for j in range(i+1,N):
            temp = check(num[i]*num[j])
            if temp != -1:
                solve.append(temp)
    max_num = -1
    for i in solve:
        if i > max_num:
            max_num = i
    print(f'#{tc} {max_num}')