target=input()
stack = []
ans = []
for item in target:
    if item.isalpha():
        ans.append(item)
        continue

    if item in ['+','-']:
        while stack and stack[-1] != '(' :
            ans.append(stack.pop())
        stack.append(item)
    elif item in ['*','/']:
        while stack and stack[-1] in ['*','/']:
            ans.append(stack.pop())
        stack.append(item)
    elif item == ')':
        while stack[-1] !='(':
            ans.append(stack.pop())
        stack.pop()
    else:
        stack.append(item)

while stack:
    ans.append(stack.pop())
for a in ans:
    print(a,end='')