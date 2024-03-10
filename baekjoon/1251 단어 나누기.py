target = input()
T = len(target)
ans = target[:1][::-1] + target[1:2][::-1] + target[2:][::-1]
for i in range(1,T-1):
    for j in range(i+1,T):
        a = target[:i]
        b = target[i:j]
        c = target[j:]
        newString = a[::-1] + b[::-1] + c[::-1]
        if ans > newString:
            ans = newString
print(ans)