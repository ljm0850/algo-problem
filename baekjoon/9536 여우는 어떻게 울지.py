import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    total = input().split()
    check = set()
    while True:
        animal = input().split()
        if animal[0] == 'what':
            break
        else:
            check.add(animal[2])
    ans = ''
    for say in total:
        if not say in check:
            ans += say + ' '
    print(ans.rstrip())