X = int(input())
cnt = 1
while X > cnt:
    X -= cnt
    cnt += 1

if cnt%2 == 0:
    a = X
    b = cnt-X + 1
else:
    a = cnt - X + 1
    b = X
print(f'{a}/{b}')