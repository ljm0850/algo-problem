target = input()
ans = set()
for e in range(len(target)+1):
    for s in range(e):
        ans.add(target[s:e])
print(len(ans))