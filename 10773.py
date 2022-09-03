K = int(input())
stack = []
for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
total = 0
for j in stack:
    total += j
print(total)