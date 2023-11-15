import sys
sys.stdin=open('sample_input (2).txt')

T=int(input())

for tc in range(1,T+1):
    A,B = input().split()           #A는 10000이하 B는 100이하
    a=len(A)
    b=len(B)
    cnt = 0
    i = 0
    if a>=b:
        while i <= a-b+1:
            if A[i:i + b] == B:
                    cnt += 1
                    i += b
            else:
                i += 1
        print(f'#{tc} {a + (1 - b) * cnt}')
    else:
        print(f'#{tc} {a}')