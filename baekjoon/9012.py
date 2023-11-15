T = int(input())

for tc in range(1,T+1):
    target = input()
    stack = []
    solve = 'YES'
    for i in target:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                solve = 'NO'
                break
    if stack:
        solve = 'NO'
    print(solve)

