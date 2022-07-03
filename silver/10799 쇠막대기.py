def solve(target):
    ans = 0
    pipe = 0
    for i in range(len(target)):
        if target[i] =='(':
            pipe += 1
        else:
            if target[i-1] == '(':
                pipe -= 1
                ans += pipe
            else:
                pipe -= 1
                ans += 1
    print(ans)

cmd = input()
solve(cmd)