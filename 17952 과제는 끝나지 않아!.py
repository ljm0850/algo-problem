import sys

N = int(input())
stack = list()
point = 0
for _ in range(N):
    pb = list(map(int,sys.stdin.readline().split()))
    if pb[0]:
        stack.append(pb)
    if stack:
        stack[-1][2] -= 1
        if stack[-1][2] == 0:
            point += stack[-1][1]
            stack.pop()
print(point)