target = input()
TNT = input()
l = len(TNT)
answer = []

for t in target:
    answer.append(t)
    if t == TNT[-1] and len(answer) >= l:
        for i in range(l):
            if answer[-1-i] != TNT[-1-i]:
                break
        else:
            for _ in range(l):
                answer.pop()
if answer:
    for ans in answer:
        print(ans,end="")
else:
    print("FRULA")