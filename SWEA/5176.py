import sys
sys.stdin = open('sample_input.txt')

# 1부터 N까지의 자연수를 이진 탐색 트리에 저장
# 루트를 구해야 하나? 삽입하면서 계속 바꿔주는걸 구현 못하겠는데
# n의 위치는 2**h -1 고정
# n의 부모는 형제가 있을경우 n-2 // 없을경우 n-1

# 1의 위치는 최하단 제일 왼쪽 고정 2**(h-1) +1 고정

def binary(n):
    global cnt
    global solve
    if n > N:
        return
    binary(2*n)
    cnt += 1
    solve[n] = cnt
    binary(2*n+1)

T= int(input())

for tc in range(1,T+1):
    N = int(input())            #1000이하
    solve = [[] for _ in range(N+1)]
    solve[1] = 1
    cnt = 0
    binary(1)

    print(f'#{tc} {solve[1]} {solve[N//2]}')