import sys
M = int(sys.stdin.readline())
solve = set()
call = set(str(i) for i in range(1,21))
for _ in range(M):
    temp = sys.stdin.readline().split()
    if temp[0] == 'add':
        solve.add(temp[1])
    elif temp[0]== 'remove':
        solve.discard(temp[1])
    elif temp[0]== 'check' :
        if temp[1] in solve:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if temp[1] in solve:
            solve.discard(temp[1])
        else:
            solve.add(temp[1])
    elif temp[0] == 'all':
        solve = call.copy()
    else:
        solve.clear()