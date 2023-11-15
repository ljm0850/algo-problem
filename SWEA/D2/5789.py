import sys
sys.stdin=open('input (1).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    PrimeLs={} #PrimeLs는 소인수 값(각 자리는 2,3,5,7,11...)
    for i in range(2,12):
        cnt = 0
        while N % i ==0 :
            cnt +=1
            N //= i


        PrimeLs[i] = cnt

    # print(PrimeLs)

    print(f'#{tc} {PrimeLs[2]} {PrimeLs[3]} {PrimeLs[5]} {PrimeLs[7]} {PrimeLs[11]}')