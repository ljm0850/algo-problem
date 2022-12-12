import sys
n = int(sys.stdin.readline())
check = set()
for _ in range(n):
    target = sys.stdin.readline().split()
    if target[1] == 'enter':
        check.add(target[0])
    else:
        check.remove(target[0])

answer = list(check)
answer.sort(reverse=True)
for ans in answer:
    print(ans)