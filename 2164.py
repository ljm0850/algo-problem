N = int(input())

target = list(range(1,N+1))

while target:
    length = len(target)
    if length == 1:
        print(target.pop())
    elif length % 2 :         #홀수이면
        target.pop(0)
        target.append(target.pop(0))
    else:   #짝수이면
        target = target[1::2]