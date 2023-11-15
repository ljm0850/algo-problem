# import sys
# input = sys.stdin.readline
# N = int(input())
#
# class student:
#     def __init__(self,name,k,e,m):
#         self.name = name
#         self.korean = k
#         self.english = e
#         self.math = m
#
# answer = []
# for _ in range(N):
#     name,k,e,m = input().split()
#     student(name,int(k),int(e),int(m))
#     answer.append(student(name,int(k),int(e),int(m)))
# answer.sort(key=lambda x:(-x.korean,x.english,-x.math,x.name))
# for ans in answer:
#     print(ans.name)

import sys
input = sys.stdin.readline
N = int(input())
kor,eng,math = {},{},{}
answer = []
for _ in range(N):
    name,k,e,m = input().split()
    answer.append(name)
    kor[name] = int(k)
    eng[name] = int(e)
    math[name] = int(m)
answer.sort(key=lambda name:(-kor[name],eng[name],-math[name],name))
for ans in answer:
    print(ans)