import sys
sys.stdin=open('sample_input.txt')

def heap(n):
    global ls
    while n >= 2:
        if ls[n] < ls[n//2]:
            ls[n],ls[n//2] = ls[n//2],ls[n]
            n //= 2
        else:
            break

T= int(input())

for tc in range(1,T+1):
    N = int(input())            # 1,000,000 이하인 서로 다른 N개의 자연수
    N_ls = list(map(int,input().split()))
    ls = [0]
    cnt = 0
    for i in N_ls:
        cnt += 1
        ls.append(i)
        heap(cnt)

    total = 0
    while N >= 1:
        N//=2
        total += ls[N]

    print(f'#{tc} {total}')