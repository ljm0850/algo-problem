n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
solve = []
bp = 0
for i in range(1,n+1):
    solve.append('+')
    stack.append(i)
    while target:
        if stack and stack[-1] == target[0]:
            solve.append('-')
            target.pop(0)
            stack.pop()
        else:
            break
if target:
    print('NO')
else:
    for i in solve:
        print(i)