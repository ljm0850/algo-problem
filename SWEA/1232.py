import sys
sys.stdin = open('input.txt')

def solve(ls,n):
    if str(ls[n]).isdigit():
        return ls[n]
    else:
        if ls[n] == '+':
            ls[n] = solve(ls,ch[n][0]) + solve(ls,ch[n][1])
        elif ls[n] == '-':
            ls[n] = solve(ls, ch[n][0]) - solve(ls, ch[n][1])

        elif ls[n] == '*':
            ls[n] = solve(ls, ch[n][0]) * solve(ls, ch[n][1])

        else:
            ls[n] = solve(ls, ch[n][0]) / solve(ls, ch[n][1])
        return ls[n]
for tc in range(1,11):
    N = int(input())            #정점의 수,1000 이하 자연수
    target = [0]
    ch = [0]* (N+1)
    target = [0]
    for _ in range(N):
        temp = input().split()
        if temp[1].isdigit():
            target.append(int(temp[1]))
        else:
            target.append(temp[1])
            ch[int(temp[0])] = [int(temp[2]),int(temp[3])]
    print(f'#{tc} {int(solve(target,1))}')
