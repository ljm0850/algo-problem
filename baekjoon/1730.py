N = int(input())
commands = input()
arr =[[0]*N for _ in range(N)]
r,c = 0,0
for command in commands:
    moving = 1
    match command:
        case 'U':
            nr,nc = r-1,c
        case 'D':
            nr,nc = r+1,c
        case 'L':
            nr,nc = r,c-1
            moving = 2
        case 'R':
            nr,nc = r,c+1
            moving = 2
    if not (0<=nr<N and 0<=nc<N): continue
    arr[r][c] |= moving
    r,c = nr,nc
    arr[r][c] |= moving
for r in range(N):
    for c in range(N):
        match arr[r][c]:
            case 0:
                mark = '.'
            case 1:
                mark = '|'
            case 2:
                mark = '-'
            case 3:
                mark = '+'
        arr[r][c] = mark
for row in arr:
    print(''.join(row))