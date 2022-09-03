N,X = map(int,input().split())
num = map(int,input().split())
solve = []
for i in num:
    if i < X:
        solve.append(i)
print(*solve)