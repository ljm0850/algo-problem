while True:
    target = input()
    if target == '.':
        break
    stack = []
    solve = 'no'
    for i in target:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack:
                if stack.pop() != '[':
                    break
            else:
                break
        elif i == ')':
            if stack:
                if stack.pop() != '(':
                    break
            else:
                break
        elif i == '.':
            if stack:
                break
    else:
        solve = 'yes'
    print(solve)
