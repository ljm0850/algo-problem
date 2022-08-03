def solve():
    check = {num for num in range(N)}
    if target != root:
        check.remove(target)
    else:
        return 0
    stack = [target]
    while stack:
        t = stack.pop()
        for i in list(check):
            if parent[i] == t:
                stack.append(i)
                check.remove(i)
    if check == {root}:
        return 1

    check.discard(root)
    stack = [root]
    cnt = 0
    if not check:
        return 0
    while stack:
        t = stack.pop()
        temp = []
        for i in list(check):
            if parent[i] == t:
                temp.append(i)
                check.remove(i)
        if temp:
            for n in temp:
                stack.append(n)
        else:
            cnt +=1
    return cnt

def find_root():
    for i in range(N):
        if parent[i] == -1:
            root = i
    return root

N = int(input())
parent = list(map(int,input().split()))
target = int(input())
check = [0]*N
root = find_root()
ans=solve()
print(ans)