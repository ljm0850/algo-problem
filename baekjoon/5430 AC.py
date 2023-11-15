# import sys
# from collections import deque
# def change_ls():
#     nums = deque()
#     temp = ''
#     for i in target:
#         if i.isdigit():
#             temp += i
#         elif i == ',':
#             nums.append(int(temp))
#             temp = ''
#     if temp:
#         nums.append(int(temp))
#     return nums
#
# def check(ls,cmd):
#     way,s,e = 1,0,n-1
#     for c in cmd:
#         if c == 'R':
#            way *= -1
#         elif c == 'D':
#            if not ls:
#                print('error')
#                return
#            if way == 1:
#                ls.popleft()
#            elif way == -1:
#                ls.pop()
#     ans = str(ls)
#     print(ans)
# T = int(input())
# for tc in range(1,T+1):
#     p=input()                   # 수행할 함수
#     n = int(input())            # 배열에 들어 있는
#     target = sys.stdin.readline()
#     nums = change_ls()
#     check(nums,p)

import sys
def change_ls():
    nums = []
    temp = ''
    for i in target:
        if i.isdigit():
            temp += i
        elif i == ',':
            nums.append(int(temp))
            temp = ''
    if temp:
        nums.append(int(temp))
    return nums

def check(ls,cmd):
    way,s,e = 1,0,n-1
    for c in cmd:
        if c == 'R':
           way *= -1
        elif c == 'D':
            if s > e:
                print('error')
                return
            if way == 1:        # 정방향
                s += 1
            elif way == -1:
                e -= 1
    if way == 1:
        ans=ls[s:e+1]
    else:
        ans = ls[s:e+1][::-1]
    a_l = len(ans)
    if a_l:
        print('[',end='')
        for a in range(a_l-1):
            print(ans[a],end=',')
        print(f'{ans[-1]}]')
    else:
        print('[]')

T = int(input())
for tc in range(1,T+1):
    p=input()                   # 수행할 함수
    n = int(input())            # 배열에 들어 있는
    target = sys.stdin.readline()
    nums = change_ls()
    check(nums,p)