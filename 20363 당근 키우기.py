x,y = map(int,input().split())
if x >= y:
    big,small = x,y
else:
    big,small = y,x
ans = big + small + small // 10
print(ans)