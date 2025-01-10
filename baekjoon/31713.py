import sys
input = sys.stdin.readline
def solution(A:int,B:int)->int:
    cnt = 0
    A4 = 4*A
    if B > A4:
        num = B-A4
        cnt += (num // 4) + (1 if num%4 else 0)
        A += cnt
    A3 = 3*A
    if B < A3:
        cnt += A3-B
    return cnt

T = int(input())
ans = [0]*T
for tc in range(T):
    A,B = map(int,input().split())
    ans[tc] = solution(A,B)
print(*ans,sep='\n')